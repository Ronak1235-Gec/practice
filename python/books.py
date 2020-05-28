class Book:
    def __init__(self,book_id,book_name):
        self.book_id=book_id
        self.book_name=book_name
        
class Library:
    def __init__(self,id,address,blist):
        self.library_id=id
        self.address=address
        self.book_list=blist 
        
    def count_books(self,char):
        count=0
        for i in self.book_list:
            if i.book_name.startswith(char)==True:
                count+=1
        return count
    
    def remove_books(self,blist):
        for book in blist:
            for b in self.book_list:
                if b.book_name==book:
                    self.book_list.remove(b)
                    
                    
    
if __name__=='__main__':
    books=[]
    count=int(input())
    for i in range(count):
        book_id=input()
        book_name=input()
        obj=books.append(Book(book_id,book_name))
    z=Library(123,'Mumbai',books)
    char=input()
    ccount=int(input())
    names=[]
    for i in range(ccount):
        names.append(input())
    print(z.count_books(char))
    z.remove_books(names)
    for i in z.book_list:
        print(i.book_name)