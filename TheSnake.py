import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255,69,0)

colors =[]
colors.append(white)
colors.append(yellow)
colors.append(red)
colors.append(green)
colors.append(blue)
colors.append(orange)
 
dis_width = 800
dis_height = 400

foodx = 0
foody = 0

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Rodri - Snake')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    value = score_font.render("Tu Puntos: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    #unColor = random.choice(colors)
    for x in snake_list:
        pygame.draw.rect(dis, random.choice(colors), [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [int(dis_width / 6), int(dis_height / 3)])

def miRandom(max):
    m = round(random.randrange(0, max - snake_block))
    m = int(m)
    return m

def newFood():
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foodx = int(foodx)
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    foody = int(foody)
    return(foodx,foody)

 
def gameLoop():
    game_over = False
    game_close = False
    game_pause = False
 
    x1 = int(dis_width / 2)
    y1 = int(dis_height / 2)
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
    last_event_key = 0
 
    (foodx,foody) = newFood()
 
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            message("Perdiste! Espacio para continuar o Q para salir", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        if game_pause == True:
            message("Pausaste el Juego!!", random.choice(colors))
            pygame.display.update()
            
            while game_pause == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_pause = not game_pause
                        game_over = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            game_pause = not game_pause
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and last_event_key != pygame.K_RIGHT:
                    x1_change = -snake_block
                    y1_change = 0
                    last_event_key = pygame.K_LEFT
                elif event.key == pygame.K_RIGHT and last_event_key != pygame.K_LEFT:
                    x1_change = snake_block
                    y1_change = 0
                    last_event_key = pygame.K_RIGHT
                elif event.key == pygame.K_UP and last_event_key != pygame.K_DOWN:
                    y1_change = -snake_block
                    x1_change = 0
                    last_event_key = pygame.K_UP
                elif event.key == pygame.K_DOWN and last_event_key != pygame.K_UP:
                    y1_change = snake_block
                    x1_change = 0
                    last_event_key = pygame.K_DOWN
                elif event.key == pygame.K_p:
                    game_pause = not game_pause
 
        if x1 >= dis_width or x1 < -1 or y1 >= dis_height or y1 < -1:
            game_close = True


        x1 += x1_change
        y1 += y1_change

        dis.fill(black)
        pygame.draw.rect(dis, random.choice(colors), [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            (foodx,foody) = newFood()
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()