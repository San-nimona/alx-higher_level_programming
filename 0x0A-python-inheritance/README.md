<section id="inheritance">
<h2><span class="section-number">9.5. </span>Inheritance<a class="headerlink" href="#inheritance" title="Permalink to this headline">¶</a></h2>
<p>Of course, a language feature would not be worthy of the name “class” without
supporting inheritance.  The syntax for a derived class definition looks like
this:</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><pre><span></span><span class="k">class</span> <span class="nc">DerivedClassName</span><span class="p">(</span><span class="n">BaseClassName</span><span class="p">):</span>
    <span class="o">&lt;</span><span class="n">statement</span><span class="o">-</span><span class="mi">1</span><span class="o">&gt;</span>
    <span class="o">.</span>
    <span class="o">.</span>
    <span class="o">.</span>
    <span class="o">&lt;</span><span class="n">statement</span><span class="o">-</span><span class="n">N</span><span class="o">&gt;</span>
</pre></div>
</div>
<p>The name <code class="xref py py-class docutils literal notranslate"><span class="pre">BaseClassName</span></code> must be defined in a
namespace accessible from the scope containing the
derived class definition.  In place of a base class name, other arbitrary
expressions are also allowed.  This can be useful, for example, when the base
class is defined in another module:</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><pre><span></span><span class="k">class</span> <span class="nc">DerivedClassName</span><span class="p">(</span><span class="n">modname</span><span class="o">.</span><span class="n">BaseClassName</span><span class="p">):</span>
</pre></div>
</div>
<p>Execution of a derived class definition proceeds the same as for a base class.
When the class object is constructed, the base class is remembered.  This is
used for resolving attribute references: if a requested attribute is not found
in the class, the search proceeds to look in the base class.  This rule is
applied recursively if the base class itself is derived from some other class.</p>
<p>There’s nothing special about instantiation of derived classes:
<code class="docutils literal notranslate"><span class="pre">DerivedClassName()</span></code> creates a new instance of the class.  Method references
are resolved as follows: the corresponding class attribute is searched,
descending down the chain of base classes if necessary, and the method reference
is valid if this yields a function object.</p>
<p>Derived classes may override methods of their base classes.  Because methods
have no special privileges when calling other methods of the same object, a
method of a base class that calls another method defined in the same base class
may end up calling a method of a derived class that overrides it.  (For C++
programmers: all methods in Python are effectively <code class="docutils literal notranslate"><span class="pre">virtual</span></code>.)</p>
<p>An overriding method in a derived class may in fact want to extend rather than
simply replace the base class method of the same name. There is a simple way to
call the base class method directly: just call <code class="docutils literal notranslate"><span class="pre">BaseClassName.methodname(self,</span>
<span class="pre">arguments)</span></code>.  This is occasionally useful to clients as well.  (Note that this
only works if the base class is accessible as <code class="docutils literal notranslate"><span class="pre">BaseClassName</span></code> in the global
scope.)</p>
<p>Python has two built-in functions that work with inheritance:</p>
<ul class="simple">
<li><p>Use <a class="reference internal" href="../library/functions.html#isinstance" title="isinstance"><code class="xref py py-func docutils literal notranslate"><span class="pre">isinstance()</span></code></a> to check an instance’s type: <code class="docutils literal notranslate"><span class="pre">isinstance(obj,</span> <span class="pre">int)</span></code>
will be <code class="docutils literal notranslate"><span class="pre">True</span></code> only if <code class="docutils literal notranslate"><span class="pre">obj.__class__</span></code> is <a class="reference internal" href="../library/functions.html#int" title="int"><code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code></a> or some class
derived from <a class="reference internal" href="../library/functions.html#int" title="int"><code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code></a>.</p></li>
<li><p>Use <a class="reference internal" href="../library/functions.html#issubclass" title="issubclass"><code class="xref py py-func docutils literal notranslate"><span class="pre">issubclass()</span></code></a> to check class inheritance: <code class="docutils literal notranslate"><span class="pre">issubclass(bool,</span> <span class="pre">int)</span></code>
is <code class="docutils literal notranslate"><span class="pre">True</span></code> since <a class="reference internal" href="../library/functions.html#bool" title="bool"><code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code></a> is a subclass of <a class="reference internal" href="../library/functions.html#int" title="int"><code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code></a>.  However,
<code class="docutils literal notranslate"><span class="pre">issubclass(float,</span> <span class="pre">int)</span></code> is <code class="docutils literal notranslate"><span class="pre">False</span></code> since <a class="reference internal" href="../library/functions.html#float" title="float"><code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code></a> is not a
subclass of <a class="reference internal" href="../library/functions.html#int" title="int"><code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code></a>.</p></li>
</ul>
<section id="multiple-inheritance">
<span id="tut-multiple"></span><h3><span class="section-number">9.5.1. </span>Multiple Inheritance<a class="headerlink" href="#multiple-inheritance" title="Permalink to this headline">¶</a></h3>
<p>Python supports a form of multiple inheritance as well.  A class definition with
multiple base classes looks like this:</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><pre><span></span><span class="k">class</span> <span class="nc">DerivedClassName</span><span class="p">(</span><span class="n">Base1</span><span class="p">,</span> <span class="n">Base2</span><span class="p">,</span> <span class="n">Base3</span><span class="p">):</span>
    <span class="o">&lt;</span><span class="n">statement</span><span class="o">-</span><span class="mi">1</span><span class="o">&gt;</span>
    <span class="o">.</span>
    <span class="o">.</span>
    <span class="o">.</span>
    <span class="o">&lt;</span><span class="n">statement</span><span class="o">-</span><span class="n">N</span><span class="o">&gt;</span>
