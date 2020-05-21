#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # Your code here

    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

    '''
Problem:
Rock Paper Scissors

Write a function `rock_paper_scissors` to generate all of the possible plays that can be made in a game of "Rock Paper Scissors", given some input `n`, which represents the number of plays per round. 

For example, given n = 2, your function should output the following:

```python
[['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]
```

Your output should be a list of lists containing strings. Each inner list should have length equal to the input n.
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
