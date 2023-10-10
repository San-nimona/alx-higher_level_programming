<section id="reading-and-writing-files">
<span id="tut-files"></span><h2><span class="section-number">7.2. </span>Reading and Writing Files<a class="headerlink" href="#reading-and-writing-files" title="Permalink to this headline">¶</a></h2>
<p id="index-0"><a class="reference internal" href="../library/functions.html#open" title="open"><code class="xref py py-func docutils literal notranslate"><span class="pre">open()</span></code></a> returns a <a class="reference internal" href="../glossary.html#term-file-object"><span class="xref std std-term">file object</span></a>, and is most commonly used with
two positional arguments and one keyword argument:
<code class="docutils literal notranslate"><span class="pre">open(filename,</span> <span class="pre">mode,</span> <span class="pre">encoding=None)</span></code></p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><span class="copybutton" title="Hide the prompts and output" data-hidden="false">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s1">'workfile'</span><span class="p">,</span> <span class="s1">'w'</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span>
</pre></div>
</div>
<p>The first argument is a string containing the filename.  The second argument is
another string containing a few characters describing the way in which the file
will be used.  <em>mode</em> can be <code class="docutils literal notranslate"><span class="pre">'r'</span></code> when the file will only be read, <code class="docutils literal notranslate"><span class="pre">'w'</span></code>
for only writing (an existing file with the same name will be erased), and
<code class="docutils literal notranslate"><span class="pre">'a'</span></code> opens the file for appending; any data written to the file is
automatically added to the end.  <code class="docutils literal notranslate"><span class="pre">'r+'</span></code> opens the file for both reading and
writing. The <em>mode</em> argument is optional; <code class="docutils literal notranslate"><span class="pre">'r'</span></code> will be assumed if it’s
omitted.</p>
<p>Normally, files are opened in <em class="dfn">text mode</em>, that means, you read and write
strings from and to the file, which are encoded in a specific <em>encoding</em>.
If <em>encoding</em> is not specified, the default is platform dependent
(see <a class="reference internal" href="../library/functions.html#open" title="open"><code class="xref py py-func docutils literal notranslate"><span class="pre">open()</span></code></a>).
Because UTF-8 is the modern de-facto standard, <code class="docutils literal notranslate"><span class="pre">encoding="utf-8"</span></code> is
recommended unless you know that you need to use a different encoding.
Appending a <code class="docutils literal notranslate"><span class="pre">'b'</span></code> to the mode opens the file in <em class="dfn">binary mode</em>.
Binary mode data is read and written as <a class="reference internal" href="../library/stdtypes.html#bytes" title="bytes"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytes</span></code></a> objects.
You can not specify <em>encoding</em> when opening file in binary mode.</p>
<p>In text mode, the default when reading is to convert platform-specific line
endings (<code class="docutils literal notranslate"><span class="pre">\n</span></code> on Unix, <code class="docutils literal notranslate"><span class="pre">\r\n</span></code> on Windows) to just <code class="docutils literal notranslate"><span class="pre">\n</span></code>.  When writing in
text mode, the default is to convert occurrences of <code class="docutils literal notranslate"><span class="pre">\n</span></code> back to
platform-specific line endings.  This behind-the-scenes modification
to file data is fine for text files, but will corrupt binary data like that in
<code class="file docutils literal notranslate"><span class="pre">JPEG</span></code> or <code class="file docutils literal notranslate"><span class="pre">EXE</span></code> files.  Be very careful to use binary mode when
reading and writing such files.</p>
<p>It is good practice to use the <a class="reference internal" href="../reference/compound_stmts.html#with"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">with</span></code></a> keyword when dealing
with file objects.  The advantage is that the file is properly closed
after its suite finishes, even if an exception is raised at some
point.  Using <code class="xref std std-keyword docutils literal notranslate"><span class="pre">with</span></code> is also much shorter than writing
equivalent <a class="reference internal" href="../reference/compound_stmts.html#try"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">try</span></code></a>-<a class="reference internal" href="../reference/compound_stmts.html#finally"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">finally</span></code></a> blocks:</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><span class="copybutton" title="Hide the prompts and output" data-hidden="false">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s1">'workfile'</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
<span class="gp">... </span>    <span class="n">read_data</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

