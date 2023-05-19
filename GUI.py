import pygame
import sys

choice=0
level=0

pygame.init()
width = 400
height = 300
windoSize=(width,height)
windo= pygame.display.set_mode(windoSize)
font = pygame.font.SysFont("gabriola", 30)

windoStart = "Select an algorithm"
windoStart_label = font.render(windoStart, 1, (0, 255, 255))
windoStart_x = int(width / 2 - windoStart_label.get_width() / 2)
windoStart_y = int(height / 4 - windoStart_label.get_height() / 2)
windo.fill((0, 51, 102))
windo.blit(windoStart_label, (windoStart_x, windoStart_y))



bwidth = 110
bheight = 50
positionx1 = int(width / 4 - bwidth / 2)
positionx2 = int(3 * width / 4 - bwidth / 2)
positiony = int(height / 2 - bheight / 2)
bcolor = (255, 255, 0)

algo1 = "Minimax"
algo2 = "Alpha-Beta"
algo1_lable = font.render(algo1, 1, (0, 0, 0))
algo2_lable = font.render(algo2, 1, (0, 0, 0))
positionx1_lable=int(positionx1 + bwidth / 2 - algo1_lable.get_width() / 2)
positionx2_lable=int(positionx2 + bwidth / 2 - algo2_lable.get_width() / 2)
positiony_lable=int(positiony + bheight / 2 - algo1_lable.get_height() / 2)

pygame.draw.rect(windo,bcolor,(positionx1,positiony,bwidth,bheight))
pygame.draw.rect(windo,bcolor,(positionx2,positiony,bwidth,bheight))

windo.blit(algo1_lable, (positionx1_lable, positiony_lable))
windo.blit(algo2_lable, (positionx2_lable, positiony_lable))

pygame.display.set_caption('Connect-4')
pygame.display.update()

while  choice != 1 and choice != 2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if positionx1 <= mouse_x <= positionx1 + bwidth and positiony <= mouse_y <= positiony + bheight:
                choice = 1
            elif positionx2 <= mouse_x <= positionx2 + bwidth and positiony <= mouse_y <= positiony + bheight:
                choice = 2

pygame.init()
width = 600
height = 300
windoSize=(width,height)
windo= pygame.display.set_mode(windoSize)
font = pygame.font.SysFont("gabriola", 30)

windoStart = "Select the difficulty level"
windoStart_label = font.render(windoStart, 1, (0, 255, 255))
windoStart_x = int(width / 2 - windoStart_label.get_width() / 2)
windoStart_y = int(height / 4 - windoStart_label.get_height() / 2)
windo.fill((0, 51, 102))
windo.blit(windoStart_label, (windoStart_x, windoStart_y))


bwidth = 110
bheight = 50
positionx1 = int(width / 4 - bwidth / 2)
positionx2 = int(2 * width / 4 - bwidth / 2)
positionx3 = int(3 * width / 4 - bwidth / 2)
positiony = int(height / 2 - bheight / 2)
bcolor = (255, 255, 0)

level1 = "Easy"
level2 = "Medium"
level3 = "Hard"
level1_lable = font.render(level1, 1, (0, 0, 0))
level2_lable = font.render(level2, 1, (0, 0, 0))
level3_lable = font.render(level3, 1, (0, 0, 0))
positionx1_lable=int(positionx1 + bwidth / 2 - level1_lable.get_width() / 2)
positionx2_lable=int(positionx2 + bwidth / 2 - level2_lable.get_width() / 2)
positionx3_lable=int(positionx3 + bwidth / 2 - level3_lable.get_width() / 2)
positiony_lable=int(positiony + bheight / 2 - level1_lable.get_height() / 2)

pygame.draw.rect(windo,bcolor,(positionx1,positiony,bwidth,bheight))
pygame.draw.rect(windo,bcolor,(positionx2,positiony,bwidth,bheight))
pygame.draw.rect(windo,bcolor,(positionx3,positiony,bwidth,bheight))

windo.blit(level1_lable, (positionx1_lable, positiony_lable))
windo.blit(level2_lable, (positionx2_lable, positiony_lable))
windo.blit(level3_lable, (positionx3_lable, positiony_lable))
pygame.display.set_caption('Connect-4')
pygame.display.update()

while  level != 1 and level != 2 and level != 3:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if positionx1 <= mouse_x <= positionx1 + bwidth and positiony <= mouse_y <= positiony + bheight:
                level = 1
            elif positionx2 <= mouse_x <= positionx2 + bwidth and positiony <= mouse_y <= positiony + bheight:
                level = 2
            elif positionx3 <= mouse_x <= positionx3 + bwidth and positiony <= mouse_y <= positiony + bheight:
                level = 3