</pre></div>
</div>
<p>For most purposes, in the simplest cases, you can think of the search for
attributes inherited from a parent class as depth-first, left-to-right, not
searching twice in the same class where there is an overlap in the hierarchy.
Thus, if an attribute is not found in <code class="xref py py-class docutils literal notranslate"><span class="pre">DerivedClassName</span></code>, it is searched
for in <code class="xref py py-class docutils literal notranslate"><span class="pre">Base1</span></code>, then (recursively) in the base classes of <code class="xref py py-class docutils literal notranslate"><span class="pre">Base1</span></code>,
and if it was not found there, it was searched for in <code class="xref py py-class docutils literal notranslate"><span class="pre">Base2</span></code>, and so on.</p>
<p>In fact, it is slightly more complex than that; the method resolution order
changes dynamically to support cooperative calls to <a class="reference internal" href="../library/functions.html#super" title="super"><code class="xref py py-func docutils literal notranslate"><span class="pre">super()</span></code></a>.  This
approach is known in some other multiple-inheritance languages as
call-next-method and is more powerful than the super call found in
single-inheritance languages.</p>
<p>Dynamic ordering is necessary because all cases of multiple inheritance exhibit
one or more diamond relationships (where at least one of the parent classes
can be accessed through multiple paths from the bottommost class).  For example,
all classes inherit from <a class="reference internal" href="../library/functions.html#object" title="object"><code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code></a>, so any case of multiple inheritance
provides more than one path to reach <a class="reference internal" href="../library/functions.html#object" title="object"><code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code></a>.  To keep the base classes
from being accessed more than once, the dynamic algorithm linearizes the search
order in a way that preserves the left-to-right ordering specified in each
class, that calls each parent only once, and that is monotonic (meaning that a
class can be subclassed without affecting the precedence order of its parents).
Taken together, these properties make it possible to design reliable and
extensible classes with multiple inheritance.  For more detail, see
<a class="reference external" href="https://www.python.org/download/releases/2.3/mro/">https://www.python.org/download/releases/2.3/mro/</a>.</p>
</section>
</section>
