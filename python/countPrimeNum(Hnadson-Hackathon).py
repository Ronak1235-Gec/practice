def countPrimeNumbers(numbers):
    l1=[]
    
    for i in numbers:
        flag=-1
        if(i==0 or i==1):
            flag=0
        for j in range(2,i):
            if(i%j==0):
                flag=0
                break
            else:
                flag=1
        if(flag==1):
            l1.append(i)
    n=len(l1)
    return n


if __name__ == '__main__':
    numbers=[]
    count=int(input())
    for i in range(count):
        numbers.append(int(input()))
        
    print(countPrimeNumbers(numbers))