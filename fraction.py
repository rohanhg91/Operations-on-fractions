class Fraction(object):

	def __init__(self,num,den):
		self.num = num
		self.den = den


	def __str__(self):
		if self.den == 0:
			raise RuntimeError("Please Enter non-zero value")
		else:
			return str(self.num) + '/' + str(self.den)



	def __add__(self,otherfraction):
		newnum = self.num * otherfraction.den + self.den * otherfraction.num
		newden = self.den * otherfraction.den
		return Fraction(newnum, newden)



	def __sub__(self,otherfraction):
		newnum = self.num * otherfraction.den - self.den * otherfraction.num
		newden = self.den * otherfraction.den
		return Fraction(newnum, newden)



	def __mul__(self,otherfraction):
		newnum = self.num * otherfraction.num
		newden = self.den * otherfraction.den
		return Fraction(newnum, newden)



	def __div__(self, otherfraction):
		newnum = self.num * otherfraction.den
		newden = self.den * otherfraction.num
		return Fraction(newnum, newden)



	def __eq__(self,other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den
		return firstnum == secondnum



	def __le__(self,other):
		firstnum = self.num * other.den
		secondnum = self.den * other.num
		return firstnum < secondnum



	def __gt__(self,other):
		firstnum = self.num * other.den
		secondnum = self.den * other.num
		return firstnum > secondnum









