###### this is the second .py file ###########

####### write your code here ##########
import sys

k1=int(sys.argv[1])
k2=int(sys.argv[2]) #commond line input
k3=int(sys.argv[3])
if k1>151 or k1<2 or k2>151 or k2<2 or k3>151 or k3<2: # Boundary condition
    print("Invalid input")
    exit()
str=input("enter string")
print(str)
