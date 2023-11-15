<h3>What’s a database</h3>
A database is a structured collection of data organized in a way that it can be easily accessed, managed, and updated. Databases can store a variety of data types, including text, numbers, dates, and multimedia. They are an integral part of modern computing and are used in various applications, from simple desktop applications to large-scale web applications and enterprise systems.

<h3> What’s a relational database </h3>
A relational database is a type of database that organizes data into tables with rows and columns, where the tables are related to each other based on common fields. It follows the principles of relational algebra and is designed to efficiently store, retrieve, and manage structured data. The structure and relationships between tables are defined by a schema, which includes constraints, such as primary keys and foreign keys, to maintain data integrity.
<div id="maincontent"><h1>Basic SQL statements: DDL and DML</h1>
<p>In the first part of this tutorial, you’ve seen some of the SQLi
statements that you need to start building a database. This page gives
       you a review of those and adds several more that you haven’t seen yet.</p>

    <p></p><li>SQL statements are divided into two major categories:
       <strong>data definition language (DDL)</strong> and <strong>data manipulation
       language (DML)</strong>. Both of these categories contain far more statements
       than we can present here, and each of the statements is far more complex
       than we show in this introduction. If you want to master this material, we
       strongly recommend that you find a SQL reference for your own database
       software as a supplement to these pages.<p></p>

<h2>Data definition language</h2>

    <p>DDL statements are used to build and modify the structure of your
       tables and other objects in the database. When you execute a DDL statement, it
       takes effect immediately.</p>

    <p></p></li><li>The create table statement does exactly that:<p></p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">TABLE</span> &lt;<span class="hljs-keyword">table</span> name&gt; (
        &lt;attribute name <span class="hljs-number">1</span>&gt; &lt;<span class="hljs-keyword">data</span> type <span class="hljs-number">1</span>&gt;,
        ...
        &lt;attribute name n&gt; &lt;<span class="hljs-keyword">data</span> type n&gt;);</span></code></pre>

    <p>The <strong>data types</strong> that you will use most frequently are
       character strings, which might be called VARCHAR or CHAR for variable or fixed length
       strings; numeric types such as NUMBER or INTEGER, which will usually specify a
       precision; and DATE or related types. Data type syntax is variable from system to system;
       the only way to be sure is to consult the documentation for your own software.</p>

    <p></p></li><li>The alter table statement may be used as you have seen to specify
       primary and foreign key constraints, as well as to make other modifications to the table structure.
       Key constraints may also be specified in the CREATE TABLE statement.<p></p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">ALTER</span> <span class="hljs-keyword">TABLE</span> &lt;<span class="hljs-keyword">table</span> name&gt;
        <span class="hljs-keyword">ADD</span> <span class="hljs-keyword">CONSTRAINT</span> &lt;<span class="hljs-keyword">constraint</span> name&gt; <span class="hljs-keyword">PRIMARY</span> <span class="hljs-keyword">KEY</span> (&lt;attribute list&gt;);</span></code></pre>

    <p>You get to specify the constraint name. Get used to following
       a convention of tablename_pk (for example, Customers_pk), so you can remember
       what you did later. The attribute list contains the one or more attributes
       that form this PK; if more than one, the names are separated by commas.</p>

    <p></p></li><li>The foreign key constraint is a bit more complicated, since
       we have to specify both the FK attributes in this (child) table, and the PK attributes
       that they link to in the parent table.<p></p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">ALTER</span> <span class="hljs-keyword">TABLE</span> &lt;<span class="hljs-keyword">table</span> name&gt;
        <span class="hljs-keyword">ADD</span> <span class="hljs-keyword">CONSTRAINT</span> &lt;<span class="hljs-keyword">constraint</span> name&gt; <span class="hljs-keyword">FOREIGN</span> <span class="hljs-keyword">KEY</span> (&lt;attribute list&gt;)
        <span class="hljs-keyword">REFERENCES</span> &lt;parent <span class="hljs-keyword">table</span> name&gt; (&lt;attribute list&gt;);</span></code></pre>

    <p>Name the constraint in the form childtable_parenttable_fk (for
       example, Orders_Customers_fk). If there is more than one attribute in the FK,
       all of them must be included (with commas between) in both the FK attribute
       list and the REFERENCES (parent table) attribute list.</p>

    <p>You need a separate foreign key definition for each relationship
       in which this table is the child.</p>

    <p></p></li><li>If you totally mess things up and want to start over, you
       can always get rid of any object you’ve created with a drop
       statement. The syntax is different for tables and constraints.<p></p>
<pre><code class="hljs sql">        <strong><span class="hljs-operator"><span class="hljs-keyword">DROP</span> <span class="hljs-keyword">TABLE</span></span></strong><span class="hljs-operator"> &lt;<span class="hljs-keyword">table</span> name&gt;;</span>

        <span class="hljs-operator"><span class="hljs-keyword">ALTER</span> <span class="hljs-keyword">TABLE</span> &lt;<span class="hljs-keyword">table</span> name&gt;
        </span><strong><span class="hljs-operator"><span class="hljs-keyword">DROP</span> <span class="hljs-keyword">CONSTRAINT</span></span></strong><span class="hljs-operator"> &lt;<span class="hljs-keyword">constraint</span> name&gt;;</span></code></pre>

    <p>This is where consistent constraint naming comes in handy, so
       you can just remember the PK or FK name rather than remembering the syntax for
       looking up the names in another table. The DROP TABLE statement gets rid of its own
       PK constraint, but won’t work until you separately drop any FK constraints
       (or child tables) that refer to this one.
       It also gets rid of all data that was contained in the table—and it doesn't
       even ask you if you really want to do this!</p>

    <p></p></li><li>All of the information about objects in your schema is
       contained, not surprisingly, in a set of tables that is called the <strong>data
       dictionary</strong>. There are hundreds of these tables most database systems,
       but all of them will allow you to see information about your own tables,
       in many cases with a graphical interface. How you do this is entirely
       system-dependent.<p></p>

