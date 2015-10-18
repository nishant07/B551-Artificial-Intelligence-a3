# Automatic Zacate game player
# B551 Fall 2015
# PUT YOUR NAME AND USER ID HERE!
#
# Based on skeleton code by D. Crandall
#
# PUT YOUR REPORT HERE!
#
#
# This is the file you should modify to create your new smart Zacate player.
# The main program calls this program three times for each turn. 
#   1. First it calls first_roll, passing in a Dice object which records the
#      result of the first roll (state of 5 dice) and current Scorecard.
#      You should implement this method so that it returns a (0-based) list 
#      of dice indices that should be re-rolled.
#   
#   2. It then re-rolls the specified dice, and calls second_roll, with
#      the new state of the dice and scorecard. This method should also return
#      a list of dice indices that should be re-rolled.
#
#   3. Finally it calls third_roll, with the final state of the dice.
#      This function should return the name of a scorecard category that 
#      this roll should be recorded under. The names of the scorecard entries
#      are given in Scorecard.Categories.
#

from ZacateState import Dice
from ZacateState import Scorecard
import random
import itertools
def generate_unique_states():
	unique_combinations = itertools.combinations_with_replacement("123456",5)
	lst = []
	for i in unique_combinations:
		permutations = itertools.permutations(i,5)
		for i in permutations:
			lst.append(i)
	unique_states = list(set(lst))

class ZacateAutoPlayer:

      def __init__(self):
            pass  

      def first_roll(self, dice, scorecard):
      	print dice
      	print scorecard
        return [0] # always re-roll first die (blindly)

      def second_roll(self, dice, scorecard):
      	print scorecard
      	return [1, 2] # always re-roll second and third dice (blindly)
      
      
      def third_roll(self, dice, scorecard):
      	available_categories = list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())) 
            # stupidly just randomly choose a category to put this in
        choice = self.best_category(dice,available_categories) 
        print choice[0]
        print choice[1]
        return choice[0]
        #return random.choice( list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())) )
      def best_category(self, dice, available_categories):

#Categories = [ "unos", "doses", "treses", "cuatros", "cincos", "seises", "pupusa de queso", "pupusa de frijol", "elote", "triple", "cuadruple", "quintupulo", "tamal" ]      	
      	max_category = dict()
      	print dice
      	print dice.dice
      	counts = [dice.dice.count(i) for i in range(1,7)]
      	for category in available_categories:
            if category == "unos":
      			max_category[category] = counts[Scorecard.Numbers[category]-1] * 1
            if category == "doses":
            	max_category[category] = counts[Scorecard.Numbers[category]-1] * 2
            if category == "treses":
            	max_category[category] = counts[Scorecard.Numbers[category]-1] * 3
            if category == "cuatros":
            	max_category[category] = counts[Scorecard.Numbers[category]-1] * 4
            if category == "cincos":
            	max_category[category] = counts[Scorecard.Numbers[category]-1] * 5
            if category == "seises":
            	max_category[category] = counts[Scorecard.Numbers[category]-1] * 6 
            if category == "pupusa de queso":
            	max_category[category] = 40 if sorted(dice.dice) == [1,2,3,4,5] or sorted(dice.dice) == [2,3,4,5,6] else 0
            if category == "pupusa de frijol":
            	max_category[category] = 30 if (len(set([1,2,3,4]) - set(dice.dice)) == 0 or len(set([2,3,4,5]) - set(dice.dice)) == 0 or len(set([3,4,5,6]) - set(dice.dice)) == 0) else 0
            if category == "elote":
            	max_category[category] = 25 if (2 in counts) and (3 in counts) else 0
            if category == "triple":
            	max_category[category] = sum(dice.dice) if max(counts) >= 3 else 0
            if category == "cuadruple":
            	max_category[category] = sum(dice.dice) if max(counts) >= 4 else 0
            if category == "quintupulo":
            	max_category[category] = 50 if max(counts) == 5 else 0
            if category == "tamal":
            	max_category[category] = sum(dice.dice)
            else:
            	max_category[random.choice(available_categories)] = 0
        print max_category
        return [max(max_category, key= max_category.get),max_category[max(max_category, key= max_category.get)]]

