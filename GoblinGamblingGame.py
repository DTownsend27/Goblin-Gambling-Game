
from random import randint

def introText():
	print "\n\tWelcome to the Goblin Gambling Game. You have found yourself in a\n\ttavern, where a goblin intending to take your money has challenged\n\tyou to a game of dice."
	print " "
	print "\tYour pockets contain $100. The goblin's challenge is simple.\n\tHe will roll one pair of dice against a pair of dice that\n\the has given you, and you can bet whatever amount you wish to."
	print " "
	print "\tYou suspect your dice is loaded, but he is stronger than you,\n\tand you are unable to refuse his offer.\n\tYou accept his challenge reluctantly.\n"
	print "\tTo roll the dice, type 'roll.'\n\tTo buy an extra pair of dice, type 'dice.'\n\tTo check your money, type 'money.'\n\tTo see these options again, type 'help'\n"
class playerClass:
	money = 100
	number_of_dice = 1
	dice_sides = 6
	def rollDice(self):
		diceTotal = 0
		diceRolled = self.number_of_dice
		while diceRolled > 0:
			diceTotal = diceTotal + randint(1,self.dice_sides)
			diceRolled = diceRolled - 1
		return diceTotal
		
player = playerClass()
goblin = playerClass()
player.dice_sides = 5
goblin.money = 900
diceCost = 1

turn_count = 0

def gambleRoll():
	moneyBet = raw_input("\n\tHow much money would you like to bet? ")
	if not moneyBet.isdigit():
		print "\n\tPlease enter a number\n"
	else:
		moneyBet = int(moneyBet)
	if moneyBet > player.money:
		print "\n\tYou don't have that kind of cash!\n"
	else:
		goblinTotal = goblin.rollDice()
		playerTotal = player.rollDice()
		if playerTotal > goblinTotal:
			print "\n\tYou rolled a %r, and the goblin rolled a %r. You win!\n" % (playerTotal, goblinTotal)
			player.money = player.money + moneyBet
			goblin.money = goblin.money - moneyBet
		elif playerTotal == goblinTotal:
			print "\n\tYour roll tied the goblin's roll, with both of you rolling %r.\n" % playerTotal
		else:
			print "\n\tYou rolled a %r, and the goblin rolled a %r. You lose...\n" % (playerTotal, goblinTotal)
			player.money = player.money - moneyBet
			goblin.money = goblin.money + moneyBet

def buyExtraDice():
	global diceCost
	if (25*diceCost) > (player.money - 1):
		print "\n\tYou can't afford another pair of dice!\n"
	else:
		player.number_of_dice += 1
		player.money = player.money - (25*diceCost)
		goblin.money += (25*diceCost)
	
		print "\n\tYou hand over $%r to the goblin, and he produces another pair" % (diceCost * 25)
		print "\tof dice from his pocket.\n"

def playTheGame():
	while player.money > 0 and goblin.money > 0:
		global turn_count
		choice = raw_input("\tType your action, or type 'help' for all options.\n\n\t")
		if choice == 'roll':
			gambleRoll()
			turn_count += 1
			if turn_count%4==0 and turn_count>0:
				print "\tThe goblin scowls and pulls another dice out of his pocket for himself.\n"
				goblin.number_of_dice += 1
		elif choice == 'dice':
			buyExtraDice()
			global diceCost
			diceCost += 1
		elif choice == 'help':
			print "\tTo roll the dice, type 'roll.'\n\tTo buy an extra pair of dice, type 'dice.'\n\tTo check your money, type 'money.'\n\n\t"
		elif choice == 'money':
			print "\n\tYou have $%r, and the goblin has $%r\n" % (player.money, goblin.money)
	else:
		if player.money < 1:
			print "\tYou have lost against the goblin this time." 
			print "\tPerhaps with more practice you will win.\n\n\t"
		else:
			print "\n\tYou have won! The goblin slinks off into the night,"
			print "\thaving lost all of his money.\n\n\t"

introText()			
playTheGame()
playAgain = " "
while not playAgain == "n":
	playAgain = raw_input("\nPlay again? y/n ")
	if playAgain == "y":
		player.money = 100
		goblin.money = 900
		diceCost = 1
		turn_count = 0
		goblin.number_of_dice = 1
		player.number_of_dice = 1
		introText()
		playTheGame()
raw_input("Press any key to exit")
