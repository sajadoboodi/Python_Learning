def first_num(n):
    num = 0
    while(num<n):
        yield num
        num+=1

print(first_num(5))

for i in first_num(5):
    print(i)