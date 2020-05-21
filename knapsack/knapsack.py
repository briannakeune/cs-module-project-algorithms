#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    # Your code here

    pass


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')

        '''
Problem:
The specific goal of this exercise is to write a program that takes input files that look like this:

```
1 42 81
2 42 42
3 68 56
4 68 25
5 77 14
6 57 63
7 17 75
8 19 41
9 94 19
10 34 12
```

The first row number is just a row/observation number, to facilitate reading and referring to items. The second number is the size/cost of the item, i.e. the cost of putting it in your knapsack. The third number is the value, i.e. the utility/payoff you get for selecting that item. The program should also take as input a total size, which can just be a number passed from the command line. So execution may look like this: `python knapsack.py input.txt 100`.

The goal is to select a subset of the items to maximize the payoff such that the cost is below some threshold. That is, the output should be a set of items (identified by number) that solves the Knapsack problem. It's also worth outputting the total cost and value of these items. This can all just be printed and may look something like below.

This is *not* a solution, just an example:

```
Items to select: 2, 8, 10
Total cost: 98
Total value: 117
```
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