<h2>Data manipulation language</h2>

    <p>DML statements are used to work with the data in tables. When you are
       connected to most multi-user databases (whether in a client program or by a connection
       from a Web page script), you are in effect working with a private copy of your
       tables that can’t be seen by anyone else until you are finished (or tell the
       system that you are finished). You have already seen the SELECT statement; it is
       considered to be part of DML even though it just retreives data rather than
       modifying it.</p>

    <p></p></li><li>The insert statement is used, obviously, to add
       new rows to a table. <p></p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">INSERT</span> <span class="hljs-keyword">INTO</span> &lt;<span class="hljs-keyword">table</span> name&gt;
        <span class="hljs-keyword">VALUES</span> (&lt;<span class="hljs-keyword">value</span> <span class="hljs-number">1</span>&gt;, ... &lt;<span class="hljs-keyword">value</span> n&gt;);</span></code></pre>

    <p>The comma-delimited list of values must match the table structure
       exactly in the number of attributes and the data type of each attribute. Character
       type values are always enclosed in single quotes; number values are never in quotes;
       date values are often (but not always) in the format 'yyyy-mm-dd' (for example, '2006-11-30').</p>

    <p>Yes, you will need a separate INSERT statement for every row.</p>

    <p></p></li><li>The update statement is used to change values
       that are already in a table.<p></p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">UPDATE</span> &lt;<span class="hljs-keyword">table</span> name&gt;
        <span class="hljs-keyword">SET</span> &lt;attribute&gt; = &lt;expression&gt;
        <span class="hljs-keyword">WHERE</span> &lt;condition&gt;;</span></code></pre>

    <p>The update expression can be a constant, any computed value, or even the
       result of a SELECT statement that returns a single row and a single column. If the
       WHERE clause is omitted, then the specified attribute is set to the same value
       in every row of the table (which
       is usually not what you want to do). You can also set multiple attribute values at
       the same time with a comma-delimited list of attribute=expression pairs.</p>

    <p></p></li><li>The <strong>delete</strong> statement does just that, for rows
       in a table.<p></p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">DELETE</span> <span class="hljs-keyword">FROM</span> &lt;<span class="hljs-keyword">table</span> name&gt;
        <span class="hljs-keyword">WHERE</span> &lt;condition&gt;;</span></code></pre>

    <p>If the WHERE clause is omitted, then every row of the table is deleted
       (which again is usually not what you want to do)—and again, you will not get
       a “do you really want to do this?” message.</p>

    <p></p></li><li>If you are using a large multi-user system, you may need to make your DML        changes visible to the rest of the users of the
       database. Although this might be done automatically when you log out, you could also just type:<p></p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">COMMIT</span>;</span></code></pre>

    <p></p></li><li>If you’ve messed up your changes in this type of system, and want
       to restore your
       private copy of the database to the way it was before you started (this only works if
       you haven’t already typed COMMIT), just type:<p></p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">ROLLBACK</span>;</span></code></pre>

    <p>Although single-user systems don’t support <strong>commit</strong> and
       <strong>rollback</strong> statements, they
       are used in large systems to control <strong>transactions</strong>, which are
       sequences of changes to the database. Transactions are frequently covered
       in more advanced courses. </p>


<h2>Privileges</h2>

    <p>If you want anyone else to be able to view or manipulate the data in your
       tables, and if your system permits this, you will have to explicitly <strong>grant</strong>
       the appropriate privilege
       or privileges (select, insert, update, or delete) to them. This has to be done for each table.
       The most common case where you would use grants is for tables that you want to make
       available to scripts running on a Web server, for example:</p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">GRANT</span> <span class="hljs-keyword">select</span>, <span class="hljs-keyword">insert</span> <span class="hljs-keyword">ON</span> customers <span class="hljs-keyword">TO</span> webuser;</span></code></pre>
</li></div>
<div id="maincontent"><h1>Basic queries: SQL and RA</h1>
<p>Once we have created tables and loaded them with data,
    we need to retrieve this data. This website introduces the
    fundamental retrieval statements from two languages,
    SQL and Relational Algebra.
