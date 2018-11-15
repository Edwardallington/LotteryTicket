'''
Programmer: Edward Allington
Date: November 12th 2018
Program: Lottery Ticket
'''
import random
def main():
    #randomNumber()
    
    #createLotteryTicket()
    displayLotteryTicket()

def randomNumber():
    digits = []
    for i in range(6):
        digit2 = random.randint(0, 9)
        digits.append(digit2)
    return digits
    
def createLotteryTicket():
    ticket = randomNumber()
    return ticket
def displayLotteryTicket():
    digits = createLotteryTicket()
    print(f"Your lottery ticket number is: {digits[0]}{digits[1]}{digits[2]}{digits[3]}{digits[4]}{digits[5]}")
main()
