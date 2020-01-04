from pynput.keyboard import Key, Listener, KeyCode
import subprocess
import os
f = Key.cmd_l
MY_HOT_KEYS = [
    {'function1': {Key.cmd_l, Key.alt_l, KeyCode(char= "~")}},

    {'function2': {Key.shift_l, Key.cmd_l, KeyCode(char='b')}},

    {'function3': {Key.shift_l, Key.cmd_l,  Key.media_next}},

]
current_keys = set()

def function1():
    subprocess.call(
        ["/System/Applications/Dictionary.app"]
    )
    print('함수1 호출.....................................')

def function2():
    print('함수2 호출.....................................')

def function3():
    print('함수3 호출.....................................')


def key_pressed(key):
    print("pressed {}".format(key))
    for data in MY_HOT_KEYS:
        FUNCTION = list(data.keys())[0]

        KEYS = list(data.values())[0]




        if key in KEYS:
            current_keys.add(key)

            # if all(k in current_keys for k in KEYS):
            #     function = eval(FUNCTION)
            #     function()


            checker = True
            for k in KEYS:
               if k not in current_keys:
                   checker = False
                   break
            if checker:
                function = eval(FUNCTION)

                function()





def key_released(key):
    print('Released {}'.format(key))
    if key in current_keys:
        current_keys.remove(key)

    if key == Key.esc:
        return False

# with Listener(on_press=key_pressed, on_release=key_released) as lsner:
#     lsner.join()

with Listener(on_press=key_pressed, on_release= key_released) as test:
    test.join()



