'''
Programmer: Edward Allington
Date: November 12th 2018
Program: Lottery Ticket
'''
import random
def main():
    randomNumber()
    
    createLotteryTicket(2)

def randomNumber():
    digit1 = random.randint(0, 9)
    # print(digit1)
    digit2 = random.randint(0, 9)
    digit3 = random.randint(0, 9)
    digit4 = random.randint(0, 9)
    digit5 = random.randint(0, 9)
    digit6 = random.randint(0, 9)
    digits = [digit1, digit2, digit3, digit4, digit5, digit6]
    # print(f"{digits}")
    createLotteryTicket(digits)
    
def createLotteryTicket(ticketNumbers):
    ticket = ticketNumbers
    # digit1 = random.randint(0, 9)
    # # print(digit1)
    # digit2 = random.randint(0, 9)
    # digit3 = random.randint(0, 9)
    # digit4 = random.randint(0, 9)
    # digit5 = random.randint(0, 9)
    # digit6 = random.randint(0, 9)
    print(f"Your lottery ticket number is {ticket}"")
main()