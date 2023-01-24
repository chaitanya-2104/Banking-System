import pickle
class Banksystem:
    def __init__(self,name,accno,amount):
        self.name=name
        self.accno=accno
        self.amount=amount
    def deposite(self,amount):
        self.amount+=amount
    def withdrow(self,amount):
        self.amount-=amount

print("Wellcome to Chaitanya Bank System")
pas= "India@11"
print()

while True:
    p=input("enter password:")
    if p==pas:
        
        print("login sucessfully.......")
        break
    else:
        print("wrong passward please write correct password!!!!!!!!!!")
l=[]
p=open('bank.dat','rb')
while True:
    try:
        l.append(pickle.load(p))
    except:
        pass
        break
p.close()
while True:
    print("choose following option:")
    print("1. create account:")
    print("2. withdrow:")
    print("3. diposite:")
    print("4. checkbalance:")
    print("5. cheak all list:")
    print("6. exit:")
    s=int(input())
    if s==1:
        name=input("enter your name:")
        accno=int(input("enter your account number:"))
        amount=int(input("enter a amount you want to deposite:"))
        temp=0
        for i in l:
            if i.accno==accno:
                temp=1
                print("account no allreaady aviable:please try agin")
        if temp==0:
            acc = Banksystem(name,accno,amount)
            # l.append(acc)
            file=open('bank.dat','ab')
            pickle.dump(acc,file)
            l=[]
            file.close()
            p=open('bank.dat','rb')
            while True:
                try:
                    l.append(pickle.load(p))
                except:
                    pass
                    break
            p.close()
                
            
    if s==2:
        p=int(input("enter a account number: "))
        temp = 0
        for i in l:
            if i.accno == p:
                temp = 1
                am=int(input("enter a amount you want to withdrow: "))
                if am<i.amount:
                    i.withdrow(am)
                    print(i.name,"withdrow sucessfully !your balane is = ",i.amount)
                else:
                    print("your balance is less!")
            if temp==1:
                break
        if temp==0:
            print("acocount no not found,please try again")
    if s==3:
        p=int(input("enter a account number: "))
        temp=0
        for i in l:
            if i.accno==p:
                temp=1
                am=int(input("enter a amount you want to deposite:"))
                i.deposite(am)
                print(i.name,"your amount is sucessfully deposite: and your balane is!",i.amount)
            if temp==1:
                break
        if temp==0:
            print("account no is not found plase try again!")
    if s==4:
        p=int(input("enter a account number:"))
        temp=0
        for i in l:
            if i.accno==p:
                temp=1
                print(i.name,"your balane is=",i.amount)
            if temp==1:
                break
        if temp==0:
            print('account number is not found! please try again')

    if s==5:
        print("name            ","account_number       ","balance    ")
        for i in l:
           print(f'{i.name:<20}',f'{i.accno:<20}',f'{i.amount:<20}')
        print()
        print()
    if s==6:
        break