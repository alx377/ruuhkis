'''
Created on Mar 9, 2014

@author: Administrator
'''
import sfml as sf
import Rusher

# create the main window
window = sf.RenderWindow(sf.VideoMode(1200, 800), "pySFML Window")


circle = Rusher.Rusher(sf.Vector2(10.0,20.0))
# start the game loop
while window.is_open:
    # process events
    for event in window.events:
        # close window: exit
        if type(event) is sf.CloseEvent:
            window.close()
    

    circle.update_pos()

    circle.draw(window)
    window.display() # update the window
    window.clear() # clear screen
