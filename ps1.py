###### this is the first .py file ###########

####### write your code here ##########
import sys                      #include system module
n=int(sys.argv[1])              #For commond line argument
m=int(sys.argv[2])
print(m)                        #check the inputs come
print(n)
lists=[]
if m>106 or m<3 :               #Input condition
    print("invalid m value")

if n>106 or n<3  :
    print("Invalid n value")
s=0
a=[]
for i in range(n):
    print(i)              #create a array of string
    lists.append(input().split())

print(lists)
