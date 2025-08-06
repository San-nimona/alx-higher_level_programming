
<html>
<head>
	
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
	<link rel="icon" type="image/png" href="/favicon.png">
	<link href="/bundles/css?v=-E9m2V9yaCnYeWflOp9tBE0badlq1C9_T3efYqziH0w1" rel="stylesheet"/>

			<!-- Global site tag (gtag.js) - Google Analytics -->
		<script async src="https://www.googletagmanager.com/gtag/js?id=G-J2G5FTJNXP"></script>
		<script>
			window.dataLayer = window.dataLayer || [];
			function gtag() { dataLayer.push(arguments); }
			gtag('js', new Date());

			gtag('config', 'G-J2G5FTJNXP');
		</script>
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<title>Getting and setting content [text(), html() and val()] - The complete jQuery tutorial</title>
				<meta name="Keywords" content="text, innertext, html, innerhtml, val, value">
				<meta name="Description" content="A chapter on getting and setting text, HTML and values from HTML elements using jQuery.">
	<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1132262176862667" crossorigin="anonymous"></script>

	<script async src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"></script>

	

	


	
	<script>
		window.googletag = window.googletag || { cmd: [] };
		googletag.cmd.push(function()
		{
			var interstitialSlot = googletag.defineOutOfPageSlot('/21849154601,50763894/Ad.Plus-Interstitial', googletag.enums.OutOfPageFormat.INTERSTITIAL);
			if(interstitialSlot) interstitialSlot.addService(googletag.pubads());
			googletag.pubads().enableSingleRequest();
			googletag.enableServices(); googletag.display(interstitialSlot);
		});</script>



</head>

<body class="ltr">
	<div id="page">
			<div id="page-top-ad">

				
<div id="728x90-1">
	<script>
		window.googletag = window.googletag || { cmd: [] }; googletag.cmd.push(function()
		{
			googletag.defineSlot('/21849154601,50763894/Ad.Plus-728x90', [728, 90], '728x90-1').addService(googletag.pubads());
			googletag.enableServices(); googletag.display('728x90-1');
		});</script>
