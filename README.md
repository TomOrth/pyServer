# pyServer
Basic web server in python
#Basic Library
Outputs the response that you want on the screen in plain text<br />
Example:
```python
from server import Server
s = Server("Hello, world")
s.listen("0.0.0.0", 3000)
```
#Intermediate Library
Outputs either the plaintext response that you want or the html file that you want displayed

Plain Text:
```python
from server import Server
s = Server("text/plain")
s.listen("0.0.0.0", 3000, "Hello, World")
```

Html text
```python
from server import Server
s = Server("text/html")
s.listen("0.0.0.0", 3000, "hello.html")
```
hello.html
```html
<!DOCTYPE html>
<html>
  <body>
    <p><b>Hello World</b></p>
  </body>
</html>
```
Examples can be found in basicLibrary and intermediateLibrary folder
