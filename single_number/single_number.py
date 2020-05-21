'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    single_lady = 0  # she can't find her match 🤷‍♀️

    for i in range(0, len(arr)):
        print('i: ', i)
        print('singlelady index: ', single_lady)
        print(
            f'\nmatches: \nsingleladyvalue: {arr[single_lady]}\ncheckedagainst: {arr[i]}\n')
        if arr[single_lady] == arr[i]:
            single_lady = i + 1
        else:
            # because she never found her match through the array
            crazy_cat_lady = arr[single_lady]
            print('crazycat: ', crazy_cat_lady)

    return crazy_cat_lady  # expected 9 for example

    # # if the input is 1, there can be no matches, so we return it
    # if len(arr) is 1:
    #     return arr[0]
    # index = 0
    # # take the first number in the list and compare it
    # #  through each index of the given input until we fine one that matches
    # for i in range(index, len(arr)):
    #     # then we restart the loop with the next index
    #     print(f'i: {arr[i]}\narr[index]: {arr[index]}')
    #     if arr[i] == arr[index]:
    #         index += 1
    #         single_number(arr[index:])
    # # if we do not find a match, return that value
    # return arr[i]

# currently, looping through until there is nothing left...


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

'''
Problem:

Single Number

Given a non-empty array of integers where every element appears twice except for one. 
Find that single number. 
You may assume that there will _always_ be _one_ odd-number-out and 
every other number in the input shows up exactly twice.  

## Examples
```
Sample input: [2, 2, 1]
Expected output: 1
```

```
Sample iput: [4, 1, 2, 1, 2]
Expected output: 4
```

Can you implement a solution that finds the single number in _one_ pass through the input array with `O(1)` space complexity?

Understand:
    What are the inputs and outputs?
    Input: an array greater than 0.
    Output: an integer that does not match another index's value
        
    What is the topic of the challenge? Algorithm/DataStructure/Both?
    Algo
    
    What are you expected to do in this problem?
    Find the number that does not have a twin within the array.

    
Plan:
    What tools do you need to manipulate the input or output?
        Maybe a place holder for the value, index that doesn't have a match so far
        Maybe a counter to see if I have found the value more than once
        index seems important, so maybe enumerate?

    If we have the tools, what are the steps to solve the problem?
        create a single lady holder
        create a counter
        loop through array to find a match
            if no match is found 
                return the crazy cat lady
            if a match is found
                we need to move to the index after single lady found a match        

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