</div>
			</div>
		<div id="top" class="clearfix">
			
			<div id="top-logo">
				<a href="/"><i class="fa fa-graduation-cap logo"></i></a>

				<div id="site-title"><a href="/">jQuery Tutorial</a></div>
			</div>
			<a id="lnkToc" href="#sidr-main">TOC<i class="fa fa-bars"></i> </a>
		</div>
		<div id="content-container" class="clearfix">
			<aside id="sidebar">
				<div id="divSidrTop">
					Table of Contents
					<a href="javascript:void(0);" onclick="$.sidr('close', 'sidr-toc');" style="float: right;"><i class="fa fa-times"></i></a>
				</div>
				<nav id="toc">
					

					

			<div class="chapter" id="child-toc">
				<h3>Chapter/article TOC</h3>
				<ol>
						<li>
							<a href="/dom-manipulation/introduction/">
								Introduction to DOM manipulation
							</a>
						</li>
						<li class="selected">
							<a href="/dom-manipulation/getting-and-setting-content/">
								Getting and setting content [text(), html() and val()]
							</a>
						</li>
						<li>
							<a href="/dom-manipulation/getting-and-setting-attributes/">
								Getting and setting attributes [attr()]
							</a>
						</li>
						<li>
							<a href="/dom-manipulation/getting-and-setting-css-classes/">
								Getting and setting CSS classes
							</a>
						</li>
						<li>
							<a href="/dom-manipulation/the-append-and-prepend-methods/">
								The append() and prepend() methods
							</a>
						</li>
						<li>
							<a href="/dom-manipulation/the-before-and-after-methods/">
								The before() and after() methods
							</a>
						</li>
						<li>
							<a href="/dom-manipulation/the-remove-and-empty-methods/">
								The remove() and empty() methods
							</a>
						</li>
				</ol>
			</div>
			<div class="ad">
				
	<!-- jquery-tutorial.net menu -->
	<ins class="adsbygoogle"
		 style="display:inline-block;width:300px;height:250px"
		 data-ad-client="ca-pub-1132262176862667"
		 data-ad-slot="5679516320"></ins>


			</div>
		<div class="chapter">
			<h3>
				
				Introduction
			</h3>
			<ul>
					<li>
						<a href="/introduction/what-is-jquery/">
							What is jQuery?
						</a>

					</li>
					<li>
						<a href="/introduction/jquery-editor/">
							A jQuery editor
						</a>

					</li>
					<li>
						<a href="/introduction/getting-started/">
							Getting started
						</a>

					</li>
					<li>
						<a href="/introduction/hello-world/">
							Hello, world!
						</a>

					</li>
					<li>
						<a href="/introduction/the-ready-event/">
							The ready event
						</a>

					</li>
					<li>
						<a href="/introduction/method-chaining/">
							Method chaining
						</a>

					</li>
			</ul>
		</div>
		<div class="chapter">
			<h3>
				
				Selectors
			</h3>
			<ul>
					<li>
						<a href="/selectors/introduction/">
							Introduction to jQuery selectors
						</a>

					</li>
					<li>
						<a href="/selectors/using-elements-ids-and-classes/">
							Using elements, ID&#39;s and classes
						</a>

					</li>
					<li>
						<a href="/selectors/using-attributes/">
							Using attributes
						</a>

					</li>
					<li>
						<a href="/selectors/using-parent-child-relation-selectors/">
							Parent/child relation selectors
						</a>

					</li>
			</ul>
		</div>
		<div class="chapter">
			<h3>
				
				Effects
			</h3>
			<ul>
					<li>
						<a href="/effects/fading-elements/">
							Fading elements
						</a>

					</li>
					<li>
						<a href="/effects/sliding-elements/">
							Sliding elements
						</a>

					</li>
					<li>
						<a href="/effects/custom-animations-with-the-animate-method/">
							Custom animations with the animate() method
						</a>

					</li>
					<li>
						<a href="/effects/stopping-animations-with-the-stop-method/">
							Stopping animations with the stop() method
						</a>

					</li>
			</ul>
		</div>
			<div class="ad">
				
<div id="300x600-1">
	<script>window.googletag = window.googletag || { cmd: [] }; googletag.cmd.push(function() { googletag.defineSlot('/21849154601,50763894/Ad.Plus-300x600', [300, 600], '300x600-1').addService(googletag.pubads()); googletag.enableServices(); googletag.display('300x600-1'); });</script>
</div>
			</div>
		<div class="chapter">
			<h3>
				
				DOM manipulation
			</h3>
			<ul>
					<li>
						<a href="/dom-manipulation/introduction/">
							Introduction to DOM manipulation
						</a>

					</li>
					<li class="selected">
						<a href="/dom-manipulation/getting-and-setting-content/">
							Getting and setting content [text(), html() and val()]
						</a>

					</li>
					<li>
						<a href="/dom-manipulation/getting-and-setting-attributes/">
							Getting and setting attributes [attr()]
						</a>

					</li>
					<li>
						<a href="/dom-manipulation/getting-and-setting-css-classes/">
							Getting and setting CSS classes
						</a>

					</li>
					<li>
						<a href="/dom-manipulation/the-append-and-prepend-methods/">
							The append() and prepend() methods
						</a>

					</li>
					<li>
						<a href="/dom-manipulation/the-before-and-after-methods/">
							The before() and after() methods
						</a>

					</li>
					<li>
						<a href="/dom-manipulation/the-remove-and-empty-methods/">
							The remove() and empty() methods
						</a>

					</li>
			</ul>
		</div>
		<div class="chapter">
			<h3>
				
				Events
			</h3>
			<ul>
					<li>
						<a href="/events/introduction/">
							Introduction to events
						</a>

					</li>
					<li>
						<a href="/events/the-bind-method/">
							The bind() method
						</a>

					</li>
					<li>
						<a href="/events/the-unbind-method/">
							The unbind() method
						</a>

					</li>
					<li>
						<a href="/events/the-live-method/">
							The live() method
						</a>

					</li>
			</ul>
		</div>
		<div class="chapter">
			<h3>
				
				AJAX
			</h3>
			<ul>
					<li>
						<a href="/ajax/introduction/">
							Introduction to AJAX
						</a>

					</li>
					<li>
						<a href="/ajax/the-load-method/">
							The load() method
						</a>

					</li>
					<li>
						<a href="/ajax/the-get-and-post-methods/">
							The get() and post() methods
						</a>

					</li>
					<li>
						<a href="/ajax/same-origin-policy/">
							Same Origin Policy
						</a>

					</li>
					<li>
						<a href="/ajax/requesting-a-file-from-a-different-domain-using-jsonp/">
							Requesting a file from a different domain using JSONP
						</a>

					</li>
					<li>
						<a href="/ajax/showing-progress/">
							Showing progress
						</a>

					</li>
					<li>
						<a href="/ajax/aborting-an-ajax-request/">
							Aborting an AJAX request
						</a>

					</li>
			</ul>
		</div>
			<div class="ad">
				
