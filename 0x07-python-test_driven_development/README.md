<div class="post__body">
																		








<h2 class="wp-block-heading" id="h-what-is-doctest">What is Doctest?</h2><p>Testing is crucial in the software development phase. It helps ensure easy debugging, agile code, and enhanced reusability. Performing tests that cover all use cases helps prevent a codebase from breaking — minimizing exposure to vulnerabilities. Python has two main testing frameworks that developers can use, doctest and unittest.</p><p>Doctest is an inbuilt test framework that comes bundled with Python by default. The doctest module searches for code fragments that resemble interactive Python sessions and runs those sessions to confirm they operate as shown.</p>



<p>Developers commonly use doctest to test documentation. The doctest module looks for sequences of prompts in a docstring, re-executes the extracted command, and compares the output with the command’s input given in the docstrings test example.</p>



<p>The default action when running doctests is not to show the output when a test passes. However, we can change this in the doctest runner options. In addition, doctest’s integration with the Python unittest module enables us to run doctests as standard unittest test cases.</p>



<h2 class="wp-block-heading">What is Unittest?</h2>



<p>Unittest test case runners allow more options when running tests, like reporting test statistics such as tests that passed and failed.</p>



<p>Unittest uses methods created in classes to manage tests. It has support for automation, setup, and shutdown code when testing. Unittest has several rich, in-built features that are unavailable in doctest, including generators and group fixture managers like setUp and tearDown.&nbsp;</p>



<p>Since unittest follows the object-oriented method, it’s more suitable for testing class-based methods in a non-production environment. Continuous delivery tools such as Jenkins or Travis CI work better for production environments.<br>We’ll create a real-world example in the following sections, some code with customer information and discounts, and test it using doctest and unittest. Then we’ll analyze the tests and recommend the best ways to make further improvements.&nbsp;&nbsp;</p>



<h1 class="wp-block-heading">Using Unittest&nbsp;</h1>



<p>Let’s implement a <code>Customer</code> class and explore how we can test its methods using unittest.&nbsp;&nbsp;</p>



<p>At the terminal command prompt, create a <code>tests</code> directory, then create a subdirectory named <code>unittest</code>. We’ll later create our Python testing scripts in the <code>unittest</code> directory.&nbsp;</p>



<p>Use these commands to create the directory and subdirectory:</p>



<pre class="wp-block-code"><code>mkdir tests
cd tests 
mkdir unittest &amp;&amp; cd unittest</code></pre>



<p>Inside the <code>unittest</code> directory, create a Python script named <code>unittest/customer.py</code>. Then create a Customer class in that file as follows:</p>



