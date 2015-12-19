def f(x):
	import math
	return 10*math.e**(math.log(0.5)/5.27 * x)
def radiationExposure(start, stop, step):
    total = 0.0
    for i in range (int((stop-start)/step)):
        total += f(start+step*i) * step
    return total
print radiationExposure(0, 5, 1)