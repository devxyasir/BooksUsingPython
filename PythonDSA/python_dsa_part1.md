# Mastering Python & DSA: From Beginner to Advanced Thinking

**Author:** Muhammad Yasir (devxyasir)

---

# SECTION 1: INTRODUCTION TO PROGRAMMING

---

## 1.1 What Is Programming?

**Simple Explanation:**
Programming is giving instructions to a computer so it can do work for us.

**Deep Explanation:**
A computer is just a machine made of silicon and wires. It cannot think. It can only follow exact instructions. Programming is the act of writing those instructions in a language the computer understands. Every app, website, and game you use was created by programming.

Think of programming as a bridge between human ideas and machine actions. When you write a program, you are not talking to the computer directly in ones and zeros. You use a programming language that is closer to English. A special program called an interpreter or compiler translates your words into the machine's native language.

**Real-World Analogy:**
Imagine you give instructions to a friend to make a sandwich. You say: "Take two slices of bread. Put butter on one. Add cheese. Put the other slice on top." Your friend follows each step. A program is the same. It is a list of steps a computer follows without asking questions. If you forget to say "add cheese," your friend will not guess. The computer is the same. It only does what you explicitly tell it to do.

**Step-by-Step Breakdown:**
1. The programmer thinks about a problem.
2. The programmer breaks the problem into small steps.
3. The programmer writes those steps in a programming language.
4. The computer reads and runs those steps.
5. The computer shows the result.

```python
# A very first program
print("Hello, World!")
```

---

## 1.2 Why We Need Programming

**Simple Explanation:**
We need programming because computers can do repetitive and complex work faster than humans.

**Deep Explanation:**
Humans get tired. Humans make mistakes. Computers do not get tired and do not make mistakes if the instructions are correct. Programming lets us automate tasks like sending emails, sorting data, finding directions, and even driving cars.

Programming is everywhere. When you use a calculator, watch a movie on Netflix, or order food online, you are using programs. Behind every digital service is a team of programmers who wrote millions of lines of code to make your life easier.

Programming also helps us solve problems that are too big for the human mind alone. Analyzing millions of medical records to find a cure, predicting weather patterns, and securing bank transactions all require programming.

**Real-World Analogy:**
A washing machine follows a programmed cycle. You do not stand there pouring water and spinning the drum. The program does it for you. In the same way, software programs do digital work for us. A payroll system calculates salaries for thousands of employees in seconds. A navigation app finds the fastest route through a crowded city. Without programming, these tasks would take humans days or weeks.

---

## 1.3 How Computers Think

**Simple Explanation:**
Computers think in binary: ones and zeros. They only understand "on" and "off."

**Deep Explanation:**
Everything inside a computer is made of tiny switches called transistors. A switch can be on (1) or off (0). All data — numbers, text, images, videos — is stored as a combination of ones and zeros. Programming languages like Python translate human words into those ones and zeros so the computer can understand.

The computer's brain is called the CPU (Central Processing Unit). It performs basic arithmetic and logic operations at incredible speed. But the CPU only understands machine code, which is just patterns of ones and zeros. A program written in Python goes through several layers of translation before the CPU can execute it.

**Real-World Analogy:**
A light switch is either on or off. Imagine a room with millions of light switches. By turning some on and some off, you can create patterns that represent letters, colors, and sounds. That is how a computer stores information.

Think of Morse code. Dots and dashes represent letters. Binary is similar, but with only two symbols: 1 and 0. With enough 1s and 0s, you can represent anything: a song, a movie, or a full book.

---

## 1.4 Why Python Is Used

**Simple Explanation:**
Python is a programming language that reads almost like English. It is easy to learn and very powerful.

**Deep Explanation:**
Python was designed to be simple. It hides complex details so beginners can focus on logic instead of syntax. It is used in web development, data science, artificial intelligence, automation, and education. Large companies like Google, Netflix, and Instagram use Python.

Python is an interpreted language. This means you can write a line of code and run it immediately without waiting for compilation. This makes learning fast because you see results instantly. Python also has a huge collection of libraries. A library is a pre-written set of tools. If you want to analyze data, draw graphs, build a website, or train an AI model, there is probably a Python library that does most of the hard work for you.

**Real-World Analogy:**
Think of programming languages as tools. Some are like manual screwdrivers — powerful but hard to use. Python is like a power drill. It does the same job with less effort.

Another analogy: Python is like a friendly teacher who explains things in simple words. Other languages are like strict professors who make you follow many rules before you can say anything.

**Step-by-Step Breakdown:**
1. Install Python on your computer.
2. Write instructions in a file.
3. Run the file.
4. Python translates your words into computer language.
5. The computer executes the instructions.

```python
# Python looks simple
name = "Yasir"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

---

## 1.5 Setting Up Your Programming Environment

**Simple Explanation:**
Before you write code, you need a place to write it. This is called your environment.

**Deep Explanation:**
Your environment includes:
- **Python Interpreter:** The software that reads and runs your code.
- **Code Editor or IDE:** A text editor designed for programming. Popular choices are VS Code and PyCharm.
- **Terminal or Command Line:** A text-based interface to run your programs.

You can also use online environments like Replit or Google Colab if you do not want to install anything on your computer. These are great for beginners because everything is already set up.

**Real-World Analogy:**
Your environment is like a kitchen. You need a stove (Python), a counter (editor), and utensils (libraries). A good kitchen makes cooking enjoyable. A good coding environment makes programming enjoyable.

## Pro Tips
- Start with small programs. Do not try to build an app on day one.
- Read your code out loud. If it sounds like English, you are on the right track.
- Practice every day. Programming is a skill, not a subject to memorize.
- Use an IDE with syntax highlighting. It helps you spot mistakes early.

## Common Mistakes
- Thinking the computer will guess what you want. It will not.
- Forgetting small details like a colon or a bracket.
- Copying code without understanding it.
- Skipping the basics and jumping to advanced topics too quickly.

## Interview Questions
- What is programming in your own words?
- Why is Python a good language for beginners?
- How does a computer understand code?
- What is the difference between a compiler and an interpreter?

## Exercises
- Write a program that prints your name.
- Write a program that prints three lines about why you want to learn programming.
- Explain to a friend how a computer thinks.
- Install Python and run your first "Hello, World!" program.

---

# SECTION 2: PYTHON BASICS

---

## 2.1 Variables

**Simple Explanation:**
A variable is a labeled box where you store a value.

**Deep Explanation:**
When you write `x = 10`, the computer creates a box named `x` and puts the number `10` inside it. Later, you can read the value, change it, or use it in calculations. Variables let us reuse data without writing it again and again.

Variables are the memory of your program. Without variables, every piece of data would be lost as soon as you used it. A variable name must start with a letter or underscore. It cannot start with a number. Good names describe what the variable holds.

**Real-World Analogy:**
Imagine kitchen containers. One container is labeled "Sugar." Another is labeled "Salt." You store things inside and use the label to find them later. A variable is exactly that — a labeled container for data.

**Step-by-Step Breakdown:**
1. Think of a name for your data.
2. Use the `=` sign to put a value inside.
3. Use the name later to get the value back.

```python
name = "Yasir"
age = 25
pi = 3.14
is_student = True

