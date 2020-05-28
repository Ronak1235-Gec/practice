class Item:
    def __init__(self,item_id,item_name,item_price,quantity_available):
        self.item_id=item_id
        self.item_name=item_name
        self.item_price=item_price
        self.quantity_available=quantity_available
    
    def calculate_price(self,quantity):
        if self.quantity_available>=quantity:
            self.quantity_available-=quantity
            return self.item_price*quantity
        else:
            return 0
    
class Store:
    def __init__(self,item_list):
        self.item_list=item_list
    def generate_bill(self,inp):
        bill=0
        for i in inp:
            for j in self.item_list:
                if i==j.item_name:
                    bill+=j.calculate_price(inp[i])
        return bill
                
        
        
if __name__=='__main__':
    ilist=[]
    icount=int(input())
    for i in range(icount):
        id=int(input())
        name=input()
        price=int(input())
        quant=int(input())
        i=ilist.append(Item(id,name,price,quant))
    s=Store(ilist)
    inp={}
    inp_count=int(input())
    for i in range(inp_count):
        name=input()
        quantity=int(input())
        inp[name]=quantity
    # print(ilist[0].calculate_price(2))
    print(s.generate_bill(inp))
    
        