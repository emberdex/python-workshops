# Intro to Python

## Lesson 5

### What will we cover?

In this session, we'll cover:

- Web forms
- Reading request data
- Sending data to your Flask application from HTML
- Cookies
- Redirects and error handling

### Getting started with Python
If you've already managed to get Python working on your computer, you can skip this.

To follow these instructions, you need to have Python 3 installed on your computer, as well as a text editor if you're on Mac or Linux (we recommend Visual Studio Code).

**If you're on Windows:**
- Press Start, and look for a program called IDLE. Open it - you'll get a white window with some text in it.
- At the top, click File > New - you'll get another window, where you'll type your code in.
- Save this empty file somewhere, making sure the name of the file has .py at the end of it.
- ~~To run your code, press F5 on your keyboard, or click Run > Run Module.~~
- If you're trying to run Flask code, running it in IDLE won't work because of a bug with IDLE. You can continue to edit in IDLE, but if you want to run your code, find where you saved it and double-click the file. It should open in a black Command Prompt window instead.

**If you're on a Mac or Linux**
- Open Visual Studio Code, and create a new file by clicking File > New.
- Save this empty file somewhere, making sure the name of the file has .py at the end of it.
- You might be prompted to install the 'Python' extension - do so, and click Reload when it finishes. Visual Studio Code will restart.
- To run your code, in the menu bar, click Debug > Start Without Debugging. A window will appear at the bottom of Visual Studio Code with your code's output in it.

