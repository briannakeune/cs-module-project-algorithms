# Alogrithms
# How to come up with first-pass solutions
# 1. How to Understand:
# -- Drawing a blank?
# Start asking questions
# Jot them down
# Draw diagrams
# Rewrite what the questions is asking of you,
# What is the desired outcome, reverse engineer that.
# -- Fast, Bad, Wrong --
# 2. How to Plan:
# 3. Execute:
# 4. Reflect:


# Find the Middle Node of A Linked List

# Write a function that, given a linked list as input,
# returns the middle node of the linked list. If the linked list contains an even number of nodes,
# return either of the middle two nodes.


# Understand:
# Can we figure out the length of the ll? Yes
# What is a linked list?
# Will we always be given the head? Yes
# How do we traverse?
# How do we know when we've reached the end?
# Can we add more attributes to the class? No
# Singly-linked or doubly-linked list? Singly
# What's the target time complexity?
# Edge case: what do we do in the case of just two nodes?
# Is the list valid ?


# Plan:
# Out of the questions...can you start making a plan?

# - Can we figure out the length of the ll?
# If we know the length of the ll,
# then we can calculate the middle 'index' using a midepoint formula,
# and then perform the appropriate number of jumps from the head to get to the middle node
# ^ something to aim for at least ^

# New questions: can using two pointers(runners) help us in this case?
# Idea: Let's have one of the runners run twice as fast as the other through the linked list
# What happens when the faster runner reaches the end of the list?
# Where will the slower runner going to be?
# Does this satisfy our desired outcome with an even length?


# Our linked list node class looks like this:
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'{self.value}'

    def find_middle(self):
        pass


# Example

root = Node(3)
root.next = Node(4)
root.next.next = Node(5)
root.next.next.next = Node(6)
root.next.next.next.next = Node(7)

root.find_middle()  # should return the Node with value 5

# ***** SOME OTHER GOOD QUESTIONS AND STRATIGIES *****
'''
What do I need in order to find the answer?
What information do I already have?

Write on the problem to help answer ^.
Draw a quick sketch
'''
