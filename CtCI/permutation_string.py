def perm(x):
	if len(x) == 2:
		return [x, x[1]+x[0]]
	newString = x[-1]
	return join(perm(x[:-1]), newString)


def join(l, a):
	result = []
	for eachElement in l:
		for eachLocation in range(len(eachElement)):
			if eachLocation == 0:
				result.append(a+eachElement)
			elif eachLocation == (len(eachElement)-1):
				result.append(eachElement[:eachLocation]+a+eachElement[eachLocation:])
				result.append(eachElement+a)
			else:
				result.append(eachElement[:eachLocation]+a+eachElement[eachLocation:])
	return result

res = perm(input("Insert string: "))
print(res)
print('len: ',len(res))