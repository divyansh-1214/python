Module 1: Introduction to Python

• Introduction to Python

• Overview Python Based Applications

• Environment Setup

• Data Types

• Variables and its Scope

• Data Structure

• Operations on Data Structure

• Input and Output Operation

• Writing a Python Module

• Labs:

• Write a module math\_utils.py with a function to calculate the factorial of a number. Import and use it in another script.



##### interpreter

The interpreter acts as a simple calculator: you can type an expression into it and it will write the value. Expression syntax is straightforward: the operators +, -, \* and / can be used to perform arithmetic; parentheses (()) can be used for grouping





python -m venv env

env\\Scripts\\activate



###### data types



1.Numeric Data Types



Used to store numbers.



int → Integer values (e.g., 10, -5)



float → Decimal values (e.g., 3.14)



complex → Complex numbers (e.g., 2+3j)



2\. String (str)



Used to store sequence of characters



Written inside single or double quotes



Example: "Python", 'Hello'



3\. Boolean (bool)



Represents logical values



Possible values: True and False



Used in decision-making



4\. List



Ordered and mutable collection



Can store different data types



Example: \[1, "Python", 3.5]



5\. Tuple



Ordered but immutable collection



Faster than lists



Example: (1, 2, 3)



6\. Set



* Unordered collection of unique elements
* Does not allow duplicates
* Example: {1, 2, 3}



7\. Dictionary (dict)



* Stores data in key–value pairs
* Keys must be unique
* Example: {"name": "Divyansh", "age": 20}
