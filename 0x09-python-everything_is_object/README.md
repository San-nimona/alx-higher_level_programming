<div class="section" id="lists">
<h1>9. Lists<a class="headerlink" href="#lists" title="Permalink to this headline">¶</a></h1>
<p>A <strong>list</strong> is an ordered set of values, where each value is identified by an
index. The values that make up a list are called its <strong>elements</strong>. Lists are
similar to strings, which are ordered sets of characters, except that the
elements of a list can have any type.  Lists and strings — and other things
that behave like ordered sets — are called <strong>sequences</strong>.</p>
<div class="section" id="list-values">
<h2>9.1. List values<a class="headerlink" href="#list-values" title="Permalink to this headline">¶</a></h2>
<p>There are several ways to create a new list; the simplest is to enclose the
elements in square brackets ( <tt class="docutils literal"><span class="pre">[</span></tt> and <tt class="docutils literal"><span class="pre">]</span></tt>):</p>
<div class="highlight-python"><div class="highlight"><pre><span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">40</span><span class="p">]</span>
<span class="p">[</span><span class="s">"spam"</span><span class="p">,</span> <span class="s">"bungee"</span><span class="p">,</span> <span class="s">"swallow"</span><span class="p">]</span>
</pre></div>
</div>
<p>The first example is a list of four integers. The second is a list of three
strings. The elements of a list don’t have to be the same type.  The following
list contains a string, a float, an integer, and
(mirabile dictu) another list:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="p">[</span><span class="s">"hello"</span><span class="p">,</span> <span class="mf">2.0</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">]]</span>
</pre></div>
</div>
<p>A list within another list is said to be <strong>nested</strong>.</p>
<p>Finally, there is a special list that contains no elements. It is called the
empty list, and is denoted <tt class="docutils literal"><span class="pre">[]</span></tt>.</p>
<p>Like numeric 0 values and the empty string, the empty list is false in a
boolean expression:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="k">if</span> <span class="p">[]:</span>
<span class="gp">... </span>   <span class="k">print</span> <span class="s">'This is true.'</span>
<span class="gp">... </span><span class="k">else</span><span class="p">:</span>
<span class="gp">... </span>   <span class="k">print</span> <span class="s">'This is false.'</span>
<span class="gp">...</span>
<span class="go">This is false.</span>
<span class="go">&gt;&gt;&gt;</span>
</pre></div>
</div>
<p>With all these ways to create lists, it would be disappointing if we couldn’t
assign list values to variables or pass lists as parameters to functions. We
can:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">vocabulary</span> <span class="o">=</span> <span class="p">[</span><span class="s">"ameliorate"</span><span class="p">,</span> <span class="s">"castigate"</span><span class="p">,</span> <span class="s">"defenestrate"</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">numbers</span> <span class="o">=</span> <span class="p">[</span><span class="mi">17</span><span class="p">,</span> <span class="mi">123</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">empty</span> <span class="o">=</span> <span class="p">[]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">vocabulary</span><span class="p">,</span> <span class="n">numbers</span><span class="p">,</span> <span class="n">empty</span>
<span class="go">['ameliorate', 'castigate', 'defenestrate'] [17, 123] []</span>
</pre></div>
</div>
</div>
<div class="section" id="accessing-elements">
<span id="id1"></span><h2>9.2. Accessing elements<a class="headerlink" href="#accessing-elements" title="Permalink to this headline">¶</a></h2>
<p>The syntax for accessing the elements of a list is the same as the syntax for
accessing the characters of a string—the bracket operator ( <tt class="docutils literal"><span class="pre">[]</span></tt> – not to
be confused with an empty list). The expression inside the brackets specifies
the index. Remember that the indices start at 0:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">numbers</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="go">17</span>
</pre></div>
</div>
<p>Any integer expression can be used as an index:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">numbers</span><span class="p">[</span><span class="mi">9</span><span class="o">-</span><span class="mi">8</span><span class="p">]</span>
<span class="go">123</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">numbers</span><span class="p">[</span><span class="mf">1.0</span><span class="p">]</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">"&lt;stdin&gt;"</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">TypeError</span>: <span class="n">list indices must be integers</span>
</pre></div>
</div>
<p>If you try to read or write an element that does not exist, you get a runtime
error:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">numbers</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">"&lt;stdin&gt;"</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">IndexError</span>: <span class="n">list index out of range</span>
</pre></div>
</div>
<p>If an index has a negative value, it counts backward from the end of
the list:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">numbers</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
<span class="go">123</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">numbers</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span>
<span class="go">17</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">numbers</span><span class="p">[</span><span class="o">-</span><span class="mi">3</span><span class="p">]</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">"&lt;stdin&gt;"</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">IndexError</span>: <span class="n">list index out of range</span>
</pre></div>
</div>
<p><tt class="docutils literal"><span class="pre">numbers[-1]</span></tt> is the last element of the list, <tt class="docutils literal"><span class="pre">numbers[-2]</span></tt> is the second
to last, and <tt class="docutils literal"><span class="pre">numbers[-3]</span></tt> doesn’t exist.</p>
<p>It is common to use a loop variable as a list index.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="n">horsemen</span> <span class="o">=</span> <span class="p">[</span><span class="s">"war"</span><span class="p">,</span> <span class="s">"famine"</span><span class="p">,</span> <span class="s">"pestilence"</span><span class="p">,</span> <span class="s">"death"</span><span class="p">]</span>

<span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="mi">4</span><span class="p">:</span>
    <span class="k">print</span> <span class="n">horsemen</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
</pre></div>
</div>
<p>This <tt class="docutils literal"><span class="pre">while</span></tt> loop counts from 0 to 4. When the loop variable <tt class="docutils literal"><span class="pre">i</span></tt> is 4, the
condition fails and the loop terminates. So the body of the loop is only
executed when <tt class="docutils literal"><span class="pre">i</span></tt> is 0, 1, 2, and 3.</p>
<p>Each time through the loop, the variable <tt class="docutils literal"><span class="pre">i</span></tt> is used as an index into the
list, printing the <tt class="docutils literal"><span class="pre">i</span></tt>-eth element. This pattern of computation is called a
<strong>list traversal</strong>.</p>
</div>
<div class="section" id="list-length">
<h2>9.3. List length<a class="headerlink" href="#list-length" title="Permalink to this headline">¶</a></h2>
<p>The function <tt class="docutils literal"><span class="pre">len</span></tt> returns the length of a list, which is equal to the number
of its elements. It is a good idea to use this value as the upper bound of a
loop instead of a constant. That way, if the size of the list changes, you
won’t have to go through the program changing all the loops; they will work
correctly for any size list:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="n">horsemen</span> <span class="o">=</span> <span class="p">[</span><span class="s">"war"</span><span class="p">,</span> <span class="s">"famine"</span><span class="p">,</span> <span class="s">"pestilence"</span><span class="p">,</span> <span class="s">"death"</span><span class="p">]</span>

<span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">num</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">horsemen</span><span class="p">)</span>
<span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">num</span><span class="p">:</span>
    <span class="k">print</span> <span class="n">horsemen</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
</pre></div>
</div>
<p>The last time the body of the loop is executed, <tt class="docutils literal"><span class="pre">i</span></tt> is <tt class="docutils literal"><span class="pre">len(horsemen)</span> <span class="pre">-</span> <span class="pre">1</span></tt>,
which is the index of the last element. When <tt class="docutils literal"><span class="pre">i</span></tt> is equal to
<tt class="docutils literal"><span class="pre">len(horsemen)</span></tt>, the condition fails and the body is not executed, which is a
good thing, because <tt class="docutils literal"><span class="pre">len(horsemen)</span></tt> is not a legal index.</p>
<p>Although a list can contain another list, the nested list still counts as a
single element. The length of this list is 4:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="p">[</span><span class="s">'spam!'</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="p">[</span><span class="s">'Brie'</span><span class="p">,</span> <span class="s">'Roquefort'</span><span class="p">,</span> <span class="s">'Pol le Veq'</span><span class="p">],</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]]</span>
</pre></div>
</div>
</div>
<div class="section" id="list-membership">
<h2>9.4. List membership<a class="headerlink" href="#list-membership" title="Permalink to this headline">¶</a></h2>
<p><tt class="docutils literal"><span class="pre">in</span></tt> is a boolean operator that tests membership in a sequence. We
used it previously with strings, but it also works with lists and
other sequences:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">horsemen</span> <span class="o">=</span> <span class="p">[</span><span class="s">'war'</span><span class="p">,</span> <span class="s">'famine'</span><span class="p">,</span> <span class="s">'pestilence'</span><span class="p">,</span> <span class="s">'death'</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s">'pestilence'</span> <span class="ow">in</span> <span class="n">horsemen</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s">'debauchery'</span> <span class="ow">in</span> <span class="n">horsemen</span>
<span class="go">False</span>
</pre></div>
</div>
<p>Since pestilence is a member of the <tt class="docutils literal"><span class="pre">horsemen</span></tt> list, the <tt class="docutils literal"><span class="pre">in</span></tt> operator
returns <tt class="docutils literal"><span class="pre">True</span></tt>. Since debauchery is not in the list, <tt class="docutils literal"><span class="pre">in</span></tt> returns
<tt class="docutils literal"><span class="pre">False</span></tt>.</p>
<p>We can use the <tt class="docutils literal"><span class="pre">not</span></tt> in combination with <tt class="docutils literal"><span class="pre">in</span></tt> to test whether an element is
not a member of a list:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="s">'debauchery'</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">horsemen</span>
<span class="go">True</span>
</pre></div>
</div>
</div>
<div class="section" id="list-operations">
<h2>9.5. List operations<a class="headerlink" href="#list-operations" title="Permalink to this headline">¶</a></h2>
<p>The <tt class="docutils literal"><span class="pre">+</span></tt> operator concatenates lists:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span> <span class="o">=</span> <span class="p">[</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">c</span> <span class="o">=</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">c</span>
<span class="go">[1, 2, 3, 4, 5, 6]</span>
</pre></div>
</div>
<p>Similarly, the <tt class="docutils literal"><span class="pre">*</span></tt> operator repeats a list a given number of times:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="mi">4</span>
<span class="go">[0, 0, 0, 0]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span> <span class="o">*</span> <span class="mi">3</span>
<span class="go">[1, 2, 3, 1, 2, 3, 1, 2, 3]</span>
</pre></div>
</div>
<p>The first example repeats <tt class="docutils literal"><span class="pre">[0]</span></tt> four times. The second example repeats the
list <tt class="docutils literal"><span class="pre">[1,</span> <span class="pre">2,</span> <span class="pre">3]</span></tt> three times.</p>
</div>
<div class="section" id="list-slices">
<h2>9.6. List slices<a class="headerlink" href="#list-slices" title="Permalink to this headline">¶</a></h2>
<p>The slice operations we saw with strings also work on lists:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">a_list</span> <span class="o">=</span> <span class="p">[</span><span class="s">'a'</span><span class="p">,</span> <span class="s">'b'</span><span class="p">,</span> <span class="s">'c'</span><span class="p">,</span> <span class="s">'d'</span><span class="p">,</span> <span class="s">'e'</span><span class="p">,</span> <span class="s">'f'</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a_list</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="mi">3</span><span class="p">]</span>
<span class="go">['b', 'c']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a_list</span><span class="p">[:</span><span class="mi">4</span><span class="p">]</span>
<span class="go">['a', 'b', 'c', 'd']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a_list</span><span class="p">[</span><span class="mi">3</span><span class="p">:]</span>
<span class="go">['d', 'e', 'f']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a_list</span><span class="p">[:]</span>
<span class="go">['a', 'b', 'c', 'd', 'e', 'f']</span>
</pre></div>
</div>
</div>
<div class="section" id="the-range-function">
<span id="index-0"></span><h2>9.7. The <tt class="docutils literal"><span class="pre">range</span></tt> function<a class="headerlink" href="#the-range-function" title="Permalink to this headline">¶</a></h2>
<p>Lists that contain consecutive integers are common, so Python provides a simple
way to create them:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>
<span class="go">[1, 2, 3, 4]</span>
</pre></div>
</div>
<p>The <tt class="docutils literal"><span class="pre">range</span></tt> function takes two arguments and returns a list that contains all
the integers from the first to the second, including the first but <em>not the
second</em>.</p>
<p>There are two other forms of <tt class="docutils literal"><span class="pre">range</span></tt>. With a single argument, it creates a
list that starts at 0:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
<span class="go">[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]</span>
</pre></div>
</div>
<p>If there is a third argument, it specifies the space between successive values,
which is called the <strong>step size</strong>. This example counts from 1 to 10 by steps of
2:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
<span class="go">[1, 3, 5, 7, 9]</span>
</pre></div>
</div>
<p>If the step size is negative, then <tt class="docutils literal"><span class="pre">start</span></tt> must be greater than <tt class="docutils literal"><span class="pre">stop</span></tt></p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="nb">range</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="o">-</span><span class="mi">5</span><span class="p">)</span>
<span class="go">[20, 15, 10, 5]</span>
</pre></div>
</div>
<p>or the result will be an empty list.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="o">-</span><span class="mi">5</span><span class="p">)</span>
<span class="go">[]</span>
</pre></div>
</div>
</div>
<div class="section" id="lists-are-mutable">
<span id="index-1"></span><h2>9.8. Lists are mutable<a class="headerlink" href="#lists-are-mutable" title="Permalink to this headline">¶</a></h2>
<p>Unlike strings, lists are <strong>mutable</strong>, which means we can change their
elements. Using the bracket operator on the left side of an assignment, we can
update one of the elements:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">fruit</span> <span class="o">=</span> <span class="p">[</span><span class="s">"banana"</span><span class="p">,</span> <span class="s">"apple"</span><span class="p">,</span> <span class="s">"quince"</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">fruit</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="s">"pear"</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">fruit</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="s">"orange"</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">fruit</span>
<span class="go">['pear', 'apple', 'orange']</span>
</pre></div>
</div>
<p>The bracket operator applied to a list can appear anywhere in an expression.
When it appears on the left side of an assignment, it changes one of the
elements in the list, so the first element of <tt class="docutils literal"><span class="pre">fruit</span></tt> has been changed from
<tt class="docutils literal"><span class="pre">'banana'</span></tt> to <tt class="docutils literal"><span class="pre">'pear'</span></tt>, and the last from <tt class="docutils literal"><span class="pre">'quince'</span></tt> to <tt class="docutils literal"><span class="pre">'orange'</span></tt>. An
assignment to an element of a list is called <strong>item assignment</strong>. Item
assignment does not work for strings:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">my_string</span> <span class="o">=</span> <span class="s">'TEST'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">my_string</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">=</span> <span class="s">'X'</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">"&lt;stdin&gt;"</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">TypeError</span>: <span class="n">'str' object does not support item assignment</span>
</pre></div>
</div>
<p>but it does for lists:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">my_list</span> <span class="o">=</span> <span class="p">[</span><span class="s">'T'</span><span class="p">,</span> <span class="s">'E'</span><span class="p">,</span> <span class="s">'S'</span><span class="p">,</span> <span class="s">'T'</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">my_list</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">=</span> <span class="s">'X'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">my_list</span>
<span class="go">['T', 'E', 'X', 'T']</span>
</pre></div>
</div>
<p>With the slice operator we can update several elements at once:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">a_list</span> <span class="o">=</span> <span class="p">[</span><span class="s">'a'</span><span class="p">,</span> <span class="s">'b'</span><span class="p">,</span> <span class="s">'c'</span><span class="p">,</span> <span class="s">'d'</span><span class="p">,</span> <span class="s">'e'</span><span class="p">,</span> <span class="s">'f'</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a_list</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="mi">3</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s">'x'</span><span class="p">,</span> <span class="s">'y'</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">a_list</span>
<span class="go">['a', 'x', 'y', 'd', 'e', 'f']</span>
</pre></div>
</div>
<p>We can also remove elements from a list by assigning the empty list to them:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">a_list</span> <span class="o">=</span> <span class="p">[</span><span class="s">'a'</span><span class="p">,</span> <span class="s">'b'</span><span class="p">,</span> <span class="s">'c'</span><span class="p">,</span> <span class="s">'d'</span><span class="p">,</span> <span class="s">'e'</span><span class="p">,</span> <span class="s">'f'</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a_list</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="mi">3</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">a_list</span>
<span class="go">['a', 'd', 'e', 'f']</span>
</pre></div>
</div>
<p>And we can add elements to a list by squeezing them into an empty slice at the
desired location:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">a_list</span> <span class="o">=</span> <span class="p">[</span><span class="s">'a'</span><span class="p">,</span> <span class="s">'d'</span><span class="p">,</span> <span class="s">'f'</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a_list</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s">'b'</span><span class="p">,</span> <span class="s">'c'</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">a_list</span>
<span class="go">['a', 'b', 'c', 'd', 'f']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a_list</span><span class="p">[</span><span class="mi">4</span><span class="p">:</span><span class="mi">4</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s">'e'</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">a_list</span>
<span class="go">['a', 'b', 'c', 'd', 'e', 'f']</span>
</pre></div>
</div>
</div>
<div class="section" id="list-deletion">
<h2>9.9. List deletion<a class="headerlink" href="#list-deletion" title="Permalink to this headline">¶</a></h2>
<p>Using slices to delete list elements can be awkward, and therefore error-prone.
Python provides an alternative that is more readable.</p>
<p><tt class="docutils literal"><span class="pre">del</span></tt> removes an element from a list:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="s">'one'</span><span class="p">,</span> <span class="s">'two'</span><span class="p">,</span> <span class="s">'three'</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">del</span> <span class="n">a</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span>
<span class="go">['one', 'three']</span>
</pre></div>
</div>
<p>As you might expect, <tt class="docutils literal"><span class="pre">del</span></tt> handles negative indices and causes a runtime
error if the index is out of range.</p>
<p>You can use a slice as an index for <tt class="docutils literal"><span class="pre">del</span></tt>:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">a_list</span> <span class="o">=</span> <span class="p">[</span><span class="s">'a'</span><span class="p">,</span> <span class="s">'b'</span><span class="p">,</span> <span class="s">'c'</span><span class="p">,</span> <span class="s">'d'</span><span class="p">,</span> <span class="s">'e'</span><span class="p">,</span> <span class="s">'f'</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">del</span> <span class="n">a_list</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="mi">5</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">a_list</span>
<span class="go">['a', 'f']</span>
</pre></div>
</div>
<p>As usual, slices select all the elements up to, but not including, the second
index.</p>
</div>
<div class="section" id="objects-and-values">
<span id="index-2"></span><h2>9.10. Objects and values<a class="headerlink" href="#objects-and-values" title="Permalink to this headline">¶</a></h2>
<p>If we execute these assignment statements,</p>
<div class="highlight-python"><div class="highlight"><pre><span class="n">a</span> <span class="o">=</span> <span class="s">"banana"</span>
<span class="n">b</span> <span class="o">=</span> <span class="s">"banana"</span>
</pre></div>
</div>
<p>we know that <tt class="docutils literal"><span class="pre">a</span></tt> and <tt class="docutils literal"><span class="pre">b</span></tt> will refer to a string with the letters
<tt class="docutils literal"><span class="pre">"banana"</span></tt>. But we don’t know yet whether they point to the <em>same</em> string.</p>
<p>There are two possible states:</p>
<img alt="Two state diagrams for multiple references with strings" src="_images/mult_references1.png">
<p>In one case, <tt class="docutils literal"><span class="pre">a</span></tt> and <tt class="docutils literal"><span class="pre">b</span></tt> refer to two different things that have the same
value. In the second case, they refer to the same thing. These things have
names — they are called <strong>objects</strong>. An object is something a variable can
refer to.</p>
<p>We can test whether two names have the same value using <tt class="docutils literal"><span class="pre">==</span></tt>:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">==</span> <span class="n">b</span>
<span class="go">True</span>
</pre></div>
</div>
<p>We can test whether two names refer to the same object using the <em>is</em>
operator:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="ow">is</span> <span class="n">b</span>
<span class="go">True</span>
</pre></div>
</div>
<p>This tells us that both <tt class="docutils literal"><span class="pre">a</span></tt> and <tt class="docutils literal"><span class="pre">b</span></tt> refer to the same object, and that it
is the second of the two state diagrams that describes the relationship.</p>
<p>Since strings are <em>immutable</em>, Python optimizes resources by making two names
that refer to the same string value refer to the same object.</p>
<p>This is not the case with lists:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">==</span> <span class="n">b</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="ow">is</span> <span class="n">b</span>
<span class="go">False</span>
</pre></div>
</div>
<p>The state diagram here looks like this:</p>
<img alt="State diagram for equal different lists" src="_images/mult_references2.png">
<p><tt class="docutils literal"><span class="pre">a</span></tt> and <tt class="docutils literal"><span class="pre">b</span></tt> have the same value but do not refer to the same object.</p>
</div>
<div class="section" id="aliasing">
<h2>9.11. Aliasing<a class="headerlink" href="#aliasing" title="Permalink to this headline">¶</a></h2>
<p>Since variables refer to objects, if we assign one variable to another, both
variables refer to the same object:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span> <span class="o">=</span> <span class="n">a</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="ow">is</span> <span class="n">b</span>
<span class="go">True</span>
</pre></div>
</div>
<p>In this case, the state diagram looks like this:</p>
<img alt="State diagram for multiple references (aliases) to a list" src="_images/mult_references3.png">
<p>Because the same list has two different names, <tt class="docutils literal"><span class="pre">a</span></tt> and <tt class="docutils literal"><span class="pre">b</span></tt>, we say that it
is <strong>aliased</strong>. Changes made with one alias affect the other:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="mi">5</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">a</span>
<span class="go">[5, 2, 3]</span>
</pre></div>
</div>
<p>Although this behavior can be useful, it is sometimes unexpected or
undesirable. In general, it is safer to avoid aliasing when you are working
with mutable objects. Of course, for immutable objects, there’s no problem.
That’s why Python is free to alias strings when it sees an opportunity to
economize.</p>
</div>
<div class="section" id="cloning-lists">
<h2>9.12. Cloning lists<a class="headerlink" href="#cloning-lists" title="Permalink to this headline">¶</a></h2>
<p>If we want to modify a list and also keep a copy of the original, we need to be
able to make a copy of the list itself, not just the reference. This process is
sometimes called <strong>cloning</strong>, to avoid the ambiguity of the word copy.</p>
<p>The easiest way to clone a list is to use the slice operator:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">b</span> <span class="o">=</span> <span class="n">a</span><span class="p">[:]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">b</span>
<span class="go">[1, 2, 3]</span>
</pre></div>
</div>
<p>Taking any slice of <tt class="docutils literal"><span class="pre">a</span></tt> creates a new list. In this case the slice happens to
consist of the whole list.</p>
<p>Now we are free to make changes to <tt class="docutils literal"><span class="pre">b</span></tt> without worrying about <tt class="docutils literal"><span class="pre">a</span></tt>:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">b</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="mi">5</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">a</span>
<span class="go">[1, 2, 3]</span>
</pre></div>
</div>
</div>
<div class="section" id="lists-and-for-loops">
<span id="index-3"></span><h2>9.13. Lists and <tt class="docutils literal"><span class="pre">for</span></tt> loops<a class="headerlink" href="#lists-and-for-loops" title="Permalink to this headline">¶</a></h2>
<p>The <tt class="docutils literal"><span class="pre">for</span></tt> loop also works with lists. The generalized syntax of a <tt class="docutils literal"><span class="pre">for</span></tt>
loop is:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">for</span> <span class="n">VARIABLE</span> <span class="ow">in</span> <span class="n">LIST</span><span class="p">:</span>
    <span class="n">BODY</span>
</pre></div>
</div>
<p>This statement is equivalent to:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">LIST</span><span class="p">):</span>
    <span class="n">VARIABLE</span> <span class="o">=</span> <span class="n">LIST</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="n">BODY</span>
    <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
</pre></div>
</div>
<p>The <tt class="docutils literal"><span class="pre">for</span></tt> loop is more concise because we can eliminate the loop variable,
<tt class="docutils literal"><span class="pre">i</span></tt>. Here is an equivalent to the <tt class="docutils literal"><span class="pre">while</span></tt> loop from the
<a class="reference internal" href="#accessing-elements"><em>Accessing elements</em></a> section written with a <tt class="docutils literal"><span class="pre">for</span></tt> loop.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">for</span> <span class="n">horseman</span> <span class="ow">in</span> <span class="n">horsemen</span><span class="p">:</span>
    <span class="k">print</span> <span class="n">horseman</span>
</pre></div>
</div>
<p>It almost reads like English: For (every) horseman in (the list of) horsemen,
print (the name of the) horseman.</p>
<p>Any list expression can be used in a <tt class="docutils literal"><span class="pre">for</span></tt> loop:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">for</span> <span class="n">number</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">20</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">number</span> <span class="o">%</span> <span class="mi">3</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">print</span>  <span class="n">number</span>

<span class="k">for</span> <span class="n">fruit</span> <span class="ow">in</span> <span class="p">[</span><span class="s">"banana"</span><span class="p">,</span> <span class="s">"apple"</span><span class="p">,</span> <span class="s">"quince"</span><span class="p">]:</span>
    <span class="k">print</span> <span class="s">"I like to eat "</span> <span class="o">+</span> <span class="n">fruit</span> <span class="o">+</span> <span class="s">"s!"</span>
</pre></div>
</div>
<p>The first example prints all the multiples of 3 between 0 and 19. The second
example expresses enthusiasm for various fruits.</p>
<p>Since lists are mutable, it is often desirable to traverse a list, modifying
each of its elements. The following squares all the numbers from <tt class="docutils literal"><span class="pre">1</span></tt> to
<tt class="docutils literal"><span class="pre">5</span></tt>:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="n">numbers</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>

<span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">numbers</span><span class="p">)):</span>
    <span class="n">numbers</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">numbers</span><span class="p">[</span><span class="n">index</span><span class="p">]</span><span class="o">**</span><span class="mi">2</span>
</pre></div>
</div>
<p>Take a moment to think about <tt class="docutils literal"><span class="pre">range(len(numbers))</span></tt> until you understand how
it works. We are interested here in both the <em>value</em> and its <em>index</em> within the
list, so that we can assign a new value to it.</p>
<p>This pattern is common enough that Python provides a nicer way to implement it:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="n">numbers</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>

<span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">numbers</span><span class="p">):</span>
    <span class="n">numbers</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span><span class="o">**</span><span class="mi">2</span>
</pre></div>
</div>
<p><tt class="docutils literal"><span class="pre">enumerate</span></tt> generates both the index and the value associated with it during
the list traversal. Try this next example to see more clearly how <tt class="docutils literal"><span class="pre">enumerate</span></tt>
works:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">([</span><span class="s">'banana'</span><span class="p">,</span> <span class="s">'apple'</span><span class="p">,</span> <span class="s">'pear'</span><span class="p">,</span> <span class="s">'quince'</span><span class="p">]):</span>
<span class="gp">... </span>   <span class="k">print</span> <span class="n">index</span><span class="p">,</span> <span class="n">value</span>
<span class="gp">...</span>
<span class="go">0 banana</span>
<span class="go">1 apple</span>
<span class="go">2 pear</span>
<span class="go">3 quince</span>
<span class="go">&gt;&gt;&gt;</span>
</pre></div>
</div>
</div>
<div class="section" id="list-parameters">
<h2>9.14. List parameters<a class="headerlink" href="#list-parameters" title="Permalink to this headline">¶</a></h2>
<p>Passing a list as an argument actually passes a reference to the list, not a
copy of the list. Since lists are mutable changes made to the parameter change
the argument as well. For example, the function below takes a list as an
argument and multiplies each element in the list by 2:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">double_stuff</span><span class="p">(</span><span class="n">a_list</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">a_list</span><span class="p">):</span>
        <span class="n">a_list</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">value</span>
