string = "Hello"

def recursiveReversal(string,position):
	position = position - 1
	if (position >= 0):
		return str(string[position]) + str(recursiveReversal(string,position)) 
	else:
		return ""
print recursiveReversal(string,len(string))
