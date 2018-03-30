
import scipy.stats as stat
import numpy as np
import scr.FigureSupport as Fig

# 2.
# this would be a binomial distribution

# you would need to know the probability of living after 5 years
# you would need to know the population size
# you would need to know the number of ppl you want to have lived after 5 years


#3- likelihood of exactly 400 surviving
n = 573
k = 400
p = .5

binomial = stat.binom.pmf(k, n, p)

print(binomial)

#likelihood of 400 or more surviving
k2 = np.arange(400,573)
binomial2 = stat.binom.pmf(k2, n, p)
print(sum(binomial2))

