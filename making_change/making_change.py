#!/usr/bin/python

import sys


def making_change(amount, denominations):
    # Your code here

    pass


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")

'''
Problem:
Making Change

You work as a bank teller, handling people's bank transactions (this is your part-time gig while you're studying at Lambda; only fourteen more weeks of this stinking job until you go find a job as a software developer!). 

One day one of the wealthiest and also most eccentric patrons of the bank walks up to your stall. They hand you some cash and tell you they want you to figure out exactly how many ways there are to make change for the amount of money they plopped down in front of you using only pennies, nickels, dimes, quarters, and half-dollars. 

Since this is a bank, you have an infinite supply of coinange. Write a function `making_change` that receives as input an amount of money in cents as well as an array of coin denominations and calculates the total number of ways in which change can be made for the input amount using the given coin denominations. 

For example, `making_change(10)` should return 4, since there are 4 ways to make change for 10 cents using pennies, nickels, dimes, quarters, and half-dollars:

 1. We can make change for 10 cents using 10 pennies
 2. We can use 5 pennies and a nickel
 3. We can use 2 nickels
 4. We can use a single dime
Understand:
    What are the inputs and outputs?
    
    What are the constraints?
    
    What is the topic of the challenge? Algorithm/DataStructure/Both?
    
    What is the relationship between inputs & outputs?

    What are you expected to do in this problem?

Plan:
    What tools do you need to manipulate the input or output?
        Am I missing anything?
    Do I understand how to use those tools?
    Do we have tools to make conditional statements for input to become output?
    If we have the tools, what are the steps to solve the problem?

Execute:
    Can I convert most of my plan into psuedocode?
    Did i:
        declare variable with the correct type?
        follow the syntax of the language, the conditional statements and the tools?
        close all my brackets and parentheses?
        have proper indentation and spell correctly?

Reflect:
    Did my code pass all the test cases?
    Is there a different solution with better runtime?
    Can someone who has not seen your code before be able to read it and understand it at their first read?
    Any alternative solution or improvement for code readability?

'''
