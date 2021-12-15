# ICP-1
ICP-1

#### Complete the following:

#### Name: Vineeth Mohan Edukulla
#### Email: vekfd@umkc.edu

<br/>
 
 ## Basics of Python

 ### Lesson and Assignment Objectives
1. Python installation and understanding the python basic concepts
2. Write python program to input the string as a list of characters from    console, delete at least 2 characters, reverse the 
resultant string and print it.
    – Take two numbers from user and perform at least 4 arithmetic operations on them
3. Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’ without using 
regex.
4. Use the if statement conditions to write a program to print the letter grade based on an input class score. Use 
the grading scheme we are using in this class.

  
    |A ≥ 94.0%|
    |---------|
    |A-≥ 90.0%|
    |B+≥ 87.0%|
    |B≥ 84.0% |
    |B-≥ 80.0%|
    |C+≥ 77.0%|
    |C≥ 74.0% |
    |C-≥ 70.0%|
    |D+≥ 67.0%|
    |D≥ 64.0% |
    |D-≥ 60.0%|
    |F< 60.0% |

## Softwares Required :
1. Python 3
2. Github Desktop
3. pycharm

## Implementation:
1. Installed the python 3.
2. Installed pycharm and created a new project  with default interpreter.
3. Developed the code for the problems and pushed the code file video and screenshots to the github using github desktop.

## Tasks Performed
### **Task 1: Installation**
Installed the python software from https://www.python.org/downloads/

![python installation](https://i.ibb.co/y4R1jg6/python-screenshot2.png)

Installed pycharm and created new project to write and run the code.

![pycharm installation](https://i.ibb.co/KhQ8PyJ/pycharm-screenshot.png)



### Task 2a: 
 **Write python program to input the string as a list of characters from    console, delete at least 2 characters, reverse the 
resultant string and print it.**

we have removed the first two characters using the below code:
``` python
inputstring = inputstring[2:] 
```
Next reversed the remaining characters using slicing:
``` python
inputstring = inputstring[::-1]
# time complexity = O(1) and space complexity is O(n) where n is the length of the string
```
Below is the output of the code.
![Output 1](https://i.ibb.co/zrJWHYH/output1.jpg)
### Task 2b:
**Take two numbers from user and perform at least 4 arithmetic operations on them**

We have taken the input from the command line and performed Addition, Substraction, Multiplication, Division.

```python
addition = num1 + num2
multiplication = num1 * num2
division = num1 / num2
substraction = num1 - num2
print("sum {0}".format(addition))
print("multiplication {0}".format(multiplication))
print("division {0}".format(division))
print("substraction {0}".format(substraction))
# time complexity = O(1) and space complexity is O(1)
```
Below is the output of the code:

![Output 2](https://i.ibb.co/47zQkDY/output2.jpg)

### Task 3:

 **Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’ without using regex.**

 Python provides replace() method to replace a specific string in the sentence with a new string.
 replace() method is case sensitive.

 ```python
 inputstring = input("Enter the sentence: \n")
inputstring: str = inputstring.replace('python', 'pythons')
print(inputstring)
# time complexity = O(n) and space complexity is O(n) where n is the length of the string
```
Below is the output of the code.
![Output 3](https://i.ibb.co/kyXP62B/output-3.jpg)

### Task 4:

**Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the grading scheme we are using in this class.**

```python
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
```
Below is the output for the code

![Output4](https://i.ibb.co/r0z1DpC/output4.jpg)

**Code Explanation Video:**  
https://app.box.com/s/qwjidx8tral96yes12500n9l44ir0la0

OR

https://github.com/UMKC-APL-PythonDeepLearing/icp-1-vekfd/blob/master/Video%20Explanation/ICP1.mp4?raw=true












