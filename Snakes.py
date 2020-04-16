import pygame
import random
import os

pygame.init()




#colors
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
screen_width = 800
screen_height = 500

gameWindow = pygame.display.set_mode((screen_width,screen_height))


# background image
bgimg = pygame.image.load("2.jpg")
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()



pygame.display.set_caption("Snakes")
pygame.display.update()


clock = pygame.time.Clock()

font = pygame.font.SysFont(None,55)




def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,222,132))
        gameWindow.blit(bgimg,(0,0))
        text_screen(".....Welcome to Snakes.....",red,150,200)
        text_screen("Press Spacebar to continue.", red, 150, 250)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            pygame.display.update()
            clock.tick(30)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()




def gameloop():

    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
            f.close()


    with open("highscore.txt", "r") as f:
        high_score = f.read()

    snake_x = 45
    snake_y = 45
    velocity_x = 0
    velocity_y = 0
    snake_size = 20
    snk_list = []
    snk_length = 1
    exit_game = False
    game_over = False

    food_x = random.randint(20, screen_width // 1.5)
    food_y = random.randint(20, screen_height // 1.5)

    fps = 30
    score = 0


    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(high_score))

            gameWindow.fill(black)
            text_screen("Game Over! press enter to continue",red,70,screen_height//2.5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y=0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y=0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_x=0
                        velocity_y = 10
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_x=0
                        velocity_y = -10
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            score+=10
            snake_x+=velocity_x
            snake_y+=velocity_y

            if abs(snake_x-food_x)<11 and abs(snake_y-food_y)<11:
                score+=10

                snk_length+=1
                food_x = random.randint(20, screen_width // 1.5)
                food_y = random.randint(20, screen_height // 1.5)
                if score>int(high_score):
                    high_score=score


            gameWindow.fill(black)
            text_screen("Score: " + str(score)+"    Hi-score"+str(high_score), red, 5, 5)
            # food
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            # snake

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True

            plot_snake(gameWindow,green,snk_list,snake_size)

        pygame.display.update()

        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
gameloop()