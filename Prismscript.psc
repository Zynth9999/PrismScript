$use builtin.twodee as twod
//The built in 2d engine is pygame ported to psc with psc sytax
bg_color = (234, 212, 252)

screen = twod.engine.display.set_mode((300,300))
screen.fill(background_colour) 

twod.engine.display.set_caption('prism script 2d engine!')
twod.engine.display.flip()

running = True

while running: 
    for event in twod.engine.event.get():  
        if event.type == twod.engine.QUIT: 
            running = False
