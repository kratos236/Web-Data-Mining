import numpy as np
data = [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
#data=[[1,2,3],[1,2,4],[1,3,4],[1,3,5],[2,3,4]]
minsup = 0.5
minconf = 1
global count
global count_fk
global count_Fk
global count_fk_1
global Fk
Fk = []
count_fk = []
count_Fk = []
def creat_list(data):#生成商品列表
    list1 = []
    for i in data:
        for j in i:
            if j not in list1:
                list1.append(j)
    list1.sort()
    print("the list is :",end=' ')
    print(list1)
    return list1

def frequent_itemset(list1,data,minsup):#根据购买清单和商品生成1-频繁集
    f1 = []
    global count_Fk
    global Fk
    global count
    count = np.zeros(len(list1),np.int)#初始化为整数数组
    for i in data:
        for j in i:
            for k in list1:
                if k == j:
                    count[k-1] +=1#统计1-频繁集元素出现的个数
    for m in list1:
        if count[m-1] >= minsup*len(data):
            f1.append([m])
            Fk.append([m])
            count_Fk.append(count[m-1])
    print("the 1-frequent itemset is :",end=' ')
    print(f1)
    return f1

def candidate_gen(fk_1):#生成候选k-频繁集
    Ck = []
    for i in range(len(fk_1)):
        for j in range(i + 1, len(fk_1)):
            c = list(set(fk_1[i]).union(set(fk_1[j])))
            if len(c)!=len(fk_1[i])+1:
                break
            if c not in Ck:
                Ck.append(c)
            c_temp = c.copy()
            IsDel = False
            for l in c:
                c_temp.remove(l)
                c_temp.sort()
                if c_temp not in fk_1:
                    IsDel = True
                c_temp.append(l)
            if IsDel:
                Ck.pop()
    if (len(Ck) > 0):
        print("the", end=' ')
        print(len(Ck[0]), end='')
        print("-candaidate frequent itemset is :", end=' ')
        print(Ck)
        return Ck
    else:
        print("the k is", end=' ')
        print(len(fk_1[0]))
        return fk_1

def scan_F(Ck):#检验候选k-频繁集确定k-频繁集
    fk = []
    global count_fk
    global count_Fk
    global count_fk_1
    global Fk
    count_fk_1 = count_fk.copy()
    count_fk = np.zeros(len(Ck), np.int)  # 初始化为整数数组
    for k in range(len(Ck)):
        for i in data:
            if (set(i).intersection(set(Ck[k])))==set(Ck[k]):#交集是否等于本身用于统计候选频繁集个数
                count_fk[k]+=1
    for p in range(len(Ck)):
        if count_fk[p] >= minsup*len(data):
            fk.append(Ck[p])
            Fk.append(Ck[p])
            count_Fk.append(count_fk[p])
    print("the", end=' ')
    print(len(Ck[0]), end='')
    print("-frequent itemset is :", end=' ')
    print(fk)
    return fk

def generateRules(list_len):
    global Fk
    global count_Fk
    print(Fk)
    print(count_Fk)
    for i in range(len(Fk)):
        for j in range(len(Fk)):
            if Fk[i] == Fk[j]:
                break
            if not set(Fk[i]).intersection(set(Fk[j])):#i,j无交集
                list_temp = list(set(Fk[i]).union(set(Fk[j])))
                list_temp.sort()
                i_x =0
                i_y =0
                i_z =0
                if list_temp in Fk:#i,j为频繁集的真子集
                    for n in range(len(Fk)):
                        if Fk[i] == Fk[n]:
                           i_x = n
                        if Fk[j] == Fk[n]:
                           i_y = n
                        if list_temp == Fk[n]:
                           i_z = n
                    if i_x*i_y*i_z>0:
                        if count_Fk[i_z]/count_Fk[i_x] >= minconf:
                            print(Fk[i_x], end=' ')
                            print("→", end=' ')
                            print(Fk[i_y], end=' ')
                            print("the conf_rate is",end=' ')
                            print(count_Fk[i_z]/count_Fk[i_x] )
                        if count_Fk[i_z] / count_Fk[i_y] >= minconf:
                            print(Fk[i_y], end=' ')
                            print("→", end=' ')
                            print(Fk[i_x], end=' ')
                            print("the conf_rate is", end=' ')
                            print(count_Fk[i_z] / count_Fk[i_y])

list1=creat_list(data)
f1=frequent_itemset(list1,data,minsup)
fk=scan_F(candidate_gen(f1))
fk_temp=scan_F(candidate_gen(fk))
generateRules(len(list1))






