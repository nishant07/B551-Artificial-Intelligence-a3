# Automatic Zacate game player
# B551 Fall 2015
# PUT YOUR NAME AND USER ID HERE!
#
# Based on skeleton code by D. Crandall
#
# PUT YOUR REPORT HERE!
"""
I am taking the cuurect roll and comparing it will all possible rolls for how different they are to achieve from current roll.
I have assigned all possible categories and related scores to all possible rolls.
So while comparing with current roll to all possibilities I take weightage of the diffence between them, each categories' score and its probability of getting that category.
I am then predict the next move from all possible rolls which has maximum values of category scores given least difference from given roll
And I reroll the dice which are different from current roll and predicted most probable next roll.
I am doing this for both the rolls.
In the last roll I am taking which all cateogries are possible to achieve and returning the category which gives maximum score.
"""



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
class ZacateAutoPlayer:

      def __init__(self):
            #"unos", "doses", "treses", "cuatros", "cincos", "seises", 
            self.category_prob = {"pupusa de queso":0.03086419753, "pupusa de frijol":0.01234567901, "elote":0.03858024691, "triple":0.15432098765, "cuadruple":0.01929012345, "quintupulo":0.00077160493}

      def first_roll(self, dice, scorecard):
      	diff = {}
      	#finding best possible move which can achieve maximum score from given roll
      	for k,v in unique_states_and_categories.items():
      		diff_dice = list(set(dice.dice) - set(k))
      		diff_dice_num = -1*len(diff_dice)
      		temp = {}
      		for key,values in v.items():
      			if key in self.category_prob:
      				values = values*self.category_prob[key]
      			values *= diff_dice_num
      			if values == 0:
                              values = -float("inf")
                        temp[key] = values
      		diff[k] = max(temp.values())	
      	next_move = max(diff,key=diff.get)
      	dice_pos = []
      	counts = [dice.dice.count(i) for i in range(1,7)]
      	if max(counts)>=3:
      	    for i in counts:
      	        if i>= 3:
      	            num = counts.index(i)
      	    for i in range(len(dice.dice)):
      	        if i!=num:
      	            dice_pos.append(i)
        else:
            act_diff = list(set(dice.dice) - set(next_move))
            for i in act_diff:
      		dice_pos.append(dice.dice.index(i))
        return dice_pos

      def second_roll(self, dice, scorecard):
      	diff = {}
      	for k,v in unique_states_and_categories.items():
      		diff_dice = list(set(dice.dice) - set(k))
      		diff_dice_num = -1*len(diff_dice)
      		temp = {}
      		for key,values in v.items():
      			if key in self.category_prob:
      				values = values*self.category_prob[key]
      			values *= diff_dice_num
      			if values == 0:
                              values = -float("inf")
                        temp[key] = values
      		diff[k] = max(temp.values())
      	next_move = max(diff,key=diff.get)
      	dice_pos = []
      	counts = [dice.dice.count(i) for i in range(1,7)]
      	if max(counts)>=3:
      	    for i in counts:
      	        if i>= 3:
      	            num = counts.index(i)
      	    for i in range(len(dice.dice)):
      	        if i!=num:
      	            dice_pos.append(i)
        else:
            act_diff = list(set(dice.dice) - set(next_move))
            for i in act_diff:
      		dice_pos.append(dice.dice.index(i))

        return dice_pos     
      def third_roll(self, dice, scorecard):
      	available_categories = list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())) 
            # stupidly just randomly choose a category to put this in
        dic = self.best_category(dice.dice,available_categories) 
        print max(dic, key= dic.get)
        return max(dic, key= dic.get)
        
      #Finds catetory which achieves best score from given rolls 
      def best_category(self, dice, available_categories = Scorecard.Categories):

#Categories = [ "unos", "doses", "treses", "cuatros", "cincos", "seises", "pupusa de queso", "pupusa de frijol", "elote", "triple", "cuadruple", "quintupulo", "tamal" ]      	
      	max_category = dict()
      	counts = [dice.count(i) for i in range(1,7)]
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
            	max_category[category] = 40 if sorted(dice) == [1,2,3,4,5] or sorted(dice) == [2,3,4,5,6] else 0
            if category == "pupusa de frijol":
            	max_category[category] = 30 if (len(set([1,2,3,4]) - set(dice)) == 0 or len(set([2,3,4,5]) - set(dice)) == 0 or len(set([3,4,5,6]) - set(dice)) == 0) else 0
            if category == "elote":
            	max_category[category] = 25 if (2 in counts) and (3 in counts) else 0
            if category == "triple":
            	max_category[category] = sum(dice) if max(counts) >= 3 else 0
            if category == "cuadruple":
            	max_category[category] = sum(dice) if max(counts) >= 4 else 0
            if category == "quintupulo":
            	max_category[category] = 50 if max(counts) == 5 else 0
            if category == "tamal":
            	max_category[category] = sum(dice)
            else:
            	max_category[random.choice(available_categories)] = 0
        return max_category
        #return [max(max_category, key= max_category.get),max_category[max(max_category, key= max_category.get)]]
      
      #To generate all unique 7736 permutation combination and assigning them dictionary having categories as keys and their score as values
      def generate_unique_states(self):
		unique_combinations = itertools.combinations_with_replacement("123456",5)
		categories = Scorecard.Categories
		lst = []
		for i in unique_combinations:
			permutations = itertools.permutations(i,5)
			for i in permutations:
					lst.append(i)
		unique_states = list(set(lst))
		unique_states_and_categories = {}
		for i in unique_states:
			dice = map(int,list(i))
			unique_states_and_categories[i] = self.best_category(dice,categories)
		return unique_states_and_categories
#For one time calculation in one game
unique_states_and_categories = ZacateAutoPlayer().generate_unique_states()