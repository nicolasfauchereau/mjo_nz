### initial probabilities of the regimes
mu= np.array([0.5, 0.1, 0.4])
### transition matrix containing for each row the probabilities of transitions (including persistence)
p = np.array([[.6,.3,.1],[.3, .3, .4],[.4,.1,.5]])

### length of the time-series to simulate 
n = 80
x = np.zeros((n,))

def rando(p):
    import numpy as np
    u = np.random.random_sample()
    i = 0.
    s = p[0]

    while ( (u > s) & (i < p.__len__())  ):
        i+=1.
        s = s + p[i]
    index = i
    return index

x[0] = rando(mu)

for i in xrange(n-1):
    x[i+1] = rando(p[x[i]])
