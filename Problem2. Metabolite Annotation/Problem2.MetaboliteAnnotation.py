''' для запуска скрипта замените путь к файлу в переменной rdir (6 строка).
    в 7 строке укажите название тестируемого файла (по умолчанию 1.txt)
     результат работы программы будет находиться по пути, указанному в rdir, с именем файла result.txt '''

import numpy as np
rdir='C:/user/'
with open(rdir+'1.txt','r') as out_file:
    with open(rdir + 'result.txt','w') as new_file:
        line=out_file.readline().strip()#кол-во тестов
        for tests in range(int(line)):
            line=out_file.readline().strip().split()#читать строку с кол-вом значений
            array1 = np.fromstring(out_file.readline(), dtype=float, sep=' ')#читать все метаболиты
            array2 = np.fromstring(out_file.readline(), dtype=float, sep=' ')#читать все аддукты
            signal=[float(i) for i in out_file.readline().strip().split()]#брать каждый сигнал и передавать в функцию ниже
            for i in signal:#делаем перебор по сигналам
                ar2,dct=1,dict()#ar2-порядковый номер элемента в 2 массиве, начиная с 1-го
                for val in np.nditer(array2):#перебор значений в массиве 2, начиная с 1-го
                    n=val+array1# n-одномерный массив, состоящий из суммы массива 1 и числа val из массива 2
                    n=np.abs(n-i)# здесь n перезаписываю как массив из дельт (все метаболиты + 1 аддукт - 1 сигнал) 
                    ind = np.argmin(n)# находим индекс минимального значения в массиве n (напр. 13)
                    dct[ar2]=[ind+1,n[ind]]# добавляем в словарь: ключ - порядковый номер эл-та массива 2; в значение - список из: индекса минимального эл-та массива 1 и его значения (т.е. напр. [13,0.000473])
                    ar2+=1# увеличиваем порядковый номер элемента в 2 массиве (т.е. типа берем следующий эл-т) 
                sorted_tuples = sorted(dct.items(), key=lambda x: x[1][1])# сортируем все минимальные значения и находим из них самое минимальное. Сортировка идет по 2 элементу в списке значений (напр. 2:[13,0.000473],18:[4,0.000478],5:[133,0.000489]...). На выходе получаем кортеж.
                new_file.write(str(sorted_tuples[0][1][0])+' '+str(sorted_tuples[0][0])+'\n')# здесь просто обращаемся по нужным индексам этого кортежа, чтобы записать в файл.
                