</p>
<article class="topic">
<h2>Retrieving data from one table</h2>
<section id="sql" class="intro">
    <h3>Retrieval with SQL</h3>

    <p>In SQL, to retrieve data stored in our tables, we use the <strong>SELECT</strong>
        statement. The result of this statement is always in the form of a table
        that we can view with our database client software or use with programming
        languages to build dynamic web
        pages or desktop applications. While the result may look like a table, it is not
        stored in the database like the named tables are. The result of a SELECT statement
        can also be used as part of another statement.</p>
    <section>
        <h4>Basic syntax of <code class="sql">SELECT</code> statement</h4>

        <p>The basic syntax consists of four clauses as
            shown in the figure below. While SQL is not case sensitive, by convention
            many database developers use uppercase for keywords to improve readability.
        </p>
        <figure>
    <pre><code class="hljs sql"><span class="hljs-operator"><span class="hljs-keyword">SELECT</span> {attribute}+
  <span class="hljs-keyword">FROM</span> {<span class="hljs-keyword">table</span>}+
  [ <span class="hljs-keyword">WHERE</span> {<span class="hljs-built_in">boolean</span> predicate <span class="hljs-keyword">to</span> pick <span class="hljs-keyword">rows</span>} ]
  [ <span class="hljs-keyword">ORDER</span> <span class="hljs-keyword">BY</span> {attribute}+ ];</span></code></pre>
            <figcaption>The four basic clauses of a SQL <code class="sql">SELECT</code> statement.</figcaption>
        </figure>

        <p>Of the four clauses, only the first two are required. The two shown in
            square brackets are optional. When you
            start learning to build queries, it is helpful to follow a specific step-by-step
            sequence, look at the data after each modification to the query, and be
            sure that you understand the results at each step. This iterative refinement
            will allow you to hone in on just the right SQL statement to retrieve the desired
            information. Below is a summary of the clauses.</p>
        <ul>
            <li>The <code class="sql">SELECT</code> clause allows us to specify a comma-separated
                list of attribute names corresponding to the columns that are to be retrieved.
               You can use an asterisk character, *, to retrieve all the columns.
            </li>
            <li>In queries where all the data is found in one table, the
               <code class="sql">FROM</code> clause is where we
                specify the name of the table from which to retrieve rows. In other articles
                we will use it to retrieve rows from multiple tables.</li>
            <li>The <code class="sql">WHERE</code> clause is used to constrain which rows
                to retrieve. We do this by specifying a boolean predicate that compares the
                values of table columns to literal values or to other columns.</li>
            <li>The <code class="sql">ORDER BY</code> clause gives us a way to order the display
               of the rows in the result of the statement.</li>
        </ul>

        <p>The example of the next section provides more information on how to retrieve
            information using this <code class="sql">SELECT</code> statement.</p>
    </section>

    <section class="example">
        <h4>SQL Example: customers in a specified zip code</h4>

        <p>We’ll build a list
            of customers who live in a specific zip code area, showing their first and
            last names and phone numbers and listing them in alphabetical order by last name.
            A company might want to do this to initiate a marketing campaign to customers
            in this area. In this example, we’ll use zip code 90840.
            Listed below are the refinement steps we take to arrive at the
            statement that will retrieve what we need.
        </p>
        <ol>
            <li>Start by retrieving <em>all</em> of the relevant data; in this case, that
                is all data of every customer. In our database all of this is stored in
                only one table, so that table is specified in the FROM clause. Since we
                want to retrieve all columns from this table, instead of naming each of
                them individually, we can use the abbreviation symbol * to indicate that
                all columns are to be retrieved. That completes the recipe for our
                SQL statement which is shown below; note, we have no use for the two
                optional clauses in this initial statement. In the same figure below,
                you will also find the result of this query executed on a tiny database.
                <figure id="refine1">
<pre><code class="hljs sql"><span class="hljs-operator"><span class="hljs-keyword">SELECT</span> *
  <span class="hljs-keyword">FROM</span> customers;</span></code></pre>
                    <table class="datatable"><caption>Customers</caption><thead><tr><th class="datatable" scope="col" id="1"></th><th class="datatable" scope="col" id="1"></th><th class="datatable" scope="col" id="1"></th><th class="datatable" scope="col" id="1"></th><th class="datatable" scope="col" id="1"></th></tr></thead><tbody><tr><td class="datatable" headers="1">Tom</td><td class="datatable" headers="1">Jewett</td><td class="datatable" headers="1">714-555-1212</td><td class="datatable" headers="1">10200 Slater</td><td class="datatable" headers="1">92708</td></tr><tr><td class="datatable" headers="1">Alvaro</td><td class="datatable" headers="1">Monge</td><td class="datatable" headers="1">562-333-4141</td><td class="datatable" headers="1">2145 Main</td><td class="datatable" headers="1">90840</td></tr><tr><td class="datatable" headers="1">Wayne</td><td class="datatable" headers="1">Dick</td><td class="datatable" headers="1">562-777-3030</td><td class="datatable" headers="1">1250 Bellflower</td><td class="datatable" headers="1">90840</td></tr></tbody></table>                    <figcaption>SQL statement to retrieve all customers and the result set</figcaption>
                </figure>
                While the result of a query is known as a <strong>result set</strong>,
                the result is not in fact always a set. The result could be a multiset,
                that is, a collection of rows that can have duplicate rows.
            </li>

            <li>Clearly we need to a refinement step as the query retrieves all customers
                while we are only interested in customers who live in zip code 90840.
                We need to specify in the statement that the only rows to retrieve from
                the database are those that meet this criteria. Such qualifying criteria
                is specified in the <code class="sql">WHERE</code> clause using
                <a href="http://en.wikipedia.org/wiki/Boolean_expression">boolean expressions</a>.
                Our first statement is thus refined as shown in the figure below.
                <figure id="refine2">
<pre><code class="hljs sql"><span class="hljs-operator"><span class="hljs-keyword">SELECT</span> *
  <span class="hljs-keyword">FROM</span> customers
  <span class="hljs-keyword">WHERE</span> cZipCode = <span class="hljs-string">'90840'</span>;</span></code></pre>
                    <table class="datatable"><caption>Customers in zip code 90840</caption><thead><tr><th class="datatable" scope="col" id="2"></th><th class="datatable" scope="col" id="2"></th><th class="datatable" scope="col" id="2"></th><th class="datatable" scope="col" id="2"></th><th class="datatable" scope="col" id="2"></th></tr></thead><tbody><tr><td class="datatable" headers="2">Alvaro</td><td class="datatable" headers="2">Monge</td><td class="datatable" headers="2">562-333-4141</td><td class="datatable" headers="2">2145 Main</td><td class="datatable" headers="2">90840</td></tr><tr><td class="datatable" headers="2">Wayne</td><td class="datatable" headers="2">Dick</td><td class="datatable" headers="2">562-777-3030</td><td class="datatable" headers="2">1250 Bellflower</td><td class="datatable" headers="2">90840</td></tr></tbody></table>                    <figcaption>Refinement #2 to retrieve desired customers.</figcaption>
                </figure>
                Note that SQL syntax requires the use of <em>single</em> quotes
                around literal strings like <code>'90840'</code>. While not
                illustrated in this example and unlike SQL keywords,
                literal strings and strings stored in the database
                <em>are case sensitive</em>; thus, <code>'Long Beach'</code>
                is a different string than <code>'long beach'</code>.
            </li>

            <li>We need just a couple of more refinements. While we now are retrieving
                only the customers we desire, we are also retrieving every column
                from the table yet, not all are needed. We need a way to
                pick the attributes (columns) we want. This is done by listing them
                in the <code class="sql">SELECT</code> clause, each column name separated by a comma.
                The figure below shows this refinement and its corresponding result set.
                <figure id="refine3">
