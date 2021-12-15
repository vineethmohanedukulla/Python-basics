"""
(QUESTION 1) –Input the string as a list of characters from console,
delete at least 2 characters, reverse the resultant string and print it.
"""
print("Question 1 ----------------------------------------")
inputstring = input("Enter the list of characters: \n")
inputstring = inputstring[2:]  # removed first two characters
inputstring = inputstring[::-1]  # reverse the resultant string.
print(inputstring)
# time complexity = O(1) and space complexity is O(n) where n is the length of the string

print("Question 1B-----------------------------------------")
""" (QUESTION 1B)) Take two numbers from user and perform at least 4 arithmetic operations on them.
"""
num1 = int(input("Enter first number to perform opertions: \n"))
num2 = int(input("Enter second number to perform operations: \n"))
addition = num1 + num2
multiplication = num1 * num2
division = num1 / num2
substraction = num1 - num2
print("sum {0}".format(addition))
print("multiplication {0}".format(multiplication))
print("division {0}".format(division))
print("substraction {0}".format(substraction))
# time complexity = O(1) and space complexity is O(1)

print("Question 2-----------------------------------------")
"""
(QUESTION 2)Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’ without using regex.
"""
inputstring = input("Enter the sentence: \n")
inputstring: str = inputstring.replace('python', 'pythons')
print(inputstring)
# time complexity = O(n) and space complexity is O(n) where n is the length of the string

print("Question 3-----------------------------------------")
"""
(QUESTION 3)Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the grading scheme we are using in this class.
"""
score = int(input("enter the score: \n"))
if score < 0 or score > 100:
    print('invalid score, please enter valid score from 0 to 100 only')
elif score >= 94:
    print('A')
elif score >= 90:
    print('A-')
elif score >= 87:
    print('B+')
elif score >= 84:
    print('B')
elif score >= 80:
    print('B-')
elif score >= 77:
    print('C+')
elif score >= 74:
    print('C')
elif score >= 70:
    print('C-')
elif score >= 67:
    print('D+')
elif score >= 64:
    print('D')
elif score >= 60:
    print('D-')
else:
    print('F')  # time complexity = O(1) and space complexity is O(1)