print(name)
print(age + 5)
```

---

## 2.2 Data Types

**Simple Explanation:**
Data types tell the computer what kind of value is stored: text, number, true/false, etc.

**Deep Explanation:**
The main data types in Python are:
- **String (`str`):** Text like "Hello". Used for names, messages, and any textual data.
- **Integer (`int`):** Whole numbers like 5, -3, 100. Used for counting and indexing.
- **Float (`float`):** Decimal numbers like 3.14, -0.5. Used for measurements and calculations with fractions.
- **Boolean (`bool`):** True or False. Used for conditions and flags.
- **None (`NoneType`):** Represents nothing. Used when a variable has no value yet.

The computer stores each type differently in memory. Knowing the type helps you choose the right operations. You cannot add a string and a number directly. You must convert them first.

**Real-World Analogy:**
In a form, some boxes ask for your name (text), some ask for your age (number), and some ask yes/no questions (boolean). Each box expects a different kind of answer.

```python
name = "Yasir"       # str
age = 25             # int
height = 5.9         # float
is_coder = True      # bool
result = None        # NoneType

print(type(name))
print(type(age))
```

---

## 2.3 Type Conversion

**Simple Explanation:**
Type conversion means changing a value from one data type to another.

**Deep Explanation:**
Python provides built-in functions for conversion:
- `int()` converts to integer.
- `float()` converts to decimal.
- `str()` converts to text.
- `bool()` converts to True or False.

Conversion is needed when you read user input because `input()` always returns a string. If you want to do math, you must convert the input to a number first.

**Real-World Analogy:**
Type conversion is like translating languages. If someone speaks English and you speak Spanish, you need a translator to understand each other. In code, if one part gives text and another part needs a number, you use a converter in between.

```python
age_string = "25"
age_number = int(age_string)
print(age_number + 5)

pi_string = str(3.14)
print("The value of pi is " + pi_string)
```

---

## 2.4 Strings

**Simple Explanation:**
A string is a piece of text. It is written inside quotes.

**Deep Explanation:**
Strings are sequences of characters. You can combine them, repeat them, slice them, and search inside them. Python gives many built-in tools to work with strings easily.

Key string operations:
- **Concatenation:** Joining strings with `+`.
- **Repetition:** Repeating a string with `*`.
- **Indexing:** Accessing one character with square brackets.
- **Slicing:** Getting a part of a string with `[start:end]`.
- **Methods:** `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.join()`.

Strings are immutable. This means once created, you cannot change a single character inside. You must create a new string instead.

**Real-World Analogy:**
A string is like a beaded necklace. Each bead is a letter. You can look at one bead, a group of beads, or the whole necklace. You cannot change the color of one bead without making a new necklace.

**Step-by-Step Breakdown:**
1. Create a string with single or double quotes.
2. Use `+` to join two strings.
3. Use `*` to repeat a string.
4. Use square brackets to access one character.
5. Use slicing to get a part of the string.

```python
text = "Hello, World!"
print(text[0])          # H
print(text[0:5])        # Hello
print(text.upper())     # HELLO, WORLD!
print("Hi " * 3)        # Hi Hi Hi
print(text.replace("World", "Python"))
```

---

## 2.5 String Formatting

**Simple Explanation:**
String formatting is inserting values into a string cleanly.

**Deep Explanation:**
There are three main ways to format strings in Python:
- **f-strings (recommended):** `f"Hello {name}"`
- **`.format()` method:** `"Hello {}".format(name)`
- **%-formatting (old):** `"Hello %s" % name`

f-strings are the fastest and easiest to read. They were introduced in Python 3.6 and are now the standard.

**Real-World Analogy:**
String formatting is like filling in a form template. The template has blank spaces. You insert the correct information into each space.

```python
name = "Yasir"
age = 25

# f-string
print(f"My name is {name} and I am {age} years old.")

# .format()
print("My name is {} and I am {} years old.".format(name, age))
```

---

## 2.6 Numbers and Operators

**Simple Explanation:**
Numbers in Python can be whole numbers or decimals. You can add, subtract, multiply, and divide them.

**Deep Explanation:**
- **Integers** have no decimal part. They are exact.
- **Floats** have a decimal part. They are approximate because of how computers store them.
- **Operators:** `+` add, `-` subtract, `*` multiply, `/` divide, `//` floor divide, `%` remainder, `**` power.

Operator precedence matters. Python follows the standard math order: parentheses first, then powers, then multiplication and division, then addition and subtraction.

**Real-World Analogy:**
Numbers are like money. Whole bills are integers. Coins make it a float. You can count, combine, split, and compare money just like numbers.

```python
a = 10
b = 3
print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a // b)   # 3
print(a % b)    # 1
print(a ** b)   # 1000
```

---

## 2.7 Input and Output

**Simple Explanation:**
Output is when the computer shows you something. Input is when you give something to the computer.

**Deep Explanation:**
- `print()` sends data to the screen.
- `input()` pauses the program, waits for the user to type something, and returns it as a string.
- You can convert the input string to a number using `int()` or `float()`.

