''' для запуска скрипта замените путь к файлу в переменной rdir (6 строка).
    в 7 строке укажите название тестируемого файла (по умолчанию 1.txt)
     результат работы программы будет находиться по пути, указанному в rdir, с именем файла result.txt '''

tp,trp,a,c=tuple(),tuple(),0,0 #tp - хранит 1 строку по горизонтали, trp - хранит имена комбинаций
rdir='E:/Stepik/'
with open(rdir+'1.txt','r') as out_file:
    with open(rdir + 'result.txt','w') as new_file:
        line=out_file.readline().strip()
        while True:
            line=out_file.readline().strip().split()
            if len(line)==2:
                n,l=int(line[0]),int(line[1])#число и длина последовательностей
            if len(line)==1:
                line=line[0]
                tp+=(line,) #добавляет каждую строку, равную длине последовательности, в кортеж
                c+=1
                if c==n: #вход, когда все последовательности записаны в кортеж
                    m,d='',{'__':'__'}                    
                    for i in range(l): # перебор по длине
                        for j in range(n): # перебор по вертикали
                            m+=str(tp[j][i]) # беру вертикальный срез символов из строк  
                        if m in d.values():
                            for k,v in d.items():
                                if m==v:
                                    trp+=(str(k),) #добавить номер комбинации в другой кортеж                                     
                        else:
                            a+=1
                            d[a]=m                            
                            trp+=(str(a),)
                        m=''                                                                            
                    new_file.write(str(a)+'\n')
                    new_file.writelines(i+' ' for i in trp)
                    new_file.write('\n')    
                    tp,trp,d,a,c=tuple(),tuple(),{'__':'__'},0,0
            if not line:
                break