<pre><code class="hljs sql"><span class="hljs-operator"><span class="hljs-keyword">SELECT</span> cLastName, cFirstName, cPhone
  <span class="hljs-keyword">FROM</span> customers
  <span class="hljs-keyword">WHERE</span> cZipCode = <span class="hljs-string">'90840'</span>;</span></code></pre>
                    <table class="datatable"><caption>Columns from SELECT</caption><thead><tr><th class="datatable" scope="col" id="3"></th><th class="datatable" scope="col" id="3"></th><th class="datatable" scope="col" id="3"></th></tr></thead><tbody><tr><td class="datatable" headers="3">Monge</td><td class="datatable" headers="3">Alvaro</td><td class="datatable" headers="3">562-333-4141</td></tr><tr><td class="datatable" headers="3">Dick</td><td class="datatable" headers="3">Wayne</td><td class="datatable" headers="3">562-777-3030</td></tr></tbody></table>                    <figcaption>Refinement #3 to retrieve specific columns.</figcaption>
                </figure>
                Note that changing the order of the columns (like showing the last name first)
                does not change the meaning of the results.
            </li>

            <li>For practical purposes our last refinement is all that we need. To make
                the result set more appealing to a human, we may want to order the result set.
                Imagine having a result set that is 100 times of what we are showing here!
                It would be better to display the result sorted alphabetically by the name
                of the customer. In SQL, you can use the <code class="sql">ORDER BY</code> clause to
                specify the order in which to retrieve the results. Once again, this ordering
                does not change the meaning of the results; the result set does not change,
                all it changes is the order in which the rows are displayed. This final
                refinement and its result are shown below.
                <figure id="refine4">
<pre><code class="hljs sql"><span class="hljs-operator"><span class="hljs-keyword">SELECT</span> cLastName, cFirstName, cPhone
  <span class="hljs-keyword">FROM</span> customers
  <span class="hljs-keyword">WHERE</span> cZipCode = <span class="hljs-string">'90840'</span>
  <span class="hljs-keyword">ORDER</span> <span class="hljs-keyword">BY</span> cLastName <span class="hljs-keyword">ASC</span>, cFirstName <span class="hljs-keyword">ASC</span>;</span></code></pre>
                    <table class="datatable"><caption>Rows in order</caption><thead><tr><th class="datatable" scope="col" id="4"></th><th class="datatable" scope="col" id="4"></th><th class="datatable" scope="col" id="4"></th></tr></thead><tbody><tr><td class="datatable" headers="4">Dick</td><td class="datatable" headers="4">Wayne</td><td class="datatable" headers="4">562-777-3030</td></tr><tr><td class="datatable" headers="4">Monge</td><td class="datatable" headers="4">Alvaro</td><td class="datatable" headers="4">562-333-4141</td></tr></tbody></table>                    <figcaption>Refinement #4 to order the rows in the result.</figcaption>
                </figure>
                The keyword <code class="sql">ASC</code> is used to order the rows in ascending
                values, which is the default ordering so the keyword is not necessary and is
                shown here for completeness. To order rows in descending values, use the
                keyword <code class="sql">DESC</code>. In the statement above, rows are first
                ordered in ascending value of the last name and in case of ties (two or more
                customers with the same name), then the rows are ordered in ascending value
                of the first name.
            </li>
        </ol>

    </section>
</section>


