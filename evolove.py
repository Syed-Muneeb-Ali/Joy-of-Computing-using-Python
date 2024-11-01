import random 

def evolve(x): 
	
	# index of the bit in x(list) 
	# in which change will happen 
	i = random.randint(0, len(x)-1) 
	
	# p is one then only change 
	# will happen 
	p = random.randint(1, 10) 
	if(p == 1): 
		
		if(x[i] == 0): 
			x[i] = 1
			
		else: 
			x[i] = 1
			
# Driver code 
x =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

# the process of evolution 
# will take place 500 times 
for j in range(0, 500): 
	evolve(x)
	print(x)
	
print(x) 
