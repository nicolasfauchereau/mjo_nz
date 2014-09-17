def markov_chain_ts(mu,p,N):
    """
    simulate a discrete K states markov chain time-series given:
        INPUTS
    1) mu (np.array) = the probability of each discrete state, must be of length K (number of states)
    2) p (np.array) = the transition matrix, describing the probability of transitions 
    from each state to every other 
    must be of shape (K,K) with first row describing probablity of transition
    from state 0 to states 0(i.e. itself) to K (number of states)
    3) N (integer) = the lenth of the one dimensional time-series to simulate 
    returns:
        OUTPUTS
    x = a np.array of length N with simulated states (from 0 to K-1)
    """
    x = np.zeros((N,)).astype(np.int32)

    def rMC(p):
        import numpy as np
        u = np.random.random_sample()
        i = 0.
        s = p[0]

        while ( (u > s) & (i < p.__len__())  ):  
            i+=1.
            s = s + p[i]
        index = i 
        return index

    x[0] = rMC(mu)

    for i in xrange(N-1):
        x[i+1] = rMC(p[x[i]])

    return x.astype(np.int32)