<section id="relational_algebra">
    <h3>Retrieval with relational algebra</h3>

    <p>SQL is a
        <a href="http://en.wikipedia.org/wiki/Declarative_language">declarative language</a>.
        As such, SQL is used to <em>declare what is to be retrieved</em> from the database.
        In our SQL statement above, we did not specify how to retrieve the result.
        In an imperative language, we do specify the steps to take to solve a problem,
        such as how to retrieve a result from a database. Thus, it is the responsibility
        of the database system to determine how to retrieve what is declared in SQL.
        In relational database systems, this is commonly done by translating SQL into
        <a href="http://en.wikipedia.org/wiki/Relational_algebra">Relational Algebra</a>.
    </p>

    <p>Like all algebras, <abbr title="relational algebra">RA</abbr> applies operators
        to operands to produce results of the same type as the operands.
        RA operands are relations and thus the results are also relations. Furthermore,
        like all algebras, the results of operators can be
        used as operands in building more complex expressions. We
        introduce two of the RA operators following the example and refinements above
        for SQL.</p>
    <section>
        <h4>RA operators: σ and π</h4>

        <p>To retrieve a single relation in RA, we only need to use
            its name. The common notation in the relational model
            is to use uppercase letters for relation scheme (R, S, T, U, etc)
            and lowercase letters for relations (r, s, t, u, etc).
            Thus, the simplest RA expression is to retrieve all columns and
            every row of a relation is just the name of the relation: <i>r</i>
        </p>

        <p>The two RA operators introduced here are σ, the select operator,
            and π, the project operator.</p>
        <ul>
            <li>The <strong>select (RA)</strong> operator specified by the symbol σ
                picks tuples that satisfy a predicate; thus, serving a similar purpose
                as the SQL <code class="sql">WHERE</code> clause. This RA select operator σ
                is unary taking a single relation or RA expression as its operand.
                The <strong>predicate</strong>, θ, to specify which tuples are required
                is written as a subscript of the operator, giving the syntax of
                <code class="ra_expression">σ<sub>θ</sub>e</code>, where e is
                a RA expression.
                <p>The scheme of the result of
                    <code class="ra_expression">σ<sub>θ</sub>r</code> is R—the
                    same scheme we started with—since the entire tuple is selected, as long
                    as the tuple satisfies the predicate. The result of this operation includes all
                    tuples of relation r that satisfy the predicate θ—that is, θ
                    evaluates to true.</p>
            </li>
            <li>The <strong>project (RA)</strong> operator specified by the symbol π
                picks attributes, confusingly like the SQL <code class="sql">SELECT</code> clause.
                It is also a unary operator that takes a single relation or expression as its operand
                and the attributes to retrieve are specified as a
                a <strong>subscheme</strong>, X (subset of its operand).
                The syntax is <code class="ra_expression">π<sub>X</sub>e</code>
                where, as before, e is a RA expression. Following are additional properties
                of the project operator.
                <ul>
                    <li>For X to be a subscheme of R, it must be a <em>subset of
                            the attributes in R</em> that preserves the assignment rule from R
                        (that is, each attribute of X must have the same domain as its
                        corresponding attribute in R).
                    </li>
                    <li>The scheme of the result of
                        π<sub>X</sub><i>r</i> is X. The tuples resulting from this
                        operation are tuples of the original relation, <i>r</i>, but cut down to the
                        attributes contained in X.
                    </li>

                    <li>If X is a super key of <i>r</i>, then there will be the same
                        number of tuples in the result as there were to begin with in <i>r</i>.
                        If X is <i>not</i> a
                        super key of <i>r</i>, then any duplicate (non-distinct) tuples are eliminated
                        from the result, ensuring the result is always a set. This is unlike SQL
                        where the result of a <code class="sql">SELECT</code> statement with a
                        <code class="sql">WHERE</code> clause is a multiset.
                    </li>
                </ul>
            </li><li>As with other algebras, we can use
                <a href="http://en.wikipedia.org/wiki/Function_composition">function composition</a>
                by applying the project operator to the
                result of the select operator from the previous set to get:
                <code class="ra_expression">π<sub>X</sub>σ<sub>θ</sub>r</code>
            </li>
        </ul>

    </section>

    <section class="example">
        <h4>RA Example: customers in a specified zip code</h4>

        <p>Given the above RA syntax, we can now use RA to create expressions that match
            the SQL statements from above which retrieve the customers who live in zip code 90840.
        </p>
        <ol>
            <li>The first step is to retrieve all customers. This is done by a RA expression that
                consists of just the name of the relation, thus the RA expression
                <code class="ra_expression">customers</code> is
                the equivalent of the <a href="#refine1">first SQL statement above</a>. Its
                scheme is the same as the Customers scheme.
            </li>

            <li>To retrieve the equivalent
                result set as the <a href="#refine2">SQL statement in refinement #2</a>,
                we apply the σ operator to the result set of our previous expression:
                <pre><code class="ra_expression hljs">σ<sub>cZipCode='90840'</sub>customers</code></pre>
                Again, the scheme of the result set is the same as the Customers scheme.
            </li>

            <li>Now, applying function composition here, we can retrieve just the columns we
                desire from the result set of the previous expression to get the RA expression
                that retrieves the equivalent
                result set as the <a href="#refine3">SQL statement in refinement #3</a>:
                <pre><code class="ra_expression hljs">π<sub>cLastName, cFirstName, cPhone</sub> σ<sub>cZipCode='90840'</sub>customers</code></pre>
            </li>
            <li>Note that, in RA the <em>results of expressions are strictly sets of tuples</em>,
                thus, there is no way to specify the order of tuples in a result set. This is
                unlike SQL and its <code class="SQL">ORDER BY</code> caluse.
            </li>
        </ol>
    </section>
</section>
</article>
</div>
<h1>SQL technique: functions</h1>

    <p>Sometimes, the information that we need is not actually
       stored in the database, but has to be computed in some way from the
       stored data. In our order entry example, there are two derived
       attributes (/subtotal in OrderLines and /total in Orders) that are part
       of the class diagram but not part of the relation scheme. We can
       compute these by using SQL functions in the SELECT statement.</p>

    <p>There are many, many functions in any implementation of
       SQL—far more than we can show here. Unfortunately, many of the
       functions are defined quite differently in different database packages, so you
       should always consult a reference manual for your specific software.</p>

