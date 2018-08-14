#3. 求交集
#給定兩兩個 list a, b, 求得兩兩個 list 之間的交集元素 list。
#注意回傳的 list 之值必須是遞增排序，⽽而且每個元素 只能出現⼀一次。

def inter(a,b):
    retA = []
    for i in a:
            if i in b:
                retA.append(i)
    newls = list(set(retA))
#    print(newls)
    finalls = sorted(newls)
    #排序
    return finalls

a = [1, 2, 3, 4, 5, 5, 8]
b = [1,5,8,4]
print(inter(a,b))
