
import random
import pygame
import time
import sys
import numpy as np
from math import sqrt
# 初始化Pygame并创建游戏界面



#读取历史成绩
def read_s():
    global rank
    fr = open('data.txt','r')
    str = fr.read()
    rank =str.split(",")[:-1]
    rank = np.array(rank,dtype=float)
    rank.sort()
    fr.close()
def write_s():
    global elapsed_time
    fw = open('data.txt','a+')
    fw.write('%.2f,'%(elapsed_time))
    fw.close 
def del_s():
    global rank
    rank = None
    fw = open('data.txt','w')
    fw.write('')
    fw.close   
#参数初始化
def game_init(n=4,size=(500, 600)):
    pygame.init()
    global screen,grid_size,reset_button_rect,screen_rect ,start_button_rect,num_bar_rect,rank_bar_rect,time_rect,width,height,start_time,time_bar_w  ,time_bar_h  ,start_bar_w ,start_bar_h ,reset_bar_w ,reset_bar_h ,rank_bar_w  ,rank_bar_h  ,num_bar_w   ,num_bar_h   ,screen_bar_w,screen_bar_h
    global size_input_bar_w,size_input_bar_h,size_input_bar_rect,n_input_bar_w,n_input_bar_h,n_input_bar_rect,rect2,T1,T2,TTT
    TTT = False
    T1 = False
    T2 = False
    rect2 = None
    width = size[0]
    height =size[1]
    grid_size = n
    start_time = None
    time_bar_w   = 200
    time_bar_h   = 100
    start_bar_w  = 100
    start_bar_h  = 100
    reset_bar_w  = 100
    reset_bar_h  = 100
    rank_bar_w   = 100
    rank_bar_h   = 100
    num_bar_w    = width - rank_bar_h
    num_bar_h    = 100
    screen_bar_w = width - rank_bar_w
    screen_bar_h = height - num_bar_h - reset_bar_h
    size_input_bar_w = 80
    size_input_bar_h = 30
    size_input_bar_rect = pygame.Rect(width-90,height-90,size_input_bar_w,size_input_bar_h)
    n_input_bar_w = 80
    n_input_bar_h = 30
    n_input_bar_rect = pygame.Rect(width-90,height-50,n_input_bar_w,n_input_bar_h)
    #数字区域
    screen_rect = pygame.Rect(0, num_bar_h, screen_bar_w//grid_size*grid_size, screen_bar_h//grid_size*grid_size)
    #重置按钮区
    reset_button_rect = pygame.Rect(reset_bar_w//6                        ,num_bar_h + screen_bar_h + reset_bar_h*5//18, reset_bar_w*2//3, reset_bar_h*4//9)
    #开始按钮区
    start_button_rect = pygame.Rect(reset_bar_w + start_bar_w//6          ,num_bar_h + screen_bar_h + start_bar_h*5//18, start_bar_w*2//3, start_bar_h*4//9)
    #时间
    time_rect         = pygame.Rect(reset_bar_w+start_bar_w +time_bar_w//6,num_bar_h + screen_bar_h +  time_bar_h*5//18,   time_bar_w*2//3, time_bar_h*4//9)
    #顶部当前数字区
    num_bar_rect      = pygame.Rect(0                 , 0                   , num_bar_w, num_bar_h)
    #排名栏
    rank_bar_rect     = pygame.Rect(num_bar_h        , 0                   , rank_bar_w , rank_bar_h)
 
    # 初始化Pygame并创建游戏界面
    global current_num
    current_num = 0 
    del_s()
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    #绘画
    draw_game()
    
# 绘制游戏界面
def draw_game():

    draw_grid()
    draw_rank()
    draw_numbers()
    draw_buttons()
    draw_current_number()
    draw_timer()
    
# 绘制方格
def draw_grid():
    global w,h,color_Rect,mouse_down,mouse_up,down_t,R
    num=grid_size*grid_size
    R=[0 for i in range(num)]
    down_t=[0 for i in range(num)]
    mouse_up=[0 for i in range(num)]
    mouse_down=[0 for i in range(num)]
    color_Rect=[0 for i in range(num)]
    w = screen_bar_w//grid_size
    h = screen_bar_h//grid_size
    for i in range(grid_size):
        for j in range(grid_size):
            rect = pygame.Rect(j*w, i*h+num_bar_h, w, h)
            color_Rect[i*grid_size+j]=rect
            mouse_down[i*grid_size+j] = False 
            mouse_up[i*grid_size+j] = False
            down_t[i*grid_size+j] = 0
            R[i*grid_size+j] = 0
            pygame.draw.rect(screen, (0,0,0), rect, 1)
    a=1
def handle_click():
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(color_Rect)):
                
                if color_Rect[i].collidepoint(pygame.mouse.get_pos()):
                    mouse_down[i]=True
                    down_t[i] = pygame.time.get_ticks()
                    R[i] = random.randint(0,255) 
        elif event.type == pygame.MOUSEBUTTONUP:
            for i in range(len(color_Rect)):                
                if color_Rect[i].collidepoint(pygame.mouse.get_pos()):
                    mouse_up[i]=True 
    # 更新屏幕
    for i in range(len(color_Rect)):
        if mouse_down[i]:
            
            Rect_color_loop(color_Rect[i], pygame.time.get_ticks()/10,R[i])    
            font = pygame.font.Font(None, h*2//3)
            text = font.render('%d'%(numbers[i]), True, (0, 0, 0))
            text_rect = text.get_rect(center=color_Rect[i].center)
            screen.blit(text, text_rect) 
        if mouse_up[i] and pygame.time.get_ticks()-down_t[i] >2000 :
            mouse_down[i] = False
            mouse_up[i]=False
            clean_rect(color_Rect[i])
def Rect_color_loop(CRect, t,randt):
    a=CRect
    x,y=CRect.center
    for i in range(CRect.top+1,CRect.bottom-1):
        for j in range(CRect.left+1,CRect.right-1):
            distance = int(sqrt((j-x)**2 + (i-y)**2))
            R =  (distance + t+randt )% 255 
            G =  (distance + 2*t+randt )% 255 
            B =  (distance + 3*t +randt)% 255 
            screen.set_at((j,i), (R,G,B))
    
def clean_rect(rect):
    screen.fill((255,255,255),(rect.x+1,rect.y+1,rect.width-2,rect.height-2))
# 绘制排名            
def draw_rank():  
    global rank,grid_size,height,width 
    read_s()         
    for i  in range(grid_size*2):
        rect = pygame.Rect(num_bar_w,i*h//2+num_bar_h,rank_bar_w,h//2)
        screen.fill((255,255,255), (num_bar_w+1,i*h//2+num_bar_h+1,rank_bar_w-2,h//2-2))
        pygame.draw.rect(screen, (0,0,0), rect, 1)
def write_rank():
    if rank is not None:
        n = len(rank)
        font = pygame.font.Font(None, h//3) 
        for i  in range(n): 
            if i == grid_size*2:
                break  
            rect = pygame.Rect(num_bar_w+1,i*h//2+num_bar_h+1,rank_bar_w-2,h//2-2)
            text = font.render('%.2f'%(rank[i]), True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            screen.fill((255,255,255), rect)
            screen.blit(text, text_rect)

# 绘制数字
def draw_numbers():
    global rank,grid_size,height,width,numbers 
    generate_numbers()
    font = pygame.font.Font(None, h*2//3)
    for i in range(len(numbers)):
        text = font.render('%d'%(numbers[i]), True, (0, 0, 0))
        row = i // grid_size
        col = i % grid_size
        rect = pygame.Rect(w*col, h*row+num_bar_h, w, h)
        fill_rect = pygame.Rect(w*col+1, h*row+num_bar_h+1, w-2, h-2)
        text_rect = text.get_rect(center=rect.center)
        screen.fill((255,255,255), fill_rect)
        screen.blit(text, text_rect)

# 生成数字
def generate_numbers():
    global numbers
    numbers = list(range(1, grid_size**2+1))
    random.shuffle(numbers)



# 绘制“重置”和“开始”按钮
def draw_buttons():
    draw_reset_button()
    draw_start_button()

# 绘制“重置”按钮
def draw_reset_button():
    rect = reset_button_rect
    color = (255, 0, 0)
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.Font(None, reset_bar_h*8//27)
    text = font.render("Reset", True, (255, 255, 255))
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)

# 绘制“开始”按钮
def draw_start_button():
    rect = start_button_rect
    color = (0, 255, 0)
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.Font(None, start_bar_h*8//27)
    text = font.render("Start", True, (255, 255, 255))
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)
    
global bg_color,clicked,hovered,rect2 
bg_color = (255,255,255)
clicked = False
hovered = False
rect2 = None
global text1,text2,T1,T2
T1 = False
T2 = False
text1 = '4'
text2 = "500,600 "
global TTT
TTT = False
def handle_events():
    global reset_button_rect,start_button_rect,screen_rect,rect2,clicked,hovered,text1,text2,active,T1,T2,TTT
    for event in pygame.event.get():
        x,y = pygame.mouse.get_pos()
        T = True      
        if event.type == pygame.QUIT:
            pygame.quit()
            TTT = True
            return
        elif event.type == pygame.MOUSEBUTTONDOWN:
            active = False
            text1 = input_box(event, n_input_bar_rect, text1)
            text2 = input_box(event, size_input_bar_rect, text2) 
            if reset_button_rect.collidepoint(event.pos):
                reset_game()
            elif start_button_rect.collidepoint(event.pos):
                start_game()
            elif screen_rect.collidepoint(event.pos) and start_time is not None :
                handle_mouse_click(event.pos)

            
        if n_input_bar_rect.collidepoint(pygame.mouse.get_pos()) :
            text_rect = n_input_bar_rect
            text1 = input_box(event, text_rect, text1)
            T = False
            T1 = active
            if T1 :
                T2=False                
        if size_input_bar_rect.collidepoint(pygame.mouse.get_pos()) :
            text_rect = size_input_bar_rect
            text2 = input_box(event, text_rect, text2)
            T = False 
            T2 = active
            if T2 :
                T1=False
        if not T1 :
            active = False
            text1 = input_box(event, n_input_bar_rect, text1)
        if not T2 :
            active = False  
            text2 = input_box(event,size_input_bar_rect, text2) 
        if T1 or T2 :
            active = True
        
        if event.type == pygame.KEYDOWN:
            if T1:
                rect = n_input_bar_rect
                text = text1
            if T2:
                rect = n_input_bar_rect
                text = text2
            if active:
                if event.key == pygame.K_RETURN:
                    size = text2.split(',')
                    if int(text1)!= grid_size or size[0] != width or size[1]!= height:
                        active = False
                        game_init(n=int(text1),size=(int(size[0]),int(size[1])))
                        T= False
                        return
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            if T and active:
                font = pygame.font.Font(None, 20)
                text_surface = font.render(text, True, (0, 0, 0))
                screen.fill((255,255,255),(rect.x+1,rect.y+1,rect.width-2,rect.height-2))
                screen.blit(text_surface, (rect.x + 5, rect.y + 5))
                if T1:
                    text1 = text
                else : text2 =text 
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(color_Rect)):
                
                if color_Rect[i].collidepoint(pygame.mouse.get_pos()):
                    mouse_down[i]=True
                    down_t[i] = pygame.time.get_ticks()
                    R[i] = random.randint(0,255) 
        elif event.type == pygame.MOUSEBUTTONUP:
            for i in range(len(color_Rect)):                
                mouse_up[i]=True 
    # 更新屏幕
    for i in range(len(color_Rect)):
        if mouse_down[i]:
            
            Rect_color_loop(color_Rect[i], pygame.time.get_ticks()/10,R[i])    
            font = pygame.font.Font(None, h*2//3)
            text = font.render('%d'%(numbers[i]), True, (0, 0, 0))
            text_rect = text.get_rect(center=color_Rect[i].center)
            screen.blit(text, text_rect)
        uu=pygame.time.get_ticks() 
        if mouse_up[i] and uu-down_t[i] >1000 :
            mouse_down[i] = False
            mouse_up[i]=False
            down_t[i]=0
            clean_rect(color_Rect[i])
            font = pygame.font.Font(None, h*2//3)
            text = font.render('%d'%(numbers[i]), True, (0, 0, 0))
            text_rect = text.get_rect(center=color_Rect[i].center)
            screen.blit(text, text_rect)   
global active
active = False                
def input_box(event, rect, text):
    T = True
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    global active
    if event.type == pygame.MOUSEBUTTONDOWN:       
        if rect.collidepoint(event.pos) :
            active = True
            a=1
        else:
            active = False
    color = color_active if active else color_inactive
    if event.type == pygame.KEYDOWN:
        if active:
            if event.key == pygame.K_RETURN:
                size = text2.split(',')
                if int(text1)!= grid_size or size[0] != width or size[1]!= height:
                    active = False
                    game_init(n=int(text1),size=(int(size[0]),int(size[1])))
                    T= False
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
    if T :
        pygame.draw.rect(screen, color, rect, 1)
        font = pygame.font.Font(None, 20)
        text_surface = font.render(text, True, (0, 0, 0))
        screen.fill((255,255,255),(rect.x+1,rect.y+1,rect.width-2,rect.height-2))
        screen.blit(text_surface, (rect.x + 5, rect.y + 5))         
    return text
hovered = False   
def handle_game(rect,T):
    global rect2,bg_color,clicked,hovered
    x,y = rect.x,rect.y
    row = (y-num_bar_h) // h
    col = x //w
    index = row * grid_size + col
    font = pygame.font.Font(None, h*2//3)
    text = font.render('%d'%(numbers[index]), True, (0, 0, 0))
    rect = pygame.Rect(w*col+1, h*row+num_bar_h+1, w-2, h-2)
    text_rect = text.get_rect(center=rect.center)
    if T :
        rect2 = rect
        # 根据状态更新背景颜色
        if clicked:
            bg_color = (0,200,0)
        else:
            bg_color = (255,255,255)
        screen.fill(bg_color, rect)
        screen.blit(text, text_rect)          
    else :
        screen.fill((255,255,255), rect)
        screen.blit(text, text_rect)        
                     
# 重置游戏
def reset_game():
    global numbers, start_time, current_num
    start_time = None
    current_num = 0    
    generate_numbers()
    del_s()
    draw_rank()
    draw_current_number()
    draw_numbers()


# 开始游戏
def start_game():
    global start_time,current_num
    current_num = 0
    start_time = time.time()
    draw_current_number()

    
# 处理鼠标点击事件
def handle_mouse_click(pos):
    global numbers
    global current_num
    x, y = pos
    row = (y-num_bar_h) //h
    col = x//w
    index = row * grid_size + col
    if numbers[index] == current_num+1:
        current_num+=1
        draw_current_number()

def draw_current_number():

    font = pygame.font.Font(None, num_bar_h*2//3)
    num = current_num
    text = font.render("Number: {}".format(num), True, (0, 0, 0))
    text_rect = text.get_rect(center=num_bar_rect.center)
    screen.fill((250,250,250),num_bar_rect)
    screen.blit(text, text_rect)
    if is_game_over() :
        write_s()
        read_s()
        write_rank()
        

# 判断游戏是否结束
def is_game_over():
    global current_num
    return current_num == len(numbers)

# 绘制计时器
def draw_timer():
    if start_time is not None and not is_game_over():
        global elapsed_time
        
        elapsed_time = time.time() - start_time
        font = pygame.font.Font(None, time_bar_h*8//27)
        text = font.render(f"Time: {elapsed_time:.2f} s", True, (0, 0, 0))
        text_rect = text.get_rect(center=time_rect.center)
        screen.fill((255,255,255),(reset_bar_w+start_bar_w ,num_bar_h + screen_bar_h , time_bar_w, time_bar_h))
        screen.blit(text, text_rect)
        

# 主循环
def start():
    game_init()
    while True:

        draw_timer()
        handle_events()
        if TTT:
            break
        time.sleep(0.01)
        pygame.display.update()


