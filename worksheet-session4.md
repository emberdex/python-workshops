# Intro to Python

## Lesson 4

### What will we cover?

In this session, we'll cover:

- Serving static content from your Flask server
- Fundamentals of HTML and CSS
- Styling your existing Web page

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

If you have trouble with any of this, feel free to ask a mentor for help!

### Serving static content from your Flask server

In certain situations, it can be useful to serve static content from your Flask server, such as images and downloadable files. Static content does not change unless you replace the file - Flask merely serves the content for you.

To start adding static content to your site, create a new folder in the same place you created the `templates` folder last session called "static". This is where you'll place any files you want to serve in the future.

Start off by placing an image of yourself or something that describes you in that folder - call it something meaningful, as we'll need that name for later.

Next, we'll take that template file we created last session and add a new tag to it to display your image. We'll explain what tags are later in this session, but for now, open up your template file and below the `</ul>` part, add the following code:

```html
<img src="{{ url_for('static', filename='your_image.jpg') }}" />
```

Make sure you replace the filename with the one in your `static` folder. The `url_for()` function tells Flask to create a link for a piece of static content on your computer - your web browser can then use this to download that content from your Flask server.

### Fundamentals of HTML and CSS

The HyperText Markup Language, or HTML for short, is a language that describes the contents and layout of a web page to your browser. Any page you view on the Internet is built using HTML, and it remains a standard used since the Internet was created.

The fundamental building blocks of HTML pages are called _tags_ - these are individual components of a page, and are enclosed in angle brackets (`<>`). Different tags have different purposes; for example, the `<h1>` tag is used to create headings, the `<img>` tag is used to add images, and so on. Note that most tags have a closing tag associated with them, with a couple of exceptions; for example, a `<h1>` tag will have an associated `</h1>` tag to close it off.

If you look at the template file we created last session, you can see lots of these tags inside one another. The most basic HTML page looks something like this:

```html
<html>
    <head>

    </head>

    <body>

    </body>
</html>
```

The `<html>` tag contains all the other tags in your page, and is there to tell the browser to treat the contents of the file as a HTML webpage. 

Inside the `<head>` tag goes all of the supporting information for your website, for example any scripts that might need to run to make your website work, and the title of your web page. 

The `<body>` tag contains everything your user will see, for example the text, images and links on your website.

Tags can also have attributes, which are values that tell your browser how to display that tag. We saw an example of this earlier when adding the image to our site; the `<img>` tag had a `src` attribute which told our browser where to find the image. 

Other common attributes include the `alt` attribute - this is used on images and some other elements to describe these images to people with visual impairments and those who use screen readers when browsing the Internet - this is an important step in making your website accessible to everybody. Another common attribute is the `id` tag - this is used in scripts that affect the appearance of your Web page to select elements on the page.

An attribute we'll be seeing a lot of in the future is the `class` attribute - we can use this to add styles to our elements later. For example, a paragraph might have its own class so that it can be styled uniquely:

```html
<p class="my-unique-paragraph">Colours and borders and fonts, oh my!</p>
```

For Flask templates specifically, anything between a set of curly braces (`{{ }}` or `{% %}`) are template blocks - these are used by Flask to substitute values into your webpage.

Some examples of useful tags include:

- `<h1>`, `<h2>`, `<h3>` through to `<h6>` are headings - these are useful for creating distinct sections on your website, or if you need larger text. You place the text you need between the opening and closing tags, like so:
```html
<h1>Here's my really big text!</h1>
<h6>And here's my much smaller text.</h6>
```
- `<p>` is a paragraph - this is used for blocks of text on your site.
- `<img>` is an image - this needs a `src` attribute for your browser to know where to load your image from. For example: `<img src="my_image.jpg" />`. The `<img>` tag does not need an associated closing tag.
- `<title>` sets the title of the webpage, shown at the top of your browser window.

There are many more useful tags which we'll come across in the future.

Earlier, we mentioned that you could use the `class` attribute to style elements. Styling is done using cascading style sheets, or CSS for short, which describe the style of HTML elements to your web browser. 

The `class` attribute can be used in CSS to style any element that shares that class - these are called class selectors. You can also apply styles to all tags of a certain type - this is called an element selector, and you could use this to, for example, apply a style to all `<p>` tags in your webpage.

If we go back to the unique paragraph we showed earlier in this worksheet, you can see it has a class attribute of "my-unique-paragraph":

```html
<p class="my-unique-paragraph">Colours and borders and fonts, oh my!</p>
```

In CSS, a class selector looks something like this (the dot at the start tells CSS to look for classes):

```css
.my-unique-paragraph {
    /* stuff goes in here */
}
```

Anything between the curly braces would be applied to any element that has that class. You can also use element selectors to style tags like so:

```css
p {
    /* Something else in here */
}
```

Anything between the curly braces would affect any `<p>` tag on your page, with one exception: if that `<p>` tag has a `class` attribute, any styles in that class will take precedence over those inside the element selector.

The part between the curly braces is called the _declaration_ - declarations contain properties, which tell your web browser how you want the selected elements to look. For example, if I wanted all `<p>` tags on the page to be red, my CSS would look like this:

```css
p {
    color: red;
}
```

