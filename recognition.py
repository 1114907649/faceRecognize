import cv2
import numpy as np
import pandas as pd
import os
from PIL import Image
import torch
from network.lightcnn112 import LightCNN_29Layers
import pickle

class Recognize:
    def __init__(self, num_classes=358):
        self.fars = [10 ** -4, 10 ** -3, 10 ** -2]
        self.num_classes = num_classes
        self.root = './ttt'
        self.image_size = (112, 112)
        self.batch_size = 1
        self.model_dir = './model/casia'
        self.model_name = 'ver1_e15.pth.tar'
        self.model = self.model_load()
        self.vis = self.get_vis_nir_info()
        self.feat_vis, self.labels_vis = self.extract_feats_labels(self.vis)
 

    def model_load(self):
        model = LightCNN_29Layers(num_classes=self.num_classes)
        pretrained = os.path.join(self.model_dir, self.model_name)
        weights = torch.load(pretrained)
        weights = weights['state_dict']
        model_dict = model.state_dict()
        weights = {k.replace('module.', ''): v for k, v in weights.items() if
                   k.replace('module.', '') in model_dict.keys() and 'fc2' not in k}
        print("==> len of weights to be loaded: {}. \n".format(len(weights)))
        model.load_state_dict(weights, strict=False)
        model.eval().cuda()
        return model

    def face_match(self, img):
        
        #img = img.resize(self.image_size)
        feat_img = self.extract_input_fl(img)
        similarity = np.dot(feat_img, self.feat_vis.T)
        print(np.max(similarity))
        if np.max(similarity)>0.7:
            top_inds = np.argmax(similarity)
            return self.labels_vis[top_inds]
        
        return -1

    def get(self, img):
        img_flip = np.fliplr(img)
        img = np.transpose(img, (2, 0, 1))  # 1*112*112
        img_flip = np.transpose(img_flip, (2, 0, 1))
        input_blob = np.zeros((2, 1, self.image_size[1], self.image_size[0]),
                              dtype=np.uint8)
        input_blob[0] = img
        input_blob[1] = img_flip
        return input_blob

    @torch.no_grad()
    def forward_db(self, batch_data):
        # imgs = torch.Tensor(batch_data)
        imgs = torch.Tensor(batch_data).cuda()
        imgs.div_(255)
        feat = self.model(imgs)
        feat = feat.reshape([self.batch_size, 2 * feat.shape[1]])
        return feat.cpu().numpy()


# 将 pids 和 img_feats 组合成一个元组

    def extract_feats_labels(self,data_list):
#        img_feats = []
#        pids = []
#        os.remove('feature/feature.pickle')
#        f = open('feature/feature.pickle', 'ab') 
#        for (imgPath, pid) in data_list:
#            img = Image.open(os.path.join(self.root, imgPath)).convert('L') 
#            img = np.array(img)
#            img = img[..., np.newaxis]
#            ft = self.forward_db(self.get(img)).flatten()
#            data = [pid, ft]
#            #pickle.dump(data, f)
#            img_feats.append(ft)
#            pids.append(pid)
#        
#            
#        img_feats = np.array(img_feats, dtype=np.float32)
#        img_input_feats = img_feats[:, 0:img_feats.shape[1] // 2] + img_feats[:, img_feats.shape[1] // 2:]
#        img_input_feats = img_input_feats / np.sqrt(np.sum(img_input_feats ** 2, -1, keepdims=True))
#
#        pickle.dump([pids,img_input_feats], f)
#        print(len(img_input_feats[-1]))
#        a=img_input_feats[-1]
#        return img_input_feats, pids
        pids ,img_feats =[],[]
        with open('feature/feature.pickle', 'rb') as f:
            pids ,img_feats = pickle.load(f)
        return img_feats, pids


    def extract_input_fl(self, img):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)).convert('L')
        img_feat = []
        img = np.array(img)
        img = img[..., np.newaxis]

        img_feat.append(self.forward_db(self.get(img)).flatten())
        img_feat = np.array(img_feat).astype(np.float32)
        img_input_feat = img_feat[:, 0:img_feat.shape[1] // 2] + img_feat[:, img_feat.shape[1] // 2:]
        img_input_feat = img_input_feat / np.sqrt(np.sum(img_input_feat ** 2, -1, keepdims=True))
        return img_input_feat

    def get_vis_nir_info(self):
        vis = pd.read_csv('./vis_gallery_1.txt', header=None, sep=' ')
        vis_labels = [(s.split('\\')[-2]) for s in vis[0]]
        vis = vis[0].apply(lambda s: self.rename_path(s)).tolist()
        vis = [(p, l) for (p, l) in zip(vis, vis_labels)]
        return vis

    def rename_path(self, s):
        """messy path names, inconsistency between 10-folds and how data are actually saved"""
        s = s.split(".")[0]
        gr, mod, id, img = s.split("\\")
        ext = 'jpg'
        return "%s_%s_%s_%s.%s" % (gr, mod, id, img, ext)
    def save_feat(self,id,img):
        
        ft = self.extract_input_fl(img)
        pids ,img_feats =[],[]
        with open('feature/feature.pickle', 'rb') as f:
            pids ,img_feats = pickle.load(f)
        self.labels_vis=np.append(self.labels_vis,id)
        self.feat_vis = np.append(self.feat_vis,ft, axis=0)
        with open('feature/feature.pickle', 'wb') as f:
            pickle.dump([self.labels_vis, self.feat_vis],f)


    


if __name__ == '__main__':
    img = cv2.imread('./ttt/s3_VIS_20432_005.jpg')
    rec = Recognize()
    print(rec.face_match(img))
    rec.save_feat(999,img)