This lesson is a continuation of Lesson 3, so it's important to have followed it from start to finish as we'll use some of those files and concepts later. If you missed lesson 3, you can find the guide [here.](http://hacksoc.net/python-3)

If you have trouble with any of this, feel free to ask a mentor for help! Note that for this session, **you'll need all of the files you created in sessions 3 and 4 to progress.**

_**Disclaimer:** the following worksheet is not a guide for creating a secure login form, and should not be used as such. It merely serves as an example of how to use web forms and how to hook them up to Flask applications._

### Web forms

Web forms are a powerful means of accepting data from your user, and are commonly found wherever text is entered on typical websites. This extends to login pages, social media sites (where there are comment boxes, places to create posts) and comment boxes.

In this example, we'll create a sample login page, which we can wire up to our Flask application later. First, let's start by creating a new file in our `templates` folder, called `login.html`. This is where we'll place our login form.

To make life easier, you can start by taking this skeleton code and pasting it into your new template:

```html
<html>
    <head>
        <title>Login</title>
    </head>

    <body>
        <h1>Login</h1>
        <!-- All of your form stuff should go beneath this line -->
    </body>
</html>
```

This creates the base for our login page. Next, we can start off by using the `<form>` tag to create a form on our page. Leave it empty for now, it should just look something like this:

```html
<form>

</form>
```

Next, we can start populating our form with fields. These are the various text boxes and buttons you see inside the form, and each one of them has a unique identifier (the `name` attribute) to allow them to be processed by our Flask application. We can start by using the `<input>` tag to add some text boxes; we'll use these as our username and password fields:

```html
<form>
    <input type="text" name="username" placeholder="Username"><br />
    <input type="password" name="password" placeholder="Password"><br />
</form>
```

The `<input>` tag has three attributes:

- The `type` attribute tells the browser what type of input element this is. In this case, we want a text box and a password box respectively.
- The `name` attribute is the unique identifier we alluded to earlier - in this case, we'll call it "username".
- The `placeholder` attribute is some placeholder text that will appear inside our text box.

Finally, the `<br />` tag is a line break - placing this in our page will start a new line.

Now, we can add a submit button to actually perform the login; we'll do this using the `<button>` tag:

```html
<button type="submit">Login</button>
```

The `type` attribute tells the browser what to do - giving it a value of "submit" tells the browser to submit the form that this button belongs to. The text between the tags is the text you want to appear inside the button.

Your login template should now look something like this:

```html
<html>
    <head>
        <title>Login</title>
    </head>

    <body>
        <h1>Login</h1>
        <form>
            <input type="text" name="username" placeholder="Username"><br />
            <input type="password" name="password" placeholder="Password"><br />
            <button type="submit">Login</button>
        </form>
    </body>
</html>
```

Finally, we can hook this up to an endpoint on our site. In our `app.py`, create a new endpoint on `/login` that uses this template, using the code we've written before as an example. If you get stuck, your code should look something like this:

```python
@app.route('/login')
def show_login_page():
    return render_template("login.html")
```

Now, when you restart your Flask application and [click this link](http://localhost:5000/login), you should be presented with a login page. This won't do anything at the moment; don't worry though, the next few sections will be spent hooking this up to our Flask application.

### Reading request data

In order to log the user in, we're going to need to write some code to read the username and password they've entered, and check it against our records to see if it matches. To do this, we can use a POST request - this is a type of HTTP request that sends some data to a server, instead of requesting it like a GET request would do.

We can start by defining a username and password in our `app.py`, below all of our imports:

```python
username = "my-super-secret-username"
password = "MySuperSecretPassword"
```

Next, we need to import some objects from the Flask library so we can read the data, as well as do some of the other things in this section:

```python
from flask import request, redirect, abort, url_for
```

Then, we can modify the endpoint we created earlier to accept both GET and POST requests. We do this by changing the `@app.route()` decorator to specify this:

```python
@app.route("/login", methods=['GET', 'POST'])
```

Now our endpoint is set up to receive both GET and POST requests. We can define different behaviours depending on whether the request is a GET or POST request - in this case, we want to display the login page if we receive a GET request, and handle the login if we receive a POST request. We can look at the `request.method` attribute to test for this:

```python
@app.route("/login", methods=['GET', 'POST'])
def show_login_page():
    if request.method == "GET":
        return render_template("login.html")
```

These code changes won't have changed the behaviour just yet - now we need to specify what happens when we send a POST request:

```python
if request.method == "POST":
    # Do something here!
```

Now, we need to check that what the user typed as their username and password actually matches our records. To see these fields, we can use the dictionary stored in `request.form`:

```python
if request.method == "POST":
    if request.form["username"] == username and request.form["password"] == password:
        return redirect("/")
    else:
        abort(401)
```

The keys "username" and "password" will vary depending on what you specified as the `name` attribute in your form. If the user enters the username and password correctly, we should redirect them back to the homepage, otherwise we should throw a HTTP 401 (Unauthorised) error and not continue with the request.

The final code should look like this:

```python
@app.route('/login', methods=['GET', 'POST'])
def show_login_page():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        if request.form["username"] == username and request.form["password"] == password:
            return redirect("/")
        else:
            abort(401)
```

### Redirects and error handling

We can use redirects and error handling to display pages if an error condition occurs, such as the user entering an invalid username, or the user trying to go to a page which doesn't exist. You can use the `@app.errorhandler()` decorator to handle certain HTTP error codes which may occur, enabling you to create custom pages for these errors and do whatever you need to do in the background.

We can start by creating a new function with this decorator to handle the 401 error we threw before:

```python
@app.errorhandler(401)
def handle_unauthorised(error):
    return "The username or password you entered was incorrect. Please try again.", 401
```

The number after our return statement is important - this is the HTTP status code that we want to send back to our browser. If you are handling an error condition, you should always signal that condition to your browser - never send back HTTP 200 (the default "OK" status code) if something has gone wrong!

Now, when a 401 error occurs, Flask will catch this and call this function to handle the error.

We can also use the `redirect()` function to redirect the user to another page. This can either take an absolute URL (e.g `"http://www.google.com"`), or the return value of `url_for()` - you should use the latter if you're redirecting to other pages within your own website.

### Sending data to your Flask application from HTML

Finally, we can begin to wire up the HTML to our Flask application to make it send the data from our login form to our server. To do this, we'll need to add a few attributes to our `<form>` tag we created earlier to tell it how and where to send the data to our server:

- The `method` attribute tells the browser which HTTP method to use to submit the form. In this case, we want a POST request.
- The `action` attribute tells the browser where to send the form data. In this case, we want it to be `"/login"`.

The form tag should now look something like this:

```html
<form method="POST" action="/login">
    ... everything else in between
</form>
```

Now, restart your Flask application and try to log in again. Everything should work now!

### Cookies

Cookies are pieces of data that a website can store on your computer for future reference. These are often used for tracking sessions, website settings and security purposes. You can send cookies to your user's web browser from Flask, and it will store these for you.

To read cookies, you can use the `request.cookies` object to look for a cookie, like so:

```python
cookie = request.cookies.get('my-cookie')
```

If a cookie is found under the name you specify, the function will return the value of the cookie, otherwise it will return `None`.

If you want to send a cookie, you'll need to use the response builder built into Flask to do so. You can import it like so:

```python
from flask import make_response
```

Then, when responding to requests, you can use `make_response()` to build a more fleshed-out response, containing cookies:

```python
@app.route('/my-test-page')
def test():
    resp = make_response(render_template("test.html"))
    resp.set_cookie("my-cookie", "This is a test cookie!")

    return resp
```

`resp` contains the contents of the template `"test.html"`, as well as the cookie we set using `resp.set_cookie()`.