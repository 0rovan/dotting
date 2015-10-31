from time import sleep
from threading import Thread,Event
from sys import stdout


class Dotter(object):
    def __init__(self,delay=100,symbol='.'):
        self.event=Event()
        self.delay=delay
        self.symbol=symbol
        self.status=False
    def __loop(self):
        while not self.event.is_set():
            stdout.write(self.symbol)
            stdout.flush()
            sleep(self.delay/1000)
    def start(self):
        if not self.status:
            self.event.clear()
            Thread(target=self.__loop).start()
            self.status=True
    def stop(self,newLine=True):
        if self.status:
            self.event.set()
            if newLine:
                stdout.write('\n')
            self.status=False
    def set(self,delay=None,symbol=None):
        if delay!=None:
            self.delay=delay
        if symbol!=None:
            self.symbol=symbol
        if self.status:
            self.stop(False)
            self.start()
