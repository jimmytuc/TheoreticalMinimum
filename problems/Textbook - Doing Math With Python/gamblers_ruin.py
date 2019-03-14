
"""
The "How Many Tosses Before You Run Out of Money?" Problem [1]

Here, we're gonna illustrate the Gambler's Ruin problem. We have a "coin-flip" simulation where you'll win $1.00 if the flip lands on heads and lose $1.50 if the flip lands on tails. [2]

[1] Saha, A. (2015). Doing Math with Python: Use Programming to Explore Algebra, Statistics, Calculus, and More! San Francisco: No Starch Press (Ch. 5, Challenge #3).
[2] I make some changes to the original problem. Instead of stopping exactly when the bankroll is <= 0, we will keep on going for a predefined 'trials' variable, I will also plot it on matplotlib.
"""

import random, matplotlib.pyplot as plt

class CoinFlipGame:

	def __init__(self, bankroll):
		self.__bankroll = bankroll

	def getBankroll(self):
		return self.__bankroll

	def playGame(self):
		flip = random.randint(1, 2) # 1 = heads; 2 = tails
		if flip == 1:
			self.__bankroll = self.__bankroll + 1.00
		else:
			self.__bankroll = self.__bankroll - 1.50

trials = 1000
starting_bankrolls = [10, 25, 100]

if __name__ == '__main__':

	plt.figure()
	for n_br, k_br in enumerate(starting_bankrolls):
		cfg = CoinFlipGame(k_br)
		resulting_bankroll = []
		
		for i_tr in range(1, trials + 1):
			cfg.playGame()
			resulting_bankroll.append(cfg.getBankroll())

		plt.plot(range(1, trials + 1), resulting_bankroll, label="Starting at: $"+str(k_br))

	plt.legend()
	plt.axhline(y=0, color='black')

	plt.title("Illustration of Gamblers Ruin Problem", fontsize=20)
	plt.xlabel("Trials", fontsize=16)
	plt.ylabel("Resulting Bankroll", fontsize=16)
	plt.show()
