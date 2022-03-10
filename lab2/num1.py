'''Найдите с помощью алгоритма полного перебора пятибуквенные пароли, соответствующие следующим хэш-значенияи SHA-256 и выведите их на экран:'''
import hashlib as h
import threading as th
import time
from datetime import timedelta

class obj:
    def __init__(self, a = 'a', b = '', c= '', d= '', e= ''):
        self.s = a+b+c+d+e

    def __hash__(self):
            m = h.sha256()
            m.update(self.s.encode('ascii'))
            return m.hexdigest()


def cicle(s,e):
    b = '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad'
    c = '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b'
    d = '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f'
    al = 'abcdefghijklmnopqrstuvwxyz'
    for u in al[s:e]:
        for j in al:
            for k in al:
                for f in al:
                    for y in al:
                        word = obj(u, j, k, f, y)
                        if (word.__hash__() == c) or (word.__hash__() == b) or (word.__hash__() == d):
                            print(word.s,th.current_thread().name)
                            return 1



al = "abcdefghijklmnopqrstuvwxyz"
x = int(input("Сколько потоков использовать >>"))
if x > 10:
    x = 10
elif x < 1:
    x = 1

st = 0
en = 26 // x + 26 % x

threads = []
th_time = []

for i in range(x):
    t = th.Thread(target=cicle, args=(st,en))
    threads.append(t)
    start_time = time.monotonic()
    t.start()
    th_time.append(start_time)
#    print(al[st:en], type(al[st:en]))
    st = en
    en = en + 26 // x
#for thr in threads:
for i in range(x):
    #thr.join()
    threads[i].join()
    end_time = time.monotonic()
    th_time[i] = end_time - th_time[i]
#print(timedelta(seconds=end_time - start_time))
for i in range(x):
    print(timedelta(seconds=th_time[i]))
#mbr что такое файловая система чем отличается поток от процесса
