from pynput import keyboard


class User:
    def __init__(self, up_callback, down_callback, right_callback, left_callback):
        self.up_callback = up_callback
        self.down_callback = down_callback
        self.right_callback = right_callback
        self.left_callback = left_callback

    def on_press(self, key):
        if key == keyboard.Key.up:
            self.up_callback()

        elif key == keyboard.Key.down:
            self.down_callback()

        elif key == keyboard.Key.right:
            self.right_callback()

        elif key == keyboard.Key.left:
            self.left_callback()

    def on_release(self, key):
        pass

    def start(self):
        listener = keyboard.Listener(on_press=self.on_press,
                                     on_release=self.on_release)
        listener.start()

