import threading
import time
from threading import Thread
import random


mythreadies = []
importantVar = 0  # if 1 то не выводится и не работает


class MyThread(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.alive = 0  #  ожидание - (0) в процессе - (1)
        self.prior = 5  # приоритет
        self.res = 0  # результат вычислений
        self.unblocked = 1
        self.col = 0

    def run(self):
        self.wait()

    def wait(self):
        while self.unblocked:
            while not self.alive:
                pass
            self.go()
        self.stop()

    def stop(self):
        while True:
            pass

    def go(self):
        while(self.alive):
            t = random.randint(0,1)
            self.res = (self.res * self.col + t)/(self.col + 1)
            self.col += 1
        self.wait()

    def changePrior(self, n):
        self.prior = n

    def block(self):
        self.unblocked = 0



def zprint():
    print('\n')
    for i1 in range(3):
        if mythreadies[i1].unblocked == 0:
            condition = 'block'
        elif mythreadies[i1].alive == 0:
            condition = ' wait'
        else:
            condition = '   go'
        print('_' * 60)
        print('Thread ', mythreadies[i1].num, ' | ', condition, ' | ', mythreadies[i1].res)
    print('_' * 60)
    print('\n' * 5)


def only():
    proverka = mythreadies[0].alive or mythreadies[1].alive or mythreadies[2].alive
    return proverka  # если все потоки стоят то 0 иначе 1



def inquit():
    global importantVar
    while True:
        q = input()
        print(1)
        try:
            q = int(q)
            if q == 0 or q == 1 or q == 2:
                importantVar = 1
                q2 = input()
                try:
                    q2 = int(q2)
                    if q2 == 0:
                        mythreadies[q].block()
                        importantVar = 0
                    else:
                        mythreadies[q].changePrior(q2)
                        importantVar = 0
                        zprint()
                except ValueError:
                    print("\nНЕВЕРНЫЙ ВВОД. Заново\n")
                    importantVar = 0
            else:
                print("askjdfhajksdfhkjasdhflkasjdhflkasjdhfkajdsfhlka")
        except ValueError:
            print("\nНЕВЕРНЫЙ ВВОД. Заново\n")


def timy(n):
    t_start = time.time()
    t_end = 0
    while(t_end < (t_start + n)):
        t_end = time.time()
    return 1


def runny():
    global importantVar
    for i in range(3):
        mythreadies[i].start()
    while True:
        for i in range(3):

            if mythreadies[i].unblocked == 0:
                continue
            while only() or importantVar:
                pass
            mythreadies[i].alive = 1
            zprint()
            if timy(mythreadies[i].prior):
                mythreadies[i].alive = 0



for i in range(3):
    t = MyThread(i)
    mythreadies.append(t)
inquit = Thread(target= inquit)
inquit.start()
runny()

