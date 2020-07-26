import math
d=input("enter no of deciml points")
I=10**(d-1)
def cp(a):
	for i in range(2,a):
		if a%i==0:
			return 0
			exit
	return 1
f=open("textfile.txt","w+")
while I<10**d:
	if cp(I)==1:
		if cp(I+2)==1:
			p=str(I)
			q=str(I+2)
			f.write(p)
			f.write(" ")
			f.write(q)
			f.write("\n")
	I+=1
f.close()





