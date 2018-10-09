# Intro to Python
## Session 2

### What will we cover?
In this session, we'll cover the following concepts:

- _**"Hello World"**_, or writing your first line of code
- Variables and types
- Math operations
- Conditional programming (if statements)
- Functions
- Lists
- Loops (for, while loops)
- String operations
- Error handling

We covered some of these in lesson 1, but it's important to recap.
If you need help at any point, then raise your hand or ask a mentor - they'll be more than happy to help!
Important keywords are in _italics_ - it can be helpful to remember these.

### Getting started with Python
If you've already managed to get Python working on your computer, you can skip this.

To follow these instructions, you need to have Python 3 installed on your computer, as well as a text editor if you're on Mac or Linux (we recommend Visual Studio Code).

**If you're on Windows:**
- Press Start, and look for a program called IDLE. Open it - you'll get a white window with some text in it.
- At the top, click File > New - you'll get another window, where you'll type your code in.
- Save this empty file somewhere, making sure the name of the file has .py at the end of it.
- To run your code, press F5 on your keyboard, or click Run > Run Module.

**If you're on a Mac or Linux**
- Open Visual Studio Code, and create a new file by clicking File > New.
- Save this empty file somewhere, making sure the name of the file has .py at the end of it.
- You might be prompted to install the 'Python' extension - do so, and click Reload when it finishes. Visual Studio Code will restart.
- To run your code, in the menu bar, click Debug > Start Without Debugging. A window will appear at the bottom of Visual Studio Code with your code's output in it.

If you have trouble with any of this, feel free to ask a mentor for help!

### Hello World, or writing your first line of code

When learning a new programming language, the first line of code you'll write is "Hello World" - a simple program which just prints "Hello World" to the screen.

In Python, such a program might look something like this:

```python
print("Hello World!")
```

If you run this program and it works, congratulations! You just wrote your very first line of Python code. If not, don't worry - refer back to the "Getting Started" section of this worksheet for some pointers on getting Python set up on your computer.

### Variables and types

A _variable_ is a value in your code that you can change. This is useful for storing values that you might need to use later. You can create variables like this:

```python
testing = 3
```

This creates a _variable_ called "testing", and assigns it with a value of 3. You can then use this variable later on in your code, for example if you want to print its value to the screen:

```python
testing = 3
print(testing)
```

Variables in Python have _types_ - when you assign a value to a variable, Python automatically works out what "type" that variable should be. This is called _dynamic typing_.

Examples of types include:

- Integers (whole numbers) - `int`
- Strings (blocks of text, e.g. `"Hello World"`) - `str`
- Decimal numbers - `float`
- Booleans (`True` or `False`) - `bool`

You don't have to worry about these for now, but knowing about types can be very important in the future.

### Math operations

In Python, you can perform maths on numbers using _operators_. For example, if you wish to add two numbers together:

```python
mynumber = 2 + 3
print(mynumber)
```

In this case, we have used the `+` operator to add `2` and `3` together. As a result, the variable `mynumber` has a value of 5.

Examples of some operators you can use are:

- Addition - `+`
- Subtraction - `-`
- Multiplication - `*`
- Division - `/`
- Modulus - `%`
    - The modulus operator returns the remainder of a division.
    - For example, `10 % 3` would return 1, because `10` divided by `3` would give you 3 with 1 number "left over".
- Powers - `**`
    - For example, `3 ** 2` would return 9, because 3 to the power of 2 is 9.

### Conditional programming (if statements)

There are times where you might want to run a piece of code only under certain conditions. For that, we have the `if` statement.

An `if` statement in Python looks something like this:

```python
myvariable = 3

if myvariable == 3:
    print("My variable is 3")
```

The part after `if` is the _condition_ - this determines whether the code should run. If the condition is `True`, the code runs. If not, it is skipped over.

The `==` symbol is an _equality_ check - this compares the values on either side of it, in this case `myvariable` and `3`, and checks if they are the same. If they are, it returns `True`, otherwise it returns `False`.

Examples of other comparisons you can do include:

- Not equal - `!=`
    - This is `True` if the values on either side are **not** the same.
- Less than - `<`
    - This is `True` if the value on the left is **less than** the value on the right.
- Greater than - `>`
    - Same principle as less than, but is `True` if the value on the left is **greater than** the value on the right.
- Less than or equal to - `<=`, greater than or equal to - `>=`
    - These work the same as the less than or greater than operators, but they are also `True` if the values are the same.

For example, you might have some code that looks like this:

```python
myvalue = 4

if myvalue >= 4:
    print("my value is 4 or more")
```

In this case, the code would run, because the condition is true (`myvalue` is greater than or equal to 4). If you were to change it to a smaller number, the code would no longer work.

You can also have multiple conditions in a single if statement, using `and` & `or`:

```python
myvalue = 4

if myvalue >= 4 and myvalue <= 6:
    print("My value is between 4 and 6")
```

In this case, the code only runs if both of the conditions are true. If you were to change the number to something not between 4 or 6, the code would no longer run, because one of the conditions is no longer true.

You can also choose to run a piece of code if the condition in your if statement is not true, using the `else` statement:

