###### this is the first .py file ###########

####### write your code here ##########
import sys                      #include system module
n=int(sys.argv[1])              #For commond line argument
m=int(sys.argv[2])
x=0
y=0
c=0
z=0
j=0
print(m)                        #check the inputs come
print(n)
lists=[]
list2=[]

if m>106 or m<3 :               #Input condition
    print("invalid m value")
    exit()


if n>106 or n<3  :
    print("Invalid n value")
    exit()
s=0
a=[]
for i in range(n):
    s= list(input())
    a = a+ [s]


for i in range(n):
    for j in range(m):  #Checking the "S" avalibility and go in four direction
        if a[i][j]=="S":
            x=0
            y=0
            z=0
            c=0
            while i-x >= 0 :
                if a[i-x][j]!="S":
                    break
                x=x+1
            while i+y<n :
                if a[i+y][j]!="S":
                    break
                y=y+1
            while j-z>=0 :
                if a[i][j-z]!="S":
                    break
                z=z+1
            while j+c<m :
                if a[i][j+c]!="S":
                    break
                c=c+1
            list1=[x,y,z,c]
            e = min(list1)
            list2.append(e)
print(list2)
u=max(list2) #taking max value
del list2[list2.index(u)] #remove max value
v=max(list2)
 #now get 2nd max value

u=(u-1)*4+1
v=(v-1)*4+1
print(u,v)
