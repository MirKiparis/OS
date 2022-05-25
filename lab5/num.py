import threading
import time
from threading import Thread


mythreadies = []
importantVar = 0  # if 1 то не выводится и не работает


class MyThread(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.alive = 0  # заблокирован - (-1) ожидание - (0) в процессе - (1)
        self.prior = 5  # приоритет
        self.res = 0  # результат вычислений

    def run(self):
        print("Thread ", self.num, '\n')
        self.wait()

    def wait(self):
        while not self.alive:
            pass
        self.go()

    def go(self):
        for i in range(self.prior):
            self.res += i
            time.sleep(1)
        self.alive = 0
        self.wait()

    def changePrior(self, n):
        self.prior = n

    def block(self):
        self.alive = -1


for i in range(3):
    t = MyThread(i)
    mythreadies.append(t)


def zprint():
    print('\n')
    for i1 in range(3):
        if mythreadies[i1].alive == -1:
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
    proverka = mythreadies[0].alive | mythreadies[1].alive | mythreadies[2].alive
    return proverka  # если все потоки стоят то 0 иначе 1


def runny():
    global importantVar
    for i in range(3):
        mythreadies[i].start()
    while True:
        for i in range(3):
            zprint()
            while only() or importantVar:
                pass
            mythreadies[i].alive = 1


def inquit():
    global importantVar
    '''
    ввести номер потока и приоритет изменится время и результат
    если ввести номер потока и B то поток окончательно заблокируется
    '''
    while True:
        q = input()
        if q == '1' or q == '2' or q == '3':
            importantVar = 1
            q2 = input()
            if q2 == 'b' or q2 == 'B':
                mythreadies[int(q)].alive = -1
                importantVar = 0
            else:
                try:
                    q2 = int(q2)
                    mythreadies[int(q)].changePrior(int(q2))
                    importantVar = 0
                except ValueError:
                    print("\nНЕВЕРНЫЙ ВВОД. Заново\n")
                    importantVar = 0
        else:
            print("askjdfhajksdfhkjasdhflkasjdhflkasjdhfkajdsfhlka")


inquit = Thread(target = inquit)
runny()