</pre></div>
</div>
<p>If we put <tt class="docutils literal"><span class="pre">double_stuff</span></tt> in a file named <tt class="docutils literal"><span class="pre">ch09.py</span></tt>, we can test it out like
this:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">ch09</span> <span class="kn">import</span> <span class="n">double_stuff</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">things</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="s">'Spam'</span><span class="p">,</span> <span class="mf">9.5</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">double_stuff</span><span class="p">(</span><span class="n">things</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">things</span>
<span class="go">[4, 10, 'SpamSpam', 19.0]</span>
<span class="go">&gt;&gt;&gt;</span>
</pre></div>
</div>
<p>The parameter <tt class="docutils literal"><span class="pre">a_list</span></tt> and the variable <tt class="docutils literal"><span class="pre">things</span></tt> are aliases for the
same object. The state diagram looks like this:</p>
<img alt="State diagram for multiple references to a list as a parameter" src="_images/mult_references4.png">
<p>Since the list object is shared by two frames, we drew it between them.</p>
<p>If a function modifies a list parameter, the caller sees the change.</p>
</div>
<div class="section" id="pure-functions-and-modifiers">
<span id="pure-func-mod"></span><h2>9.15. Pure functions and modifiers<a class="headerlink" href="#pure-functions-and-modifiers" title="Permalink to this headline">¶</a></h2>
<p>Functions which take lists as arguments and change them during execution are
called <strong>modifiers</strong> and the changes they make are called <strong>side effects</strong>.</p>
<p>A <strong>pure function</strong> does not produce side effects. It communicates with the
calling program only through parameters, which it does not modify, and a return
value. Here is <tt class="docutils literal"><span class="pre">double_stuff</span></tt> written as a pure function:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">double_stuff</span><span class="p">(</span><span class="n">a_list</span><span class="p">):</span>
    <span class="n">new_list</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">a_list</span><span class="p">:</span>
        <span class="n">new_list</span> <span class="o">+=</span> <span class="p">[</span><span class="mi">2</span> <span class="o">*</span> <span class="n">value</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">new_list</span>
</pre></div>
</div>
<p>This version of <tt class="docutils literal"><span class="pre">double_stuff</span></tt> does not change its arguments:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">ch09</span> <span class="kn">import</span> <span class="n">double_stuff</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">things</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="s">'Spam'</span><span class="p">,</span> <span class="mf">9.5</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">double_stuff</span><span class="p">(</span><span class="n">things</span><span class="p">)</span>
<span class="go">[4, 10, 'SpamSpam', 19.0]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">things</span>
<span class="go">[2, 5, 'Spam', 9.5]</span>
<span class="go">&gt;&gt;&gt;</span>
</pre></div>
</div>
<p>To use the pure function version of <tt class="docutils literal"><span class="pre">double_stuff</span></tt> to modify <tt class="docutils literal"><span class="pre">things</span></tt>,
you would assign the return value back to <tt class="docutils literal"><span class="pre">things</span></tt>:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">things</span> <span class="o">=</span> <span class="n">double_stuff</span><span class="p">(</span><span class="n">things</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">things</span>
<span class="go">[4, 10, 'SpamSpam', 19.0]</span>
<span class="go">&gt;&gt;&gt;</span>
</pre></div>
</div>
</div>
<div class="section" id="which-is-better">
<h2>9.16. Which is better?<a class="headerlink" href="#which-is-better" title="Permalink to this headline">¶</a></h2>
<p>Anything that can be done with modifiers can also be done with pure functions.
In fact, some programming languages only allow pure functions. There is some
evidence that programs that use pure functions are faster to develop and less
error-prone than programs that use modifiers. Nevertheless, modifiers are
convenient at times, and in some cases, functional programs are less efficient.</p>
<p>In general, we recommend that you write pure functions whenever it is
reasonable to do so and resort to modifiers only if there is a compelling
advantage. This approach might be called a <em>functional programming style</em>.</p>
</div>
<div class="section" id="nested-lists">
<h2>9.17. Nested lists<a class="headerlink" href="#nested-lists" title="Permalink to this headline">¶</a></h2>
<p>A nested list is a list that appears as an element in another list. In this
list, the element with index 3 is a nested list:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">nested</span> <span class="o">=</span> <span class="p">[</span><span class="s">"hello"</span><span class="p">,</span> <span class="mf">2.0</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">]]</span>
</pre></div>
</div>
<p>If we print <tt class="docutils literal"><span class="pre">nested[3]</span></tt>, we get <tt class="docutils literal"><span class="pre">[10,</span> <span class="pre">20]</span></tt>. To extract an element from the
nested list, we can proceed in two steps:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">elem</span> <span class="o">=</span> <span class="n">nested</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">elem</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="go">10</span>
</pre></div>
</div>
<p>Or we can combine them:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">nested</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
<span class="go">20</span>
</pre></div>
</div>
<p>Bracket operators evaluate from left to right, so this expression gets the
three-eth element of <tt class="docutils literal"><span class="pre">nested</span></tt> and extracts the one-eth element from it.</p>
</div>
<div class="section" id="matrices">
<h2>9.18. Matrices<a class="headerlink" href="#matrices" title="Permalink to this headline">¶</a></h2>
<p>Nested lists are often used to represent matrices. For example, the matrix:</p>
<img alt="Matrix illustration" src="_images/matrix.png">
<p>might be represented as:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">matrix</span> <span class="o">=</span> <span class="p">[[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">],</span> <span class="p">[</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">],</span> <span class="p">[</span><span class="mi">7</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">9</span><span class="p">]]</span>
</pre></div>
</div>
<p><tt class="docutils literal"><span class="pre">matrix</span></tt> is a list with three elements, where each element is a row of the
matrix. We can select an entire row from the matrix in the usual way:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">matrix</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
<span class="go">[4, 5, 6]</span>
</pre></div>
</div>
<p>Or we can extract a single element from the matrix using the double-index form:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">matrix</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
<span class="go">5</span>
</pre></div>
</div>
<p>The first index selects the row, and the second index selects the column.
Although this way of representing matrices is common, it is not the only
possibility. A small variation is to use a list of columns instead of a list of
rows. Later we will see a more radical alternative using a dictionary.</p>
</div>
<div class="section" id="test-driven-development-tdd">
<span id="index-4"></span><h2>9.19. Test-driven development (TDD)<a class="headerlink" href="#test-driven-development-tdd" title="Permalink to this headline">¶</a></h2>
<p><strong>Test-driven development (TDD)</strong> is a software development practice which
arrives at a desired feature through a series of small, iterative steps
motivated by automated tests which are <em>written first</em> that express increasing
refinements of the desired feature.</p>
<p>Doctest enables us to easily demonstrate TDD. Let’s say we want a function
which creates a <tt class="docutils literal"><span class="pre">rows</span></tt> by <tt class="docutils literal"><span class="pre">columns</span></tt> matrix given arguments for <tt class="docutils literal"><span class="pre">rows</span></tt> and
<tt class="docutils literal"><span class="pre">columns</span></tt>.</p>
<p>We first setup a test for this function in a file named <tt class="docutils literal"><span class="pre">matrices.py</span></tt>:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">make_matrix</span><span class="p">(</span><span class="n">rows</span><span class="p">,</span> <span class="n">columns</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; make_matrix(3, 5)</span>
<span class="sd">      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]</span>
<span class="sd">    """</span>


<span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">'__main__'</span><span class="p">:</span>
    <span class="kn">import</span> <span class="nn">doctest</span>
    <span class="n">doctest</span><span class="o">.</span><span class="n">testmod</span><span class="p">()</span>
</pre></div>
</div>
<p>Running this returns in a failing test:</p>
<div class="highlight-python"><div class="highlight"><pre>**********************************************************************
File "matrices.py", line 3, in __main__.make_matrix
Failed example:
    make_matrix(3, 5)
Expected:
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
Got nothing
**********************************************************************
1 items had failures:
   1 of   1 in __main__.make_matrix
***Test Failed*** 1 failures.
</pre></div>
</div>
<p>The test fails because the body of the function contains only a single triple
quoted string and no return statement, so it returns <tt class="docutils literal"><span class="pre">None</span></tt>.  Our test
indicates that we wanted it to return a matrix with 3 rows of 5 columns of
zeros.</p>
<p>The rule in using TDD is to use the <em>simplest thing that works</em> in writing a
solution to pass the test, so in this case we can simply return the desired
result:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">make_matrix</span><span class="p">(</span><span class="n">rows</span><span class="p">,</span> <span class="n">columns</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; make_matrix(3, 5)</span>
<span class="sd">      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">[[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">]]</span>
</pre></div>
</div>
<p>Running this now the test passes, but our current implementation of
<tt class="docutils literal"><span class="pre">make_matrix</span></tt> always returns the same result, which is clearly not what we
intended. To fix this, we first motivate our improvement by adding a test:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">make_matrix</span><span class="p">(</span><span class="n">rows</span><span class="p">,</span> <span class="n">columns</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; make_matrix(3, 5)</span>
<span class="sd">      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]</span>
<span class="sd">      &gt;&gt;&gt; make_matrix(4, 2)</span>
<span class="sd">      [[0, 0], [0, 0], [0, 0], [0, 0]]</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">[[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">]]</span>
</pre></div>
</div>
<p>which as we expect fails:</p>
<div class="highlight-python"><div class="highlight"><pre>**********************************************************************
File "matrices.py", line 5, in __main__.make_matrix
Failed example:
    make_matrix(4, 2)
Expected:
    [[0, 0], [0, 0], [0, 0], [0, 0]]
Got:
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
**********************************************************************
1 items had failures:
   1 of   2 in __main__.make_matrix
***Test Failed*** 1 failures.
</pre></div>
</div>
<p>This technique is called <em>test-driven</em> because code should only be written when
there is a failing test to make pass. Motivated by the failing test, we can now
produce a more general solution:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">make_matrix</span><span class="p">(</span><span class="n">rows</span><span class="p">,</span> <span class="n">columns</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; make_matrix(3, 5)</span>
<span class="sd">      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]</span>
<span class="sd">      &gt;&gt;&gt; make_matrix(4, 2)</span>
<span class="sd">      [[0, 0], [0, 0], [0, 0], [0, 0]]</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">[[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="n">columns</span><span class="p">]</span> <span class="o">*</span> <span class="n">rows</span>
</pre></div>
</div>
<p>This solution appears to work, and we may think we are finished, but
when we use the new function later we discover a bug:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">matrices</span> <span class="kn">import</span> <span class="o">*</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span> <span class="o">=</span> <span class="n">make_matrix</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span>
<span class="go">[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="mi">2</span><span class="p">]</span> <span class="o">=</span> <span class="mi">7</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">m</span>
<span class="go">[[0, 0, 7], [0, 0, 7], [0, 0, 7], [0, 0, 7]]</span>
<span class="go">&gt;&gt;&gt;</span>
</pre></div>
</div>
<p>We wanted to assign the element in the second row and the third column the
value 7, instead, <em>all</em> elements in the third column are 7!</p>
<p>Upon reflection, we realize that in our current solution, each row is an
<em>alias</em> of the other rows. This is definitely not what we intended, so we set
about fixing the problem, <em>first by writing a failing test</em>:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">make_matrix</span><span class="p">(</span><span class="n">rows</span><span class="p">,</span> <span class="n">columns</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; make_matrix(3, 5)</span>
<span class="sd">      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]</span>
<span class="sd">      &gt;&gt;&gt; make_matrix(4, 2)</span>
<span class="sd">      [[0, 0], [0, 0], [0, 0], [0, 0]]</span>
<span class="sd">      &gt;&gt;&gt; m = make_matrix(4, 2)</span>
<span class="sd">      &gt;&gt;&gt; m[1][1] = 7</span>
<span class="sd">      &gt;&gt;&gt; m</span>
<span class="sd">      [[0, 0], [0, 7], [0, 0], [0, 0]]</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="p">[[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="n">columns</span><span class="p">]</span> <span class="o">*</span> <span class="n">rows</span>
</pre></div>
</div>
<p>With a failing test to fix, we are now driven to a better solution:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">make_matrix</span><span class="p">(</span><span class="n">rows</span><span class="p">,</span> <span class="n">columns</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; make_matrix(3, 5)</span>
<span class="sd">      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]</span>
<span class="sd">      &gt;&gt;&gt; make_matrix(4, 2)</span>
<span class="sd">      [[0, 0], [0, 0], [0, 0], [0, 0]]</span>
<span class="sd">      &gt;&gt;&gt; m = make_matrix(4, 2)</span>
<span class="sd">      &gt;&gt;&gt; m[1][1] = 7</span>
<span class="sd">      &gt;&gt;&gt; m</span>
<span class="sd">      [[0, 0], [0, 7], [0, 0], [0, 0]]</span>
<span class="sd">    """</span>
    <span class="n">matrix</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">rows</span><span class="p">):</span>
        <span class="n">matrix</span> <span class="o">+=</span> <span class="p">[[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="n">columns</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">matrix</span>
</pre></div>
</div>
<p>Using TDD has several benefits to our software development process.  It:</p>
<ul class="simple">
<li>helps us think concretely about the problem we are trying to solve <em>before</em>
we attempt to solve it.</li>
<li>encourages breaking down complex problems into smaller, simpler problems and
working our way toward a solution of the larger problem step-by-step.</li>
<li>assures that we have a well developed automated test suite for our software,
facilitating later additions and improvements.</li>
</ul>
</div>
<div class="section" id="strings-and-lists">
<span id="index-5"></span><h2>9.20. Strings and lists<a class="headerlink" href="#strings-and-lists" title="Permalink to this headline">¶</a></h2>
<p>Python has a command called <tt class="docutils literal"><span class="pre">list</span></tt> that takes a sequence type as an argument
and creates a list out of its elements.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="s">"Crunchy Frog"</span><span class="p">)</span>
<span class="go">['C', 'r', 'u', 'n', 'c', 'h', 'y', ' ', 'F', 'r', 'o', 'g']</span>
</pre></div>
</div>
<p>There is also a <tt class="docutils literal"><span class="pre">str</span></tt> command that takes any Python value as an argument and
returns a string representation of it.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="nb">str</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<span class="go">'5'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">str</span><span class="p">(</span><span class="bp">None</span><span class="p">)</span>
<span class="go">'None'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">str</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="s">"nope"</span><span class="p">))</span>
<span class="go">"['n', 'o', 'p', 'e']"</span>
</pre></div>
</div>
<p>As we can see from the last example, <tt class="docutils literal"><span class="pre">str</span></tt> can’t be used to join a list of
characters together. To do this we could use the <tt class="docutils literal"><span class="pre">join</span></tt> function in the
<tt class="docutils literal"><span class="pre">string</span></tt> module:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">string</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">char_list</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="s">"Frog"</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">char_list</span>
<span class="go">['F', 'r', 'o', 'g']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">string</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">char_list</span><span class="p">,</span> <span class="s">''</span><span class="p">)</span>
<span class="go">'Frog'</span>
</pre></div>
</div>
<p>Two of the most useful functions in the <tt class="docutils literal"><span class="pre">string</span></tt> module involve lists of
strings. The <tt class="docutils literal"><span class="pre">split</span></tt> function breaks a string into a list of words.  By
default, any number of whitespace characters is considered a word boundary:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">string</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">song</span> <span class="o">=</span> <span class="s">"The rain in Spain..."</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">string</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">song</span><span class="p">)</span>
<span class="go">['The', 'rain', 'in', 'Spain...']</span>
</pre></div>
</div>
<p>An optional argument called a <strong>delimiter</strong> can be used to specify which
characters to use as word boundaries. The following example uses the string
<tt class="docutils literal"><span class="pre">ai</span></tt> as the delimiter:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">string</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">song</span><span class="p">,</span> <span class="s">'ai'</span><span class="p">)</span>
<span class="go">['The r', 'n in Sp', 'n...']</span>
</pre></div>
</div>
<p>Notice that the delimiter doesn’t appear in the list.</p>
<p><tt class="docutils literal"><span class="pre">string.join</span></tt> is the inverse of <tt class="docutils literal"><span class="pre">string.split</span></tt>. It takes two arguments: a
list of strings and a <em>separator</em> which will be placed between each element in
the list in the resultant string.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">string</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">words</span> <span class="o">=</span> <span class="p">[</span><span class="s">'crunchy'</span><span class="p">,</span> <span class="s">'raw'</span><span class="p">,</span> <span class="s">'unboned'</span><span class="p">,</span> <span class="s">'real'</span><span class="p">,</span> <span class="s">'dead'</span><span class="p">,</span> <span class="s">'frog'</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">string</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">words</span><span class="p">,</span> <span class="s">' '</span><span class="p">)</span>
<span class="go">'crunchy raw unboned real dead frog'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">string</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">words</span><span class="p">,</span> <span class="s">'**'</span><span class="p">)</span>
<span class="go">'crunchy**raw**unboned**real**dead**frog'</span>
</pre></div>
</div>
</div>
<div class="section" id="glossary">
<h2>9.21. Glossary<a class="headerlink" href="#glossary" title="Permalink to this headline">¶</a></h2>
<dl class="glossary docutils">
<dt id="term-aliases">aliases</dt>
<dd>Multiple variables that contain references to the same object.</dd>
<dt id="term-clone">clone</dt>
<dd>To create a new object that has the same value as an existing object.
Copying a reference to an object creates an alias but doesn’t clone the
object.</dd>
<dt id="term-delimiter">delimiter</dt>
<dd>A character or string used to indicate where a string should be split.</dd>
<dt id="term-element">element</dt>
<dd>One of the values in a list (or other sequence). The bracket operator
selects elements of a list.</dd>
<dt id="term-index">index</dt>
<dd>An integer variable or value that indicates an element of a list.</dd>
<dt id="term-list">list</dt>
<dd>A named collection of objects, where each object is identified by an
index.</dd>
<dt id="term-list-traversal">list traversal</dt>
<dd>The sequential accessing of each element in a list.</dd>
<dt id="term-modifier">modifier</dt>
<dd>A function which changes its arguments inside the function body. Only
mutable types can be changed by modifiers.</dd>
<dt id="term-mutable-type">mutable type</dt>
<dd>A data type in which the elements can be modified. All mutable types
are compound types. Lists are mutable data types; strings are not.</dd>
<dt id="term-nested-list">nested list</dt>
<dd>A list that is an element of another list.</dd>
<dt id="term-object">object</dt>
<dd>A thing to which a variable can refer.</dd>
<dt id="term-pure-function">pure function</dt>
<dd>A function which has no side effects. Pure functions only make changes
to the calling program through their return values.</dd>
<dt id="term-sequence">sequence</dt>
<dd>Any of the data types that consist of an ordered set of elements, with
each element identified by an index.</dd>
<dt id="term-side-effect">side effect</dt>
<dd>A change in the state of a program made by calling a function that is
not a result of reading the return value from the function. Side
effects can only be produced by modifiers.</dd>
<dt id="term-step-size">step size</dt>
<dd>The interval between successive elements of a linear sequence. The
third (and optional argument) to the <tt class="docutils literal"><span class="pre">range</span></tt> function is called the
step size.  If not specified, it defaults to 1.</dd>
<dt id="term-test-driven-development-tdd">test-driven development (TDD)</dt>
<dd>A software development practice which arrives at a desired feature
through a series of small, iterative steps motivated by automated tests
which are <em>written first</em> that express increasing refinements of the
desired feature.  (see the Wikipedia article on <a class="reference external" href="http://en.wikipedia.org/wiki/Test_driven_development">Test-driven
development</a>
for more information.)</dd>
</dl>
</div>
<div class="section" id="exercises">
<h2>9.22. Exercises<a class="headerlink" href="#exercises" title="Permalink to this headline">¶</a></h2>
<ol class="arabic">
<li><p class="first">Write a loop that traverses:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="p">[</span><span class="s">'spam!'</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="p">[</span><span class="s">'Brie'</span><span class="p">,</span> <span class="s">'Roquefort'</span><span class="p">,</span> <span class="s">'Pol le Veq'</span><span class="p">],</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]]</span>
</pre></div>
</div>
<p>and prints the length of each element. What happens if you send an integer
to <tt class="docutils literal"><span class="pre">len</span></tt>? Change <tt class="docutils literal"><span class="pre">1</span></tt> to <tt class="docutils literal"><span class="pre">'one'</span></tt> and run your solution again.</p>
</li>
<li><p class="first">Open a file named <tt class="docutils literal"><span class="pre">ch09e02.py</span></tt> and with the following content:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="c">#  Add your doctests here:</span>
<span class="sd">"""</span>
<span class="sd">"""</span>

