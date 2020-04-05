def Pow(a,b):
	i = 0
	s = a
	if a==0 and b>0:
		return 0
	if a>0:
		for i in range(b-1):			
			s=s*a
		return s
	else:
		if b%2==0 :
			return	Pow(abs(a),b)
		else:
			return	-(Pow(abs(a),b))
def Max(x,y,z) :
		if x>y :
			max=x
		else :
			max=y
		if max>z :
			return max
		else :
			max=z
			return max
def Search(simvol) :
			for i in "Hello" :
				if simvol==i :
						return "Yes"
					
