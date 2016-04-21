# merging two arrays

# each array have sorted independently 
# Time complexity: if each array have same n length, so that would be O(n).
# if each array have different length, assume another array have m length, so the complexity would be O(n+m)
# Space complexity: O(n)
# appending, accessing and printing the array would not be considered as contribution to complexity

def merge(a, b):
	n, m = len(a), len(b)
	i, j = 0, 0
	res = []
	while i < n and j < m:
		if a[i] < b[j]:
			res.append(a[i])
			i += 1
		else:
			res.append(b[j])
			j += 1
	
	if i < n:
		res += a[i:]
	elif j < m:
		res += b[j:]
	
	return res

T = int(input())
for _ in range(T):
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	print(merge(a, b))