Output can be customized with `sep` and `end` parameters in `print()`. By default, `print()` separates items with a space and ends with a newline.

**Real-World Analogy:**
Output is like a waiter bringing food to your table. Input is like you telling the waiter your order. The program asks, you answer, and the program uses your answer.

```python
name = input("What is your name? ")
print("Hello, " + name + "!")

age = int(input("How old are you? "))
print("Next year you will be", age + 1)
```

---

## 2.8 Boolean Logic

**Simple Explanation:**
Boolean logic deals with True and False values. It helps programs make decisions.

**Deep Explanation:**
Boolean operations:
- **`and`:** True only if both sides are True.
- **`or`:** True if at least one side is True.
- **`not`:** Flips True to False and vice versa.

Comparison operators also return booleans: `==`, `!=`, `<`, `>`, `<=`, `>=`.

**Real-World Analogy:**
You want to go outside. You check if it is sunny AND warm. Both must be true. If you are willing to go if it is sunny OR warm, only one needs to be true.

```python
is_sunny = True
is_warm = False

print(is_sunny and is_warm)  # False
print(is_sunny or is_warm)   # True
print(not is_sunny)          # False
```

---

## 2.9 Conditions

**Simple Explanation:**
Conditions let your program make decisions. If something is true, do this. Otherwise, do that.

**Deep Explanation:**
The `if` statement checks a condition. If the condition is true, the code inside runs. You can add `elif` (else if) for more checks, and `else` for a fallback.

Comparison operators:
- `==` equal
- `!=` not equal
- `<` less than
- `>` greater than
- `<=` less than or equal
- `>=` greater than or equal

You can combine conditions with `and`, `or`, and `not`.

**Real-World Analogy:**
You check the weather before leaving home. If it is raining, you take an umbrella. Else if it is cold, you take a jacket. Else, you just walk out.

**Step-by-Step Breakdown:**
1. Write `if` followed by a condition.
2. Add a colon at the end.
3. Indent the code that should run.
4. Use `elif` for extra conditions.
5. Use `else` for everything else.

```python
score = 75

if score >= 90:
    print("A grade")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
else:
    print("Need improvement")
```

---

## 2.10 Nested Conditions

**Simple Explanation:**
A nested condition is an `if` statement inside another `if` statement.

**Deep Explanation:**
Sometimes one decision is not enough. You need to check multiple layers. For example, first check if the user is logged in. Then, if they are logged in, check if they are an admin. Nested conditions let you build complex decision trees.

**Real-World Analogy:**
At an airport, first you show your ticket. If you have a ticket, you go to security. If you pass security, you go to the gate. Each step is a condition that depends on the previous step.

```python
is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("Welcome, admin!")
    else:
        print("Welcome, user!")
else:
    print("Please log in.")
```

---

## 2.11 Loops

**Simple Explanation:**
A loop repeats a block of code multiple times.

**Deep Explanation:**
- **`for` loop:** Repeats for each item in a collection or range. Use it when you know how many times to repeat.
- **`while` loop:** Repeats as long as a condition is true. Use it when you do not know how many times to repeat.
- **`break`:** Stops the loop early.
- **`continue`:** Skips the current round and moves to the next.
- **`else` with loops:** Runs after the loop finishes normally (not by break).

**Real-World Analogy:**
A `for` loop is like a playlist that plays each song once. A `while` loop is like eating popcorn until the bowl is empty. You do not know how many handfuls it will take, but you stop when the condition (bowl empty) is true.

**Step-by-Step Breakdown:**
1. Decide what needs to repeat.
2. Choose `for` if you know how many times. Choose `while` if you do not.
3. Write the loop with proper indentation.
4. Make sure the loop can end (infinite loops are bad).

```python
# for loop
for i in range(5):
    print(i)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

## 2.12 Nested Loops

**Simple Explanation:**
A nested loop is a loop inside another loop.

**Deep Explanation:**
Nested loops are used for multi-dimensional data like tables and grids. The outer loop runs once, and the inner loop runs completely for each iteration of the outer loop.

Be careful with nested loops. They can make your program slow if the data is large. Two nested loops over `n` items result in `n * n` operations.

**Real-World Analogy:**
Imagine a clock. The hour hand moves once. For each hour, the minute hand moves sixty times. The minute hand is the inner loop. The hour hand is the outer loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")
```

## Pro Tips
- Use meaningful variable names. `student_age` is better than `x`.
- Convert input immediately after receiving it.
- Use `f-strings` for clean output: `print(f"Hello {name}")`.
- Avoid infinite loops by updating your condition variable inside the loop.
- Use `enumerate()` when you need both the index and the value in a loop.

## Common Mistakes
- Forgetting to indent code after `if`, `for`, or `while`.
- Using `=` instead of `==` in conditions.
- Creating infinite `while` loops by forgetting to update the condition variable.
- Forgetting that `input()` always returns a string.
- Modifying a list while looping over it, which causes skipped items.

## Interview Questions
- What is the difference between `=` and `==`?
- What is the difference between a `for` loop and a `while` loop?
- How do you convert user input to an integer?
- What is the difference between `break` and `continue`?
- When would you use a nested loop?

## Exercises
- Write a program that asks for two numbers and prints their sum.
- Write a program that prints all even numbers from 1 to 20.
- Write a program that checks if a number is positive, negative, or zero.
- Write a program that prints a string in reverse using a loop.
- Write a program that prints a multiplication table from 1 to 5.
- Write a program that counts the vowels in a string.

---

# SECTION 3: FUNCTIONS

---

## 3.1 Why Functions Exist

**Simple Explanation:**
A function is a named block of code that you can run whenever you need it.

**Deep Explanation:**
Without functions, you would copy and paste the same code many times. Functions let you write code once and reuse it. This makes programs shorter, cleaner, and easier to fix. Functions also help you break a big problem into smaller pieces.

Think of a function as a mini-program inside your main program. It has its own inputs, its own logic, and its own output. When you call a function, you are telling the computer: "Pause what you are doing, run this mini-program, then come back and continue."

