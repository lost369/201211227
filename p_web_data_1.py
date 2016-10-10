{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import urllib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "response = urllib.urlopen('http://python.org/')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<addinfourl at 65133256L whose fp = <socket._fileobject object at 0x0000000003DEE750>>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "_html=response.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "p=re.compile('href=\"(http://.*?)\"')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "res=p.findall(_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://www.ie6countdown.com/\n",
      "http://browsehappy.com/\n",
      "http://www.google.com/chromeframe/?redirect=true\n",
      "http://plus.google.com/+Python\n",
      "http://www.facebook.com/pythonlang?fref=ts\n",
      "http://twitter.com/ThePSF\n",
      "http://brochure.getpython.info/\n",
      "http://wiki.python.org/moin/Languages\n",
      "http://python.org/dev/peps/\n",
      "http://planetpython.org/\n",
      "http://pyfound.blogspot.com/\n",
      "http://pycon.blogspot.com/\n",
      "http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator\n",
      "http://blog.python.org\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/6vXS6z9YHg0/python-360-beta-1-is-now-available.html\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/ukG8L0FEq2Q/python-360-alpha-4-preview-release-is.html\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/6i6vUY_x_SE/python-360-alpha-3-preview-release-is.html\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/1zUlkKxW27U/python-2712-released.html\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/gCTfatUv_t4/python-352-and-python-345-are-now.html\n",
      "http://www.djangoproject.com/\n",
      "http://www.pylonsproject.org/\n",
      "http://bottlepy.org\n",
      "http://tornadoweb.org\n",
      "http://flask.pocoo.org/\n",
      "http://www.web2py.com/\n",
      "http://www.wxpython.org/\n",
      "http://wiki.python.org/moin/TkInter\n",
      "http://www.pygtk.org\n",
      "http://www.riverbankcomputing.co.uk/software/pyqt/intro\n",
      "http://www.scipy.org\n",
      "http://pandas.pydata.org/\n",
      "http://ipython.org\n",
      "http://buildbot.net/\n",
      "http://trac.edgewall.org/\n",
      "http://roundup.sourceforge.net/\n",
      "http://www.ansible.com\n",
      "http://www.saltstack.com\n",
      "http://brochure.getpython.info/\n",
      "http://wiki.python.org/moin/Languages\n",
      "http://python.org/dev/peps/\n",
      "http://planetpython.org/\n",
      "http://pyfound.blogspot.com/\n",
      "http://pycon.blogspot.com/\n",
      "http://docs.python.org/devguide/\n",
      "http://bugs.python.org/\n",
      "http://pythonmentors.com/\n"
     ]
    }
   ],
   "source": [
    "for item in res:\n",
    "    print item"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "p=re.compile('<p>(.*?)</p>')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "res=p.findall(_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<strong>Notice:</strong> While Javascript is not essential for this website, your interaction with the content will be limited. Please turn Javascript on for the full experience. \n",
      "<strong>Notice:</strong> Your browser is <em>ancient</em> and <a href=\"http://www.ie6countdown.com/\">Microsoft agrees</a>. <a href=\"http://browsehappy.com/\">Upgrade to a different browser</a> or <a href=\"http://www.google.com/chromeframe/?redirect=true\">install Google Chrome Frame</a> to experience a better web.\n",
      "The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. <a href=\"//docs.python.org/3/tutorial/controlflow.html#defining-functions\">More about defining functions in Python&nbsp;3</a>\n",
      "Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. <a href=\"//docs.python.org/3/tutorial/introduction.html#lists\">More about lists in Python&nbsp;3</a>\n",
      "Calculations are simple with Python, and expression syntax is straightforward: the operators <code>+</code>, <code>-</code>, <code>*</code> and <code>/</code> work as expected; parentheses <code>()</code> can be used for grouping. <a href=\"http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator\">More about simple math functions in Python&nbsp;3</a>.\n",
      "Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. <a href=\"//docs.python.org/3/tutorial/\">Whet your appetite</a> with our Python&nbsp;3 overview.\n",
      "Python knows the usual control flow statements that other languages speak &mdash; <code>if</code>, <code>for</code>, <code>while</code> and <code>range</code> &mdash; with some of its own twists, of course. <a href=\"//docs.python.org/3/tutorial/controlflow.html\">More control flow tools in Python&nbsp;3</a>\n",
      "Python is a programming language that lets you work quickly <span class=\"breaker\"></span>and integrate systems more effectively. <a class=\"readmore\" href=\"/doc/\">Learn More</a>\n",
      "Whether you're new to programming or an experienced developer, it's easy to learn and use Python.\n",
      "<a href=\"/about/gettingstarted/\">Start with our Beginner&rsquo;s Guide</a>\n",
      "Python source code and installers are available for download for all versions! Not sure which version to use? <a href=\"https://wiki.python.org/moin/Python2orPython3\">Check here</a>.\n",
      "Latest: <a href=\"/downloads/release/python-352/\">Python 3.5.2</a> - <a href=\"/downloads/release/python-2712/\">Python 2.7.12</a>\n",
      "Documentation for Python's standard library, along with tutorials and guides, are available online.\n",
      "<a href=\"https://docs.python.org\">docs.python.org</a>\n",
      "Looking for work or have a Python related position that you're trying to hire for? Our <strong>relaunched community-run job board</strong> is the place to go.\n",
      "<a href=\"//jobs.python.org\">jobs.python.org</a>\n",
      "<a href=\"/success-stories/industrial-light-magic-runs-python/\">Industrial Light &amp; Magic Runs on Python</a> <em>by Tim Fortenberry</em>\n",
      "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. <a class=\"readmore\" href=\"/psf/\">Learn more</a> \n"
     ]
    }
   ],
   "source": [
    "for item in res:\n",
    "    print item"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from lxml import etree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "_htmlTree = etree.HTML(_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Element html at 0x3f78cc8>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "_htmlTree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "nodes = _htmlTree.xpath('//a[@href]')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<Element a at 0x3f73488>,\n",
       " <Element a at 0x3f734c8>,\n",
       " <Element a at 0x3f73588>,\n",
       " <Element a at 0x3f73608>,\n",
       " <Element a at 0x3f73548>,\n",
       " <Element a at 0x3f73508>,\n",
       " <Element a at 0x3f735c8>,\n",
       " <Element a at 0x3f73648>,\n",
       " <Element a at 0x3f73688>,\n",
       " <Element a at 0x3f736c8>,\n",
       " <Element a at 0x3f73708>,\n",
       " <Element a at 0x3f73748>,\n",
       " <Element a at 0x3f73788>,\n",
       " <Element a at 0x3f737c8>,\n",
       " <Element a at 0x3f73808>,\n",
       " <Element a at 0x3f73848>,\n",
       " <Element a at 0x3f73888>,\n",
       " <Element a at 0x3f738c8>,\n",
       " <Element a at 0x3f73908>,\n",
       " <Element a at 0x3f73948>,\n",
       " <Element a at 0x3f73988>,\n",
       " <Element a at 0x3f739c8>,\n",
       " <Element a at 0x3f73a08>,\n",
       " <Element a at 0x3f73a48>,\n",
       " <Element a at 0x3f73a88>,\n",
       " <Element a at 0x3f73ac8>,\n",
       " <Element a at 0x3f73b08>,\n",
       " <Element a at 0x3f73b48>,\n",
       " <Element a at 0x3f73b88>,\n",
       " <Element a at 0x3f73bc8>,\n",
       " <Element a at 0x3f73c08>,\n",
       " <Element a at 0x3f73c48>,\n",
       " <Element a at 0x3f73c88>,\n",
       " <Element a at 0x3f73cc8>,\n",
       " <Element a at 0x3f73d08>,\n",
       " <Element a at 0x3f73d48>,\n",
       " <Element a at 0x3f73d88>,\n",
       " <Element a at 0x3f73dc8>,\n",
       " <Element a at 0x3f73e08>,\n",
       " <Element a at 0x3f73e48>,\n",
       " <Element a at 0x3f73e88>,\n",
       " <Element a at 0x3f73ec8>,\n",
       " <Element a at 0x3f73f08>,\n",
       " <Element a at 0x3f73f48>,\n",
       " <Element a at 0x3f73f88>,\n",
       " <Element a at 0x3f73fc8>,\n",
       " <Element a at 0x3f74048>,\n",
       " <Element a at 0x3f74088>,\n",
       " <Element a at 0x3f740c8>,\n",
       " <Element a at 0x3f74108>,\n",
       " <Element a at 0x3f74148>,\n",
       " <Element a at 0x3f74188>,\n",
       " <Element a at 0x3f741c8>,\n",
       " <Element a at 0x3f74208>,\n",
       " <Element a at 0x3f74248>,\n",
       " <Element a at 0x3f74288>,\n",
       " <Element a at 0x3f742c8>,\n",
       " <Element a at 0x3f74308>,\n",
       " <Element a at 0x3f74348>,\n",
       " <Element a at 0x3f74388>,\n",
       " <Element a at 0x3f743c8>,\n",
       " <Element a at 0x3f74408>,\n",
       " <Element a at 0x3f74448>,\n",
       " <Element a at 0x3f74488>,\n",
       " <Element a at 0x3f744c8>,\n",
       " <Element a at 0x3f74508>,\n",
       " <Element a at 0x3f74548>,\n",
       " <Element a at 0x3f74588>,\n",
       " <Element a at 0x3f745c8>,\n",
       " <Element a at 0x3f74608>,\n",
       " <Element a at 0x3f74648>,\n",
       " <Element a at 0x3f74688>,\n",
       " <Element a at 0x3f746c8>,\n",
       " <Element a at 0x3f74708>,\n",
       " <Element a at 0x3f74748>,\n",
       " <Element a at 0x3f74788>,\n",
       " <Element a at 0x3f747c8>,\n",
       " <Element a at 0x3f74808>,\n",
       " <Element a at 0x3f74848>,\n",
       " <Element a at 0x3f74888>,\n",
       " <Element a at 0x3f748c8>,\n",
       " <Element a at 0x3f74908>,\n",
       " <Element a at 0x3f74948>,\n",
       " <Element a at 0x3f74988>,\n",
       " <Element a at 0x3f749c8>,\n",
       " <Element a at 0x3f74a08>,\n",
       " <Element a at 0x3f74a48>,\n",
       " <Element a at 0x3f74a88>,\n",
       " <Element a at 0x3f74ac8>,\n",
       " <Element a at 0x3f74b08>,\n",
       " <Element a at 0x3f74b48>,\n",
       " <Element a at 0x3f74b88>,\n",
       " <Element a at 0x3f74bc8>,\n",
       " <Element a at 0x3f74c08>,\n",
       " <Element a at 0x3f74c48>,\n",
       " <Element a at 0x3f74c88>,\n",
       " <Element a at 0x3f74cc8>,\n",
       " <Element a at 0x3f74d08>,\n",
       " <Element a at 0x3f74d48>,\n",
       " <Element a at 0x3f74d88>,\n",
       " <Element a at 0x3f74dc8>,\n",
       " <Element a at 0x3f74e08>,\n",
       " <Element a at 0x3f74e48>,\n",
       " <Element a at 0x3f74e88>,\n",
       " <Element a at 0x3f74ec8>,\n",
       " <Element a at 0x3f74f08>,\n",
       " <Element a at 0x3f74f48>,\n",
       " <Element a at 0x3f74f88>,\n",
       " <Element a at 0x3f74fc8>,\n",
       " <Element a at 0x3f75048>,\n",
       " <Element a at 0x3f75088>,\n",
       " <Element a at 0x3f750c8>,\n",
       " <Element a at 0x3f75108>,\n",
       " <Element a at 0x3f75148>,\n",
       " <Element a at 0x3f75188>,\n",
       " <Element a at 0x3f751c8>,\n",
       " <Element a at 0x3f75208>,\n",
       " <Element a at 0x3f75248>,\n",
       " <Element a at 0x3f75288>,\n",
       " <Element a at 0x3f752c8>,\n",
       " <Element a at 0x3f75308>,\n",
       " <Element a at 0x3f75348>,\n",
       " <Element a at 0x3f75388>,\n",
       " <Element a at 0x3f753c8>,\n",
       " <Element a at 0x3f75408>,\n",
       " <Element a at 0x3f75448>,\n",
       " <Element a at 0x3f75488>,\n",
       " <Element a at 0x3f754c8>,\n",
       " <Element a at 0x3f75508>,\n",
       " <Element a at 0x3f75548>,\n",
       " <Element a at 0x3f75588>,\n",
       " <Element a at 0x3f755c8>,\n",
       " <Element a at 0x3f75608>,\n",
       " <Element a at 0x3f75648>,\n",
       " <Element a at 0x3f75688>,\n",
       " <Element a at 0x3f756c8>,\n",
       " <Element a at 0x3f75708>,\n",
       " <Element a at 0x3f75748>,\n",
       " <Element a at 0x3f75788>,\n",
       " <Element a at 0x3f757c8>,\n",
       " <Element a at 0x3f75808>,\n",
       " <Element a at 0x3f75848>,\n",
       " <Element a at 0x3f75888>,\n",
       " <Element a at 0x3f758c8>,\n",
       " <Element a at 0x3f75908>,\n",
       " <Element a at 0x3f75948>,\n",
       " <Element a at 0x3f75988>,\n",
       " <Element a at 0x3f759c8>,\n",
       " <Element a at 0x3f75a08>,\n",
       " <Element a at 0x3f75a48>,\n",
       " <Element a at 0x3f75a88>,\n",
       " <Element a at 0x3f75ac8>,\n",
       " <Element a at 0x3f75b08>,\n",
       " <Element a at 0x3f75b48>,\n",
       " <Element a at 0x3f75b88>,\n",
       " <Element a at 0x3f75bc8>,\n",
       " <Element a at 0x3f75c08>,\n",
       " <Element a at 0x3f75c48>,\n",
       " <Element a at 0x3f75c88>,\n",
       " <Element a at 0x3f75cc8>,\n",
       " <Element a at 0x3f75d08>,\n",
       " <Element a at 0x3f75d48>,\n",
       " <Element a at 0x3f75d88>,\n",
       " <Element a at 0x3f75dc8>,\n",
       " <Element a at 0x3f75e08>,\n",
       " <Element a at 0x3f75e48>,\n",
       " <Element a at 0x3f75e88>,\n",
       " <Element a at 0x3f75ec8>,\n",
       " <Element a at 0x3f75f08>,\n",
       " <Element a at 0x3f75f48>,\n",
       " <Element a at 0x3f75f88>,\n",
       " <Element a at 0x3f75fc8>,\n",
       " <Element a at 0x3f76048>,\n",
       " <Element a at 0x3f76088>,\n",
       " <Element a at 0x3f760c8>,\n",
       " <Element a at 0x3f76108>,\n",
       " <Element a at 0x3f76148>,\n",
       " <Element a at 0x3f76188>,\n",
       " <Element a at 0x3f761c8>,\n",
       " <Element a at 0x3f76208>,\n",
       " <Element a at 0x3f76248>,\n",
       " <Element a at 0x3f76288>,\n",
       " <Element a at 0x3f762c8>,\n",
       " <Element a at 0x3f76308>,\n",
       " <Element a at 0x3f76348>,\n",
       " <Element a at 0x3f76388>,\n",
       " <Element a at 0x3f763c8>,\n",
       " <Element a at 0x3f76408>,\n",
       " <Element a at 0x3f76448>,\n",
       " <Element a at 0x3f76488>,\n",
       " <Element a at 0x3f764c8>,\n",
       " <Element a at 0x3f76508>,\n",
       " <Element a at 0x3f76548>,\n",
       " <Element a at 0x3f76588>,\n",
       " <Element a at 0x3f765c8>,\n",
       " <Element a at 0x3f76608>]"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nodes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'href': '#content', 'title': 'Skip to content'}\n",
      "{'href': '#python-network', 'aria-hidden': 'true', 'id': 'close-python-network', 'class': 'jump-link'}\n",
      "{'href': '/', 'class': 'current_item selectedcurrent_branch selected', 'title': 'The Python Programming Language'}\n",
      "{'href': '/psf-landing/', 'title': 'The Python Software Foundation'}\n",
      "{'href': 'https://docs.python.org', 'title': 'Python Documentation'}\n",
      "{'href': 'https://pypi.python.org/', 'title': 'Python Package Index'}\n",
      "{'href': '/jobs/', 'title': 'Python Job Board'}\n",
      "{'href': '/community/', 'title': 'Python Community'}\n",
      "{'href': '#top', 'aria-hidden': 'true', 'id': 'python-network', 'class': 'jump-link'}\n",
      "{'href': '/'}\n",
      "{'href': '#site-map', 'id': 'site-map-link', 'class': 'jump-to-menu'}\n",
      "{'href': '#', 'class': 'action-trigger'}\n",
      "{'href': 'javascript:;', 'class': 'text-shrink', 'title': 'Make Text Smaller'}\n",
      "{'href': 'javascript:;', 'class': 'text-grow', 'title': 'Make Text Larger'}\n",
      "{'href': 'javascript:;', 'class': 'text-reset', 'title': 'Reset any font size changes I have made'}\n",
      "{'href': '#', 'class': 'action-trigger'}\n",
      "{'href': 'http://plus.google.com/+Python'}\n",
      "{'href': 'http://www.facebook.com/pythonlang?fref=ts'}\n",
      "{'href': 'http://twitter.com/ThePSF'}\n",
      "{'href': '/community/irc/'}\n",
      "{'href': '/accounts/login/', 'title': 'Sign Up or Sign In to Python.org'}\n",
      "{'href': '/accounts/signup/'}\n",
      "{'href': '/accounts/login/'}\n",
      "{'href': '/about/', 'class': '', 'title': ''}\n",
      "{'href': '/about/apps/', 'title': ''}\n",
      "{'href': '/about/quotes/', 'title': ''}\n",
      "{'href': '/about/gettingstarted/', 'title': ''}\n",
      "{'href': '/about/help/', 'title': ''}\n",
      "{'href': 'http://brochure.getpython.info/', 'title': ''}\n",
      "{'href': '/downloads/', 'class': '', 'title': ''}\n",
      "{'href': '/downloads/', 'title': ''}\n",
      "{'href': '/downloads/source/', 'title': ''}\n",
      "{'href': '/downloads/windows/', 'title': ''}\n",
      "{'href': '/downloads/mac-osx/', 'title': ''}\n",
      "{'href': '/download/other/', 'title': ''}\n",
      "{'href': 'https://docs.python.org/3/license.html', 'title': ''}\n",
      "{'href': '/download/alternatives', 'title': ''}\n",
      "{'href': '/doc/', 'class': '', 'title': ''}\n",
      "{'href': '/doc/', 'title': ''}\n",
      "{'href': '/doc/av', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/BeginnersGuide', 'title': ''}\n",
      "{'href': 'https://docs.python.org/devguide/', 'title': ''}\n",
      "{'href': 'https://docs.python.org/faq/', 'title': ''}\n",
      "{'href': 'http://wiki.python.org/moin/Languages', 'title': ''}\n",
      "{'href': 'http://python.org/dev/peps/', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/PythonBooks', 'title': ''}\n",
      "{'href': '/community/', 'class': '', 'title': ''}\n",
      "{'href': '/community/diversity/', 'title': ''}\n",
      "{'href': '/community/irc/', 'title': ''}\n",
      "{'href': '/community/lists/', 'title': ''}\n",
      "{'href': '/community/workshops/', 'title': ''}\n",
      "{'href': '/community/sigs/', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/', 'title': ''}\n",
      "{'href': '/community/logos/', 'title': ''}\n",
      "{'href': '/community/merchandise/', 'title': ''}\n",
      "{'href': '/community/awards', 'title': ''}\n",
      "{'href': '/about/success/', 'class': '', 'title': 'success-stories'}\n",
      "{'href': '/about/success/#arts', 'title': ''}\n",
      "{'href': '/about/success/#business', 'title': ''}\n",
      "{'href': '/about/success/#education', 'title': ''}\n",
      "{'href': '/about/success/#engineering', 'title': ''}\n",
      "{'href': '/about/success/#government', 'title': ''}\n",
      "{'href': '/about/success/#scientific', 'title': ''}\n",
      "{'href': '/about/success/#software-development', 'title': ''}\n",
      "{'href': '/blogs/', 'class': '', 'title': 'News from around the Python world'}\n",
      "{'href': '/blogs/', 'title': 'Python Insider Blog Posts'}\n",
      "{'href': 'http://planetpython.org/', 'title': 'Planet Python'}\n",
      "{'href': 'http://pyfound.blogspot.com/', 'title': 'PSF Blog'}\n",
      "{'href': 'http://pycon.blogspot.com/', 'title': 'PyCon Blog'}\n",
      "{'href': '/events/', 'class': '', 'title': ''}\n",
      "{'href': '/events/python-events', 'title': ''}\n",
      "{'href': '/events/python-user-group/', 'title': ''}\n",
      "{'href': '/events/python-events/past/', 'title': ''}\n",
      "{'href': '/events/python-user-group/past/', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event', 'title': ''}\n",
      "{'href': '/shell/', 'data-shell-container': '#dive-into-python', 'class': 'button prompt', 'id': 'start-shell'}\n",
      "{'href': '//docs.python.org/3/tutorial/controlflow.html#defining-functions'}\n",
      "{'href': '//docs.python.org/3/tutorial/introduction.html#lists'}\n",
      "{'href': 'http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator'}\n",
      "{'href': '//docs.python.org/3/tutorial/'}\n",
      "{'href': '//docs.python.org/3/tutorial/controlflow.html'}\n",
      "{'href': '/doc/', 'class': 'readmore'}\n",
      "{'href': '/about/gettingstarted/'}\n",
      "{'href': 'https://wiki.python.org/moin/Python2orPython3'}\n",
      "{'href': '/downloads/release/python-352/'}\n",
      "{'href': '/downloads/release/python-2712/'}\n",
      "{'href': 'https://docs.python.org'}\n",
      "{'href': '//jobs.python.org'}\n",
      "{'href': 'http://blog.python.org', 'title': 'More News'}\n",
      "{'href': 'http://feedproxy.google.com/~r/PythonInsider/~3/6vXS6z9YHg0/python-360-beta-1-is-now-available.html'}\n",
      "{'href': 'http://feedproxy.google.com/~r/PythonInsider/~3/ukG8L0FEq2Q/python-360-alpha-4-preview-release-is.html'}\n",
      "{'href': 'http://feedproxy.google.com/~r/PythonInsider/~3/6i6vUY_x_SE/python-360-alpha-3-preview-release-is.html'}\n",
      "{'href': 'http://feedproxy.google.com/~r/PythonInsider/~3/1zUlkKxW27U/python-2712-released.html'}\n",
      "{'href': 'http://feedproxy.google.com/~r/PythonInsider/~3/gCTfatUv_t4/python-352-and-python-345-are-now.html'}\n",
      "{'href': '/events/calendars/', 'title': 'More Events'}\n",
      "{'href': '/events/python-events/459/'}\n",
      "{'href': '/events/python-events/446/'}\n",
      "{'href': '/events/python-user-group/454/'}\n",
      "{'href': '/events/python-events/449/'}\n",
      "{'href': '/events/python-events/417/'}\n",
      "{'href': '/success-stories/', 'title': 'More Success Stories'}\n",
      "{'href': '/success-stories/industrial-light-magic-runs-python/'}\n",
      "{'href': '/success-stories/industrial-light-magic-runs-python/'}\n",
      "{'href': '/about/apps', 'title': 'More Applications'}\n",
      "{'href': 'http://www.djangoproject.com/', 'class': 'tag'}\n",
      "{'href': 'http://www.pylonsproject.org/', 'class': 'tag'}\n",
      "{'href': 'http://bottlepy.org', 'class': 'tag'}\n",
      "{'href': 'http://tornadoweb.org', 'class': 'tag'}\n",
      "{'href': 'http://flask.pocoo.org/', 'class': 'tag'}\n",
      "{'href': 'http://www.web2py.com/', 'class': 'tag'}\n",
      "{'href': 'http://www.wxpython.org/', 'class': 'tag'}\n",
      "{'href': 'http://wiki.python.org/moin/TkInter', 'class': 'tag'}\n",
      "{'href': 'http://www.pygtk.org', 'class': 'tag'}\n",
      "{'href': 'https://wiki.gnome.org/Projects/PyGObject', 'class': 'tag'}\n",
      "{'href': 'http://www.riverbankcomputing.co.uk/software/pyqt/intro', 'class': 'tag'}\n",
      "{'href': 'http://www.scipy.org', 'class': 'tag'}\n",
      "{'href': 'http://pandas.pydata.org/', 'class': 'tag'}\n",
      "{'href': 'http://ipython.org', 'class': 'tag'}\n",
      "{'href': 'http://buildbot.net/', 'class': 'tag'}\n",
      "{'href': 'http://trac.edgewall.org/', 'class': 'tag'}\n",
      "{'href': 'http://roundup.sourceforge.net/', 'class': 'tag'}\n",
      "{'href': 'http://www.ansible.com', 'class': 'tag'}\n",
      "{'href': 'http://www.saltstack.com', 'class': 'tag'}\n",
      "{'href': 'https://www.openstack.org', 'class': 'tag'}\n",
      "{'href': '/dev/peps/'}\n",
      "{'href': '/dev/peps/peps.rss', 'class': 'rss-link', 'aria-hidden': 'true'}\n",
      "{'href': '/psf/'}\n",
      "{'href': '/psf/', 'class': 'readmore'}\n",
      "{'href': '/users/membership/', 'class': 'button'}\n",
      "{'href': '/psf/donations/', 'class': 'button'}\n",
      "{'href': '#python-network', 'id': 'back-to-top-1', 'class': 'jump-link'}\n",
      "{'href': '/about/'}\n",
      "{'href': '/about/apps/', 'title': ''}\n",
      "{'href': '/about/quotes/', 'title': ''}\n",
      "{'href': '/about/gettingstarted/', 'title': ''}\n",
      "{'href': '/about/help/', 'title': ''}\n",
      "{'href': 'http://brochure.getpython.info/', 'title': ''}\n",
      "{'href': '/downloads/'}\n",
      "{'href': '/downloads/', 'title': ''}\n",
      "{'href': '/downloads/source/', 'title': ''}\n",
      "{'href': '/downloads/windows/', 'title': ''}\n",
      "{'href': '/downloads/mac-osx/', 'title': ''}\n",
      "{'href': '/download/other/', 'title': ''}\n",
      "{'href': 'https://docs.python.org/3/license.html', 'title': ''}\n",
      "{'href': '/download/alternatives', 'title': ''}\n",
      "{'href': '/doc/'}\n",
      "{'href': '/doc/', 'title': ''}\n",
      "{'href': '/doc/av', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/BeginnersGuide', 'title': ''}\n",
      "{'href': 'https://docs.python.org/devguide/', 'title': ''}\n",
      "{'href': 'https://docs.python.org/faq/', 'title': ''}\n",
      "{'href': 'http://wiki.python.org/moin/Languages', 'title': ''}\n",
      "{'href': 'http://python.org/dev/peps/', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/PythonBooks', 'title': ''}\n",
      "{'href': '/community/'}\n",
      "{'href': '/community/diversity/', 'title': ''}\n",
      "{'href': '/community/irc/', 'title': ''}\n",
      "{'href': '/community/lists/', 'title': ''}\n",
      "{'href': '/community/workshops/', 'title': ''}\n",
      "{'href': '/community/sigs/', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/', 'title': ''}\n",
      "{'href': '/community/logos/', 'title': ''}\n",
      "{'href': '/community/merchandise/', 'title': ''}\n",
      "{'href': '/community/awards', 'title': ''}\n",
      "{'href': '/about/success/', 'title': 'success-stories'}\n",
      "{'href': '/about/success/#arts', 'title': ''}\n",
      "{'href': '/about/success/#business', 'title': ''}\n",
      "{'href': '/about/success/#education', 'title': ''}\n",
      "{'href': '/about/success/#engineering', 'title': ''}\n",
      "{'href': '/about/success/#government', 'title': ''}\n",
      "{'href': '/about/success/#scientific', 'title': ''}\n",
      "{'href': '/about/success/#software-development', 'title': ''}\n",
      "{'href': '/blogs/', 'title': 'News from around the Python world'}\n",
      "{'href': '/blogs/', 'title': 'Python Insider Blog Posts'}\n",
      "{'href': 'http://planetpython.org/', 'title': 'Planet Python'}\n",
      "{'href': 'http://pyfound.blogspot.com/', 'title': 'PSF Blog'}\n",
      "{'href': 'http://pycon.blogspot.com/', 'title': 'PyCon Blog'}\n",
      "{'href': '/events/'}\n",
      "{'href': '/events/python-events', 'title': ''}\n",
      "{'href': '/events/python-user-group/', 'title': ''}\n",
      "{'href': '/events/python-events/past/', 'title': ''}\n",
      "{'href': '/events/python-user-group/past/', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event', 'title': ''}\n",
      "{'href': '/dev/'}\n",
      "{'href': 'http://docs.python.org/devguide/', 'title': ''}\n",
      "{'href': 'http://bugs.python.org/', 'title': ''}\n",
      "{'href': 'https://mail.python.org/mailman/listinfo/python-dev', 'title': ''}\n",
      "{'href': 'http://pythonmentors.com/', 'title': ''}\n",
      "{'href': '#python-network', 'id': 'back-to-top-2', 'class': 'jump-link'}\n",
      "{'href': '/about/help/'}\n",
      "{'href': '/community/diversity/'}\n",
      "{'href': 'https://github.com/python/pythondotorg/issues'}\n",
      "{'href': 'https://status.python.org/'}\n",
      "{'href': '/psf-landing/'}\n",
      "{'href': '/about/legal/'}\n",
      "{'href': '/privacy/'}\n"
     ]
    }
   ],
   "source": [
    "for node in nodes:\n",
    "    print node.attrib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from lxml.cssselect import CSSSelector"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sel=CSSSelector('a[href]')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import lxml.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "html= lxml.html.fromstring(_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "results=sel(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "196\n"
     ]
    }
   ],
   "source": [
    "print len(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " #content Skip to content\n",
      "#python-network \n",
      "                    \n",
      "/ Python\n",
      "/psf-landing/ PSF\n",
      "https://docs.python.org Docs\n",
      "https://pypi.python.org/ PyPI\n",
      "/jobs/ Jobs\n",
      "/community/ Community\n",
      "#top \n",
      "                    \n",
      "/ None\n",
      "#site-map None\n",
      "# None\n",
      "javascript:; Smaller\n",
      "javascript:; Larger\n",
      "javascript:; Reset\n",
      "# Socialize\n",
      "http://plus.google.com/+Python None\n",
      "http://www.facebook.com/pythonlang?fref=ts None\n",
      "http://twitter.com/ThePSF None\n",
      "/community/irc/ None\n",
      "/accounts/login/ Sign In\n",
      "/accounts/signup/ Sign Up / Register\n",
      "/accounts/login/ Sign In\n",
      "/about/ About\n",
      "/about/apps/ Applications\n",
      "/about/quotes/ Quotes\n",
      "/about/gettingstarted/ Getting Started\n",
      "/about/help/ Help\n",
      "http://brochure.getpython.info/ Python Brochure\n",
      "/downloads/ Downloads\n",
      "/downloads/ All releases\n",
      "/downloads/source/ Source code\n",
      "/downloads/windows/ Windows\n",
      "/downloads/mac-osx/ Mac OS X\n",
      "/download/other/ Other Platforms\n",
      "https://docs.python.org/3/license.html License\n",
      "/download/alternatives Alternative Implementations\n",
      "/doc/ Documentation\n",
      "/doc/ Docs\n",
      "/doc/av Audio/Visual Talks\n",
      "https://wiki.python.org/moin/BeginnersGuide Beginner's Guide\n",
      "https://docs.python.org/devguide/ Developer's Guide\n",
      "https://docs.python.org/faq/ FAQ\n",
      "http://wiki.python.org/moin/Languages Non-English Docs\n",
      "http://python.org/dev/peps/ PEP Index\n",
      "https://wiki.python.org/moin/PythonBooks Python Books\n",
      "/community/ Community\n",
      "/community/diversity/ Diversity\n",
      "/community/irc/ IRC\n",
      "/community/lists/ Mailing Lists\n",
      "/community/workshops/ Python Conferences\n",
      "/community/sigs/ Special Interest Groups\n",
      "https://wiki.python.org/moin/ Python Wiki\n",
      "/community/logos/ Python Logo\n",
      "/community/merchandise/ Merchandise\n",
      "/community/awards Community Awards\n",
      "/about/success/ Success Stories\n",
      "/about/success/#arts Arts\n",
      "/about/success/#business Business\n",
      "/about/success/#education Education\n",
      "/about/success/#engineering Engineering\n",
      "/about/success/#government Government\n",
      "/about/success/#scientific Scientific\n",
      "/about/success/#software-development Software Development\n",
      "/blogs/ News\n",
      "/blogs/ Python News\n",
      "http://planetpython.org/ Community News\n",
      "http://pyfound.blogspot.com/ PSF News\n",
      "http://pycon.blogspot.com/ PyCon News\n",
      "/events/ Events\n",
      "/events/python-events Python Events\n",
      "/events/python-user-group/ User Group Events\n",
      "/events/python-events/past/ Python Events Archive\n",
      "/events/python-user-group/past/ User Group Events Archive\n",
      "https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event Submit an Event\n",
      "/shell/ >_\n",
      "                        \n",
      "//docs.python.org/3/tutorial/controlflow.html#defining-functions More about defining functions in Python 3\n",
      "//docs.python.org/3/tutorial/introduction.html#lists More about lists in Python 3\n",
      "http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator More about simple math functions in Python 3\n",
      "//docs.python.org/3/tutorial/ Whet your appetite\n",
      "//docs.python.org/3/tutorial/controlflow.html More control flow tools in Python 3\n",
      "/doc/ Learn More\n",
      "/about/gettingstarted/ Start with our Beginner’s Guide\n",
      "https://wiki.python.org/moin/Python2orPython3 Check here\n",
      "/downloads/release/python-352/ Python 3.5.2\n",
      "/downloads/release/python-2712/ Python 2.7.12\n",
      "https://docs.python.org docs.python.org\n",
      "//jobs.python.org jobs.python.org\n",
      "http://blog.python.org More\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/6vXS6z9YHg0/python-360-beta-1-is-now-available.html Python 3.6.0b1 is the first of four planned beta releases of ...\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/ukG8L0FEq2Q/python-360-alpha-4-preview-release-is.html Python 3.6.0a4 has been released.  3.6.0a4 is the last of four planned alpha ...\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/6i6vUY_x_SE/python-360-alpha-3-preview-release-is.html Python 3.6.0a3 has been released.  3.6.0a3 is the third of four planned alpha ...\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/1zUlkKxW27U/python-2712-released.html The Python 2.7.x series has a new bugfix release, Python ...\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/gCTfatUv_t4/python-352-and-python-345-are-now.html Python 3.5.2 and Python 3.4.5 are now available for download. ...\n",
      "/events/calendars/ More\n",
      "/events/python-events/459/ PyConChina 2016 (Shenzhen)\n",
      "/events/python-events/446/ Python San Sebastian 2016\n",
      "/events/python-user-group/454/ TechPyWorkshop 2016\n",
      "/events/python-events/449/ PyCon Siberia 2016\n",
      "/events/python-events/417/ PyCon ZA 2016\n",
      "/success-stories/ More\n",
      "/success-stories/industrial-light-magic-runs-python/ ILM runs a batch processing environment capable of modeling, rendering and compositing tens of thousands of motion picture frames per day. Thousands of machines running Linux, IRIX, Compaq Tru64, OS X, Solaris, and Windows join together to provide a production pipeline used by ~800 users daily. Speed of development is key, and Python was a faster way to code (and re-code) the programs that control this production pipeline.\n",
      "/success-stories/industrial-light-magic-runs-python/ Industrial Light & Magic Runs on Python\n",
      "/about/apps More\n",
      "http://www.djangoproject.com/ Django\n",
      "http://www.pylonsproject.org/ Pyramid\n",
      "http://bottlepy.org Bottle\n",
      "http://tornadoweb.org Tornado\n",
      "http://flask.pocoo.org/ Flask\n",
      "http://www.web2py.com/ web2py\n",
      "http://www.wxpython.org/ wxPython\n",
      "http://wiki.python.org/moin/TkInter tkInter\n",
      "http://www.pygtk.org PyGtk\n",
      "https://wiki.gnome.org/Projects/PyGObject PyGObject\n",
      "http://www.riverbankcomputing.co.uk/software/pyqt/intro PyQt\n",
      "http://www.scipy.org SciPy\n",
      "http://pandas.pydata.org/ Pandas\n",
      "http://ipython.org IPython\n",
      "http://buildbot.net/ Buildbot\n",
      "http://trac.edgewall.org/ Trac\n",
      "http://roundup.sourceforge.net/ Roundup\n",
      "http://www.ansible.com Ansible\n",
      "http://www.saltstack.com Salt\n",
      "https://www.openstack.org OpenStack\n",
      "/dev/peps/ Python Enhancement Proposals\n",
      "/dev/peps/peps.rss None\n",
      "/psf/ Python Software Foundation\n",
      "/psf/ Learn more\n",
      "/users/membership/ Become a Member\n",
      "/psf/donations/ Donate to the PSF\n",
      "#python-network None\n",
      "/about/ About\n",
      "/about/apps/ Applications\n",
      "/about/quotes/ Quotes\n",
      "/about/gettingstarted/ Getting Started\n",
      "/about/help/ Help\n",
      "http://brochure.getpython.info/ Python Brochure\n",
      "/downloads/ Downloads\n",
      "/downloads/ All releases\n",
      "/downloads/source/ Source code\n",
      "/downloads/windows/ Windows\n",
      "/downloads/mac-osx/ Mac OS X\n",
      "/download/other/ Other Platforms\n",
      "https://docs.python.org/3/license.html License\n",
      "/download/alternatives Alternative Implementations\n",
      "/doc/ Documentation\n",
      "/doc/ Docs\n",
      "/doc/av Audio/Visual Talks\n",
      "https://wiki.python.org/moin/BeginnersGuide Beginner's Guide\n",
      "https://docs.python.org/devguide/ Developer's Guide\n",
      "https://docs.python.org/faq/ FAQ\n",
      "http://wiki.python.org/moin/Languages Non-English Docs\n",
      "http://python.org/dev/peps/ PEP Index\n",
      "https://wiki.python.org/moin/PythonBooks Python Books\n",
      "/community/ Community\n",
      "/community/diversity/ Diversity\n",
      "/community/irc/ IRC\n",
      "/community/lists/ Mailing Lists\n",
      "/community/workshops/ Python Conferences\n",
      "/community/sigs/ Special Interest Groups\n",
      "https://wiki.python.org/moin/ Python Wiki\n",
      "/community/logos/ Python Logo\n",
      "/community/merchandise/ Merchandise\n",
      "/community/awards Community Awards\n",
      "/about/success/ Success Stories\n",
      "/about/success/#arts Arts\n",
      "/about/success/#business Business\n",
      "/about/success/#education Education\n",
      "/about/success/#engineering Engineering\n",
      "/about/success/#government Government\n",
      "/about/success/#scientific Scientific\n",
      "/about/success/#software-development Software Development\n",
      "/blogs/ News\n",
      "/blogs/ Python News\n",
      "http://planetpython.org/ Community News\n",
      "http://pyfound.blogspot.com/ PSF News\n",
      "http://pycon.blogspot.com/ PyCon News\n",
      "/events/ Events\n",
      "/events/python-events Python Events\n",
      "/events/python-user-group/ User Group Events\n",
      "/events/python-events/past/ Python Events Archive\n",
      "/events/python-user-group/past/ User Group Events Archive\n",
      "https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event Submit an Event\n",
      "/dev/ Contributing\n",
      "http://docs.python.org/devguide/ Developer's Guide\n",
      "http://bugs.python.org/ Issue Tracker\n",
      "https://mail.python.org/mailman/listinfo/python-dev python-dev list\n",
      "http://pythonmentors.com/ Core Mentorship\n",
      "#python-network None\n",
      "/about/help/ Help & \n",
      "/community/diversity/ Diversity \n",
      "https://github.com/python/pythondotorg/issues Submit Website Bug\n",
      "https://status.python.org/ Status \n",
      "/psf-landing/ Python Software Foundation\n",
      "/about/legal/ Legal Statements\n",
      "/privacy/ Privacy Policy\n"
     ]
    }
   ],
   "source": [
    "for item in results:\n",
    "    print item.get('href'), item.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "sel=CSSSelector('body p')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "results=sel(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    }
   ],
   "source": [
    "print len(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n",
      "The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. \n",
      "Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. \n",
      "Calculations are simple with Python, and expression syntax is straightforward: the operators \n",
      "Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. \n",
      "Python knows the usual control flow statements that other languages speak — \n",
      "Python is a programming language that lets you work quickly \n",
      "Whether you're new to programming or an experienced developer, it's easy to learn and use Python.\n",
      "None\n",
      "Python source code and installers are available for download for all versions! Not sure which version to use? \n",
      "Latest: \n",
      "Documentation for Python's standard library, along with tutorials and guides, are available online.\n",
      "None\n",
      "Looking for work or have a Python related position that you're trying to hire for? Our \n",
      "None\n",
      "None\n",
      "None\n",
      "None\n",
      "None\n",
      "None\n",
      "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. \n",
      "\r\n",
      "    \n",
      "None\n"
     ]
    }
   ],
   "source": [
    "for item in results:\n",
    "    print item.text\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
