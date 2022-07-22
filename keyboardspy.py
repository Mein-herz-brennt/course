import keyboard
from abc import ABCMeta, abstractmethod


class KeyboardListener(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get_keys(self, key):
        pass


class Observable(metaclass=ABCMeta):
    def __init__(self, observer, observer2):
        self.observers = [observer]

    def notify_observers(self, key):
        for item in self.observers:
            item.get_keys(key)


class KeyLogger(KeyboardListener):
    def __init__(self):
        super().__init__()
        self.key_list = []

    def get_keys(self, key):
        self.key_list.append(key)

    def logging(self):
        for key in self.key_list:
            print(key)


class KeyFileLogger(KeyboardListener):
    def __init__(self):
        super().__init__()
        self.key_list = []

    def get_keys(self, key):
        self.key_list.append(key)

    def key_write(self):
        f = open("pushed_keys.txt", 'a')
        for key in self.key_list:
            f.write(key + '\n')
        f.close()


class KeyboardSpy(Observable):

    def __init__(self, observer: KeyboardListener, observer2: KeyboardListener):
        super().__init__(observer, observer2)
        self.obs = observer
        self.obs2 = observer2

    def header(self):
        while True:

            key = keyboard.read_key()
            if keyboard.is_pressed("ctrl") and key == "q":  # To finish use "ctrl+q".
                print('Finished!')
                break
            else:

                obs = Observable(self.obs, self.obs2)
                obs.notify_observers(key)


if __name__ == "__main__":
    keylogger = KeyLogger()
    keyfilelogger = KeyFileLogger()
    keyboardSpy = KeyboardSpy(keylogger, keyfilelogger)
    keyboardSpy.header()
    keylogger.logging()
    keyfilelogger.key_write()
