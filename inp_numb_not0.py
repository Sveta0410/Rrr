print('Введите длину списка')
n=int(input()) #длина
print('Введите элементы списка')
a=[]
for i in range (n):
    x=input()
    if x.isdigit() and int(x)!=0:
        a.append(int(x))
    elif x.isdigit()==False:
        print('Нельзя вводить не числовые значения')
    elif int(x)<0:
        print('Нельзя вводить отрицательные числа')
    elif int(x)==0:
        print('Нельзя вводить ноль')
a.sort(reverse=True)
print(a)
for i in range(len (a) -1):
    x1=a[i]
    x2=a[i+1]
    x3=a[i+2]
    if x1+x2>x3 and x1+x3>x2 and x2+x3>x2:
        p=(x1+x2+x3)/2
        s=(p*(p-x1)*(p-x2)*(p-x3))**0.5
        break
print(s)
print(x1, x2, x3)