""" Program to implement the game, Deal or No Deal"""

import random
import time

class suitcase:
    def __init__(self,x,a):
        self.amount=x
        self.no=a
        self.status="closed"
    def opendisp(self):
        print """
     ____
 ___|____|___
|            |
| Rs""",self.amount," "*(7-len(str(self.amount)))+"""|
|____________|"""

    @staticmethod
    def maindisp(ob1,ob2,ob3,ob4):
        
        if ob1.status=="open":
            dis1="Rs"+str(ob1.amount)+" "*(8-len(str(ob1.amount)))
        elif ob1.status=="player's choice":
            dis1="   ****   "
        else:
            dis1=(" "*4)+str(ob1.no)+" "*(6-len(str(ob1.no)))
            
        if ob2.status=="open":
            dis2="Rs"+str(ob2.amount)+" "*(8-len(str(ob2.amount)))
        elif ob2.status=="player's choice":
            dis2="   ****   "
        else:
            dis2=(" "*4)+str(ob2.no)+" "*(6-len(str(ob2.no)))
             
        if ob3.status=="open":
            dis3="Rs"+str(ob3.amount)+" "*(8-len(str(ob3.amount)))
        elif ob3.status=="player's choice":
            dis3="   ****   "
        else:
            dis3=(" "*4)+str(ob3.no)+" "*(6-len(str(ob3.no)))
            
        if ob4.status=="open":
            dis4="Rs"+str(ob4.amount)+" "*(8-len(str(ob4.amount)))
        elif ob4.status=="player's choice":
            dis4="   ****   "
        else:
            dis4=(" "*4)+str(ob4.no)+" "*(6-len(str(ob4.no)))
        print """
     ____            ____            ____            ____
 ___|____|___    ___|____|___    ___|____|___    ___|____|___   
|            |  |            |  |            |  |            |
|""",dis1,"""|  |""",dis2,"""|  |""",dis3,"""|  |""",dis4,"""| 
|____________|  |____________|  |____________|  |____________|      """

amtlis=[1000000,750000,500000,350000,200000,100000,80000,50000,10000,13500,12000,1,500,5000,360,1000]
suitlis=[]

for i in range(1,17):
    leng=len(amtlis)-1
    no=random.randint(0,leng)
    x=amtlis[no]
    amtlis.pop(no)
    ob=suitcase(x,i)
    suitlis.append(ob)

def deal():
    total=0
    count=0
    for i in suitlis:
        if i.status=="closed" or i.status=="player's choice":
            total+=i.amount
            count+=1
    avg=total/count
    print "Now comes the time to meet the DEAL STRIKER !!"
    time.sleep(2)
    print "HERE'S THE DEAL:",avg
    print "Your destiny is in your hands"
    print "Take it or leave it!"
    return avg

def displeft():
    print "THESE ARE THE AMOUNTS LEFT IN THE REMAINING SUITCASES"
    for i in suitlis:
        if i.status=="closed" or i.status=="player's choice":
            print "Rs"+str(i.amount),
    print
    
def disp16():
    def n():
        for i in suitlis:
            yield i
    gen=n()
    for i in range(4):
        a=next(gen)
        b=next(gen)
        c=next(gen)
        d=next(gen)
        suitcase.maindisp(a,b,c,d)

print "CHOOSE YOUR LUCKY SUITCASE"
print
while True:
    try:
        player=int(raw_input("Enter any number between 1-16:"))
        if player<=16 and player>=1:
            suitlis[player-1].status="player's choice"
            break
        else:
            raise Exception,"Number not in range 1 to 16. Enter again"
    except Exception,e:
        print e.message
print
print "YOU HAVE CHOSEN SUITCASE NUMBER:",player
print
print "Now you begin to open the remaining suitcases"
for i in range(14):
    disp16()
    while True:
        print
        choi=int(raw_input("Enter the number on the suitcase which you wish to reveal:"))
        if suitlis[choi-1].status=="closed":
            break
        else:
            print "SUITCASE HAS ALREADY BEEN CHOSEN ,Enter again!!!"
    print
    print "OPENING SUITCASE............"
    time.sleep(2)
    suitlis[choi-1].opendisp()
    suitlis[choi-1].status="open"
    print
    print
    time.sleep(1)
    if (i+1)%3==0 or i==13:
        displeft()
        print
        if i==13:
            print "This is the final deal that is going to be offered to you"
            print
        average=deal()
        offer=raw_input("Enter A for Accept or D for Decline  :")

        if offer=="a" or offer=="A":
            print
            print "YOU HAVE ACCEPTED THE DEAL STRIKER'S OFFER!!!"
            print
            print "YOU HAVE WON: Rs",average,"!!!"

            print "Here's what you missed......."
            time.sleep(3)
            suitlis[player-1].opendisp()
            print
            if suitlis[player-1].amount>average:
                print "BAD LUCK! YOU SHOULD HAVE ACCEPTED THE DEAL!!!"
            elif suitlis[player-1].amount<average:
                print "YOU ARE LUCKY. YOUR SUITCASE CONTAINED MONEY LESS THAN THe DEAL OFFERED TO YOU!!!!"
            else:
                print "YOUR SUITCASE CONTAINED THE SAME AMOUNT OF MONEY AS THE DEAL OFFERED!"
            break            

        else:
            print
            print "YOU HAVE DECLINED THE DEAL AND CHOSEN TO MOVE FORWARD"
else:
    print "You have declined all offers and chosen to take away the money in your own suitcase"
    suitlis[player-1].opendisp()
    print
    print "YOU HAVE WON: Rs",suitlis[player-1].amount,"!!!"
