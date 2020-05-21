'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # Your code here

    pass


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


'''
Problem:
Eating Cookies

Cookie Monster can eat either 1, 2, or 3 cookies at a time. If he were given a jar of cookies with `n` cookies inside of it, how many ways could he eat all `n` cookies in the cookie jar? Implement a function `eating_cookies` that counts the number of possible ways Cookie Monster can eat all of the cookies in the jar. 

For example, for a jar of cookies with `n = 3` (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

 1. He can eat 1 cookie at a time 3 times
 2. He can eat 1 cookie, then 2 cookies 
 3. He can eat 2 cookies, then 1 cookie
 4. He can eat 3 cookies all at once. 

Thus, `eating_cookies(3)` should return an answer of 4.

Can you implement a solution that runs fast enough to pass the large input test?

Understand:
    What are the inputs and outputs?
        Input: We can assume it would be an integer of some kind
        Output: An integer of how many ways he can eat the cookies of input
    
    What are the constraints?
        He can eat a max of 3 cookies at once, 
        so if there is 4 cookies it excludes the attempt of him eating all four cookies at once.
        He has to eat *all* of the cookies, because he's an addict.
        * Why does he need to know how many ways he can eat cookies?
        We only need to *count* the amount of ways he eats cookies. *Not really a constraint more of an observation*
    
    What is the topic of the challenge? Algorithm/DataStructure/Both?
    Algo...?
    * Could we use a data structure to help with this problem? 
        maybe some kind of tree
    ** This sounds like a good problem for dynamic programming?
    
    What is the relationship between inputs & outputs?
    * indicate an inverse option
    1 = 1
        eats 1 cookie 1 time
    2 = 2
        eats 1 cookie 2 times
        eats 2 cookies 1 time
    3 = 4
        eats 1 cookie 3 times
        eats 1 cookie 1 time, then 2 cookies 1 time
        eats 2 cookies 1 time, then 1 cookie 1 time *
        eats 3 cookies 1 time
    4 = 6
        eats 1 cookie 4 times
        eats 1 cookie 2 time, 2 cookies 1 time
        eats 2 cookies 1 time, eats 1 cookie 2 time *
        eat 1 cookie 1 time, eat 2 cookies 1 time, eat 1 cookie 1 time
        eats 2 cookies 2 times
        eats 1 cookie 1 time, 3 cookies 1 time
        eats 3 cookies 1 time, eats 1 cookie 1 time *
        
    5 =
        eats 1 cookie 5 times                           |
        eats 1 cookie 3 times, 2 cookies 1 time         |
        eats 2 cookies, 1 time, 1 cookie 3 times        | factors of 1? is that how I word that?
        eats 1 cookie 2 times, eats 3 cookies 1 time
        eats 3 cookies 1 time, eats 1 cookie 2 times
        eats 1 cookie 1 time, eats 2 cookies 2 time
        eats 2 cookies 2 times, eats 1 cookie 1 time
        eats 2 cookies 1 time, eats 3 cookies 1 time
        eats 3 cookies 1 time, eats 2 cookies 1 time
        ...

        Observations:
        He can put 3 different amounts of cookies in his mouth at once
        Also the inverse option is included in the output count

        * what if the input is 0? No cookies?




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
