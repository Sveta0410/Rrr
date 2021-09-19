print('Введите длину списка')
n=int(input()) # длина
while n<3:
    print('Количество элементов списка должно быть больше трёх')
    print('Введите длину списка ещё раз')
    n = int(input())
print('Введите элементы списка')
a=[]
while len(a)<n:
    x=input()
    if x.isdigit() and int(x)!=0:
        a.append(int(x))
    elif x.isdigit()==False or int(x)==0:
        print('Введите число больше 0')
a.sort(reverse=True)
print(a)
for i in range(len (a) -1):
    x1=a[i]
    x2=a[i+1]
    x3=a[i+2]
    if x1+x2>x3 and x1+x3>x2 and x2+x3>x1:
        p=(x1+x2+x3)/2
        s=(p*(p-x1)*(p-x2)*(p-x3))**0.5
        print(s)
        print(x1, x2, x3)
        break
    else:
        print('Треугольник составить невозможно')
        break
