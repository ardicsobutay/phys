def f(x):
	import math
	return 10*math.e**(math.log(0.5)/5.27 * x)
def radiationExposure(start, stop, step):
	sum = 0
	i = start
 	while i < stop:
  		sum += step * f(i)
  		i += step
 	return sum
 
print radiationExposure(0, 5, 1)