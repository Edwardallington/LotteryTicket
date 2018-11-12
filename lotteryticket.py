'''
Programmer: Edward Allington
Date: November 12th 2018
Program: Lottery Ticket
'''
import random
def main():
    createlotteryticket()

def createlotteryticket():
    ticket = []
    digit1 = random.randint(0, 9)
    # print(digit1)
    digit2 = random.randint(0, 9)
    digit3 = random.randint(0, 9)
    digit4 = random.randint(0, 9)
    digit5 = random.randint(0, 9)
    digit6 = random.randint(0, 9)
    print(ticket)
main()