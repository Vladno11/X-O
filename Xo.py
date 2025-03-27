import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
click_positions=[]
XorO=1
brK=0
kliknuto=[True]*9
pobeda=[[0,1,2],[0,4,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6],[3,4,5],[6,7,8]]
PCrta=([[[100,150],[400,150]],
        [[100,100],[400,400]],
        [[150,100],[150,400]],
        [[250,100],[250,400]],
        [[350,100],[350,400]],
        [[400,100],[100,400]],
        [[100,250],[400,250]],
        [[100,350],[400,350]]])
spojenex=[]
spojeneo=[]

while running:
    screen.fill((41, 37, 37))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y= event.pos
            if brK<=8:
                if 100 <= x <= 200 and 100 <= y <= 200 and kliknuto[0]:
                    click_positions.append(((150,150), XorO))
                    XorO *=-1
                    brK+=1
                    kliknuto[0]=False
                if 200 <= x <= 300 and 100 <= y <= 200 and kliknuto[1]:
                    click_positions.append(((250,150), XorO))
                    XorO *=-1
                    brK += 1
                    kliknuto[1] = False
                if 300 <= x <= 400 and 100 <= y <= 200 and kliknuto[2]:
                    click_positions.append(((350,150), XorO))
                    XorO *=-1
                    brK += 1
                    kliknuto[2] = False
                if 100 <= x <= 200 and 200 <= y <= 300 and kliknuto[3]:
                    click_positions.append(((150,250), XorO))
                    XorO *=-1
                    brK += 1
                    kliknuto[3] = False
                if 200 <= x <= 300 and 200 <= y <= 300 and kliknuto[4]:
                    click_positions.append(((250,250), XorO))
                    XorO *=-1
                    brK += 1
                    kliknuto[4] = False
                if 300 <= x <= 400 and 200 <= y <= 300 and kliknuto[5]:
                    click_positions.append(((350,250), XorO))
                    XorO *=-1
                    brK += 1
                    kliknuto[5] = False
                if 100 <= x <= 200 and 300 <= y <= 400 and kliknuto[6]:
                    click_positions.append(((150,350), XorO))
                    XorO *=-1
                    brK += 1
                    kliknuto[6] = False
                if 200 <= x <= 300 and 300 <= y <= 400 and kliknuto[7]:
                    click_positions.append(((250,350), XorO))
                    XorO *=-1
                    brK += 1
                    kliknuto[7] = False
                if 300 <= x <= 400 and 300 <= y <= 400 and kliknuto[8]:
                    click_positions.append(((350,350), XorO))
                    XorO *=-1
                    brK += 1
                    kliknuto[8] = False
                id=0
                if XorO == -1:
                    for id in range(9):
                        if kliknuto[id] == False and id not in spojeneo and id not in spojenex:
                            spojeneo.append(id)
                elif XorO == 1:
                    for id in range(9):
                        if kliknuto[id] == False and id not in spojeneo and id not in spojenex:
                            spojenex.append(id)
                for i, komb in enumerate(pobeda):  # Dodali smo i indeks
                    if set(komb).issubset(spojenex):
                        print("Pobeda X")
                        pygame.draw.line(screen, (0, 255, 0), PCrta[i][0], PCrta[i][1], width=10)
                        pygame.display.update()
                        running = False
                    if set(komb).issubset(spojeneo):
                        print("Pobeda O")
                        pygame.draw.line(screen, (0, 255, 0), PCrta[i][0], PCrta[i][1], width=10)
                        pygame.display.update()
                        running = False






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