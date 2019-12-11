def accuracy(accuracy):
    import seaborn as sb, numpy as np
    from scipy.stats import binom
    accuracy = accuracy/100.0
    data_binom = binom.rvs(n=1,p=accuracy,loc=0,size=1)
    return(accuracy)
