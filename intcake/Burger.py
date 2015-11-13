def mergeSort(x):
	if len(x) == 1:
		return x
	else:
		return merge(mergeSort(x[0:(len(x)//2)]), mergeSort(x[(n//2 + 1):len(x)]))

def merge(l,r):
	res = []
	while isSorted:
		i,j=0,0
		if i<len(l):
			pass
		if l[i] <= j:
			res.append(l[i])
			i+=1
		else:
			res.append(r[j])
			j+=1
