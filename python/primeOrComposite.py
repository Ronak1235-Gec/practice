
def check_prime(num):
    flag=-1
    if num>1:
        for i in range(2,num//2):
            if(num%i==0):
                flag=0
                break
            else:
                flag=1 
    return flag
    
def prime_composite_list(li):
    prime=[]
    composite=[]
    for i in li:
        if check_prime(i)==1:
            prime.append(i)
        elif check_prime(i)==0:
            composite.append(i)
    res=[]
    res.append(prime)
    res.append(composite)
    return res
                
if __name__=='__main__':
    inp=[]
    count=int(input())
    for i in range(count):
        inp.append(int(input()))
    # print(check_prime(inp[1]))
    result=prime_composite_list(inp)
    print(result)