**Real-World Analogy:**
A blender is a function. You put ingredients in, press a button, and get a smoothie. You do not rebuild the blender every time you want a drink. You just use the machine again.

Another analogy is a recipe card. You write the recipe once. Every time you want to cook that dish, you pull out the card and follow the steps.

**Step-by-Step Breakdown:**
1. Define a function with `def`.
2. Give it a name and parentheses.
3. Write the code inside with indentation.
4. Call the function by its name to run it.

```python
def greet():
    print("Hello, welcome!")

greet()
greet()
```

---

## 3.2 Parameters and Arguments

**Simple Explanation:**
Parameters are placeholders inside a function. Arguments are the actual values you pass in.

**Deep Explanation:**
When you define `def add(a, b)`, `a` and `b` are parameters. When you call `add(3, 5)`, `3` and `5` are arguments. The function uses the arguments to do its work.

Python functions can have:
- **Required arguments:** Must be provided.
- **Default arguments:** Have a preset value if not provided.
- **Keyword arguments:** Passed by name, so order does not matter.
- **Variable arguments:** `*args` for extra positional arguments.
- **Keyword variable arguments:** `**kwargs` for extra named arguments.

**Real-World Analogy:**
A recipe says "add 2 cups of flour." The "2 cups" is a parameter. When you actually bake, you pour real flour. That real flour is the argument.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Yasir")
greet("Sara")

def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9 (default exponent 2)
print(power(2, 3))   # 8
```

---

## 3.3 Return Values

**Simple Explanation:**
A function can send a result back to the place that called it.

**Deep Explanation:**
`return` stops the function and sends a value back. You can store that value in a variable, print it, or use it in another calculation. A function without `return` gives back `None`.

Functions can return multiple values as a tuple. This is useful when you need to send back more than one piece of information.

**Real-World Analogy:**
You give money to a cashier. The cashier gives you change back. The change is the return value. You can then put that change in your pocket.

```python
def add(a, b):
    return a + b

result = add(4, 7)
print(result)   # 11

def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5])
print(minimum, maximum)
```

---

## 3.4 Scope

**Simple Explanation:**
Scope means where a variable can be used. A variable created inside a function only lives inside that function.

**Deep Explanation:**
- **Local scope:** Inside a function. Variables here are hidden from the outside.
- **Global scope:** Outside all functions. Variables here can be read anywhere, but should not be changed from inside a function without the `global` keyword.
- **Enclosing scope:** In nested functions, the inner function can read variables from the outer function.

Using local variables is safer because different functions cannot accidentally change each other's data.

**Real-World Analogy:**
A conversation in a meeting room is local. People outside cannot hear it. A message on the company bulletin board is global. Everyone can see it.

```python
message = "Global hello"

def say_hello():
    message = "Local hello"
    print(message)

say_hello()
print(message)
```

---

## 3.5 Lambda Functions

**Simple Explanation:**
A lambda is a small, anonymous function written in one line.

**Deep Explanation:**
Lambdas are useful for short operations that you do not want to define as a full function. They are often used with `map()`, `filter()`, and `sorted()`.

A lambda can have any number of arguments but only one expression. The expression is evaluated and returned automatically.

**Real-World Analogy:**
A lambda is like a sticky note with a quick calculation. You use it once and throw it away. You do not file it in a folder like a formal document.

```python
square = lambda x: x ** 2
print(square(5))  # 25

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
```

---

## 3.6 Map and Filter

**Simple Explanation:**
`map()` transforms every item in a collection. `filter()` keeps only items that pass a test.

**Deep Explanation:**
- **`map(function, collection)`:** Applies the function to every item and returns the results.
- **`filter(function, collection)`:** Applies the function to every item. If the function returns True, the item is kept.

Both return iterators. You usually wrap them in `list()` to see the results.

**Real-World Analogy:**
`map` is like a factory assembly line. Every item that comes in gets modified. `filter` is like a quality control checkpoint. Only good items pass through.

```python
numbers = [1, 2, 3, 4, 5]

# map: double every number
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# filter: keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
```

---

## 3.7 Docstrings

**Simple Explanation:**
A docstring is a comment inside a function that explains what the function does.

**Deep Explanation:**
Docstrings are written as the first line inside a function using triple quotes. They document the purpose, parameters, and return value. Good documentation helps other programmers (and your future self) understand your code.

**Real-World Analogy:**
A docstring is like the label on a medicine bottle. It tells you what the medicine does, how much to take, and what the side effects are.

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width

print(calculate_area.__doc__)
```

---

## 3.8 Reusability Thinking

**Simple Explanation:**
Think of functions as LEGO blocks. Build small pieces. Combine them to make something big.

**Deep Explanation:**
Good programmers do not write one giant block of code. They write many small functions that each do one job well. Then they connect those functions together. This makes debugging easy because you can test each block separately.

This approach is called **modular programming**. Each module (function) has a single responsibility. When something breaks, you know exactly which module to fix.

**Real-World Analogy:**
A car factory does not build a car in one step. It builds the engine, the wheels, the seats, and the body separately. Then it assembles them. Each part is like a function.

```python
def get_length(items):
    count = 0
    for _ in items:
        count += 1
    return count

def get_average(numbers):
    total = sum(numbers)
    length = get_length(numbers)
    return total / length

scores = [80, 90, 100]
print(get_average(scores))
```

## Pro Tips
- Give functions clear names that describe what they do.
- One function should do one thing.
- Use parameters instead of global variables.
- Write docstrings for every function you create.
- Use default parameters for common cases.

## Common Mistakes
- Forgetting to call the function after defining it.
- Forgetting `return` and wondering why the result is `None`.
- Trying to use a local variable outside its function.
- Using too many global variables, making code hard to trace.

## Interview Questions
- What is the difference between a parameter and an argument?
- What does `return` do in a function?
- What is scope and why does it matter?
- What is a lambda function?
- When would you use `map()` and `filter()`?

## Exercises
- Write a function that takes a name and prints a greeting.
- Write a function that takes two numbers and returns the larger one.
- Write a function that takes a list of numbers and returns their sum.
- Write a lambda that checks if a number is even.
- Use `map()` to convert a list of strings to uppercase.
- Use `filter()` to remove empty strings from a list.