<div id="300x250-1">
	<script>window.googletag = window.googletag || { cmd: [] }; googletag.cmd.push(function() { googletag.defineSlot('/21849154601,50763894/Ad.Plus-300x250', [300, 250], '300x250-1').addService(googletag.pubads()); googletag.enableServices(); googletag.display('300x250-1'); });</script>
</div>
			</div>
		<div class="chapter">
			<h3>
				
				Working with dimensions
			</h3>
			<ul>
					<li>
						<a href="/dimensions/working-with-widths-and-heights/">
							Working with widths and heights
						</a>

					</li>
			</ul>
		</div>
		<div class="chapter">
			<h3>
				
				Utilities &amp; Helpers
			</h3>
			<ul>
					<li>
						<a href="/utilities-helpers/looping-with-the-each-method/">
							Looping with the each() method
						</a>

					</li>
					<li>
						<a href="/utilities-helpers/the-toarray-and-makearray-methods/">
							The toArray() and makeArray() methods
						</a>

					</li>
			</ul>
		</div>
		<div class="chapter">
			<h3>
				
				Misc
			</h3>
			<ul>
					<li>
						<a href="/misc/other-frameworks-and-the-no-conflict-method/">
							Other frameworks and the noConflict() method
						</a>

					</li>
			</ul>
		</div>

				</nav>
			</aside>
			<div id="content">
					<ul class="nav nav-pills nav-fill" id="top-menu">
						<li class="nav-item" title="Login">
							<a href="#" onclick="LoginOrOut(false);">
								<i class="fa fa-user"></i>
							</a>
						</li>
							<li class="nav-item current">
								<a href="/">
									jQuery
								</a>
							</li>
													<li class="nav-item">
								<a href="http://asp.mvc-tutorial.com/" title="The ASP.NET Core MVC Tutorial">
									ASP.NET MVC
								</a>
							</li>
							<li class="nav-item">
								<a href="http://asp.net-tutorials.com/" title="The complete ASP.NET WebForms tutorial">
									ASP.NET WebForms
								</a>
							</li>
							<li class="nav-item">
								<a href="http://csharp.net-tutorials.com/" title="The complete C# tutorial">
									C#
								</a>
							</li>
							<li class="nav-item">
								<a href="http://css3-tutorial.net/" title="The complete CSS3 tutorial">
									CSS3 
								</a>
							</li>
							<li class="nav-item">
								<a href="http://html5-tutorial.net/" title="The complete HTML5 tutorial">
									HTML5
								</a>
							</li>
							<li class="nav-item">
								<a href="http://javascript-tutorial.com/" title="The complete JavaScript Tutorial">
									JavaScript
								</a>
							</li>
							<li class="nav-item">
								<a href="http://php5-tutorial.com/" title="The complete PHP tutorial">
									PHP5
								</a>
							</li>
							<li class="nav-item">
								<a href="http://wpf-tutorial.com/" title="The complete WPF tutorial">
									WPF
								</a>
							</li>
					</ul>
					<div id="user-bar" data-is-logged-in="0">

					</div>
				<article>
							<div class="alert" style="background-color: #eee;" data-nosnippet>
			<i>
				<span>
					<b>Need to learn JavaScript?</b>
					jQuery is a JavaScript framework, so if you don't already know about the JavaScript programming language, we recommend that you learn it now:
				</span>
				<b><a href="https://javascript-tutorial.com/" target="_blank">Learn JavaScript</a></b>
			</i>
		</div>
		<div id="chapter-title">DOM manipulation:</div>
