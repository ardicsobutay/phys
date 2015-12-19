def radiationExposure(start, stop, step):
    currentValue = start
    totalRad = 0.0
    while currentValue < stop:
        totalRad += f(currentValue) * step
        currentValue += step
    return totalRad

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    
print radiationExposure(0, 5, 1)