---

# SECTION 4: DATA STRUCTURES IN PYTHON

---

## 4.1 List — The Flexible Container

**Simple Explanation:**
A list is a collection of items stored in order. You can add, remove, and change items easily.

**Deep Explanation:**
Lists in Python are dynamic arrays. They keep items in order. You access items by index starting from 0. Lists can hold any type of data: numbers, strings, or even other lists. They are the most common structure in Python because of their flexibility.

Important list methods:
- `.append(x)`: Add `x` to the end.
- `.insert(i, x)`: Insert `x` at position `i`.
- `.remove(x)`: Remove the first occurrence of `x`.
- `.pop(i)`: Remove and return the item at index `i`.
- `.sort()`: Sort the list in place.
- `.reverse()`: Reverse the list in place.
- `.index(x)`: Find the index of `x`.
- `.count(x)`: Count how many times `x` appears.
- `.copy()`: Make a shallow copy.

Lists are mutable, meaning you can change them after creation.

**Real-World Analogy:**
A list is like a to-do list on paper. You write tasks in order. You can add new tasks at the end, cross some out, or change the order.

**Step-by-Step Breakdown:**
1. Create a list with square brackets.
2. Access items by index.
3. Use `.append()` to add at the end.
4. Use `.remove()` to delete an item.
5. Use a loop to visit each item.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits[0] = "avocado"
print(fruits[1])

for fruit in fruits:
    print(fruit)
```

---

## 4.2 Nested Lists and Matrices

**Simple Explanation:**
A nested list is a list inside another list. It is used to represent tables, grids, and matrices.

**Deep Explanation:**
Nested lists are lists where each item is also a list. You access items with double indexing: `matrix[row][column]`. Nested lists are the foundation for representing 2D data in Python before you learn libraries like NumPy.

**Real-World Analogy:**
A nested list is like a classroom seating chart. Each row is a list of students. The whole chart is a list of rows.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # 6 (row 1, column 2)

# Print all rows
for row in matrix:
    print(row)
```

---

## 4.3 Dictionary — The Lookup System

**Simple Explanation:**
A dictionary stores data in key-value pairs. You look up a key and get the value.

**Deep Explanation:**
Dictionaries use a technique called hashing. When you give a key, the dictionary computes where the value is stored and retrieves it instantly. This makes lookups extremely fast, even with millions of items.

Important dictionary methods:
- `.get(key, default)`: Safely get a value.
- `.keys()`: Get all keys.
- `.values()`: Get all values.
- `.items()`: Get all key-value pairs.
- `.update(other)`: Merge another dictionary.
- `.pop(key)`: Remove a key and return its value.

Dictionary keys must be immutable (strings, numbers, tuples). Values can be anything.

**Real-World Analogy:**
A dictionary is like a real dictionary. You look up a word (key) and find its meaning (value). It is also like a phone book. You search a name and find a number.

**Step-by-Step Breakdown:**
1. Create a dictionary with curly braces.
2. Add or update a key with `dict[key] = value`.
3. Read a value with `dict[key]`.
4. Use `.get()` to safely read a key that might not exist.

```python
student = {
    "name": "Yasir",
    "age": 25,
    "course": "Python"
}

print(student["name"])
student["grade"] = "A"
print(student.get("city", "Unknown"))

# Loop through dictionary
for key, value in student.items():
    print(f"{key}: {value}")
```

---

## 4.4 Nested Dictionaries

**Simple Explanation:**
A nested dictionary is a dictionary inside another dictionary.

**Deep Explanation:**
Nested dictionaries are useful for complex data. For example, a school database where each student has their own dictionary of information. You access nested data with chained square brackets.

**Real-World Analogy:**
A filing cabinet has drawers. Each drawer has folders. Each folder has papers. Nested dictionaries are the same structure.

```python
school = {
    "student1": {"name": "Yasir", "grade": "A"},
    "student2": {"name": "Sara", "grade": "B"}
}

print(school["student1"]["name"])  # Yasir
```

---

## 4.5 Set — Unique Items Only

**Simple Explanation:**
A set is a collection that only keeps unique items. It automatically removes duplicates.

**Deep Explanation:**
Sets are implemented using hash tables, just like dictionaries. They do not store order. They are perfect for checking membership and removing duplicates from data. Set operations like union, intersection, and difference are very fast.

Set operations:
- **Union (`|`):** All items from both sets.
- **Intersection (`&`):** Items common to both sets.
- **Difference (`-`):** Items in the first set but not the second.
- **Symmetric Difference (`^`):** Items in either set, but not both.

**Real-World Analogy:**
A set is like a basket of unique colored balls. If you drop a red ball twice, the basket still only holds one red ball.

```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3}

a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # intersection: {3}
print(a | b)  # union: {1, 2, 3, 4, 5}
print(a - b)  # difference: {1, 2}
```

---

## 4.6 Tuple — Fixed Data

**Simple Explanation:**
A tuple is like a list, but you cannot change it after creation.

**Deep Explanation:**
Tuples are immutable. Once created, their contents are locked. This makes them faster than lists and safer for data that should not change. Tuples are often used for coordinates, database records, and function return values with multiple items.

Because tuples are immutable, they can be used as dictionary keys. Lists cannot.

**Real-World Analogy:**
A tuple is like a sealed envelope. You can read what is inside, but you cannot change it. It protects important information from accidental edits.

```python
point = (10, 20)
name_and_age = ("Yasir", 25)

print(point[0])
# point[0] = 15  # This will raise an error

# Tuple unpacking
name, age = name_and_age
print(name)
```

---

## 4.7 When to Use Which Structure

**Simple Explanation:**
Each data structure is a tool. Use the right tool for the job.

**Deep Explanation:**
- **List:** Use when order matters and you need to change items. Good for sequences, stacks, and queues.
- **Dictionary:** Use when you need fast lookups by a unique key. Good for mappings, caches, and indexes.
- **Set:** Use when you need uniqueness and fast membership testing. Good for removing duplicates and mathematical sets.
- **Tuple:** Use when data should not change. Good for fixed records, coordinates, and dictionary keys.

