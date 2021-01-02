import pygame , os , sys , random , math

class SlidePuzzle:
    def __init__(self , gs , ts , ms):
        self.gs,self.ts,self.ms = gs,ts,ms
        
        self.tiles_len = (gs[0] * gs[1]) -1 # X_size * Y_size - The free playing block
        
        self.tiles = [(x,y) for y in range(gs[1]) for x in range(gs[0])]
        
        self.tilepos_x , self.tilepos_y= [x*(ts+ms)+ms  for x in range(gs[0])] , [y*(ts+ms)+ms  for y in range(gs[1])]
         
        self.font = pygame.font.Font(None , 80)
        
        self.prev = None
        
        self.speed = 200
        
        self.rect = pygame.Rect(0,0,gs[0]*(ts+ms)+ms,gs[1]*(ts+ms)+ms)
        
        
        pic = pygame.transform.smoothscale(pygame.image.load('imag.jpg'),self.rect.size)
        
        
                self.images = []
        for i in range(self.tiles_len):   
            x1 , y1 = self.tilepos_x[self.tiles[i][0]] ,self.tilepos_y[self.tiles[i][1]]
            image = pic.subsurface(x1 , y1 , ts ,ts) 
            text = self.font.render(str(i+1),2,(0,0,0))
            x2 , y2 = text.get_size()
            image.blit(text , ((ts-x2)/2,(ts-y2)/2))
            self.images.append(image)