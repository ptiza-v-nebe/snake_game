from pynput import keyboard


# this class represents the actual bridge to the users keyboard
class User:
    def __init__(self):
        self.up_callback = 0
        self.down_callback = 0
        self.right_callback = 0
        self.left_callback = 0

    # callbacks for controlling
    # each callback is called if one of the direction keys is pressed
    def set_callbacks(self, up_callback, down_callback, right_callback, left_callback):
        self.up_callback = up_callback
        self.down_callback = down_callback
        self.right_callback = right_callback
        self.left_callback = left_callback

    # the callbacks are called on specific key press detection
    def on_press(self, key):
        if key == keyboard.KeyCode().from_char('w') and self.up_callback != 0:
            self.up_callback()

        elif key == keyboard.KeyCode().from_char('s') and self.down_callback != 0:
            self.down_callback()

        elif key == keyboard.KeyCode().from_char('d') and self.right_callback != 0:
            self.right_callback()

        elif key == keyboard.KeyCode().from_char('a') and self.left_callback != 0:
            self.left_callback()

    # do nothing on release
    def on_release(self, key):
        pass

    # start the keyboard listener thread and return
    def start(self):
        listener = keyboard.Listener(on_press=self.on_press,
                                     on_release=self.on_release)
        listener.start()

