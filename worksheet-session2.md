# Intro to Python
## Session 2

### What will we cover?
In this session, we'll cover the following concepts:

- _**"Hello World"**_, or writing your first line of code
- Variables and types
- Math operations
- Conditional programming (if statements)
- Loops (for, while loops)
- Functions
- Lists
- String operations
- Error handling and exceptions
- Decorators

We covered some of these in lesson 1, but it's important to recap.
If you need help at any point, then raise your hand or ask a mentor - they'll be more than happy to help!
Important keywords are in _italics_ - it can be helpful to remember these.

### Hello World, or writing your first line of code

When learning a new programming language, the first line of code you'll write is "Hello World" - a simple program which just prints "Hello World" to the screen.

In Python, such a program might look something like this:

```python
print("Hello World!)
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

### Functions
