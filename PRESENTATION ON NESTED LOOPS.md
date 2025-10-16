#  		  PRESENTATION ON NESTED LOOPS

### 

### 

### BEFORE THE UNDESTANDING OF LOOPS WE HAVE TO CLEAR OUR FEW CONCEPTS:



1. **Variable**
2. **Methods**
3. **Scope**
4. **Loops**



#### FIRSTLY, WE'LL TAKE AT LEAST ONE EXAMPLE OF EACH POINT:



#### Let's Talk About Variable First.

#### 

#### Definition of a Variable in Python:

#### 

#### A variable in Python is like a container or box that is used to store data.

#### It has a name (identifier) which refers to the value stored in it.





#### Secondly Let's Talk About Methods range():

#### Definition:

#### 

#### The range() method in Python is used to generate a sequence of numbers.

#### It is most commonly used with loops like for loops.

#### Example:

#### range(start, stop, step)



#### Scope:

#### Definition:

#### Scope defines where a variable can be accessed inside your program.

#### 

#### There are 2 types of scopes in Python:

#### There are 2 types of scopes in Python:

#### 

#### Scope Type	Meaning

#### L – Local	Inside a function

#### G – Global	Outside all functions (main program)



### x = 10  # Global variable

### 

### def my\_func():

### &nbsp;   y = 5  # Local variable

### &nbsp;   print("Inside function:", y)

### 

### my\_func()

### print("Outside function:", x)





#### Loops

#### Definition:

#### Loops are used to repeat a block of code multiple times without writing it again and again.

#### 

#### Types of Loops in Python:

#### Loop Type	Description

#### 

#### for loop	Used to iterate over a sequence like list, string, or range

#### while loop	Runs as long as a condition is true





for i in range(5):

&nbsp;   print("Hello", i)



count = 1

while count <= 3:

&nbsp;   print("Counting:", count)

&nbsp;   count += 1







#### Nested Loops – Definition

#### 

#### Definition:

#### A nested loop is a loop inside another loop.

#### 

#### The outer loop runs first.

#### 

#### For each iteration of the outer loop, the inner loop runs completely.







\# Outer loop → Classes

for class\_num in range(1, 3):  # 1 to 2

&nbsp;   print("Class", class\_num)



&nbsp;   # Inner loop → Students

&nbsp;   for student\_num in range(1, 3):  # 1 to 2

&nbsp;       print("  Student", student\_num)



for i in range(1, 4):       # Table number

&nbsp;   for j in range(1, 6):   # Multiply by 1 to 5

&nbsp;       print(f"{i} x {j} = {i\*j}")

&nbsp;   print("---")  # Separate each table



# 

# THE END OF MY PRESENTATION



