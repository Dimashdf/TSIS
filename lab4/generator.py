#Exercises 1;
def sq_gen(N):
    for i in range(N):
        yield i**2
    
N = int(input("N:"))
sq=sq_gen(N)
for i in sq:
    print(i)


#Exercises 2;
def even_gen(n):
    for i in range(0,n):
        if(i%2==0):
            yield i
n = int(input("n:"))
even = even_gen(n)
print(','.join(map(str,even)))

#Exercises 3;
def div_gen(n):
    for i in range(0,n):
        if i%3==0 and i%4==0:
            yield(i)

n = int(input("n:"))
div=div_gen(n)
print(list(div))

#Exercises 4;
def sqfr_gen(a,b):
    for i in range(a,b+1):
        yield i**2

a = int(input("a:"))
b = int(input("b:"))
sq=sqfr_gen(a,b)
for i in sq:
    print(i)


#Exercises 5;
def ret_gen(n):
    while n>=0:
        yield n
        n-=1
n= int(input("n:"))
re = ret_gen(n)
print(list(re))

