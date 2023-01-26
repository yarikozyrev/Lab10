summ = int(input())
money = [64, 32, 16, 8, 4, 2, 1]
 
for a in money:
    while summ>=a:
        print(a,end=" ");summ-=a
