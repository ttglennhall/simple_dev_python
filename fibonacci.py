memo = {0:0, 1:1}

def F(n):
	if not n in memo:
		memo[n] = F(n-1) + F(n-2)
	return memo[n]

print(F(100))