<span class="c"># Write your Python code here:</span>


<span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">'__main__'</span><span class="p">:</span>
    <span class="kn">import</span> <span class="nn">doctest</span>
    <span class="n">doctest</span><span class="o">.</span><span class="n">testmod</span><span class="p">()</span>
</pre></div>
</div>
<p>Add each of the following sets of doctests to the docstring at the top of
the file and write Python code to make the doctests pass.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="sd">"""</span>
<span class="sd">  &gt;&gt;&gt; a_list[3]</span>
<span class="sd">  42</span>
<span class="sd">  &gt;&gt;&gt; a_list[6]</span>
<span class="sd">  'Ni!'</span>
<span class="sd">  &gt;&gt;&gt; len(a_list)</span>
<span class="sd">  8</span>
<span class="sd">"""</span>
</pre></div>
</div>
<div class="highlight-python"><div class="highlight"><pre><span class="sd">"""</span>
<span class="sd">  &gt;&gt;&gt; b_list[1:]</span>
<span class="sd">  ['Stills', 'Nash']</span>
<span class="sd">  &gt;&gt;&gt; group = b_list + c_list</span>
<span class="sd">  &gt;&gt;&gt; group[-1]</span>
<span class="sd">  'Young'</span>
<span class="sd">"""</span>
</pre></div>
</div>
<div class="highlight-python"><div class="highlight"><pre><span class="sd">"""</span>
<span class="sd">  &gt;&gt;&gt; 'war' in mystery_list</span>
<span class="sd">  False</span>
<span class="sd">  &gt;&gt;&gt; 'peace' in mystery_list</span>
<span class="sd">  True</span>
<span class="sd">  &gt;&gt;&gt; 'justice' in mystery_list</span>
<span class="sd">  True</span>
<span class="sd">  &gt;&gt;&gt; 'oppression' in mystery_list</span>
<span class="sd">  False</span>
<span class="sd">  &gt;&gt;&gt; 'equality' in mystery_list</span>
<span class="sd">  True</span>
<span class="sd">"""</span>
</pre></div>
</div>
<div class="highlight-python"><div class="highlight"><pre><span class="sd">"""</span>
<span class="sd">  &gt;&gt;&gt; range(a, b, c)</span>
<span class="sd">  [5, 9, 13, 17]</span>
<span class="sd">"""</span>
</pre></div>
</div>
<p>Only add one set of doctests at a time. The next set of doctests should not
be added until the previous set pass.</p>
</li>
<li><p class="first">What is the Python interpreter’s response to the following?</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">2</span><span class="p">)</span>
</pre></div>
</div>
<p>The three arguments to the <em>range</em> function are <em>start</em>, <em>stop</em>, and <em>step</em>,
respectively. In this example, <tt class="docutils literal"><span class="pre">start</span></tt> is greater than <tt class="docutils literal"><span class="pre">stop</span></tt>.  What
happens if <tt class="docutils literal"><span class="pre">start</span> <span class="pre">&lt;</span> <span class="pre">stop</span></tt> and <tt class="docutils literal"><span class="pre">step</span> <span class="pre">&lt;</span> <span class="pre">0</span></tt>? Write a rule for the
relationships among <tt class="docutils literal"><span class="pre">start</span></tt>, <tt class="docutils literal"><span class="pre">stop</span></tt>, and <tt class="docutils literal"><span class="pre">step</span></tt>.</p>
</li>
<li><p class="first">Draw a state diagram for <tt class="docutils literal"><span class="pre">a</span></tt> and <tt class="docutils literal"><span class="pre">b</span></tt> before and after the third line of
the following python code is executed:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="n">b</span> <span class="o">=</span> <span class="n">a</span><span class="p">[:]</span>
<span class="n">b</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="mi">5</span>
</pre></div>
</div>
</li>
<li><p class="first">What will be the output of the following program?</p>
<div class="highlight-python"><div class="highlight"><pre><span class="n">this</span> <span class="o">=</span> <span class="p">[</span><span class="s">'I'</span><span class="p">,</span> <span class="s">'am'</span><span class="p">,</span> <span class="s">'not'</span><span class="p">,</span> <span class="s">'a'</span><span class="p">,</span> <span class="s">'crook'</span><span class="p">]</span>
<span class="n">that</span> <span class="o">=</span> <span class="p">[</span><span class="s">'I'</span><span class="p">,</span> <span class="s">'am'</span><span class="p">,</span> <span class="s">'not'</span><span class="p">,</span> <span class="s">'a'</span><span class="p">,</span> <span class="s">'crook'</span><span class="p">]</span>
<span class="k">print</span> <span class="s">"Test 1: </span><span class="si">%s</span><span class="s">"</span> <span class="o">%</span> <span class="p">(</span><span class="n">this</span> <span class="ow">is</span> <span class="n">that</span><span class="p">)</span>
<span class="n">that</span> <span class="o">=</span> <span class="n">this</span>
<span class="k">print</span> <span class="s">"Test 2: </span><span class="si">%s</span><span class="s">"</span> <span class="o">%</span> <span class="p">(</span><span class="n">this</span> <span class="ow">is</span> <span class="n">that</span><span class="p">)</span>
</pre></div>
</div>
<p>Provide a <em>detailed</em> explaination of the results.</p>
</li>
<li><p class="first">Open a file named <tt class="docutils literal"><span class="pre">ch09e06.py</span></tt> and use the same procedure as in exercise 2
to make the following doctests pass:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="sd">"""</span>
<span class="sd">  &gt;&gt;&gt; 13 in junk</span>
<span class="sd">  True</span>
<span class="sd">  &gt;&gt;&gt; del junk[4]</span>
<span class="sd">  &gt;&gt;&gt; junk</span>
<span class="sd">  [3, 7, 9, 10, 17, 21, 24, 27]</span>
<span class="sd">  &gt;&gt;&gt; del junk[a:b]</span>
<span class="sd">  &gt;&gt;&gt; junk</span>
<span class="sd">  [3, 7, 27]</span>
<span class="sd">"""</span>
</pre></div>
</div>
<div class="highlight-python"><div class="highlight"><pre><span class="sd">"""</span>
<span class="sd">  &gt;&gt;&gt; nlist[2][1]</span>
<span class="sd">  0</span>
<span class="sd">  &gt;&gt;&gt; nlist[0][2]</span>
<span class="sd">  17</span>
<span class="sd">  &gt;&gt;&gt; nlist[1][1]</span>
<span class="sd">  5</span>
<span class="sd">"""</span>
</pre></div>
</div>
<div class="highlight-python"><div class="highlight"><pre><span class="sd">"""</span>
<span class="sd">  &gt;&gt;&gt; import string</span>
<span class="sd">  &gt;&gt;&gt; string.split(message, '??')</span>
<span class="sd">  ['this', 'and', 'that']</span>
<span class="sd">"""</span>
</pre></div>
</div>
</li>
<li><p class="first">Lists can be used to represent mathematical <em>vectors</em>.  In this exercise
and several that follow you will write functions to perform standard
operations on vectors.  Create a file named <tt class="docutils literal"><span class="pre">vectors.py</span></tt> and write Python
code to make the doctests for each function pass.</p>
<p>Write a function <tt class="docutils literal"><span class="pre">add_vectors(u,</span> <span class="pre">v)</span></tt> that takes two lists of numbers of
the same length, and returns a new list containing the sums of the
corresponding elements of each.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">add_vectors</span><span class="p">(</span><span class="n">u</span><span class="p">,</span> <span class="n">v</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; add_vectors([1, 0], [1, 1])</span>
<span class="sd">      [2, 1]</span>
<span class="sd">      &gt;&gt;&gt; add_vectors([1, 2], [1, 4])</span>
<span class="sd">      [2, 6]</span>
<span class="sd">      &gt;&gt;&gt; add_vectors([1, 2, 1], [1, 4, 3])</span>
<span class="sd">      [2, 6, 4]</span>
<span class="sd">      &gt;&gt;&gt; add_vectors([11, 0, -4, 5], [2, -4, 17, 0])</span>
<span class="sd">      [13, -4, 13, 5]</span>
<span class="sd">    """</span>
</pre></div>
</div>
<p><tt class="docutils literal"><span class="pre">add_vectors</span></tt> should pass the doctests above.</p>
</li>
<li><p class="first">Write a function <tt class="docutils literal"><span class="pre">scalar_mult(s,</span> <span class="pre">v)</span></tt> that takes a number, <tt class="docutils literal"><span class="pre">s</span></tt>, and a
list, <tt class="docutils literal"><span class="pre">v</span></tt> and returns the <a class="reference external" href="http://en.wikipedia.org/wiki/Scalar_multiple">scalar multiple</a> of <tt class="docutils literal"><span class="pre">v</span></tt> by <tt class="docutils literal"><span class="pre">s</span></tt>.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">scalar_mult</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">v</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; scalar_mult(5, [1, 2])</span>
<span class="sd">      [5, 10]</span>
<span class="sd">      &gt;&gt;&gt; scalar_mult(3, [1, 0, -1])</span>
<span class="sd">      [3, 0, -3]</span>
<span class="sd">      &gt;&gt;&gt; scalar_mult(7, [3, 0, 5, 11, 2])</span>
<span class="sd">      [21, 0, 35, 77, 14]</span>
<span class="sd">    """</span>
</pre></div>
</div>
</li>
<li><p class="first">Write a function <tt class="docutils literal"><span class="pre">dot_product(u,</span> <span class="pre">v)</span></tt> that takes two lists of numbers of
the same length, and returns the sum of the products of the corresponding
elements of each (the <a class="reference external" href="http://en.wikipedia.org/wiki/Dot_product">dot_product</a>).</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">dot_product</span><span class="p">(</span><span class="n">u</span><span class="p">,</span> <span class="n">v</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; dot_product([1, 1], [1, 1])</span>
<span class="sd">      2</span>
<span class="sd">      &gt;&gt;&gt; dot_product([1, 2], [1, 4])</span>
<span class="sd">      9</span>
<span class="sd">      &gt;&gt;&gt; dot_product([1, 2, 1], [1, 4, 3])</span>
<span class="sd">      12</span>
<span class="sd">      &gt;&gt;&gt; dot_product([2, 0, -1, 1], [1, 5, 2, 0])</span>
<span class="sd">      0</span>
<span class="sd">    """</span>
</pre></div>
</div>
<p>Verify that <tt class="docutils literal"><span class="pre">dot_product</span></tt> passes the doctests above.</p>
</li>
<li><p class="first"><em>Extra challenge for the mathematically inclined</em>: Write a function
<tt class="docutils literal"><span class="pre">cross_product(u,</span> <span class="pre">v)</span></tt> that takes two lists of numbers of length 3 and
returns their
<a class="reference external" href="http://en.wikipedia.org/wiki/Cross_product">cross product</a>.  You should
write your own doctests and use the test driven development process
described in the chapter.</p>
</li>
<li><p class="first">Create a new module named <tt class="docutils literal"><span class="pre">matrices.py</span></tt> and add the following two
functions introduced in the section on test-driven development:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">add_row</span><span class="p">(</span><span class="n">matrix</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; m = [[0, 0], [0, 0]]</span>
<span class="sd">      &gt;&gt;&gt; add_row(m)</span>
<span class="sd">      [[0, 0], [0, 0], [0, 0]]</span>
<span class="sd">      &gt;&gt;&gt; n = [[3, 2, 5], [1, 4, 7]]</span>
<span class="sd">      &gt;&gt;&gt; add_row(n)</span>
<span class="sd">      [[3, 2, 5], [1, 4, 7], [0, 0, 0]]</span>
<span class="sd">      &gt;&gt;&gt; n</span>
<span class="sd">      [[3, 2, 5], [1, 4, 7]]</span>
<span class="sd">    """</span>
</pre></div>
</div>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">add_column</span><span class="p">(</span><span class="n">matrix</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; m = [[0, 0], [0, 0]]</span>
<span class="sd">      &gt;&gt;&gt; add_column(m)</span>
<span class="sd">      [[0, 0, 0], [0, 0, 0]]</span>
<span class="sd">      &gt;&gt;&gt; n = [[3, 2], [5, 1], [4, 7]]</span>
<span class="sd">      &gt;&gt;&gt; add_column(n)</span>
<span class="sd">      [[3, 2, 0], [5, 1, 0], [4, 7, 0]]</span>
<span class="sd">      &gt;&gt;&gt; n</span>
<span class="sd">      [[3, 2], [5, 1], [4, 7]]</span>
<span class="sd">    """</span>
</pre></div>
</div>
<p>Your new functions should pass the doctests. Note that the last doctest in
each function assures that <tt class="docutils literal"><span class="pre">add_row</span></tt> and <tt class="docutils literal"><span class="pre">add_column</span></tt> are pure
functions. ( <em>hint:</em> Python has a <tt class="docutils literal"><span class="pre">copy</span></tt> module with a function named
<tt class="docutils literal"><span class="pre">deepcopy</span></tt> that could make your task easier here. We will talk more about
<tt class="docutils literal"><span class="pre">deepcopy</span></tt> in chapter 13, but google python copy module if you would like
to try it now.)</p>
</li>
<li><p class="first">Write a function <tt class="docutils literal"><span class="pre">add_matrices(m1,</span> <span class="pre">m2)</span></tt> that adds <tt class="docutils literal"><span class="pre">m1</span></tt> and <tt class="docutils literal"><span class="pre">m2</span></tt> and
returns a new matrix containing their sum. You can assume that <tt class="docutils literal"><span class="pre">m1</span></tt> and
<tt class="docutils literal"><span class="pre">m2</span></tt> are the same size. You add two matrices by adding their corresponding
values.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">add_matrices</span><span class="p">(</span><span class="n">m1</span><span class="p">,</span> <span class="n">m2</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; a = [[1, 2], [3, 4]]</span>
<span class="sd">      &gt;&gt;&gt; b = [[2, 2], [2, 2]]</span>
<span class="sd">      &gt;&gt;&gt; add_matrices(a, b)</span>
<span class="sd">      [[3, 4], [5, 6]]</span>
<span class="sd">      &gt;&gt;&gt; c = [[8, 2], [3, 4], [5, 7]]</span>
<span class="sd">      &gt;&gt;&gt; d = [[3, 2], [9, 2], [10, 12]]</span>
<span class="sd">      &gt;&gt;&gt; add_matrices(c, d)</span>
<span class="sd">      [[11, 4], [12, 6], [15, 19]]</span>
<span class="sd">      &gt;&gt;&gt; c</span>
<span class="sd">      [[8, 2], [3, 4], [5, 7]]</span>
<span class="sd">      &gt;&gt;&gt; d</span>
<span class="sd">      [[3, 2], [9, 2], [10, 12]]</span>
<span class="sd">   """</span>
</pre></div>
</div>
<p>Add your new function to <tt class="docutils literal"><span class="pre">matrices.py</span></tt> and be sure it passes the doctests
above. The last two doctests confirm that <tt class="docutils literal"><span class="pre">add_matrices</span></tt> is a pure
function.</p>
</li>
<li><p class="first">Write a function <tt class="docutils literal"><span class="pre">scalar_mult(s,</span> <span class="pre">m)</span></tt> that multiplies a matrix, <tt class="docutils literal"><span class="pre">m</span></tt>, by a
scalar, <tt class="docutils literal"><span class="pre">s</span></tt>.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">scalar_mult</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">m</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; a = [[1, 2], [3, 4]]</span>
<span class="sd">      &gt;&gt;&gt; scalar_mult(3, a)</span>
<span class="sd">      [[3, 6], [9, 12]]</span>
<span class="sd">      &gt;&gt;&gt; b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]</span>
<span class="sd">      &gt;&gt;&gt; scalar_mult(10, b)</span>
<span class="sd">      [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]</span>
<span class="sd">      &gt;&gt;&gt; b</span>
<span class="sd">      [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]</span>
<span class="sd">    """</span>
</pre></div>
</div>
<p>Add your new function to <tt class="docutils literal"><span class="pre">matrices.py</span></tt> and be sure it passes the doctests
above.</p>
</li>
<li><p class="first">Write functions <tt class="docutils literal"><span class="pre">row_times_column</span></tt> and <tt class="docutils literal"><span class="pre">matrix_mult</span></tt>:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">row_times_column</span><span class="p">(</span><span class="n">m1</span><span class="p">,</span> <span class="n">row</span><span class="p">,</span> <span class="n">m2</span><span class="p">,</span> <span class="n">column</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)</span>
<span class="sd">      19</span>
<span class="sd">      &gt;&gt;&gt; row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)</span>
<span class="sd">      22</span>
<span class="sd">      &gt;&gt;&gt; row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)</span>
<span class="sd">      43</span>
<span class="sd">      &gt;&gt;&gt; row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)</span>
<span class="sd">      50</span>
<span class="sd">    """</span>
</pre></div>
</div>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">matrix_mult</span><span class="p">(</span><span class="n">m1</span><span class="p">,</span> <span class="n">m2</span><span class="p">):</span>
   <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; matrix_mult([[1, 2], [3,  4]], [[5, 6], [7, 8]])</span>
