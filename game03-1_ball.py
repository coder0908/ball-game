import pygame 

pygame.init()
#이미지 불러오기
im_bar=pygame.image.load("C:\image\kbutton3-a(1).png")
im_ball=pygame.image.load("C:\image\kball-a.png")
#디스플레이 설정
background = pygame.display.set_mode((1000,600))
pygame.display.set_caption('ball')  #창 이름
#디스플레이 크기 정의
x=pygame.display.get_window_size()[0]
y=pygame.display.get_window_size()[1]

#폰트 정의
font = pygame.font.SysFont(None,30)    #font  #(글자체,사이즈)

point=0
x_pos=340
y_pos=99
x_s=1
y_s=1
#bar 위치
x1_pos=490
y1_pos=590
#bar 속도
x1_s=0

fps = pygame.time.Clock()
bar_size_x=im_bar.get_rect().size[0]
bar_size_y=im_bar.get_rect().size[1]
ball_size_x=im_ball.get_rect().size[0]
ball_size_y=im_ball.get_rect().size[1]


   
play = True
while play:
    deltaTime = fps.tick(150)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
             play=False    
    
    #ball 동작 (벽에 다으면 튕기기)
    x_pos+=x_s 
    y_pos+=y_s    
    if x_pos+(ball_size_x) >= x:
        x_s=-2     
        if point>=10:
         x_s=-4
    if x_pos <= 0:
        x_s=+2
        if point>=10:
         x_s=+2
    if y_pos <= 0:
        y_s=+2
        if point>=10:
         x_s=+4
    
    if y_pos == y-ball_size_y:
        
        
        background.blit(font_GAMEOVER,(500,300))
        pygame.display.update()
        pygame.time.delay(2000)
        play = False     
    
    # bar , ball 위치정의 (colliderect 사용위함)
    bar_rect = im_bar.get_rect()           # bar definition
    bar_rect.left = x1_pos               #
    bar_rect.top = y1_pos                #

    ball_rect = im_ball.get_rect()       # balldefinition
    ball_rect.left = x_pos              #
    ball_rect.top = y_pos                #

    
    
    #bar , ball 충돌시 동작
    if bar_rect.colliderect(ball_rect):
        
        y_s = -y_s
        point+=1
    
    #point , gameover 정의하기 (font)
    font_point = font.render(str(point),False,(100,240,50))
    font_GAMEOVER = font.render('GAMEOVER',False,(255,0,0))    
#gameover 크기 정의 (font)
    f_GAMEOVER_size_x = font_GAMEOVER.get_rect().size[0]
    f_GAMEOVER_size_y = font_GAMEOVER.get_rect().size[1]
#gameover 크기 정하기
    f_GAMEOVER_x_pos = x/2- (f_GAMEOVER_size_x/2)
    f_GAMEOVER_y_pos = y/2- (f_GAMEOVER_size_y/2)
    
    #bar 동작
    x1_pos+=x1_s
    #bar 움직일때
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT :
            x1_s=-2          
        if event.key == pygame.K_RIGHT:
            x1_s=+2
    #bar 멈출때
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            x1_s=0
        if event.key == pygame.K_RIGHT:
            x1_s=0
    #bar 벽과 충돌시 정지
    if x1_pos<= 0:
        x1_pos=0 
    if x1_pos+(bar_size_x)>= x:
        x1_pos=x-bar_size_x
    
    
    
    
    
    
    background.fill((0,0,0))
    background.blit(im_ball,(x_pos,y_pos))
    background.blit(im_bar,(x1_pos,y1_pos))
    
   
   
    background.blit(font_point,(50,50))
##################################################
    
    #포인트 20점 #다음 스테이지
    if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
             background.fill((0,0,0))
                     
        #디스플레이 설정
            background = pygame.display.set_mode((1000,600))
        
            pygame.display.set_caption('logic game')  #창 이름
        #디스플레이 크기 정의
            x=pygame.display.get_window_size()[0]
            y=pygame.display.get_window_size()[1]
        #font
            pygame.font.SysFont(None,200)
        #
            r= font.render('get ready for next game!!!!',False,(255,255,0))
            background.blit(r,(0,0))
            pygame.display.update()
            pygame.time.delay(2000)
        
        #3cec count
            for i in range(1,4):
                r1= font.render(str(-(i-4)), False,(255,255,0))
                background.fill((0,0,0))
                background.blit(r1,(0,0))
                pygame.time.delay(1000)
                pygame.display.update()
                point=10
        
        
        
              
       

        
        
        

        
    
    pygame.display.update()
pygame.quit()

exit()    
if event.type == pygame.QUIT:
            play1 = False
    
        
      
      
if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and pygame.K_1 and pygame.K_p:
             play = False
                  