Note that all properties must end with semicolons. There are a variety of useful CSS properties, some of which we'll use later:

- `font-family` controls the font used for text on your Web page. For example, we can use the `font-family` property to make all `<p>` tags use a sans-serif font:

```css
p {
    font-family: sans-serif;
}
```
- You can also specify additional fonts in a list & your browser will look for them from left to right, but you should be careful with this as you can't guarantee that any device you view your site on will have these fonts installed:

```css
p {
    /* this will look terrible */
    font-family: "Comic Sans MS", "Arial", sans-serif;
}
```
- `font-size` controls the font size of text on your webpage using CSS units, which you can learn more about [here.](https://www.w3schools.com/cssref/css_units.asp) For example, if you wanted to make that unique paragraph twice its normal size, you could specify that using the `em` unit:

```css
.my-unique-paragraph {
    font-size: 2em;
}
```
- `color` specifies the foreground colour of elements (e.g. text), and `background-color` specifies the background colour (note the American English spellings). You can either use [CSS colour names](https://www.w3schools.com/cssref/css_colors.asp), or use a [CSS colour picker](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool) to pick your own - make sure to use the `hex` value:

```css
p {
    color: #ff0000;
    background-color: black;
}
```
- `width` specifies the width of an element. This is especially useful for things such as images, where large images might run off the end of the screen; you can use the same [CSS units](https://www.w3schools.com/cssref/css_units.asp) to specify the width. For example, you might want an image to be 25% the width of your page:

```css
.my-image {
    width: 25%;
}
```

#### Styling your existing Web page

We can take the Web page we've been creating over the past couple of sessions and apply some styles to it. Firstly, we need to start off by editing our existing HTML file, which should already look like this:

```html
<html>
    <head>
        <title>Hello World!</title>
    </head>
    <body>
        <h1>Hi! My name is {{ name }}.</h1>
        <p>My hobbies include:</p>
        <ul>
            {% for hobby in hobbies %}
                <li>{{ hobby }}</li>
            {% endfor %}
        </ul>

        <img src="{{ url_for('static', filename='me.png') }}" />
    </body>
</html>
```

As we've seen already, the page looks pretty boring, so we can begin to spruce it up a little bit. Start by adding some classes to the `<h1>`, `<p>` and `<ul>` tags in the body - make sure they each have different names, otherwise you won't be able to style them uniquely. The result might look something like this:

```html
<h1 class="my-name">Hi! My name is {{ name }}.</h1>
<p class="my-hobbies-subheading">My hobbies include:</p>
<ul class="my-hobbies-list">
    {% for hobby in hobbies %}
        <li>{{ hobby }}</li>
    {% endfor %}
</ul>

<img class="my-image" src="{{ url_for('static', filename='me.png') }}" />
```

Next, we need a means of serving a CSS stylesheet to our Web page. We can do this using the static content technique we picked up earlier - start by creating a file called "styles.css" in your `static` folder. This is where we'll put all of the styles in your webpage.

Now we need to link the stylesheet to your webpage. In the `<head>`, below the `<title>`, you need to add the following tag:

```html
<link href="{{ url_for('static', filename='styles.css') }}" type="text/css" rel="stylesheet" />
```

This tells the browser to load the stylesheet from our Flask server and use it to style our webpage.

- The `href` attribute tells the browser where to look for the stylesheet - in this case, we use the Flask `url_for()` function to create a link to our static stylesheet.
- The `type` attribute tells your browser what kind of file is being loaded: in this case, it's a text file containing some CSS.
- The `rel` attribute tells your browser to treat the contents of the file as a stylesheet.

Now, the browser will load our stylesheet. When you restart your program and go to your webpage, you can see in the output that your stylesheet is being downloaded by your browser:

```
127.0.0.1 - - [23/Oct/2018 15:01:11] "GET /static/styles.css HTTP/1.1" 200 -
```

Now, we can start writing some CSS to style our webpage. We can start by adding selectors for our classes, making sure to change yours to the ones you specified while editing the template:

```css
.my-name {

}

.my-hobbies-subheading {

}

.my-hobbies-list {

}

.my-image {
    
}
```

If you want to change the style of the page itself, you can also add an element selector for the `body` tag:

```css
body {

}
```

This would enable you to set properties on the page itself, including setting the background color and setting a font that applies to all elements.

You can now set properties on all of these selectors to add styles to your webpage:

```css
body {
    background-color: #8FBFEF;
    font-family: "Verdana", sans-serif;
    color: #09335C;
}

.my-name {
    font-style: italic;
    font-size; 1.5em;
}

.my-hobbies-subheading {
    font-weight: bold;
}

.my-hobbies-list {
    font-style: italic;
}

.my-image {
    width: 25%;
}
```

Feel free to experiment with these styles - this is the fun of using CSS to style webpages! You can find a more comprehensive list of CSS properties and their effects [here.](https://www.w3schools.com/cssref/)

Save your changes and restart your Flask application for the changes to take effect. Your website should now look a lot nicer than it did before - here's my finished product:

![An image of my finished Flask website.](https://i.imgur.com/7i0w95J.png)

Congratulations - if you've made it this far, you've successfully built a simple web application in Flask, learning the concepts of Python, HTML and CSS along the way.