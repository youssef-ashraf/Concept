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
            
    def getBlank(self):  return self.tiles[-1]      
    def setBlank(self,pos): self.tiles[-1] = pos 
    opentile = property(getBlank,setBlank)
    
    def switch(self,tile):self.tiles[self.tiles.index(tile)] , self.opentile , self.prev = self.opentile , tile , self.opentile
    def in_grid(self,tile): return tile[0]>=0 and tile[0]<self.gs[0] and tile[1]>=0 and tile[1]<self.gs[1]
    def adjacent(self): x,y = self.opentile ; return (x-1 , y) ,(x+1 , y) ,(x, y-1),(x , y+1)


     def random(self):
            adj = self.adjacent()
        self.switch(random.choice([pos for pos in adj if self.in_grid(pos) and pos != self.prev]))
    
    def update(self , df):
        s = self.speed * df
        mouse = pygame.mouse.get_pressed()
        mpos = pygame.mouse.get_pos()
        
        if mouse[0]:  
            x,y = mpos[0]%(self.ts+self.ms),mpos[1]%(self.ts+self.ms)
            if x>self.ms and y>self.ms:
                tile = mpos[0]//self.ts , mpos[1]//self.ts #tile
                
                if self.in_grid(tile) and (tile in self.adjacent()):self.switch(tile)
        
    
    def draw(self , screen):
        for i in range(self.tiles_len):
            x , y = self.tilepos_x[self.tiles[i][0]] ,self.tilepos_y[self.tiles[i][1]]
            screen.blit(self.images[i] , (x,y))
            
def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_caption('Slide Game')
    size = 6
    padding = 5
    square_sz = 100
    screen = pygame.display.set_mode((size*square_sz+(padding*(size + 1)), size*square_sz+(padding*(size + 1)))) #screen size
    fpsclock = pygame.time.Clock()
    program  = SlidePuzzle((size,size) , square_sz , padding)
    for i in range(200):
            program.random()

 while True:
        df = fpsclock.tick()/1000
        
        screen.fill((0,0,0)) #color
        program.draw(screen)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit() ; pygame.quit; sys.exit()
        program.update(df)


main()           
