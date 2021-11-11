import pygame, sys, random, time, os
from pygame.locals import *
import pygame.camera
# IMPORT CLASSES
from GameOfLife import GameOfLife
from PredatorAndPrey import PredatorAndPrey
from BriansBrain import BriansBrain

pygame.init()

cells_x = 70
cells_y = 40

res = 20
frame_rate = 15
cells = [[0 for x in range(cells_y)] for y in range(cells_x)]

display = pygame.display.set_mode((cells_x*res-res+2, cells_y*res-res+2))
pygame.display.set_caption('Cellular Automata')
clock = pygame.time.Clock()
display.fill(pygame.Color("black"))
pygame.font.init()

class Main:

    def main(self):
        # HEADING
        heading = pygame.font.Font('fonts/SourceCode.otf',80)
        TextSurf = heading.render("CELLULAR AUTOMATA", True, (255,255,255))
        TextRect = TextSurf.get_rect()
        TextRect.center = ((cells_x*res/2),(cells_y*res/4-100))
        display.blit(TextSurf, TextRect)

        # FOOTER
        credits = pygame.font.Font('fonts/SourceCode.otf',20)
        TextSurf = credits.render("Luke Wilde", True, (255,255,255))
        TextRect = TextSurf.get_rect()
        TextRect.center = ((cells_x*res-90),(cells_y*res-25))
        display.blit(TextSurf, TextRect)

        # GAME OF LIFE
        button_gol = pygame.Rect(0, 0, 450, 60)
        button_gol.center = ((cells_x*res/2+250),(cells_y*res/3))

        button_text = pygame.font.Font("fonts/SourceCode.otf",30)
        gol_TextSurf = button_text.render("CONWAY'S GAME OF LIFE", True, (0, 0, 0))
        gol_TextRect = gol_TextSurf.get_rect()
        gol_TextRect.center = ((cells_x*res/2+250),(cells_y*res/3))
        display.blit(gol_TextSurf, gol_TextRect)

        # PREDATOR PREY
        button_pvp = pygame.Rect(0, 0, 450, 60)
        button_pvp.center = ((cells_x*res/2-250),(cells_y*res/3))

        button_text = pygame.font.Font("fonts/SourceCode.otf",30)
        pvp_TextSurf = button_text.render("PREDATOR AND PREY", True, (0, 0, 0))
        pvp_TextRect = pvp_TextSurf.get_rect()
        pvp_TextRect.center = ((cells_x*res/2-250),(cells_y*res/3))
        display.blit(pvp_TextSurf, pvp_TextRect)

        # BRIANS BRAIN
        button_bb = pygame.Rect(0, 0, 450, 60)
        button_bb.center = ((cells_x*res/2-250),(cells_y*res/2))

        button_text = pygame.font.Font("fonts/SourceCode.otf",30)
        bb_TextSurf = button_text.render("BRIAN'S BRAIN", True, (0, 0, 0))
        bb_TextRect = bb_TextSurf.get_rect()
        bb_TextRect.center = ((cells_x*res/2-250),(cells_y*res/2))
        display.blit(bb_TextSurf, bb_TextRect)


        while True:
            gol_colour = (255,255,255)
            pvp_colour = (255,255,255)
            bb_colour = (255,255,255)

            mouse_pos = pygame.mouse.get_pos()
            # GAME OF LIFE
            if button_gol.collidepoint(mouse_pos):
                gol_colour = (66, 134, 244)
                pygame.draw.rect(display, gol_colour , button_gol)

            # PREDATOR AND PREY
            if button_pvp.collidepoint(mouse_pos):
                pvp_colour = (66, 134, 244)
                pygame.draw.rect(display, pvp_colour , button_pvp)

            # PREDATOR AND PREY
            if button_bb.collidepoint(mouse_pos):
                bb_colour = (66, 134, 244)
                pygame.draw.rect(display, bb_colour , button_bb)

            # GAME OF LIKE
            pygame.draw.rect(display, gol_colour , button_gol)
            display.blit(gol_TextSurf, gol_TextRect)

            # PREDATOR AND PREY
            pygame.draw.rect(display, pvp_colour , button_pvp)
            display.blit(pvp_TextSurf, pvp_TextRect)

            # BRIANS BRAIN
            pygame.draw.rect(display, bb_colour , button_bb)
            display.blit(bb_TextSurf, bb_TextRect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                # IF GAME OF LIFE IS CLICKED
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button_gol.collidepoint(mouse_pos):
                        # record = input('Record y/n? : ')
                        # Pass through random values determined by HEX
                        # hexval = 'c6c2d51ed240a64f322fb7c7c582d6e5fdcaa933'
                        # decimal = int(hexval, 16)
                        
                        # new_cells_x = (decimal % 5) * random.randint(5,10)
                        # new_cells_y = (decimal % 5) * random.randint(5,10)

                        # Looks much nicer
                        new_cells_x = 30
                        new_cells_y = 30
                        
                        
                        GameOfLife.gameOfLife(self, new_cells_x, new_cells_y, res, frame_rate, cells, clock)
                # IF PREDATOR AND PREY IS CLICKED
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button_pvp.collidepoint(mouse_pos):
                        PredatorAndPrey.runAutomaton(self)
                # IF PREDATOR AND PREY IS CLICKED
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button_bb.collidepoint(mouse_pos):
                        BriansBrain.main(self)

            pygame.display.update()
            clock.tick(frame_rate)

if __name__ == "__main__":
    start = Main()
    start.main()