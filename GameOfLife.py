import pygame, sys, random, time
from pygame.locals import *


class GameOfLife:

    def gameOfLife(self, cells_x, cells_y, res, frame_rate, cells, clock):
        display = pygame.display.set_mode((cells_x*res-res+2, cells_y*res-res+2))
        display.fill(pygame.Color("black"))
        # time.sleep(2)
        colours = [[215, 169, 227], [139, 190, 232], [168, 213, 186]]
        session = True
        cell_size = 15  
        start_cells = 500
        gen = 0

        for c in range(start_cells):
            rand_x = random.randrange(0,cells_x)
            rand_y = random.randrange(0,cells_y)
            cells[rand_x][rand_y] = 1
            col = random.randrange(0,3)
            pygame.draw.rect(display, (colours[col][0], colours[col][1], colours[col][2]), (rand_x*res,rand_y*res,cell_size,cell_size), 0)
        pygame.display.update()


        while session:
            gen += 1
            pygame.display.set_caption('Conway\'s Game Of Life - Generation '+ str(gen))

            # if(option == 'y'):
            #     filepath = 'frames/'+str(gen)+'.bmp'
            #     pygame.image.save(display, filepath)
            
            clock.tick(frame_rate)
            display.fill(pygame.Color("black"))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();

            new = [[0 for x in range(cells_y)] for y in range(cells_x)]

            for y in range(cells_y-1):
                for x in range(cells_x-1):
                    if cells[x-1][y-1] + cells[x][y-1] + cells[x+1][y-1] + cells[x-1][y] + cells[x+1][y] + cells[x-1][y+1] + cells[x][y+1] + cells[x+1][y+1] < 2 and cells[x][y] == 1:
                        new[x][y] = 0
                    elif cells[x-1][y-1] + cells[x][y-1] + cells[x+1][y-1] + cells[x-1][y] + cells[x+1][y] + cells[x-1][y+1] + cells[x][y+1] + cells[x+1][y+1] == 2 or cells[x-1][y-1] + cells[x][y-1] + cells[x+1][y-1] + cells[x-1][y] + cells[x+1][y] + cells[x-1][y+1] + cells[x][y+1] + cells[x+1][y+1] == 3 and cells[x][y] == 1:
                        new[x][y] = cells[x][y]
                    elif cells[x-1][y-1] + cells[x][y-1] + cells[x+1][y-1] + cells[x-1][y] + cells[x+1][y] + cells[x-1][y+1] + cells[x][y+1] + cells[x+1][y+1] > 3 and cells[x][y] == 1:
                        new[x][y] = 0
                    elif cells[x-1][y-1] + cells[x][y-1] + cells[x+1][y-1] + cells[x-1][y] + cells[x+1][y] + cells[x-1][y+1] + cells[x][y+1] + cells[x+1][y+1] == 3 and cells[x][y] == 0:
                        new[x][y] = 1

            
            for i in range(cells_y):
                col = random.randrange(0,3)
                for j in range(cells_x):
                    cells[j][i] = new[j][i]
                    if cells[j][i] == 1:
                        pygame.draw.rect(display, (colours[col][0], colours[col][1], colours[col][2]), (j*res+2,i*res+2,cell_size,cell_size), 0)
                        
            pygame.display.update()