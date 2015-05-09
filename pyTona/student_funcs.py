import os
import random
import threading
import time


factorials = None
size = None
dir_height = None


class GeneralThreader(threading.Thread):
    def __init__(self, func, *args, **kwargs):
        super(GeneralThreader, self).__init__(*args, **kwargs)
        self.func = func
        self._stop = threading.Event()
        self.result = None

    def stop(self):
        self._stop.set()

    def run(self):
        self.result = self.func()

class FactorialFinder(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(FactorialFinder, self).__init__(*args, **kwargs)
        self.fac_list = [1]
        self._stop = threading.Event()
        self.num_facs = 0

    def stop(self):
        self._stop.set()

    def run(self):
        self.num_facs = 0
        while not self._stop.isSet() and self.num_facs <= 1000:
            self.num_facs += 1
            self.fac_list.append(self.fac_list[-1] * self.num_facs)
            time.sleep(.02)


def gen_fact(index):
    index = int(index)
    global factorials
    if factorials is None:
        factorials = FactorialFinder()
        factorials.start()

    if index > 1000:
        return "Too High"
    elif index > factorials.num_facs:
        return "Multiplying"
    else:
        return factorials.fac_list[index]

def gen_story():
    letter_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !.,;:\"'?"

    f = open("StoryTime!.txt", 'w')

    for i in range(random.randint(250000, 500000)):
        f.write(random.choice(letter_set))

    f.close()

    return "You can read it at StoryTime!.txt"


def find_size():
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)

    return total_size


def get_size():
    global size

    if size is None:
        size = GeneralThreader(find_size)
        size.start()


    if size.result is None:
        return "Let me get that for you."

    else:
        return size.result

def find_height():
    dirs = [f[0] for f in os.walk(".")]
    max_h = 1
    for d in dirs:
        h = len(d.split("\\"))
        if h > max_h:
            max_h = h

    return max_h

def get_height():
    global dir_height

    if dir_height is None:
        dir_height = GeneralThreader(find_height)
        dir_height.start()

    if dir_height.result is None:
        return "I'm measuring"

    else:
        return str(dir_height.result) + " feet"

