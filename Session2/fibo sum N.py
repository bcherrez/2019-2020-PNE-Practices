def fibo(n):
    index1=0
    index2=1
    sumn= 0
    count=0

    for number in range(0,n+1) :
        if number==0 :
            sumn=0
        elif number==1:
            sumn= sumn + 1
        else:
            count= index1 + index2
            index1 = index2
            index2 = count
            sumn=sumn + count
    return sumn

print("Sumn of the firsts 5 terms of the fibonacci series is:",fibo(5))
print("Sumn of the firsts 10 terms of the fibonacci series is:",fibo(10))
