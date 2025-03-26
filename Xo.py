import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
click_positions=[]
XorO=1

while running:
    screen.fill((41, 37, 37))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y= event.pos
            if 100 <= x <= 200 and 100 <= y <= 200:
                click_positions.append(((150,150), XorO))
                XorO *=-1
            if 200 <= x <= 300 and 100 <= y <= 200:
                click_positions.append(((250,150), XorO))
                XorO *=-1
            if 300 <= x <= 400 and 100 <= y <= 200:
                click_positions.append(((350,150), XorO))
                XorO *=-1
            if 100 <= x <= 200 and 200 <= y <= 300:
                click_positions.append(((150,250), XorO))
                XorO *=-1
            if 200 <= x <= 300 and 200 <= y <= 300:
                click_positions.append(((250,250), XorO))
                XorO *=-1
            if 300 <= x <= 400 and 200 <= y <= 300:
                click_positions.append(((350,250), XorO))
                XorO *=-1
            if 100 <= x <= 200 and 300 <= y <= 400:
                click_positions.append(((150,350), XorO))
                XorO *=-1
            if 200 <= x <= 300 and 300 <= y <= 400:
                click_positions.append(((250,350), XorO))
                XorO *=-1
            if 300 <= x <= 400 and 300 <= y <= 400:
                click_positions.append(((350,350), XorO))
                XorO *=-1




    pygame.draw.line(screen, (217, 199, 199), (200, 100), (200, 400), width=5)
    pygame.draw.line(screen, (217, 199, 199), (300, 100), (300, 400), width=5)
    pygame.draw.line(screen, (217, 199, 199), (100, 200), (400, 200), width=5)
    pygame.draw.line(screen, (217, 199, 199), (100, 300), (400, 300), width=5)


    for pos, symbol in click_positions:
        if symbol == 1:
            pygame.draw.circle(screen, (217, 199, 199), pos, 40, width=10)
        else:
            x,y = pos
            pygame.draw.line(screen, (217, 199, 199), (x-30, y-30), (x+30, y+30), width=10)
            pygame.draw.line(screen, (217, 199, 199), (x + 30, y - 30), (x - 30, y + 30), width=10)


    pygame.display.flip()

pygame.quit()