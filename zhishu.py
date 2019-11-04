# 将正整数分解质因数
def prime(n):
	l = []
	while n > 1:
		for i in range(2,n+1):
			if n % i == 0:
				l.append(i)
				n = n // i
				break
	return l

s = int(input("enter number:"))

if s > 0 :
	print(s,"=","*".join(str(i) for i in prime(s)))