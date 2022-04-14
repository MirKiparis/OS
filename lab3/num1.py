import threading as th
import random as r

import queue

locker = th.RLock()
truesignal = True
stoppr = False
stoppot = False
que = queue.Queue(maxsize=200)
n = ''

def putq(quet):
    while truesignal and n != 'q':
      #with locker:
        if not stoppr:
            t = r.randint(0, 99)
            quet.put(t)
            print("%15s%3d%10s%d" % (th.current_thread().name, quet.qsize(), "- добавлен:",t))
            time.sleep(0.5)
        if n == 'q':
            break


def getq(quet):
    while truesignal or not quet.empty():
       with locker:
        if not stoppot:
            t = quet.get()
            print("%15s%3d%10s%d" % (th.current_thread().name, quet.qsize(),"- удален:",t))
            time.sleep(0.25)
        if n == 'q' and quet.empty():
            break



def signal():
    print("Нажмите q чтобы завешить процесс >>")
    global truesignal, stoppr, stoppot, n, que
    while truesignal :
            if n == 'q':
                stoppr = True
                stoppot = False
                break
            else:
                q = que.qsize()
                if q == 0 or que.empty():
                    stoppot = True
                    stoppr = False
                elif q <= 80 and q > 0:
                    stoppr = False
                    stoppot = False
                elif q >= 100:
                    stoppot = False
                    stoppr = True
                elif q<100 and q>80:
                    stoppr = True
                    stoppot = False



def button():
    global truesignal, stoppr, stoppot,n
    while truesignal:
        n = input(" >>> ")
        print("\nГОТОВО\n")
        if n == 'q':
            stoppr = True
            stoppot = False
            truesignal = False
            break


pr = list()
pot = list()
sin = th.Thread(target=button, args=()).start()
signal = th.Thread(target=signal, args=()).start()

for i in range(3):
        thr = th.Thread(target = putq, args = (que,), name = f"Производитель-{i+1}")
        pr.append(thr)
        #thr.start()
for i in range(2):
        thrt = th.Thread(target = getq, args = (que,), name = f"Потребитель-{i+1}")
        pot.append(thrt)
        #thrt.start()
#    if not truesignal:
       # break
for i in pr:
    i.start()
for i in pot:
    i.start()
while truesignal and n != 'q':
    if n == 'q':
        break