<h1 id="aelm0" data-element-id="0">Getting and setting content [text(), html() and val()]</h1><p id="aelm2904" data-element-id="2904">The simplest aspect of DOM manipulation is retrieving and setting text, values and HTML. These three things might seem like the same thing, but they're not. Text is a textual (no HTML) representation of the inner content for all regular elements, values are for form elements and HTML is the same as text, but including any markup.</p><p id="aelm2905" data-element-id="2905">Fortunately for us, jQuery comes with a method for each of the three, allowing us to both retrieve and set these properties: The text(), html() and val() methods. Here's a little example which will show you the difference between them and how simple they are to use:</p><script async src="https://cdn.ad.plus/player/adplus.js"></script>
<script data-playerPro="current">(function() { var s = document.querySelector('script[data-playerPro="current"]'); s.removeAttribute("data-playerPro"); (playerPro = window.playerPro || []).push({ id: "z2I717k6zq5b", after: s, appParams: { "C_NETWORK_CODE": "50763894", "C_WEBSITE": "net-tutorials.com" } }); })();</script>



<pre id="aelm2906" data-element-id="2906"><code>&lt;div id="divTest"&gt;
	&lt;b&gt;Test&lt;/b&gt;
	&lt;input type="text" id="txtTest" name="txtTest" value="Input field" /&gt;
&lt;/div&gt;

&lt;script type="text/javascript"&gt;
$(function()
{
	alert("Text: " + $("#divTest").text());
	alert("HTML: " + $("#divTest").html());
	alert("Value: " + $("#divTest").val());
	
	alert("Text: " + $("#txtTest").text());
	alert("HTML: " + $("#txtTest").html());
	alert("Value: " + $("#txtTest").val());
});
&lt;/script&gt;</code></pre><p id="aelm2907" data-element-id="2907">So a call to one of these methods with no parameters will simply return the desired property. If we want to set the property instead, we simply specify an extra parameter. Here's a complete example:</p><pre id="aelm2908" data-element-id="2908"><code>&lt;div id="divText"&gt;&lt;/div&gt;
&lt;div id="divHtml"&gt;&lt;/div&gt;
&lt;input type="text" id="txtTest" name="txtTest" value="Input field" /&gt;

&lt;script type="text/javascript"&gt;
$(function()
{
	$("#divText").text("A dynamically set text");
	$("#divHtml").html("&lt;b&gt;&lt;i&gt;A dynamically set HTML string&lt;/i&gt;&lt;/b&gt;");
	$("#txtTest").val("A dynamically set value");
});
&lt;/script&gt;</code></pre><p id="aelm2909" data-element-id="2909">And that's how easy it is to set text, HTML and values.</p>			<input type="hidden" name="IL_IN_ARTICLE">
<p id="aelm2910" data-element-id="2910">These three functions comes with one overload more though, where you specify a callback function as the first and only parameter. This callback function will be called with two parameters by jQuery, the index of the current element in the list of elements selected, as well as the existing value, before it's replaced with a new value. You then return the string that you wish to use as the new value from the function. This overload works for both html(), text() and val(), but for the sake of simplicity, we only use the text() version in this example:</p><pre id="aelm2911" data-element-id="2911"><code>&lt;p&gt;Paragraph 1&lt;/p&gt;
&lt;p&gt;Paragraph 2&lt;/p&gt;
&lt;p&gt;Paragraph 3&lt;/p&gt;