<span class="sd">      [[19, 22], [43, 50]]</span>
<span class="sd">      &gt;&gt;&gt; matrix_mult([[1, 2, 3], [4,  5, 6]], [[7, 8], [9, 1], [2, 3]])</span>
<span class="sd">      [[31, 19], [85, 55]]</span>
<span class="sd">      &gt;&gt;&gt; matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])</span>
<span class="sd">      [[39, 54, 69], [13, 23, 33], [14, 19, 24]]</span>
<span class="sd">    """</span>
</pre></div>
</div>
<p>Add your new functions to <tt class="docutils literal"><span class="pre">matrices.py</span></tt> and be sure it passes the doctests
above.</p>
</li>
<li><p class="first">Create a new module named <tt class="docutils literal"><span class="pre">numberlists.py</span></tt> and add the following functions
to the module:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">only_evens</span><span class="p">(</span><span class="n">numbers</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; only_evens([1, 3, 4, 6, 7, 8])</span>
<span class="sd">      [4, 6, 8]</span>
<span class="sd">      &gt;&gt;&gt; only_evens([2, 4, 6, 8, 10, 11, 0])</span>
<span class="sd">      [2, 4, 6, 8, 10, 0]</span>
<span class="sd">      &gt;&gt;&gt; only_evens([1, 3, 5, 7, 9, 11])</span>
<span class="sd">      []</span>
<span class="sd">      &gt;&gt;&gt; only_evens([4, 0, -1, 2, 6, 7, -4])</span>
<span class="sd">      [4, 0, 2, 6, -4]</span>
<span class="sd">      &gt;&gt;&gt; nums = [1, 2, 3, 4]</span>
<span class="sd">      &gt;&gt;&gt; only_evens(nums)</span>
<span class="sd">      [2, 4]</span>
<span class="sd">      &gt;&gt;&gt; nums</span>
<span class="sd">      [1, 2, 3, 4]</span>
<span class="sd">    """</span>
</pre></div>
</div>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">only_odds</span><span class="p">(</span><span class="n">numbers</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; only_odds([1, 3, 4, 6, 7, 8])</span>
<span class="sd">      [1, 3, 7]</span>
<span class="sd">      &gt;&gt;&gt; only_odds([2, 4, 6, 8, 10, 11, 0])</span>
<span class="sd">      [11]</span>
<span class="sd">      &gt;&gt;&gt; only_odds([1, 3, 5, 7, 9, 11])</span>
<span class="sd">      [1, 3, 5, 7, 9, 11]</span>
<span class="sd">      &gt;&gt;&gt; only_odds([4, 0, -1, 2, 6, 7, -4])</span>
<span class="sd">      [-1, 7]</span>
<span class="sd">      &gt;&gt;&gt; nums = [1, 2, 3, 4]</span>
<span class="sd">      &gt;&gt;&gt; only_odds(nums)</span>
<span class="sd">      [1, 3]</span>
<span class="sd">      &gt;&gt;&gt; nums</span>
<span class="sd">      [1, 2, 3, 4]</span>
<span class="sd">    """</span>
</pre></div>
</div>
<p>Be sure these new functions pass the doctests.</p>
</li>
<li><p class="first">Add a function <tt class="docutils literal"><span class="pre">multiples_of(num,</span> <span class="pre">numlist)</span></tt> to <tt class="docutils literal"><span class="pre">numberlists.py</span></tt> that
takes an integer (<tt class="docutils literal"><span class="pre">num</span></tt>), and a list of integers (<tt class="docutils literal"><span class="pre">numlist</span></tt>) as
arguments and returns a list of those integers in <tt class="docutils literal"><span class="pre">numlist</span></tt> that are
multiples of <tt class="docutils literal"><span class="pre">num</span></tt>.  Add your own doctests and use TDD to develope this
function.</p>
</li>
<li><p class="first">Given:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="kn">import</span> <span class="nn">string</span>

<span class="n">song</span> <span class="o">=</span> <span class="s">"The rain in Spain..."</span>
</pre></div>
</div>
<p>Describe the relationship between <tt class="docutils literal"><span class="pre">string.join(string.split(song))</span></tt> and
<tt class="docutils literal"><span class="pre">song</span></tt>. Are they the same for all strings? When would they be different?</p>
</li>
<li><p class="first">Write a function <tt class="docutils literal"><span class="pre">replace(s,</span> <span class="pre">old,</span> <span class="pre">new)</span></tt> that replaces all occurences of
<tt class="docutils literal"><span class="pre">old</span></tt> with <tt class="docutils literal"><span class="pre">new</span></tt> in a string <tt class="docutils literal"><span class="pre">s</span></tt>.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">replace</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">old</span><span class="p">,</span> <span class="n">new</span><span class="p">):</span>
    <span class="sd">"""</span>
<span class="sd">      &gt;&gt;&gt; replace('Mississippi', 'i', 'I')</span>
<span class="sd">      'MIssIssIppI'</span>
<span class="sd">      &gt;&gt;&gt; s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'</span>
<span class="sd">      &gt;&gt;&gt; replace(s, 'om', 'am')</span>
<span class="sd">      'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!'</span>
<span class="sd">      &gt;&gt;&gt; replace(s, 'o', 'a')</span>
<span class="sd">      'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!'</span>
<span class="sd">    """</span>
</pre></div>
</div>
<p>Your solution should pass the doctests above. <em>Hint</em>: use <tt class="docutils literal"><span class="pre">string.split</span></tt>
and <tt class="docutils literal"><span class="pre">string.join</span></tt>.</p>
</li>
</ol>
</div>
</div>