<h2>Computed columns</h2>
<p>We can compute values from information that is in a table
       simply by showing the computation in the SELECT clause. Each computation
       creates a new column in the output table, just as if it were a named attribute.</p>

    <p><i>Example:</i> We want to find the subtotal for each line
       of the OrderLines table, just as shown in the UML class diagram. Obviously,
       the total of each line is simply the unit sale price times the quantity
       ordered, so we don’t even need a function yet—just the
       computation. We have included all three of the OrderLines PK attributes in the SELECT
       clause attribute list, to be sure that we show the subtotal for each distinct line.</p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">SELECT</span> custID, orderDate, UPC, unitSalePrice * quantity
        <span class="hljs-keyword">FROM</span> orderlines;</span></code></pre>

    <p>
    </p><table class="datatable"><caption>Order line subtotals</caption><thead><tr><th class="datatable" scope="col" id="1"></th><th class="datatable" scope="col" id="1"></th><th class="datatable" scope="col" id="1"></th><th class="datatable" scope="col" id="1"></th></tr></thead><tbody><tr><td class="datatable" headers="1">5678</td><td class="datatable" headers="1">2003-07-14</td><td class="datatable" headers="1">51820 33622</td><td class="datatable" headers="1">11.95</td></tr><tr><td class="datatable" headers="1">9012</td><td class="datatable" headers="1">2003-07-14</td><td class="datatable" headers="1">51820 33622</td><td class="datatable" headers="1">23.90</td></tr><tr><td class="datatable" headers="1">9012</td><td class="datatable" headers="1">2003-07-14</td><td class="datatable" headers="1">11373 24793</td><td class="datatable" headers="1">21.25</td></tr><tr><td class="datatable" headers="1">5678</td><td class="datatable" headers="1">2003-07-18</td><td class="datatable" headers="1">81809 73555</td><td class="datatable" headers="1">18.00</td></tr><tr><td class="datatable" headers="1">5678</td><td class="datatable" headers="1">2003-07-20</td><td class="datatable" headers="1">51820 33622</td><td class="datatable" headers="1">23.90</td></tr><tr><td class="datatable" headers="1">5678</td><td class="datatable" headers="1">2003-07-20</td><td class="datatable" headers="1">81809 73555</td><td class="datatable" headers="1">9.00</td></tr><tr><td class="datatable" headers="1">5678</td><td class="datatable" headers="1">2003-07-20</td><td class="datatable" headers="1">81810 63591</td><td class="datatable" headers="1">24.75</td></tr></tbody></table>    <p></p>

    <p>Computations are not limited just to column names; they may
       also include constants. For example, unitsaleprice * 1.06 might be used to
       find the sale price plus sales tax.</p>

    <p>Notice that the computation itself is shown as the heading
       for the computed column. This is awkward to read, and doesn’t really tell
       us what the column means. We can create our own column heading or alias using
       the <strong>AS</strong> keyword as shown below. (In fact, we could simply write the
       new name of the column without saying AS. Please don’t do this—it
       hurts readability of your code.) If you want your column alias to have
       spaces in it, you will have to enclose it in <i>double</i> quote marks. </p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">SELECT</span> custID, orderDate, UPC,
          unitSalePrice * quantity <span class="hljs-keyword">AS</span> subtotal
        <span class="hljs-keyword">FROM</span> orderlines;</span></code></pre>

    <p>
    </p><table class="datatable"><caption>Order line subtotals</caption><thead><tr><th class="datatable" scope="col" id="2"></th><th class="datatable" scope="col" id="2"></th><th class="datatable" scope="col" id="2"></th><th class="datatable" scope="col" id="2"></th></tr></thead><tbody><tr><td class="datatable" headers="2">5678</td><td class="datatable" headers="2">2003-07-14</td><td class="datatable" headers="2">51820 33622</td><td class="datatable" headers="2">11.95</td></tr><tr><td class="datatable" headers="2">9012</td><td class="datatable" headers="2">2003-07-14</td><td class="datatable" headers="2">51820 33622</td><td class="datatable" headers="2">23.90</td></tr><tr><td class="datatable" headers="2">9012</td><td class="datatable" headers="2">2003-07-14</td><td class="datatable" headers="2">11373 24793</td><td class="datatable" headers="2">21.25</td></tr><tr><td class="datatable" headers="2">5678</td><td class="datatable" headers="2">2003-07-18</td><td class="datatable" headers="2">81809 73555</td><td class="datatable" headers="2">18.00</td></tr><tr><td class="datatable" headers="2">5678</td><td class="datatable" headers="2">2003-07-20</td><td class="datatable" headers="2">51820 33622</td><td class="datatable" headers="2">23.90</td></tr><tr><td class="datatable" headers="2">5678</td><td class="datatable" headers="2">2003-07-20</td><td class="datatable" headers="2">81809 73555</td><td class="datatable" headers="2">9.00</td></tr><tr><td class="datatable" headers="2">5678</td><td class="datatable" headers="2">2003-07-20</td><td class="datatable" headers="2">81810 63591</td><td class="datatable" headers="2">24.75</td></tr></tbody></table>    <p></p>

