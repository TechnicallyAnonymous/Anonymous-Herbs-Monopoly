import pygame,random

import mainboard

pygame.init()

display_width = 1600
display_height = 800

white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
red = (255,50,0)
blue = (0,0,255)
green = (0,255,0)
back = (100,10,100)

fps = 100
clock = pygame.time.Clock()

a=0
b=0
turn = True

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Ved - Ayur")
pygame.display.update()
clock.tick(fps)

def addimage(link,x,y):                              #function to draw image with its left top border at (x,y) pixel(origin is at top left of screen and y axis down and x axis right)
     img = pygame.image.load(link)
     gameDisplay.blit(img, [x,y])


def button(msg,x,y,l,h,ac,ic,function,tc):         #this function creates a button and provides functions to be done on clicking it 
    
    pygame.draw.rect(gameDisplay, ic, [x,y,l,h])
    mouse = pygame.mouse.get_pos()                  #keep track of cursor location on screen
    click = pygame.mouse.get_pressed()            #keep track of mouse click
        
    if x < mouse[0] < x+l and y < mouse[1] < y+h:
           pygame.draw.rect(gameDisplay, ac, [x,y,l,h])
           if click[0]==1:                                 
                
                if function == "next":
                    mainboard.mainscreen()

    
                if function == "quit1":
                    quit()
    _font = pygame.font.Font('freesansbold.ttf',20)
    text_in_box(msg, _font,tc,x,y,l,h)                        
   

def text_in_box(text, font,tc,x,y,l,h):                    
    textSurface = font.render(text, True, tc)
    textRect = textSurface.get_rect()
    textRect.center = (x+l/2,y+h/2)
    gameDisplay.blit(textSurface, textRect)

def message_to_screen(msg, color,x,y,s):            
    font = pygame.font.SysFont(None, s)
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x,y])

def rolldice():                                      
     global a,b
     global turn 
     a = random.randrange(1,7)
     b = random.randrange(1,7)
     turn = False
     pygame.display.update()
     return a+b

