import builtin.twodee as twod
#The built in 2d engine is pygame ported to psc with psc sytax
bg_color = (234, 212, 252)
logo = twod.engine.image.load('PrismScript.png')

screen = twod.engine.display.set_mode((1024,1024))
screen.fill(bg_color) 

twod.engine.display.set_caption('prism script 2d engine!')
screen.blit(logo, (x,y))
twod.engine.display.flip()

running = True
events = twod.engine.event.get()

while running: 
    
    for event in twod.engine.event.get():  
        if event.type == twod.engine.QUIT: 
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == twod.engine.K_a:
            x 
        if event.key == twod.engine.K_d:
            location += 1
