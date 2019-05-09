# Program to create the game 2048

# Importing required functions

import time

# Instructions of the game

choice=raw_input("Do you want a tutorial for the game 2048? Enter y or n")

if choice=="Y" or choice=="y":
    
    print '''This game is called 2048.
The game contains a grid with 4 rows and 4 columns
Initially the grid will have two 2's in random positions
for ex:
0  0  0  0
0  2  0  0
0  0  0  2
0  0  0  0
You can move these elements in any direction using the controls
w=up
a=left
s=down
d=right'''

    time.sleep(15)

    print'''
for ex:when you enter a,the elements move left and you get:
0  0  0  0
2  0  0  0
2  0  0  0
0  0  0  0
or when you enter s,the elements move down and you get:
0  0  0  0
0  0  0  0
0  0  0  0
0  2  0  2'''

    time.sleep(12)

    print'''
Every time you enter a direction the elements move and a 2 gets added in a random position.
Also when two adjacent elements are the same they get added.
For ex:
0  2  0  2
2  0  4  0
0  0  0  0
0  0  0  2
enter direction: a
4  0  0  0
2  4  0  0
0  0  0  0
2  0  0  0'''

    time.sleep(12)

    print '''
What happened in the above example?
When a is entered, all the elements move to the left that is:
2  2  0  0
2  4  0  0
0  0  0  0
2  0  0  0
Further since 2 and 2 will be adjacent to each other in the first row,they get added and become 4
4  0  0  0
2  4  0  0
0  0  0  0
2  0  0  0'''

    time.sleep(12)

    print'''
The purpose of the game is to achieve your end limit which you choose.
for ex: if you choose 64 as the end limit the game ends as soon as you manage to add 32 and 32 and get 64 as one
element in the grid
Good Luck!'''

    time.sleep(12)

# Initialising variables

main=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]                

score=0
moves=0
count=0        #Count for undo

# To create the initial grid

from random import *

def ran1():
    rand=randint(0,3)
    return rand

rand1=ran1()
rand2=ran1()
rand3=ran1()
rand4=ran1()

main[rand1][rand2]=2
main[rand3][rand4]=2

# To print the grid

def prinmain():
    for i in range(4):
        print
        for j in range(4):
            leng=len(str(main[i][j]))
            print main[i][j]," "*(4-leng),

# Functions for moving all elements in the specified direction            
       
def up():
    for j in range(4): 
        for i in range(1,4):
            if main[i-1][j]==0:
                main[i-1][j]=main[i][j]
                main[i][j]=0


def down():
    for j in range(4):
        for i in range(3):
            if main[i+1][j]==0:
                main[i+1][j]=main[i][j]
                main[i][j]=0

              
def left():
    for i in range(4):
        for j in range(3,0,-1):
            if main[i][j-1]==0:
                main[i][j-1]=main[i][j]
                main[i][j]=0
        
def right():
    for i in range(4):
        for j in range(3):
            if main[i][j+1]==0:
                main[i][j+1]=main[i][j]
                main[i][j]=0

# Generating random 2 after each turn

def ran2():
    global x
    list1=[]
    list2=[]
    for i in range(0,4):                              #i is the row and j is the column
        for j in range(0,4):
            if main[i][j]==0:
                list1.append(i)
                list2.append(j)
    leng=len(list1)-1
    if len(list1)==0:
        x=0
    else:
        number=randint(0,leng)
        row=list1[number]
        col=list2[number]
        main[row][col]=2
        if x!=0:
            prinmain()

# Function to display winning message

def cong():
    print
    print "Congratulations!!You won the game in",moves,"moves"

# Function to create deep copy of a list

def listcon(fro,to):
    to=[]
    for i in fro:
        li=[]
        for j in i:
            li.append(j)
        to.append(li)
    return to
        
print
print

y=True
check=0

while y:
    y=int(raw_input("Enter the end limit of the game(32/64/128/256/512/1024/2048)"))
    if y!=32 and y!=64 and y!=128 and y!=256 and y!=512 and y!=1024 and y!=2048:
        print "Sorry. Invalid limit. Enter again"
    else:
        break

prinmain()
 
# Main game loop variable
x=1

undo1=[]
undo2=[]

# Main Game Loop

while x:     

    undo2=listcon(undo1,undo2)
    undo1=listcon(main,undo1)

    x=raw_input("enter direction")                     
    moves+=1                                  

    if x=="w":

        ini=[]
        ini=listcon(main,ini)
                                                       
        for k in range(3):
            up()
            
        for col in range(4):
            for row in range(1,4):
                if main[row][col]==main[row-1][col]:
                    main[row-1][col]+=main[row][col]
                    main[row][col]=0
                    sum1=main[row-1][col]
                    
                    if sum1>0:
                        score+=sum1
                        
                    if sum1==y:
                        prinmain()
                        cong()
                        x=0

        if ini==main:
            print "Sorry. All the elements are already up.Enter again"
            continue
                    
        up()
        up()
        ran2()
        count=0
            
    elif x=="s":

        ini=[]
        ini=listcon(main,ini)
        
        for k in range(3):
            down()
            
        for col in range(4):
            for row in range(3,0,-1):
                if main[row-1][col]==main[row][col]:
                    main[row][col]+=main[row-1][col]
                    main[row-1][col]=0
                    sum1=main[row][col]
                    
                    if sum1>0:
                        score+=sum1
                        
                    if sum1==y:
                        prinmain()
                        cong()
                        x=0
                        
        if ini==main:
            print "Sorry. All the elements are already down.Enter again"
            continue

        down()
        down()
        ran2()
        count=0
        
    elif x=="a":

        ini=[]
        ini=listcon(main,ini)
        
        for k in range(3):
            left()
            
        for row in range(4):
            for col in range(1,4):
                if main[row][col]==main[row][col-1]:
                    main[row][col-1]+=main[row][col]
                    main[row][col]=0
                    sum1=main[row][col-1]
                    
                    if sum1>0:
                        score+=sum1
                        
                    if sum1==y:
                        prinmain()
                        cong()
                        x=0

        if ini==main:
            print "Sorry. All the elements are already in the left.Enter again"
            continue
        
        left()
        left()
        ran2()
        count=0
        
    elif x=="d":

        ini=[]
        ini=listcon(main,ini)
        
        for k in range(3):
            right()
            
        for row in range(4):
            for col in range(3,0,-1):
                if main[row][col-1]==main[row][col]:
                    main[row][col]+=main[row][col-1]
                    main[row][col-1]=0
                    sum1=main[row][col]

                    if sum1>0:
                        score+=sum1
                        
                    if sum1==y:
                        prinmain()
                        cong()
                        x=0

        if ini==main:
            print "Sorry. All the elements are already in the right.Enter again"
            continue
                    
        right()
        right()
        ran2()
        count=0
        
    elif x=="undo":

        count+=1
        if count>1:
            print "Sorry. Cannot undo more than once."
            prinmain()
            continue
        else:
            main=listcon(undo2,main)
            prinmain()

    else:

        choice=raw_input("Do you really want to quit? enter y or n")
        if choice=="n" or choice=="N":
            print "You chose to continue"
            continue
        elif choice=="y":
            print "You quit"
            break
        
print "Your Score is:",score
print
print "Credits: Nagalekha Ramesh and S.S.Shreya"
print "We hope you liked our game!! Thanks for playing :)"