<pre class="wp-block-code"><code>class Customer:
    """A sample customer class"""

    discount = 0.95

    def __init__(self, first_name, last_name, purchase):
        self.first_name = first_name
        self.last_name = last_name
        self.purchase = purchase

    @property
    def customer_mail(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def customer_fullname(self):
        return f'{self.first} {self.last}'

    def apply_discount(self):
        self.purchase = int(self.purchase * self.discount)</code></pre>



<p>In the Customer class, create a constructor to instantiate our objects: <code>first_name</code>, <code>last_name</code>, and <code>purchase</code>. Then create these three methods: <code>customer_mail</code>, <code>customer_fullname</code>, and <code>apply_discount</code>.&nbsp;</p>



<p>The <code>customer_mail</code> method returns a formatted customer’s email, <code>customer_fullname</code> returns the customer name, and <code>apply_discount</code> applies a five percent discount on the goods purchased. The <code>@property</code> decorator allows us to define the class methods like attributes through getters and setters.</p>



<p>To test the various methods we have created, we must create another Python file in the same directory and name it <code>unittest/test_customer.py</code>. It is a Python convention that all test files begin with a <code>test</code> prefix followed by the name of the file we’re testing.</p>



<p>Write the tests in the <code>test_customer.py</code> file like this:</p>



<pre class="wp-block-code"><code>import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer('John', 'Brad', 5000)
        self.customer_2 = Customer('Tina', 'Smith', 3000)

    def test_customer_mail(self):
        self.assertEqual(self.customer_1.customer_mail, 'John.Brad@email.com')
        self.assertEqual(self.customer_2.customer_mail, 'Tina.Smith@email.com')

    def test_customer_fullname(self):
        self.assertEqual(self.customer_1.customer_fullname, 'John Brad')
        self.assertEqual(self.customer_2.customer_fullname, 'Tina Smith')

    def test_apply_discount(self):
        self.customer_1.apply_discount()
        self.customer_2.apply_discount()

        self.assertEqual(self.customer_1.purchase, 4750)
        self.assertEqual(self.customer_2.purchase, 2850)


if __name__ == '__main__':
    unittest.main()
</code></pre>



<p>Now, we import unittest from the Python package, then import the <code>Customer</code> class we created in the <code>customer.py</code> file. In the <code>TestCustomer</code> class, we pass the <code>TestCase</code> from unittest as it allows us to check specific responses for every set of inputs. We then create three individual tests with methods starting with the prefix <code>test</code>. The test prefix shows the test runner which methods to test.&nbsp;</p>



<p>The <code>setUp</code> method is the first to execute when our tests run, and it’s where we define the customer instances. We use the assert method, <code>assertEqual</code>, to check equality for expected results in each test method.</p>



<p>For example, <code>test_customer_mail</code> checks whether the customer’s email corresponds to the one provided using the logic defined in the <code>unittest/customer.py</code> file and the attributes passed for that particular object. The same applies to the <code>test_customer_fullname</code> method.</p>



<p>In the last method, we apply the discount to the initial purchase and check the value passed. To learn more about various assert methods used in unittest, check out <a href="https://docs.python.org/3/library/unittest.html#assert-methods">Python’s documentation</a>.&nbsp;</p>



<p>The final block shows a simple command-line feature that enables us to run our tests. If we execute our tests in the terminal using python3 <code>test_customer.py</code>, the output is as follows:</p>



<pre class="wp-block-code"><code>...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

All our tests passed. If we try to alter the last method in our test and change the discount of the second customer to “2750”, our code throws an error as shown below:

F..
======================================================================
FAIL: test_apply_discount (__main__.TestCustomer)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_customer.py", line 23, in test_apply_discount
    self.assertEqual(self.customer_2.purchase, 2750)
AssertionError: 2850 != 2750

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)</code></pre>



<p>This testing helps to debug quickly and shows us where in the code we went wrong. By using unittest and writing tests that cover all use cases, we can improve our program’s readability, functionality, and logic flow.</p>



<h1 class="wp-block-heading">Using Doctest</h1>



<p>Using doctest is more straightforward than unittest, and has fewer steps. Although doctest is easy to use, we should use it wisely as there are several caveats.&nbsp;</p>



<p>Let’s start our demonstration using the same example as before.</p>



<p>In the tests directory we created, create a new directory, name it <code>tests/doctest</code> and create a <code>doctest_customer.py</code> file in it using these commands:</p>



<pre class="wp-block-code"><code>mkdir doctest
cd doctest &amp;&amp; touch doctest_customer.py</code></pre>



<p>We now have two test directories, <code>unittest</code> and <code>doctest</code>. The unittest directory is where we created our unittest examples earlier.&nbsp;<br>Inside <code>doctest/doctest_customer.py</code>, create the <code>Customer</code> class as follows:</p>



<pre class="wp-block-code"><code>class Customer:
    """
    A sample customer class
    """
    discount = 0.95

    def __init__(self, first, last, purchase):
        self.first = first
        self.last = last
        self.purchase = purchase

    def customer_mail(self):
        return f'{self.first}.{self.last}@email.com'

    def customer_fullname(self):
        return f'{self.first} {self.last}'

    def apply_discount(self):
        self.purchase = int(self.purchase * self.discount)
        return self.purchase</code></pre>



<p>In the terminal, type <code>python3</code> to get into the Python shell, then perform this operation:</p>



<pre class="wp-block-code"><code>Python 3.8.10 (default, Nov 26 2021, 20:14:08)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; from customer import Customer
&gt;&gt;&gt; customer_1 = Customer("John", "Brad", 5000)
&gt;&gt;&gt; customer_2 = Customer("Tina", "Smith", 3000)
&gt;&gt;&gt; customer_1.customer_mail()
'John.Brad@email.com'
&gt;&gt;&gt; customer_2.customer_mail()
'Tina.Smith@email.com'
&gt;&gt;&gt; customer_1.customer_fullname()
'John Brad'
&gt;&gt;&gt; customer_2.customer_fullname()
'Tina Smith'
&gt;&gt;&gt; customer_1.apply_discount()
4750
&gt;&gt;&gt; customer_2.apply_discount()
2850
&gt;&gt;&gt;</code></pre>