Choosing the right structure makes your code faster and easier to understand.

**Real-World Analogy:**
You would not eat soup with a fork. You choose the right utensil for the food. In programming, you choose the right data structure for the data.

```python
# List for ordered tasks
tasks = ["email", "code", "test"]

# Dictionary for fast lookup by name
phone_book = {"Yasir": "1234", "Sara": "5678"}

# Set for unique tags
tags = {"python", "dsa", "python"}  # stores only one "python"

# Tuple for fixed coordinates
location = (40.7, -74.0)
```

## Pro Tips
- Use lists when order matters and you need to change items.
- Use dictionaries when you need fast lookups by name.
- Use sets to remove duplicates and check membership.
- Use tuples for fixed data that should not change.
- Use nested structures when your data has multiple levels.

## Common Mistakes
- Modifying a tuple and getting a TypeError.
- Forgetting that dictionary keys must be unique.
- Using a list when a set would be faster for membership checks.
- Trying to use a mutable object (like a list) as a dictionary key.

## Interview Questions
- What is the difference between a list and a tuple?
- Why are dictionary lookups fast?
- When should you use a set?
- What types can be used as dictionary keys?

## Exercises
- Create a list of 5 favorite movies and print them.
- Create a dictionary of 3 countries and their capitals.
- Remove duplicates from a list using a set.
- Try to modify a tuple and observe the error.
- Create a nested dictionary representing a library with books and authors.

---

# SECTION 5: OBJECT-ORIENTED PROGRAMMING (OOP)

---

## 5.1 What Is OOP?

**Simple Explanation:**
OOP is a way of writing code by creating objects that represent real-world things.

**Deep Explanation:**
In OOP, you define a class as a blueprint. Then you create objects from that blueprint. Each object has its own data (attributes) and actions (methods). This makes code organized and reusable. Large programs become easier to manage because you group related data and behavior together.

The four pillars of OOP are:
- **Encapsulation:** Bundling data and methods together.
- **Inheritance:** Reusing code from a parent class.
- **Polymorphism:** Using the same method name for different types.
- **Abstraction:** Hiding complex details behind simple interfaces.

**Real-World Analogy:**
A class is like a car design blueprint. An object is an actual car built from that blueprint. Every car has the same features (wheels, engine, color) but each car can have its own color and speed.

**Step-by-Step Breakdown:**
1. Define a class with `class`.
2. Use `__init__` to set up each new object.
3. Add methods (functions inside the class) for behavior.
4. Create objects by calling the class like a function.

```python
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")

my_car = Car("red", "Toyota")
my_car.drive()
```

---

## 5.2 Inheritance

**Simple Explanation:**
Inheritance means a new class can use the features of an existing class.

**Deep Explanation:**
When a class inherits from another, it gets all the parent class attributes and methods. You can add new features or override old ones. This saves time because you do not rewrite code that already works.

Inheritance represents an "is-a" relationship. A Dog is an Animal. A Car is a Vehicle.

**Real-World Analogy:**
A child inherits traits from a parent: eyes, height, and habits. But the child can also learn new skills. Inheritance in code is the same.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog("Buddy")
cat = Cat("Kitty")
dog.speak()
cat.speak()
```

---

## 5.3 Encapsulation and Private Attributes

**Simple Explanation:**
Encapsulation means hiding the internal details of an object and only exposing what is necessary.

**Deep Explanation:**
In Python, you can make attributes "private" by prefixing them with two underscores (`__`). This triggers name mangling, making it harder to access the attribute from outside the class. This protects data from accidental changes.

You provide public methods (getters and setters) to read and modify private data safely.

**Real-World Analogy:**
A TV has buttons on the remote, but the internal circuits are hidden. You do not need to know how the circuits work to change the channel. Encapsulation is the TV case that hides the wires.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # 150
```

---

## 5.4 Special Methods (Dunder Methods)

**Simple Explanation:**
Special methods have double underscores before and after their names. They let you define how objects behave with built-in operations.

**Deep Explanation:**
Common dunder methods:
- `__init__`: Constructor, runs when an object is created.
- `__str__`: Returns a string representation for printing.
- `__repr__`: Returns an official string representation.
- `__len__`: Defines behavior for `len()`.
- `__eq__`: Defines behavior for `==`.

These methods make your classes work naturally with Python's built-in functions.

**Real-World Analogy:**
Dunder methods are like universal adapters. They let your custom object plug into Python's standard tools.

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __len__(self):
        return self.pages

book = Book("Python Guide", 300)
print(book)
print(len(book))
```

---

## 5.5 Class Methods and Static Methods

**Simple Explanation:**
Class methods work on the class itself, not on individual objects. Static methods are regular functions inside a class.

**Deep Explanation:**
- **Class method:** Uses `@classmethod` and receives `cls` instead of `self`. It can modify class-level data.
- **Static method:** Uses `@staticmethod`. It does not receive `self` or `cls`. It is just a utility function grouped with the class.

**Real-World Analogy:**
A class method is like a school announcement that applies to all students. A static method is like a general helper service available at the school but not tied to any student.

```python
class Student:
    school_name = "Green High"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school(cls):
        return cls.school_name

    @staticmethod
    def is_valid_grade(grade):
        return 0 <= grade <= 100

