from pynput import keyboard


class User:
    def __init__(self):
        self.up_callback = 0
        self.down_callback = 0
        self.right_callback = 0
        self.left_callback = 0

    def set_callbacks(self, up_callback, down_callback, right_callback, left_callback):
        self.up_callback = up_callback
        self.down_callback = down_callback
        self.right_callback = right_callback
        self.left_callback = left_callback

    def on_press(self, key):
        if key == keyboard.Key.up and self.up_callback != 0:
            self.up_callback()

        elif key == keyboard.Key.down and self.down_callback != 0:
            self.down_callback()

        elif key == keyboard.Key.right and self.right_callback != 0:
            self.right_callback()

        elif key == keyboard.Key.left and self.left_callback != 0:
            self.left_callback()

    def on_release(self, key):
        pass

    def start(self):
        listener = keyboard.Listener(on_press=self.on_press,
                                     on_release=self.on_release)
        listener.start()

