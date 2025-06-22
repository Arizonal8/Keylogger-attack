from pynput.mouse import Controller
# Changing mouse position (left to right, top to bottom)
# from top-left of the screen you can imagine the top-left to be (0,0)
def controlmouse():
    mouse = Controller()
    mouse.position = (100,200)

controlmouse()