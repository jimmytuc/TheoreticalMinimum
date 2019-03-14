
"""
The "Law of Large Numbers" Problem [1]

The law of large numbers states that "as the number of identically distributed, randomly generated variables increases, their sample mean (average) approaches their theoretical mean." [2] The task at hand is to demonstrate the LLN by simulating dice casting, and printing the results [3].

[1] Saha, A. (2015). Doing Math with Python: Use Programming to Explore Algebra, Statistics, Calculus, and More! San Francisco: No Starch Press (Ch. 5, Challenge #2).
[2] This definition is from 'https://www.britannica.com/science/law-of-large-numbers' (archive: https://archive.fo/41rug)
[3] And as an added bonus, I'm gonna plot it on matplotlib
"""

import random, matplotlib.pyplot as plt

EV = lambda p, X: sum([c * U for c, U in zip(p, X)])
def castDie(): return random.randint(1, 6)
def empiricalMean(n):
    em = sum([castDie() for k in range(n)]) / float(n)
    print "Trial:",n,"\t\tEmpirical Mean:",em
    return em

prob_dice, value_dice = [1./6,1./6,1./6,1./6,1./6,1./6], [1,2,3,4,5,6]

# set this
trials = 25000

if __name__ == '__main__':
    EVdice = EV(prob_dice, value_dice)
    
    run_trials = range(1, trials + 1) #remember, don't be off-by-one ;-)
    run_simulation = [empiricalMean(k) for n, k in enumerate(run_trials)]
    
    plt.figure()
    
    plt.scatter(run_trials, run_simulation, color="#00FF00", label='Empirical')
    plt.axhline(y=EVdice, color="black", linewidth="1", label='$E[X] = \Sigma \ px$')
    
    plt.legend()
    plt.xlim(1, trials)
    plt.ylim(3, 4)
    plt.title("Law of Large Numbers Maresplained w/ Dice Casting", fontsize=20)
    plt.xlabel("Trials", fontsize=16)
    plt.ylabel("Expected Value", fontsize=16)
    plt.show()

