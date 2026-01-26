 Define and use custom functions within a Python program.

• Types of function

• Types of Arguments.

• Map Function.

• Filter Function

• Reduce Function

• Naming conventions

• Using Imports

• Documentation

• Executing Modules as Scripts

• Extended Keyword Arguments (\*args, \*\*kwargs)

• Lambda Functions

• Decorators

• Labs:

1. Write a function to calculate the area of a rectangle (length × width).
2. Use map to square each number in a list.
3. Use filter to extract even numbers from a list.
4. Use reduce to calculate the product of all numbers in a list.
5. Write a function that accepts any number of arguments and returns their sum.
6. Use a lambda function to sort a list of tuples by the second element.
7. Write a decorator that logs the execution time of a function.



###### types of the argument

* Positional → order matters
* Keyword → order does not matter ex hey(name = "divynash")
* Default → optional values
* \*args → multiple positional arguments - used to cantaine the multiple values
* \*\*kwargs → multiple keyword arguments - used to cantne the multiple value with the key value pair
* Arguments make functions flexible and reusable



###### map

The map() function is used to apply a given function to each item of an iterable (such as list, tuple, etc.) and return a map object.

map() is used to apply a function to each element of an iterable and return the result.



🔹 Syntax

map(function, iterable)



num = list(map(lambda x:x+1,\[1,2,3,4,5]))



###### filter

1. flter(function, iterable)
2. Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.
3. filter() selects elements based on a condition
4. Returns a filter object
5. Works with iterables
6. Commonly used with lambda functions
7. Improves code clarity and efficiency
8. Does not modify original data
9. Used in functional programming



def temp(a):

    return True

print(list(filter(temp, list(range(1, 11)))))





###### reduce

it send the first 2 value of the list to the function then that function return the value after that reduce function will use the reurned value on to the next values in the list and then return the single value

1. reduce() reduces a sequence to a single value
2. Requires functools module
3. Works on iterables
4. Function must take two arguments
5. Commonly used with lambda functions
6. Used for sum, product, max, min
7. Supports initial value



###### Executing Modules as Scripts

1. \_\_name\_\_ is a special built-in variable
2. "\_\_main\_\_" indicates direct execution
3. Prevents auto-execution during import
4. Widely used in professional Python projects



\_\_name\_\_ is the variable that cantaien the main if we run that file directly other wise it cantina the name of the module from where this script is called



###### Extended Keyword Arguments (\*args, \*\*kwargs)

1. \*args collects multiple positional arguments
2. \*\*kwargs collects multiple keyword arguments
3. \*args → tuple
4. \*\*kwargs → dictionary
5. Improves function flexibility
6. Widely used in frameworks and APIs
7. Makes code scalable and reusable



###### Lambda Functions



1. lambda arguments : expression
2. Lambda functions are anonymous functions
3. Defined using the lambda keyword
4. Contain only one expression
5. No return statement required
6. Can take multiple arguments
7. Commonly used with map(), filter(), reduce()
8. Improves conciseness and readability
