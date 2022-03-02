'''Найдите с помощью алгоритма полного перебора пятибуквенные пароли, соответствующие следующим хэш-значенияи SHA-256 и выведите их на экран:'''
import hashlib as h
class obj:
    def __init__(self, a = 'a', b = '', c= '', d= '', e= ''):
        self.s = a+b+c+d+e

    def __hash__(self):
            m = h.sha256()
            m.update(self.s.encode('ascii'))
            return m.hexdigest()


al = "abcdefghijklmnopqrstuvwxyz"
b = '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad'
c = '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b'
d = '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f'

for i in al:
    for j in al:
        for k in al:
            for f in al:
                for t in al:
                    word = obj(i, j, k, f, t)
                    if (word.__hash__() == c)or(word.__hash__() == b)or(word.__hash__() == d):
                        print(word.s)
