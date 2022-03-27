### ABCDE what is important in recursion is the return value. Must be consistent within all RECURSION!!!
### (5,3) = (4,2) + (4,3)

class find:

	def __init__(self):
		self.combine = []

	def recCount(self, y, string):
		result = []
		if y == 1:
			for i in string:
				result.append(i)
			return result
		if len(string) == y:
			result.append(string)
			return result
		for i in self.recCount(y - 1, string[1:]):
			result.append(string[0] + i)
		result += self.recCount(y, string[1:])
		return result

	def recNoCount(self, string):
		result = []
		if len(string) == 1:
			result.append(string)
			return result
		for i in range(0, len(string)):
			subs = string[:i] + string[i + 1:]
			for j in self.recNoCount(subs):
				result.append(string[i] + j)
		return result


if __name__ == '__main__':
	A = find()
	T = A.recCount(4, "ABCDEF")
	print(T)
	a = A.recNoCount("12345")
	print(a)
