<h1 style="background-color: #f0f0f0; padding: 10px;">0x05-python-exceptions</h1>
In Python, errors and exceptions are a fundamental part of the language's error-handling mechanism. Errors can occur when you run a Python program, and exceptions are a way to handle these errors gracefully. Here's an overview of errors, exceptions, and how to work with them in Python:
<ol>
<li><h4>Errors vs. Exceptions:</h4></li>
<ul>
<li><strong>Error:</strong>An error is a problem in your code that prevents it from running. Errors are often caused by syntax mistakes (e.g., a missing colon or a typo).</li>
<li><strong>Exception:</strong>An exception is a runtime error that occurs when the code is executing. It represents a situation where the code cannot proceed as expected, such as dividing by zero or trying to access an undefined variable.</li>
</ul>
<li><h4>Common Built-in Exceptions:</h4></li>
<ul>
<li><strong>SyntaxError: </strong>Raised when there is a syntax error in your code.</li>
<li><strong>IndentationError: </strong>Raised when there are issues with the indentation of your code.</li>
<li><strong>NameError: </strong>Raised when a variable or name is not defined.</li>
<li><strong>TypeError: </strong>Raised when an operation is performed on an inappropriate object type.</li>
<li><strong>ValueError: </strong>Raised when a function receives an argument of the correct type but an inappropriate value.</li>
<li><strong>ZeroDivisionError:</strong>Raised when attempting to divide by zero.</li>
</ul>
<li><h4>Handling Exceptions:</h4></li>
<ul>
<li>You can handle exceptions using <strong>try</strong> and <strong>except</strong> blocks. The <strong>try</strong> block contains the code that may raise an exception, and the <strong>except</strong> block contains the code to handle the exception.</li>
</ul>
<li><h4>Multiple except Blocks:</h4></li>
<ul>
<li>You can have multiple <strong>except</strong> blocks to handle different types of exceptions.</li>
</ul>
<li><h4>else and finally Blocks:</h4></li>
<ul>
<li>You can use an <strong>else</strong> block to specify code that should run when no exception occurs within the <strong>try</strong> block.</li>
</ul>
<li><h4> Raising Exceptions:</h4></li>
<ul>
<li>You can raise exceptions manually using the <strong>raise</strong> statement. This is useful when you want to signal an error condition in your code.</li>
</ul>
<li><h4>Custom Exceptions:</h4></li>
<ul>
<li>You can create your own custom exception classes by inheriting from the <strong>Exception</strong> class.</li>
</ul>
Clean-up actions, also known as resource management or finalization, are essential when you need to ensure that certain tasks or resources are properly handled and released, especially in the context of exceptions. 
</ol>
