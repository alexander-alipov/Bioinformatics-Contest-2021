''' для запуска скрипта замените путь к файлу в переменной rdir (51 строка).
    в 52 строке укажите название тестируемого файла (по умолчанию test1)
    результат работы программы будет находиться по пути, указанному в rdir, с именем файла result.txt '''


# Проблема с решением 3-7 тестов. А именно, переполняется память.
# 3 тест занимает 3.3 GB за счет данных в переменной path_diseases
# Суть идеи в том, чтобы записывать пути для каждый вершины,
# например, для каждой вершины в diseases записывается свой путь
# через функцию ancestors и все эти пути сохраняются в path_diseases
# за основу взят алгоритм LCA - "Storing root to n1 and root to n2 paths"
# пример реализации здесь: https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
# и здесь показана упращенная версия: http://pythoshka.ru/p432.html

import numpy as np

def read():
    m,lst=f.readline(),[] #кол-во болезней,пациентов
    for i in range(int(m)):
        line=f.readline().split()
        lst+=[[int(j) for j in line]]
    return lst

def ancestors(s):
    result=[]
    result.append(s)
    while s in keys:
        s=dct[s]
        result.append(s)
    return result
            
def inform_cont(pat,path_diseases):
    dis_k_scores=np.array([0])
    scores=[0]
    dis_score=[]
    for i in pat:
        i_pat=set(ancestors(i))
        for j_dis in path_diseases:
            if type(j_dis)==str:
                dis_score.append(max(scores))
                scores=[]
                continue
            score=next(filter(lambda x: x in i_pat,j_dis))
            scores.append(IC[score-1])
        del dis_score[0]
        dis_score.append(max(scores))
        dis_k_scores=dis_k_scores+np.vstack(dis_score)
        dis_score,scores=[],[0]
    w.write(str(np.where(dis_k_scores==max(dis_k_scores)[0])[0][0]+1)+'\n')
        
rdir='C:/Stepik/'
with open(rdir+'test1','r') as f:
    with open(rdir+'result.txt','w') as w:
        n=f.readline()#кол-во вершин
        phenotype = np.fromstring(f.readline(), dtype=int, sep=' ')
        dct = dict()
        for i in range(len(phenotype)):#поменять детей  и родителей как
            #dct[child]=[parents]
            dct[i+2]=phenotype[i]
        IC=np.fromstring(f.readline(), dtype=int, sep=' ')
        diseases,patients=read(),read()
        keys=set(dct.keys())
        path_diseases=[]
        for dis in diseases:
            path_diseases.append('s')
            for i in dis[1:]:
                path_diseases.append(ancestors(i))
        del diseases
        for pat in patients:
            inform_cont(pat[1:],path_diseases)