<p>In the snippet above, we call some of the methods in our class from the command line.&nbsp;</p>



<p>To run the doctest, place the output above into the class docstring like this:</p>



<pre class="wp-block-code"><code>class Customer:
    """
    A sample customer class

    &gt;&gt;&gt; customer_1 = Customer("John", "Brad", 5000)
    &gt;&gt;&gt; customer_2 = Customer("Tina", "Smith", 3000)
    &gt;&gt;&gt; customer_1.customer_mail()
    'John.Brad@email.com'
    &gt;&gt;&gt; customer_2.customer_mail()
    'Tina.Smith@email.com'
    &gt;&gt;&gt; customer_1.customer_fullname()
    'John Brad'
    &gt;&gt;&gt; customer_2.customer_fullname()
    'Tina Smith'
    &gt;&gt;&gt; customer_1.apply_discount()
    4750
    &gt;&gt;&gt; customer_2.apply_discount()
    2850
    """
    discount = 0.95

    def __init__(self, first, last, purchase):
        self.first = first
        self.last = last
        self.purchase = purchase

    def customer_mail(self):
        return f'{self.first}.{self.last}@email.com'

    def customer_fullname(self):
        return f'{self.first} {self.last}'

    def apply_discount(self):
        self.purchase = int(self.purchase * self.discount)
        return self.purchase

if __name__ == "__main__":
    import doctest
    doctest.testmod()</code></pre>



<p>To be able to execute our tests, we import doctest below the file, and run our tests by executing <code>python3 doctest_customer.py -v</code> in the terminal.&nbsp;</p>



<p>The output is:</p>



<pre class="wp-block-code"><code>Trying:
    customer_1 = Customer("John", "Brad", 5000)
Expecting nothing
ok
Trying:
    customer_2 = Customer("Tina", "Smith", 3000)
Expecting nothing
ok
Trying:
    customer_1.customer_mail()
Expecting:
    'John.Brad@email.com'
ok
Trying:
    customer_2.customer_mail()
Expecting:
    'Tina.Smith@email.com'
ok
Trying:
    customer_1.customer_fullname()
Expecting:
    'John Brad'
ok
Trying:
    customer_2.customer_fullname()
Expecting:
    'Tina Smith'
ok
Trying:
    customer_1.apply_discount()
Expecting:
    4750
ok
Trying:
    customer_2.apply_discount()
Expecting:
    2850
ok
5 items had no tests:
    __main__
    __main__.Customer.__init__
    __main__.Customer.apply_discount
    __main__.Customer.customer_fullname
    __main__.Customer.customer_mail
1 items passed all tests:
   8 tests in __main__.Customer
8 tests in 6 items.
8 passed and 0 failed.
Test passed.</code></pre>



<p>All the tests passed. This demonstration makes it safe to say that doctest is more suitable for writing executable documentation for a package while unittest is better suited for testing documentation, and we can use this feature when reducing bugs in software documentation. For more information about doctest, see <a href="https://docs.python.org/3.8/library/doctest.html">Python’s documentation</a>.</p>



<h1 class="wp-block-heading">Next Steps</h1>



<p>Testing is a critical software development process since it ensures the code is clean and works as expected. Choosing the right way to test your code before executing tests is crucial.&nbsp;</p>



<p>Performing tests using the unittest framework allows us to test our code in an object-oriented approach. It supports many features such as test automation, setup, and code test teardown. Doctest, in contrast, is more suitable for documentation since we can insert it in the code’s docstrings.</p>



<p><em>This blog post was created as part of the Mattermost </em><a href="https://handbook.mattermost.com/contributors/contributors/ways-to-contribute/community-content-program"><em>Community Writing Program</em></a><em> and is published under the </em><a href="https://creativecommons.org/licenses/by-nc-sa/4.0/"><em>CC BY-NC-SA 4.0 license</em></a><em>. To learn more about the Mattermost Community Writing Program, </em><a href="https://mattermost.com/blog/blog-announcing-community-writing-program/"><em>check this out</em></a><em>.</em></p>
								</div>