print(Student.get_school())
print(Student.is_valid_grade(85))
```

## Pro Tips
- Keep classes focused on one thing.
- Use inheritance when there is a true "is-a" relationship.
- Use `self` to access the object's own data inside methods.
- Use dunder methods to make your classes Pythonic.
- Encapsulate data to prevent accidental changes.

## Common Mistakes
- Forgetting `self` in method definitions.
- Trying to call a method before creating the object.
- Overcomplicating classes with too many responsibilities.
- Using inheritance when composition would be simpler.

## Interview Questions
- What is the difference between a class and an object?
- What is inheritance and why is it useful?
- What does `self` mean in Python?
- What is encapsulation?
- What is a dunder method?

## Exercises
- Create a `Student` class with name and grade.
- Create a `Teacher` class that inherits from `Person`.
- Add a method to the `Student` class that prints a greeting.
- Create a `Rectangle` class with `__str__` and `area()` methods.
- Create a class method that counts how many objects have been created.

---

# SECTION 6: ADVANCED PYTHON

---

## 6.1 List Comprehensions

**Simple Explanation:**
List comprehension is a shorter way to create a list from an existing collection.

**Deep Explanation:**
Instead of writing a loop with `.append()`, you write the logic inside square brackets. It is faster to write and often faster to run. You can also add a condition to filter items.

The general syntax is:
`[expression for item in collection if condition]`

You can also use dictionary comprehensions and set comprehensions.

**Real-World Analogy:**
Instead of picking apples one by one and placing them in a basket, you use a machine that selects only the red apples and drops them into the basket automatically.

```python
# Traditional loop
squares = []
for x in range(5):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(5)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Dictionary comprehension
squares_dict = {x: x ** 2 for x in range(5)}
print(squares_dict)
```

---

## 6.2 Generators

**Simple Explanation:**
A generator is a function that produces values one at a time instead of storing them all in memory.

**Deep Explanation:**
Generators use `yield` instead of `return`. Each time `yield` runs, the function pauses and remembers where it left off. When called again, it continues from that point. This is great for large data because you do not need to store everything at once.

Generator expressions look like list comprehensions but use parentheses instead of square brackets.

**Real-World Analogy:**
A vending machine gives one snack at a time. It does not dump all snacks on the floor. A generator is like a vending machine for data.

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)

# Generator expression
gen = (x ** 2 for x in range(1000000))
print(next(gen))
print(next(gen))
```

---

## 6.3 Iterators

**Simple Explanation:**
An iterator is an object that returns one item at a time when you ask for it.

**Deep Explanation:**
An iterator must implement two methods:
- `__iter__()`: Returns the iterator object itself.
- `__next__()`: Returns the next item or raises `StopIteration` when done.

Lists, tuples, dictionaries, and sets are all iterable. When you use a `for` loop, Python automatically creates an iterator behind the scenes.

**Real-World Analogy:**
An iterator is like a ticket dispenser at a bank. It gives you one ticket at a time. When there are no more tickets, it says "sorry, we are done."

```python
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

for num in CountDown(5):
    print(num)
```

---

## 6.4 Decorators

**Simple Explanation:**
A decorator is a function that wraps another function to add extra behavior.

**Deep Explanation:**
Decorators take a function as input, add something before or after it runs, and return the new function. They are used for logging, timing, access control, and caching. The `@` symbol is just syntactic sugar to make it clean.

You can also create decorators that accept arguments by nesting functions three levels deep.

**Real-World Analogy:**
A gift wrapper. You buy a gift. The wrapper adds a box, ribbon, and card. The gift is still inside, but now it looks better and has extra features.

```python
def say_hello(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@say_hello
def greet(name):
    print(f"Hello, {name}!")

greet("Yasir")
```

---

## 6.5 Error Handling

**Simple Explanation:**
Error handling lets your program keep running even when something goes wrong.

**Deep Explanation:**
The `try` block holds code that might fail. The `except` block catches the error and handles it. The `finally` block always runs, whether there is an error or not. This prevents your program from crashing unexpectedly.

You can catch specific exceptions or catch multiple exceptions with separate blocks. Using `finally` is good for cleanup, like closing files.

**Real-World Analogy:**
You try to open a door. If it is locked, you do not break the door. You have a backup plan: use another door. Error handling is your backup plan.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("That was not a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Done.")
```

---

## 6.6 File Input and Output

**Simple Explanation:**
File I/O means reading from and writing to files on your computer.

**Deep Explanation:**
Python provides the `open()` function to work with files. You specify the filename and mode:
- `'r'` read
- `'w'` write (overwrites)
- `'a'` append
- `'x'` create

Always close files after use, or use the `with` statement which closes automatically.

**Real-World Analogy:**
File I/O is like using a notebook. You open it, write notes, read old notes, and close it when done. The `with` statement is like a notebook that snaps shut automatically when you put it down.

```python
# Write to file
with open("notes.txt", "w") as file:
    file.write("Hello, file!\n")
    file.write("This is a new line.\n")

# Read from file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

## 6.7 Modules and Packages

**Simple Explanation:**
A module is a Python file containing code. A package is a folder of modules.

**Deep Explanation:**
Modules let you split your code into multiple files. You import them with `import` or `from ... import`. Packages let you organize modules into folders. A package folder must contain an `__init__.py` file (in older Python versions) to be recognized.

Using modules keeps your code clean, reusable, and easier to maintain. The Python standard library is a collection of modules for common tasks.

**Real-World Analogy:**
A module is like a toolbox. You keep all your screwdrivers in one box and all your wrenches in another. When you need a tool, you open the right box.

```python
# Using the math module
import math
print(math.sqrt(16))

# Using specific functions
from random import randint
print(randint(1, 10))

# Using aliases
import datetime as dt
print(dt.date.today())
```

## Pro Tips
- Use list comprehensions for simple loops. Avoid them if they become hard to read.
- Use generators when processing large files or streams.
- Use decorators for cross-cutting concerns like logging and timing.
- Catch specific errors, not all errors with a bare `except`.
- Always use `with` when working with files.
- Organize code into modules early. Do not wait until the file is 1000 lines long.

## Common Mistakes
- Nesting list comprehensions too deeply and making them unreadable.
- Confusing `yield` with `return`.
- Using a bare `except:` which hides bugs.
- Forgetting to close files when not using `with`.
- Circular imports between modules.

## Interview Questions
- What is the difference between a list comprehension and a loop?
- What does `yield` do?
- What is a decorator?
- What is the purpose of `finally`?
- What is the difference between an iterable and an iterator?
- Why should you use `with` for file operations?

## Exercises
- Use a list comprehension to create a list of squares for numbers 1 to 10.
- Write a generator that yields even numbers up to 20.
- Write a decorator that prints "Running..." before a function runs.
- Write a program that safely divides two numbers using try-except.
- Write a program that reads a file and counts the number of lines.
- Create a module with a function and import it into another file.

