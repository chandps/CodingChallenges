def palindrome(s):
	left, right = 0, len(s) - 1
	while left < right:
		if s[left] != s[right]:
			return False
		
		left += 1
		right -= 1
	return True


T = int(input())
for _ in range(T):
	str = input().replace(" ","").lower()
	print(palindrome(str))
