#Created on Mar 3, 2014
#Seven, Eleven, or Doubles
#@author: Shawn Fulmer


#############
import random
#############

######################################GAME CLASS#####################################################
class Game: 
    def __init__(self): #initializes Game class.
        self.turn = 0
        self.SEVEN = 7
        self.ELEVEN = 11
        self.score1 = 0
        self.score2 = 0 
    print("7, 11, OR DOUBLES")

    def game():         #Main game sequence.
        self.winGame(self.score1, self.score2)
        self.checkTurn(self.turn)
        self.rollDie()
    
    def checkTurn(self, turn): #Checks which players turn it is.
        if self.turn%2 == 0:
            self.turn += 1
            return self.turn
            print("TYPE & ENTER \"ROLL\"", self.turn)
            choice = (input("1.ROLL"))
            if choice.lower() == "roll":
                self.rollDie()
            else:
                print("ERROR THAT IS NOT AN INPUT! PLEASE TRY AGAIN.")
        else:
            self.turn +=1
    
    def winGame(self, score1, score2):
        if score1 == 10:
            print("YOU WON!")
        elif score2 == 10:
            print("YOU LOSE!")
        else:
            return False    
        #print("OPPONENTS TURN!")
        #rollDie()
#####################################################################################################        

######################################PLAYER CLASS###################################################
class Player: #This class inherits the dice from Die class as well as other global variables such as scores and turn.
    def checkDie(self, turn, dice, score1, score2): #Checks die and scores for player accordingly.
        diceSum = dice[0]+dice[1]
        if self.turn%2 == 0 and diceSum == self.SEVEN or self.turn%2 == 0 and diceSum == self.ELEVEN:
            self.score1 += 1
            print("NICE!", score1)
            self.game()
        elif self.turn%2 == 0 and self.dice[0] == self.dice[1]:
            self.score1 += 2
            print("DOUBLE!", score1)
            self.game()
        elif diceSum == self.SEVEN or diceSum == self.ELEVEN:
            self.score2 +=1
            print("NICE!", self.score2)
            self.game()
        elif self.dice[0] == self.dice[1]:
            self.score2 +=2
            print("DOUBLE!", self.score2, self.turn)
            self.game()
        else:
            print("TOO BAD!", self.score1, self.score2, self.turn)
            self.game()
#####################################################################################################

#####################################DIE CLASS#######################################################          
class Die:
    def rollDie(self): #assigns a value to list dice.
        print("TYPE & ENTER \"ROLL\"", self.turn)
        choice = (input("1.ROLL"))
        if choice.lower() == "roll":
            dice = []
            for i in range(2):
                dice.append(random.randrange(1,7,1))    
            print(dice, self.turn)
            self.checkDie(self.turn, self.dice, self.core1, self.score2)
        else:
            print("ERROR THAT IS NOT AN INPUT! PLEASE TRY AGAIN.")
#####################################################################################################
x = Game()
x.game()