<h2>Aggregate functions</h2>

    <p>SQL <strong>aggregate functions</strong> let us compute
       values based on multiple rows in our tables. They are also used as
       part of the SELECT clause, and also create new columns in the output.</p><p>

    </p><p><i>Example:</i> First, let’s just find the total amount
       of all our sales. To compute this, all we need is to do is to add up all of the
       price-times-quantity
       computations from every line of the OrderLines. We will use the <strong>SUM</strong>
       function to do the calculation. The output table, as you should expect, will
       contain only one row.</p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">SUM</span>(unitSalePrice * quantity) <span class="hljs-keyword">AS</span> totalsales
        <span class="hljs-keyword">FROM</span> orderlines;</span></code></pre>

    <p>
    </p><table class="datatable"><caption>Sales</caption><thead><tr><th class="datatable" scope="col" id="3"></th></tr></thead><tbody><tr><td class="datatable" headers="3">132.75</td></tr></tbody></table>    <p></p>

    <p>Next, we’ll compute the total for each order (the derived
       attribute shown in the UML Order class).
       We still need to add up order lines, but we need to group the totals for
       each order. We can do this with the <strong>GROUP BY</strong> clause. This time,
       the output will contain one row for every order, since the customerID and
       orderDate form the PK for <i>Orders</i>, not OrderLines. Notice that
       the SELECT clause and the GROUP BY clause contain exactly the same list of
       attributes, except for the calculation. In most cases, you will get an error
       message if you forget to do this.</p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">SELECT</span> custID, orderDate, <span class="hljs-keyword">SUM</span>(unitSalePrice * quantity) <span class="hljs-keyword">AS</span> total
        <span class="hljs-keyword">FROM</span> orderlines
        <span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> custID, orderDate;</span></code></pre>

    <p>
    </p><table class="datatable"><caption>Order totals</caption><thead><tr><th class="datatable" scope="col" id="4"></th><th class="datatable" scope="col" id="4"></th><th class="datatable" scope="col" id="4"></th></tr></thead><tbody><tr><td class="datatable" headers="4">5678</td><td class="datatable" headers="4">2003-07-14</td><td class="datatable" headers="4">11.95</td></tr><tr><td class="datatable" headers="4">9012</td><td class="datatable" headers="4">2003-07-14</td><td class="datatable" headers="4">45.15</td></tr><tr><td class="datatable" headers="4">5678</td><td class="datatable" headers="4">2003-07-18</td><td class="datatable" headers="4">18.00</td></tr><tr><td class="datatable" headers="4">5678</td><td class="datatable" headers="4">2003-07-20</td><td class="datatable" headers="4">57.65</td></tr></tbody></table>    <p></p>

    <p>Other frequently-used functions that work the same way as SUM
       include MIN (minimum value of those in the grouping), MAX (maximum value of those in
       the grouping, and AVG (average value of those in the grouping). </p>

    <p>The COUNT function
       is slightly different, since it returns the <i>number</i> of rows in a grouping. To
       count all rows, we can use the * (for example, to find out how many orders were placed).</p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">COUNT</span>(*)
        <span class="hljs-keyword">FROM</span> orders;</span></code></pre>

    <p>
    </p><table class="datatable"><caption>Orders</caption><thead><tr><th class="datatable" scope="col" id="5"></th></tr></thead><tbody><tr><td class="datatable" headers="5">4</td></tr></tbody></table>    <p></p>

    <p>We can also count groups of rows with identical values in a column. In
       this case, COUNT will ignore NULL values in the column. Here, we’ll find out
       how many times each product has been ordered.</p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">SELECT</span> prodname <span class="hljs-keyword">AS</span> <span class="hljs-string">"product name"</span>,
           <span class="hljs-keyword">COUNT</span>(prodname) <span class="hljs-keyword">AS</span> <span class="hljs-string">"times ordered"</span>
        <span class="hljs-keyword">FROM</span> products <span class="hljs-keyword">NATURAL</span> <span class="hljs-keyword">JOIN</span> orderlines
        <span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> prodname;</span></code></pre>

    <p>
    </p><table class="datatable"><caption>Product orders</caption><thead><tr><th class="datatable" scope="col" id="6"></th><th class="datatable" scope="col" id="6"></th></tr></thead><tbody><tr><td class="datatable" headers="6">Hammer, framing, 20 oz.</td><td class="datatable" headers="6">3</td></tr><tr><td class="datatable" headers="6">Saw, crosscut, 10 tpi</td><td class="datatable" headers="6">1</td></tr><tr><td class="datatable" headers="6">Screwdriver, Phillips #2, 6 inch</td><td class="datatable" headers="6">2</td></tr><tr><td class="datatable" headers="6">Pliers, needle-nose, 4 inch</td><td class="datatable" headers="6">1</td></tr></tbody></table>    <p></p>

    <p>A WHERE clause can be used as usual before the GROUP BY, to eliminate
      rows before the group function is executed. However, if we want to select output rows
      based on the results of the group function, the <strong>HAVING</strong> clause is used
      instead. For example, we could ask for only those products that have been sold
      more than once:</p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">SELECT</span> prodname <span class="hljs-keyword">AS</span> <span class="hljs-string">"product name"</span>,
           <span class="hljs-keyword">COUNT</span>(prodname) <span class="hljs-keyword">AS</span> <span class="hljs-string">"times ordered"</span>
        <span class="hljs-keyword">FROM</span> products <span class="hljs-keyword">NATURAL</span> <span class="hljs-keyword">JOIN</span> orderlines
        <span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> prodname
        <span class="hljs-keyword">HAVING</span> <span class="hljs-keyword">COUNT</span>(prodname) &gt; <span class="hljs-number">1</span>;</span></code></pre>


<h2>Other functions</h2>

    <p>Most database systems offer a wide variety of functions that deal with
       formatting and other miscellaneous tasks. These functions tend to be proprietary,
       differing widely from system to system in both availability and syntax. Most are used
       in the SELECT clause, although some might appear in a WHERE clause expression or
       an INSERT or UPDATE statement. Typical
       functions include:</p>

    <p></p><li>Functions for rounding, truncating, converting, and formatting
       numeric data types.<p></p>

    <p></p></li><li>Functions for concatenating, altering case, and manipulating
       character data types.<p></p>

    <p></p></li><li>Functions for formatting dates and times, or retrieving the
       date and time from the operating system. <p></p>

    <p></p></li><li>Functions for converting data types such as date or numeric to
       character string, and vice-versa. <p></p>

    <p></p></li><li>Functions for supplying visible values to null attributes,
       allowing conditional output, and other miscellaneous tasks.<p></p>
<h1>SQL technique: subqueries</h1>

    <p>Sometimes you don’t have enough information available when
       you design a query to determine which rows you want. In this case, you’ll have
       to find the required information with a <strong>subquery</strong>.</p>

    <p><i>Example:</i> Find the name of customers who live in the same
       zip code area as Wayne Dick. We might start writing this query as we would any
       of the ones that we have already done:</p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">SELECT</span> cFirstName, cLastName
        <span class="hljs-keyword">FROM</span> customers
        <span class="hljs-keyword">WHERE</span> cZipCode = ???</span></code></pre>

    <p></p><li>Oops! We don’t know what zip code to put in the
       WHERE clause. No, we can’t look it up manually and type it into the
       query—we have to find the answer based only on the information that
       we have been given!<p></p>

    <p></p></li><li>Fortunately, we also know how to find the right zip code by
       writing another query:<p></p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">SELECT</span> cZipCode
        <span class="hljs-keyword">FROM</span> Customers
        <span class="hljs-keyword">WHERE</span> cFirstName = <span class="hljs-string">'Wayne'</span> <span class="hljs-keyword">AND</span> cLastName = <span class="hljs-string">'Dick'</span>;</span></code></pre>

    <p>
    </p><table class="datatable"><caption>Zip code</caption><thead><tr><th class="datatable" scope="col" id="1"></th></tr></thead><tbody><tr><td class="datatable" headers="1">90840</td></tr></tbody></table>    <p></p>

    <p></p></li><li>Notice that this query returns a single column and a single
       row. We can use the result as the condition value for cZipCode in our
       original query. In effect, the output of the second query becomes input to the
       first one, which we can illustrate with their relation schemes:<p></p>

    <p>
       <img src="img/subqueries-customers.gif" width="378" height="138" alt="Customer subquery attributes" title="Customer subquery attributes"></p>

    <p></p></li><li>Syntactically, all we have to do is to enclose the subquery
       in parenthses, in the same place where we would normally use a constant in the
       WHERE clause. We’ll include the zip code in the SELECT line to verify
       that the answer is what we want:<p></p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">SELECT</span> cFirstName, cLastName, cZipCode
        <span class="hljs-keyword">FROM</span> customers
        <span class="hljs-keyword">WHERE</span> cZipCode =
          (<span class="hljs-keyword">SELECT</span> cZipCode
           <span class="hljs-keyword">FROM</span> customers
           <span class="hljs-keyword">WHERE</span> cFirstName = <span class="hljs-string">'Wayne'</span> <span class="hljs-keyword">AND</span> cLastName = <span class="hljs-string">'Dick'</span>);</span></code></pre>

    <p>
    </p><table class="datatable"><caption>Customers</caption><thead><tr><th class="datatable" scope="col" id="2"></th><th class="datatable" scope="col" id="2"></th><th class="datatable" scope="col" id="2"></th></tr></thead><tbody><tr><td class="datatable" headers="2">Alvaro</td><td class="datatable" headers="2">Monge</td><td class="datatable" headers="2">90840</td></tr><tr><td class="datatable" headers="2">Wayne</td><td class="datatable" headers="2">Dick</td><td class="datatable" headers="2">90840</td></tr></tbody></table>    <p></p>

    <p>A subquery that returns only one column and one row can be used
       any time that we need a single value. Another example would be to find
       the product name and sale price of all products whose unit sale price is greater
       than the average of all products. We can see that the DISTINCT keyword is
       needed, since the SELECT attributes are not a super key of the result set:</p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">DISTINCT</span> prodName, unitSalePrice
        <span class="hljs-keyword">FROM</span> Products <span class="hljs-keyword">NATURAL</span> <span class="hljs-keyword">JOIN</span> OrderLines
        <span class="hljs-keyword">WHERE</span> unitSalePrice &gt; </span><i><span class="hljs-operator">the average unit sale price</span></i></code></pre>

    <p></p></li><li>Again, we already know how to write another query that finds the average:<p></p>
<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">AVG</span>(unitSalePrice)
        <span class="hljs-keyword">FROM</span> OrderLines;</span></code></pre>

    <p>
    </p><table class="datatable"><caption>Average</caption><thead><tr><th class="datatable" scope="col" id="3"></th></tr></thead><tbody><tr><td class="datatable" headers="3">10.621428</td></tr></tbody></table>    <p></p>

    <p></p></li><li>We can visualize the combined queries with their relation schemes,
       and write the full syntax as before:<p></p>

    <p>
       <img src="img/subqueries-products.gif" width="444" height="208" alt="Products subquery attributes" title="Products subquery attributes"></p>

<pre><code class="hljs sql">        <span class="hljs-operator"><span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">DISTINCT</span> prodName, unitSalePrice
        <span class="hljs-keyword">FROM</span> Products <span class="hljs-keyword">NATURAL</span> <span class="hljs-keyword">JOIN</span> OrderLines
        <span class="hljs-keyword">WHERE</span> unitSalePrice &gt;
          (<span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">AVG</span>(unitSalePrice)
           <span class="hljs-keyword">FROM</span> OrderLines);</span></code></pre>

    <p>
    </p><table class="datatable"><caption>Above average</caption><thead><tr><th class="datatable" scope="col" id="4"></th><th class="datatable" scope="col" id="4"></th></tr></thead><tbody><tr><td class="datatable" headers="4">Hammer, framing, 20 oz.</td><td class="datatable" headers="4">11.95</td></tr><tr><td class="datatable" headers="4">Saw, crosscut, 10 tpi</td><td class="datatable" headers="4">21.25</td></tr></tbody></table>    <p></p>

    <p>Subqueries can also be used when we need more than a single value as
       part of a larger query. We’ll see examples of these in later pages.</p>