<span class="gp">&gt;&gt;&gt; </span><span class="c1"># We can check that the file has been automatically closed.</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">closed</span>
<span class="go">True</span>
</pre></div>
</div>
<p>If you’re not using the <a class="reference internal" href="../reference/compound_stmts.html#with"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">with</span></code></a> keyword, then you should call
<code class="docutils literal notranslate"><span class="pre">f.close()</span></code> to close the file and immediately free up any system
resources used by it.</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>Calling <code class="docutils literal notranslate"><span class="pre">f.write()</span></code> without using the <code class="xref std std-keyword docutils literal notranslate"><span class="pre">with</span></code> keyword or calling
<code class="docutils literal notranslate"><span class="pre">f.close()</span></code> <strong>might</strong> result in the arguments
of <code class="docutils literal notranslate"><span class="pre">f.write()</span></code> not being completely written to the disk, even if the
program exits successfully.</p>
</div>
<p>After a file object is closed, either by a <a class="reference internal" href="../reference/compound_stmts.html#with"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">with</span></code></a> statement
or by calling <code class="docutils literal notranslate"><span class="pre">f.close()</span></code>, attempts to use the file object will
automatically fail.</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><span class="copybutton" title="Hide the prompts and output" data-hidden="false">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">"&lt;stdin&gt;"</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span>
<span class="gr">ValueError</span>: <span class="n">I/O operation on closed file.</span>
</pre></div>
</div>
<section id="methods-of-file-objects">
<span id="tut-filemethods"></span><h3><span class="section-number">7.2.1. </span>Methods of File Objects<a class="headerlink" href="#methods-of-file-objects" title="Permalink to this headline">¶</a></h3>
<p>The rest of the examples in this section will assume that a file object called
<code class="docutils literal notranslate"><span class="pre">f</span></code> has already been created.</p>
<p>To read a file’s contents, call <code class="docutils literal notranslate"><span class="pre">f.read(size)</span></code>, which reads some quantity of
data and returns it as a string (in text mode) or bytes object (in binary mode).
<em>size</em> is an optional numeric argument.  When <em>size</em> is omitted or negative, the
entire contents of the file will be read and returned; it’s your problem if the
file is twice as large as your machine’s memory. Otherwise, at most <em>size</em>
characters (in text mode) or <em>size</em> bytes (in binary mode) are read and returned.
If the end of the file has been reached, <code class="docutils literal notranslate"><span class="pre">f.read()</span></code> will return an empty
string (<code class="docutils literal notranslate"><span class="pre">''</span></code>).</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><span class="copybutton" title="Hide the prompts and output" data-hidden="false">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
<span class="go">'This is the entire file.\n'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
<span class="go">''</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">f.readline()</span></code> reads a single line from the file; a newline character (<code class="docutils literal notranslate"><span class="pre">\n</span></code>)
is left at the end of the string, and is only omitted on the last line of the
file if the file doesn’t end in a newline.  This makes the return value
unambiguous; if <code class="docutils literal notranslate"><span class="pre">f.readline()</span></code> returns an empty string, the end of the file
has been reached, while a blank line is represented by <code class="docutils literal notranslate"><span class="pre">'\n'</span></code>, a string
containing only a single newline.</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><span class="copybutton" title="Hide the prompts and output" data-hidden="false">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span>
<span class="go">'This is the first line of the file.\n'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span>
<span class="go">'Second line of the file\n'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span>
<span class="go">''</span>
</pre></div>
</div>
<p>For reading lines from a file, you can loop over the file object. This is memory
efficient, fast, and leads to simple code:</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><span class="copybutton" title="Hide the prompts and output" data-hidden="false">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">f</span><span class="p">:</span>
<span class="gp">... </span>    <span class="nb">print</span><span class="p">(</span><span class="n">line</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s1">''</span><span class="p">)</span>
<span class="gp">...</span>
<span class="go">This is the first line of the file.</span>
<span class="go">Second line of the file</span>
</pre></div>
</div>
<p>If you want to read all the lines of a file in a list you can also use
<code class="docutils literal notranslate"><span class="pre">list(f)</span></code> or <code class="docutils literal notranslate"><span class="pre">f.readlines()</span></code>.</p>
<p><code class="docutils literal notranslate"><span class="pre">f.write(string)</span></code> writes the contents of <em>string</em> to the file, returning
the number of characters written.</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><span class="copybutton" title="Hide the prompts and output" data-hidden="false">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s1">'This is a test</span><span class="se">\n</span><span class="s1">'</span><span class="p">)</span>
<span class="go">15</span>
</pre></div>
</div>
<p>Other types of objects need to be converted – either to a string (in text mode)
or a bytes object (in binary mode) – before writing them:</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><span class="copybutton" title="Hide the prompts and output" data-hidden="false">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">value</span> <span class="o">=</span> <span class="p">(</span><span class="s1">'the answer'</span><span class="p">,</span> <span class="mi">42</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">s</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>  <span class="c1"># convert the tuple to string</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>
<span class="go">18</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">f.tell()</span></code> returns an integer giving the file object’s current position in the file
represented as number of bytes from the beginning of the file when in binary mode and
an opaque number when in text mode.</p>
<p>To change the file object’s position, use <code class="docutils literal notranslate"><span class="pre">f.seek(offset,</span> <span class="pre">whence)</span></code>.  The position is computed
from adding <em>offset</em> to a reference point; the reference point is selected by
the <em>whence</em> argument.  A <em>whence</em> value of 0 measures from the beginning
of the file, 1 uses the current file position, and 2 uses the end of the file as
the reference point.  <em>whence</em> can be omitted and defaults to 0, using the
beginning of the file as the reference point.</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><span class="copybutton" title="Hide the prompts and output" data-hidden="false">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s1">'workfile'</span><span class="p">,</span> <span class="s1">'rb+'</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">b</span><span class="s1">'0123456789abcdef'</span><span class="p">)</span>
<span class="go">16</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>      <span class="c1"># Go to the 6th byte in the file</span>
<span class="go">5</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="go">b'5'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="o">-</span><span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>  <span class="c1"># Go to the 3rd byte before the end</span>
<span class="go">13</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="go">b'd'</span>
</pre></div>
</div>
<p>In text files (those opened without a <code class="docutils literal notranslate"><span class="pre">b</span></code> in the mode string), only seeks
relative to the beginning of the file are allowed (the exception being seeking
to the very file end with <code class="docutils literal notranslate"><span class="pre">seek(0,</span> <span class="pre">2)</span></code>) and the only valid <em>offset</em> values are
those returned from the <code class="docutils literal notranslate"><span class="pre">f.tell()</span></code>, or zero. Any other <em>offset</em> value produces
undefined behaviour.</p>
<p>File objects have some additional methods, such as <a class="reference internal" href="../library/io.html#io.IOBase.isatty" title="io.IOBase.isatty"><code class="xref py py-meth docutils literal notranslate"><span class="pre">isatty()</span></code></a> and
<a class="reference internal" href="../library/io.html#io.IOBase.truncate" title="io.IOBase.truncate"><code class="xref py py-meth docutils literal notranslate"><span class="pre">truncate()</span></code></a> which are less frequently used; consult the Library
Reference for a complete guide to file objects.</p>
</section>
<section id="saving-structured-data-with-json">
<span id="tut-json"></span><h3><span class="section-number">7.2.2. </span>Saving structured data with <a class="reference internal" href="../library/json.html#module-json" title="json: Encode and decode the JSON format."><code class="xref py py-mod docutils literal notranslate"><span class="pre">json</span></code></a><a class="headerlink" href="#saving-structured-data-with-json" title="Permalink to this headline">¶</a></h3>
<p id="index-1">Strings can easily be written to and read from a file.  Numbers take a bit more
effort, since the <a class="reference internal" href="../library/io.html#io.TextIOBase.read" title="io.TextIOBase.read"><code class="xref py py-meth docutils literal notranslate"><span class="pre">read()</span></code></a> method only returns strings, which will have to
be passed to a function like <a class="reference internal" href="../library/functions.html#int" title="int"><code class="xref py py-func docutils literal notranslate"><span class="pre">int()</span></code></a>, which takes a string like <code class="docutils literal notranslate"><span class="pre">'123'</span></code>
and returns its numeric value 123.  When you want to save more complex data
types like nested lists and dictionaries, parsing and serializing by hand
becomes complicated.</p>
<p>Rather than having users constantly writing and debugging code to save
complicated data types to files, Python allows you to use the popular data
interchange format called <a class="reference external" href="https://json.org">JSON (JavaScript Object Notation)</a>.  The standard module called <a class="reference internal" href="../library/json.html#module-json" title="json: Encode and decode the JSON format."><code class="xref py py-mod docutils literal notranslate"><span class="pre">json</span></code></a> can take Python
data hierarchies, and convert them to string representations; this process is
called <em class="dfn">serializing</em>.  Reconstructing the data from the string representation
is called <em class="dfn">deserializing</em>.  Between serializing and deserializing, the
string representing the object may have been stored in a file or data, or
sent over a network connection to some distant machine.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The JSON format is commonly used by modern applications to allow for data
exchange.  Many programmers are already familiar with it, which makes
it a good choice for interoperability.</p>
</div>
<p>If you have an object <code class="docutils literal notranslate"><span class="pre">x</span></code>, you can view its JSON string representation with a
simple line of code:</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><span class="copybutton" title="Hide the prompts and output" data-hidden="false">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">json</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="s1">'simple'</span><span class="p">,</span> <span class="s1">'list'</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
<span class="go">'[1, "simple", "list"]'</span>
</pre></div>
</div>
<p>Another variant of the <a class="reference internal" href="../library/json.html#json.dumps" title="json.dumps"><code class="xref py py-func docutils literal notranslate"><span class="pre">dumps()</span></code></a> function, called <a class="reference internal" href="../library/json.html#json.dump" title="json.dump"><code class="xref py py-func docutils literal notranslate"><span class="pre">dump()</span></code></a>,
simply serializes the object to a <a class="reference internal" href="../glossary.html#term-text-file"><span class="xref std std-term">text file</span></a>.  So if <code class="docutils literal notranslate"><span class="pre">f</span></code> is a
<a class="reference internal" href="../glossary.html#term-text-file"><span class="xref std std-term">text file</span></a> object opened for writing, we can do this:</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><pre><span></span><span class="n">json</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">f</span><span class="p">)</span>
</pre></div>
</div>
<p>To decode the object again, if <code class="docutils literal notranslate"><span class="pre">f</span></code> is a <a class="reference internal" href="../glossary.html#term-binary-file"><span class="xref std std-term">binary file</span></a> or
<a class="reference internal" href="../glossary.html#term-text-file"><span class="xref std std-term">text file</span></a> object which has been opened for reading:</p>
<div class="highlight-python3 notranslate"><div class="highlight" style="position: relative;"><pre><span></span><span class="n">x</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>JSON files must be encoded in UTF-8. Use <code class="docutils literal notranslate"><span class="pre">encoding="utf-8"</span></code> when opening
JSON file as a <a class="reference internal" href="../glossary.html#term-text-file"><span class="xref std std-term">text file</span></a> for both of reading and writing.</p>
</div>
<p>This simple serialization technique can handle lists and dictionaries, but
serializing arbitrary class instances in JSON requires a bit of extra effort.
The reference for the <a class="reference internal" href="../library/json.html#module-json" title="json: Encode and decode the JSON format."><code class="xref py py-mod docutils literal notranslate"><span class="pre">json</span></code></a> module contains an explanation of this.</p>
</section>
</section>