---

# SECTION 7: DSA FOUNDATIONS

---

## 7.1 What Is DSA?

**Simple Explanation:**
DSA stands for Data Structures and Algorithms. Data structures are ways to store data. Algorithms are step-by-step methods to solve problems.

**Deep Explanation:**
- **Data Structure:** A container that holds data in a specific arrangement. The arrangement decides how fast you can add, remove, or search.
- **Algorithm:** A clear recipe to solve a problem. It takes input, processes it, and gives output.

Together, DSA helps you write faster and smarter programs. It is the foundation of every tech interview and every large software system.

Data structures are not magic. They are simply different ways of organizing information. The right organization makes common operations fast. The wrong organization makes them slow.

**Real-World Analogy:**
Cooking is an algorithm. The ingredients are data. The container you mix them in is the data structure. A bowl, a blender, and a frying pan all hold food, but each is best for a different task.

---

## 7.2 Why DSA Matters

**Simple Explanation:**
DSA matters because it makes your programs fast, efficient, and reliable.

**Deep Explanation:**
Without DSA, a program might take hours to finish a task that could take seconds. The right data structure can turn a slow search into an instant lookup. The right algorithm can process millions of records quickly.

In interviews, DSA questions test your problem-solving ability. In production, DSA knowledge helps you build systems that scale to millions of users.

**Real-World Analogy:**
Imagine finding a name in a phone book. If the names are random, you check every page. That is slow. If the names are alphabetical, you jump to the middle and decide which half to search. That is fast. DSA is about choosing the right organization and strategy.

---

## 7.3 Time Complexity

**Simple Explanation:**
Time complexity tells you how much longer a program takes as the data grows.

**Deep Explanation:**
We use Big-O notation to describe time complexity. It ignores small details and focuses on growth. Here are the most common ones:
- **O(1):** Constant time. No matter how big the data, it takes the same time.
- **O(log n):** Logarithmic time. Doubling the data barely adds time.
- **O(n):** Linear time. If data doubles, time doubles.
- **O(n log n):** Fast sorting time.
- **O(n^2):** Quadratic time. Slow. Doubling data makes it four times slower.
- **O(2^n):** Exponential time. Extremely slow. Used only for very small inputs.

We analyze the worst case unless stated otherwise. The worst case tells us the maximum time we might wait.

**Real-World Analogy:**
- O(1): Grabbing your favorite book from your desk. One move, always.
- O(log n): Finding a word in a dictionary. You keep splitting the book in half.
- O(n): Finding a specific toy in a messy room. You check every toy.
- O(n^2): Comparing every student with every other student in a class.
- O(2^n): Trying every possible combination on a lock.

```python
# O(1) - instant lookup
data = {"apple": 1, "banana": 2}
print(data["apple"])

# O(n) - linear scan
items = [10, 20, 30, 40]
for item in items:
    print(item)

# O(n^2) - nested loop
for i in items:
    for j in items:
        print(i, j)
```

---

## 7.4 Space Complexity

**Simple Explanation:**
Space complexity tells you how much extra memory a program needs.

**Deep Explanation:**
Every variable, list, and dictionary uses memory. Space complexity measures how memory usage grows with input size. Sometimes you trade memory for speed. That is a common technique in DSA.

For example, recursive algorithms use stack space. Each recursive call adds a layer to the call stack. Deep recursion can run out of memory even if the logic is correct.

**Real-World Analogy:**
You want to sort books. You can sort them on the shelf (in-place, less space). Or you can move them all to a new shelf (extra space, maybe faster). Space complexity is about counting the extra shelves you need.

---

## 7.5 Best, Average, and Worst Case

**Simple Explanation:**
The same algorithm can be fast or slow depending on the input. We analyze three scenarios.

**Deep Explanation:**
- **Best case:** The input is perfectly arranged for the algorithm. Rare in practice.
- **Average case:** The expected performance over random inputs.
- **Worst case:** The maximum time the algorithm might take. This is what we usually care about.

For example, in linear search, the best case is finding the target at the first position. The worst case is finding it at the last position or not finding it at all.

**Real-World Analogy:**
Travel time to work. Best case: no traffic, all green lights. Average case: normal traffic. Worst case: accident, heavy rain, all red lights.

---

## 7.6 Analyzing Code Complexity

**Simple Explanation:**
To analyze complexity, count the number of basic operations relative to the input size.

**Deep Explanation:**
Basic steps include assignments, comparisons, arithmetic, and function calls. Ignore constants and lower-order terms. Focus on the dominant term as `n` grows large.

For example, a loop that runs `n` times with 5 operations inside is O(n), not O(5n). Constants disappear in Big-O.

**Step-by-Step Breakdown:**
1. Identify the input size `n`.
2. Count how many times the basic operations run.
3. Keep only the fastest-growing term.
4. Drop constants.
5. Write the result in Big-O notation.

```python
# O(n)
def print_items(items):
    for item in items:
        print(item)

# O(n^2)
def print_pairs(items):
    for i in items:
        for j in items:
            print(i, j)

# O(log n)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## Pro Tips
- Always ask: "What happens if the input gets ten times larger?"
- Prefer O(log n) or O(n) over O(n^2) when possible.
- Space-time tradeoff: using more memory can make your code faster.
- Focus on worst-case analysis for guaranteed performance.

## Common Mistakes
- Thinking faster code is always better. Sometimes memory matters more.
- Ignoring the worst-case scenario.
- Confusing time complexity with the actual clock time.
- Forgetting that recursion uses stack space.

## Interview Questions
- What is Big-O notation?
- What is the difference between O(n) and O(n^2)?
- Give an example of an O(1) operation in Python.
- What is the time complexity of binary search?
- Explain best, average, and worst case with an example.

## Exercises
- Write a function that prints all numbers from 1 to n. What is its time complexity?
- Write a nested loop that prints all pairs in a list. What is its time complexity?
- Explain why dictionary lookup is O(1).
- Analyze the time and space complexity of a recursive factorial function.
- Compare linear search and binary search on a list of one million items.

