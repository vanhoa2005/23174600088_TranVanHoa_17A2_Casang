def sumPdivisors(n): 
	if (n % 2 != 0): 
		return 0
	res = 1
	for i in range(2, (int)(n**0.5) + 1):  
		count = 0
		curr_sum = 1
		curr_term = 1
		while (n % i == 0): 
			count+=1 
			n = n // i 
			curr_term *= i 
			curr_sum += curr_term    
		res *= curr_sum  
	if (n >= 2): 
		res *= (1 + n) 
	return res 
print(sumPdivisors(36)) 
