# Intro to Python

## Lesson 3

### What will we cover?

In this session, we'll cover:

- How to install & use libraries in Python (`pip`)
- What is Flask?
- Setting up a simple Flask project and responding to requests

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

### How to install & use libraries in Python (`pip`)

A _library_ is a collection of functions designed to do a particular task. For example, there are libraries for complex maths operations (the `math` library), talking to your computer's operating system (the `os` library), and even sending email (the `email` library). Libraries are also referred to as _modules_, but the terms can be used interchangeably.

Python comes with lots of built-in libraries, including the ones previously mentioned, but there are many more available for download on the Internet, using a tool called `pip`.

As an example of how we can use libraries in our code, we'll use the `math` library to calculate the square root of a number. Start by _importing_ the `math` library in your code, by placing this line at the top:

```python
import math
```

_Importing_ a library allows you to use its functions in your code. Now, we can write the code itself:

```python
import math

mynumber = math.sqrt(64)
print(mynumber)
```

The `math.sqrt()` part tells Python to look for the `sqrt()` function in the `math` library we imported earlier. The result of this code should be `8.0`, because the square root of 64 is 8.

You could also import only the parts of the `math` library that are important to you. To do this, you can use `from x import y`:

```python
from math import sqrt
```

This removes the need to use `math.sqrt()` - instead, you can just type `sqrt()` on its own. We'll see this later in the session.

Using `pip`, you can download more libraries to use in your Python program. We can use it to download Flask, the _framework_ we'll be using going forward in these sessions. The way you do this varies depending on your computer's operating system:

**On a Windows computer:**

- Press Start in the bottom left corner of the screen, and type "Command Prompt".
- In the black window that appears, type `pip install flask` and press enter.
- If you get an error, try searching for "Command Prompt" again, and right clicking the search result & clicking "Run as administrator".

**On a Mac or Linux computer**

- Open a terminal window. On a Mac, you can do this by pressing Command + Space at the same time, typing "Terminal" into the search bar that pops up, and pressing Enter.
- In the window that appears, type `sudo pip3 install flask` and press enter.
- You will be prompted for your computer's password - as you type it, nothing will appear, but it's still working. Once you've finished typing, press enter.

`pip` will automatically install the Flask library, as well as its _dependencies_ (the supporting libraries that Flask needs to do its job). If you get an error, then feel free to ask a mentor for help.

### What is Flask?

**Note that the instructions in this section will only work if you've managed to follow the previous section from start to finish. If you need help, feel free to ask a mentor.**

Flask is a framework that allows you to create web applications in Python. It handles everything from HTTP requests (the messages your Web browser uses to ask web sites for resources), to serving content such as images and webpages for you.

At the core of Flask is the router - this is how you hook up HTTP requests to code in your program. When a user tries to access a resource on your website, the router can run a function for you to handle that request; this is called an _endpoint_.

### Setting up a simple Flask project and responding to requests

We can create a very simple Flask application using just a few lines of code to help demonstrate this concept. First, we can start off by _importing_ Flask:

```python
from flask import Flask
```

(Note that by using `from x import y`, we only import the parts of Flask that are important to us.)

Then, we create a new Flask application. This allows us to hook up endpoints to functions in our code:

```python
app = Flask(__name__)
```

(You don't need to define `__name__` - it's a variable built into all Python programs by default.)

Now, we can hook up an endpoint and make it do something for us. We do this by creating a function that returns something:

```python
@app.route('/')
def hello_world():
    return 'Hello World!'
```

The `@app.route()` part tells the router that this function should run when we go to "`/`" on our web site - "`/`" is the "index page" of any website, and is requested when you navigate to the front page of most websites. For example, if you typed `www.apple.com` into your web browser, your browser would request the page "`/`" from `www.apple.com`.

By returning something from your function, you are sending a "response" to the HTTP request; you always need to send a response to HTTP requests, otherwise they will fail and you'll get an error.

Finally, we tell our app to listen for requests:

```python
if __name__ == "__main__":
    app.run()
```

The if statement checks whether we are running our app in a standalone fashion, as opposed to something else running it for us - you can ignore this, but it's helpful to know why it's there. The final code should look something like this:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run()
```

Finally, run your app - if there are no errors, you should see some output in the console, and your app will keep running. At this point, you can open a web browser and go to [`http://localhost:5000`](http://localhost:5000) (or, if you're reading this online, clicking that link should do the trick). You should see a white page with "Hello World!" on it - if so, your code is working fine! If not, then don't worry - mentors are on hand to help you, and sometimes getting Flask to work can be tricky.
