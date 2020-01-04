from pynput.keyboard import Key, Listener, KeyCode


MY_HOT_KEYS = [
    {'function': {}}
]


def key_pressed(key):
    print("pressed {}".format(key))


def key_released(key):
    print("released {}".format(key))

    if key == Key.esc:
        return False


with Listener(on_press=key_pressed, on_release=key_released) as Listener:
    Listener.join()
