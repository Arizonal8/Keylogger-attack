from pynput.keyboard import Controller
# Typing where ever the coursor is located
def controlkeyboard():
    keyboard = Controller()
    keyboard.type("Access granted")

controlkeyboard()