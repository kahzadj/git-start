import numpy as np

x,y = map(int,input().split())

a = np.array([np.array(input().split() ,dtype= int)for _ in range(x)])
b = np.array([np.array(input().split() ,dtype= int)for _ in range(x)])

print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')
