def solveMeSecond(a,b):
	return a+b
n = int(input())
for i in range(n):
	a,b = input().split()
	a,b = int(a),int(b)
	res = solveMeSecond(a,b)
	print(res)