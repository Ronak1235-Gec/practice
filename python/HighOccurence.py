def count_words(str1):
    words=str1.split()
    res={}
    for i in words:
        res[i]=words.count(i)
    return res
    
def max_occurence_word(str1):
    d=count_words(str1)
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]

if __name__=='__main__':
    input_string=input()
    dict=count_words(input_string)
    st=max_occurence_word(input_string)
    print(st)
    