&lt;script type="text/javascript"&gt;
$(function()
{
	$("p").text(function(index, oldText) {
		return "Existing text: " + oldText + ". New text: A dynamically set text (#" + index + ")";
	});
});
&lt;/script&gt;</code></pre><p id="aelm2912" data-element-id="2912">We start out with three similar paragraph elements, which text is their only difference. In the jQuery code, we select all of them and then use the special version of the text() method to replace their current text with a newly constructed text, based on the two parameters that jQuery provides for us: The index of the current element as well as its current text. This new text is then returned to jQuery, which will replace the current text with the new one.</p>		<div id="bottom-ad">
			
		</div>
	<hr />
	<div id="bottom-navigation" class="row">
		<div class="col-6">
				<a href="/dom-manipulation/introduction/" class="article-navigation" title="Introduction to DOM manipulation">
					<span class="title">
						Introduction to DOM manipulation
					</span>
					<span class="nav">
						<span class="fa-duotone fa-angles-left icon"></span>
						Previous
					</span>

				</a>
		</div>
		<div class="col-6">
				<a href="/dom-manipulation/getting-and-setting-attributes/" class="article-navigation right" title="Getting and setting attributes [attr()]">
					<span class="title">
						Getting and setting attributes [attr()]
					</span>
					<span class="nav">

						Next
						<span class="fa-duotone fa-angles-right icon"></span>
					</span>

				</a>
		</div>
	</div>
		<div class="alert" style="background-color: #eee;" id="divArticleAvailableLanguages">
			This article has been fully translated into the following languages:
			<div class="row">
				<ul class="column-list">
						<li class="col-lg-3 col-sm-4 col-6 available-lang-ru">
							

							<a href="/ru/213/манипуляции-с-dom/получение-и-изменение-контента-text-html-and-val/" style="font-weight: normal;">
								Russian
							</a>
						</li>
				</ul>
			</div>
			Is your preferred language not on the list? <a href="javascript:void(0);" onclick="SelectLanguage();">Click here</a> to help us translate this article into your language!
		</div>
	<script type="text/javascript">
		
		var Article = {"Id":213,"LocalizationLanguage":null,"ArticleUrl":"/dom-manipulation/getting-and-setting-content/","IsLocalizable":true,"FullyLocalizedLanguages":["ru"]};
	</script>
		<div class="ad">
			
<div id="Native-MultiPlex">
	<script>
    window.googletag = window.googletag || {cmd: []};
    googletag.cmd.push(function() {
    googletag.defineSlot('/21849154601,50763894/Ad.Plus-MultiPlex', ['fluid'], 'Native-MultiPlex').addService(googletag.pubads());
    googletag.enableServices();
    googletag.display('Native-MultiPlex');
    }); </script>
</div>
		</div>


				</article>
				<footer>
					<p>
						&copy; jquery-tutorial.net 2007-2025
					</p>
					<ul>
						<li>
							<a href="#" class="contact-link">Contact Us</a>
						</li>
							<li>
								<a href="javascript:void(0);" onclick="ShowSuggestCorrectionInfo();">Suggest Correction</a>
							</li>
						<li>
							<a href="/Localization/">Localization</a>
						</li>

					</ul>
				</footer>
			</div>
		</div>
	</div>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>


	

	<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>

	
	
	<script src="https://kit.fontawesome.com/9d896c23a3.js" crossorigin="anonymous"></script>

	<script src="/bundles/js?v=k-E4Kdifsr_qtXoXgPNJU18UpdH04gAr0yLM0F3txQk1"></script>

	<script type="text/javascript" src="/Content/Localizy.ashx"></script>

		<script type="text/javascript" src="/Content/Local/5.js"></script>



	<script type="text/javascript">
		User.Id = 0;
	</script>

	

	

			<script type="text/javascript">
			jQuery(document).ready(function($)
			{
				$('ins.adsbygoogle').each(function()
				{
					(adsbygoogle = window.adsbygoogle || []).push({});
				});
			});
		</script>



</body>
</html>
