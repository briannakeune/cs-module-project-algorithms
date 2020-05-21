'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here

    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

'''
Problem:
Product of All Other Numbers

Write a function that receives an array of integers and returns an array consisting of the product of all numbers in the array _except_ the number at that index. 

For example, given 
```
[1, 7, 3, 4]
```
your function should return 
```
[84, 12, 28, 21]
``` 
by calculating 
```
[7*3*4, 1*3*4, 1*7*4, 1*7*3]
```

In the above example, the final value at index 0 is the product of every number in the input array _except_ the number at index 0.

Can you do this in `O(n)` time with `O(1)` space _without_ using division?
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