```python
myvalue = 4

if myvalue == 5:
    print("My value is 5")
else:
    print("My value is not 5")
```

In this case, you would see "My value is not 5" on the screen, because the condition is not true. If you were to change `myvalue` to 5, you would see "My value is 5".

### Functions

Functions are blocks of code you can reuse over and over again, to avoid repeating yourself. In fact, you've been using one throughout this worksheet - `print()` is a function!

To create your own function, you _declare_ it like this:

```python
def myfunction():
    print("This is my function!")
```

The `def` keyword tells Python that the code that follows is a function. In this case, our function is called `myfunction`.

You can then _call_ these functions like so:

```python
myfunction()
```

This will run the code inside your function.

You can also _pass_ values to a function, by declaring it like so (these are called _arguments_):

```python
def myfunction(number):
    print("My number is " + str(number))

myfunction(3)
```

Note the "`number`" inside the brackets. This automatically creates a variable, called `number`, for you to use inside that function. You pass in the number by putting it between the brackets when you call the function.

Additionally, the the `str()` function converts a `number` to a `string` - this allows us to combine it with another string.

You can also have multiple _arguments_ by separating them with commas, like so:

```python
def myfunction(number1, number2):
    print(number1 + number2)

myfunction(1, 2)
```

Functions can also _return_ values, which you can then assign to variables. This is useful if you want a function to do something for you:

```python
def add3numbers(number1, number2, number3):
    result = number1 + number2 + number3
    return result

mynumber = add3numbers(1, 2, 3)
print(mynumber)
```

In this case, the value of `mynumber` is whatever gets returned by `add3numbers()` - in this instance, 6.

### Lists

Lists are a special _type_ in Python - they contain multiple items which you can access individually. You can create a list like this:

```python
fruits = ["apple", "banana", "orange", "pineapple"]
```

This creates a list, called `fruits`, with four items, `"apple"`, `"banana"`, `"orange"` and `"pineapple"`.

You can get the number of items in a list using the `len()` function:

```python
fruits = ["apple", "banana", "orange", "pineapple"]
len(fruits)
```

`len()` returns the number of items in a list, in this case `len()` returns 4.

If you want to add an item to a list, you can use the `append()` _method_ on your list, like so:

```python
fruits.append("tangerine")
```

This will add "tangerine" to the end of the list.

### Loops
Loops are used to run pieces of code repeatedly under certain conditions. Python has two types of loop: the `for` loop and the `while` loop.

A `for` loop allows you to run a piece of code for each item in a list. This is called _iterating_ over a list. You can use the list of fruits from earlier in a for loop, like so:

```python
fruits = ["apple", "banana", "orange", "pineapple"]

for fruit in fruits:
    print(fruit)
```

`fruits` is the name of the list you want to _iterate_ over, and `fruit` is the name of the "current" item in the list. This code would output the following:
```
apple
banana
orange
pineapple
```

If you want to run a piece of code a given number of times, you can do so using the `range()` function:

```python
for i in range(100):
    print(i)
```

This will print all positive integers below 100, including 0.

A `while` loop allows a piece of code to run while a certain condition is true, much like an `if` statement. For example, you could print all of the numbers from 0 to 100 using a while loop instead of a for loop:

```python
current_number = 0

while current_number <= 100:
    print(current_number)
    current_number = current_number + 1
```

The code continues to run while the condition in the `while` statement is true. Because we add one to the number every time, the code will eventually stop running when `current_number` becomes greater than 100.

Be careful - if the condition in your while loop is always true, your code will run infinitely. Don't worry if this happens - if you get stuck in a loop, you can just press `Control-C` on your keyboard to stop your program from running.

### String operations

There are some operations you can do on strings (text) that might come in useful.

One operation you can do is checking if your string contains certain text - this is called checking for a _substring_ (a string within a string).

In Python, you can do it like this:

```python
mystring = "This is a quick test."

if "quick" in mystring:
    print("Speedy!")
```

We're using the `in` keyword to check if `"quick"` is contained in `mystring` - in this case, it is, so the condition is true and our code can run. You can also use `in` with lists, to check if a list contains an item.

Another operation you can do is combining strings together - this is called _concatenation_.

In Python, you can do it using the `+` operator:

```python
mystring = "Hello " + "World!"
print(mystring)
```

This code will print `Hello World!` to the screen.

### Error handling
Sometimes, when running our Python code, errors can occur which require our attention. For example, if we try to divide a number by zero:

```python
myvariable = 3 / 0
```

Our code will crash with the following error:

`ZeroDivisionError: division by zero`

We can catch this error using a `try` block:

```python
myvariable = 0
try:
    myvariable = 3 / 0
```

Note that you need to declare any variables you want to create **outside** of the try block, otherwise you can't access them when the block finishes.

This code won't work on its own - each `try` block needs its own corresponding `except` block:

```python
myvariable = 0
try:
    myvariable = 3 / 0
except ZeroDivisionError:
    print("You tried to divide by zero")
```

This catches any `ZeroDivisionError` when one occurs - the code inside the `except` block is run if the code inside the `try` block _throws_ an error.
