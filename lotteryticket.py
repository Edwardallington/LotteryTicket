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
    #digit1 = random.randint(0, 9)
    # print(digit1)
    # digit2 = random.randint(0, 9)
    # digit3 = random.randint(0, 9)
    # digit4 = random.randint(0, 9)
    # digit5 = random.randint(0, 9)
    # digit6 = random.randint(0, 9)
    # digits = [digit1, digit2, digit3, digit4, digit5, digit6]
    # print(f"{digits}")
    for i in range(6):
        digit2 = random.randint(0, 9)
        digits.append(digit2)
    return digits
    
def createLotteryTicket():
    ticket = randomNumber()
    # digit1 = random.randint(0, 9)
    # # print(digit1)
    # digit2 = random.randint(0, 9)
    # digit3 = random.randint(0, 9)
    # digit4 = random.randint(0, 9)
    # digit5 = random.randint(0, 9)
    # digit6 = random.randint(0, 9)
    #print(f"Your lottery ticket number is {ticket}")
    return ticket
def displayLotteryTicket():
    digits = createLotteryTicket()
    # for i in range(len(digits)):
    #     print(f"{digits[0]}{digits[1]}{digits[2]}{digits[3]}{digits[4]}{digits[5]}")
    print(f"Your lottery ticket number is: {digits[0]}{digits[1]}{digits[2]}{digits[3]}{digits[4]}{digits[5]}")
main()
