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
    "response = urllib.urlopen('https://www.google.com/finance/historical?q=KRX%3AKOSPI200&ei=omDuV9CdJcLc0ATQ_7_QBQ/')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "_html = response.read()"
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
    "from lxml import etree"
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
    "_htmlTree = etree.HTML(_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "nodes = _htmlTree.xpath('//*[@class=\"lm\"]/text()')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "nodes2 = _htmlTree.xpath('//*[@class=\"rgt\"]/text()')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "nodes3 = _htmlTree.xpath('//*[@class=\"rgt rm\"]/text()')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "print len(nodes2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Oct 4, 2016 259.51 259.74 258.55 259.18 62,561,000\n",
      "Sep 30, 2016 258.30 258.91 257.29 257.49 74,918,000\n",
      "Sep 29, 2016 259.60 260.95 259.60 260.35 65,365,000\n",
      "Sep 28, 2016 259.32 259.46 257.96 258.21 59,186,000\n",
      "Sep 27, 2016 256.16 259.87 255.16 259.57 58,684,000\n",
      "Sep 26, 2016 258.07 259.32 256.90 257.48 43,876,000\n",
      "Sep 23, 2016 258.44 259.14 257.71 258.37 58,392,000\n",
      "Sep 22, 2016 258.46 259.99 258.13 258.34 59,904,000\n",
      "Sep 21, 2016 254.65 256.55 254.56 256.52 51,982,000\n",
      "Sep 20, 2016 253.86 255.23 253.33 255.09 54,626,000\n",
      "Sep 19, 2016 251.51 254.54 251.38 253.93 59,750,000\n",
      "Sep 13, 2016 253.39 253.55 251.66 251.77 74,548,000\n",
      "Sep 12, 2016 252.37 253.43 250.53 250.53 66,332,000\n",
      "Sep 9, 2016 258.68 258.94 256.21 257.31 70,053,000\n",
      "Sep 8, 2016 260.72 261.48 259.41 260.86 79,382,000\n",
      "Sep 7, 2016 261.15 262.10 260.31 260.31 68,749,000\n",
      "Sep 6, 2016 259.39 261.16 259.26 260.93 49,969,000\n",
      "Sep 5, 2016 257.85 259.74 257.63 259.64 54,167,000\n",
      "Sep 2, 2016 256.16 256.73 255.57 256.50 49,266,000\n",
      "Sep 1, 2016 254.95 256.13 253.86 256.03 56,098,000\n",
      "Aug 31, 2016 257.21 257.49 255.90 256.87 66,352,000\n",
      "Aug 30, 2016 257.27 258.93 257.00 257.49 56,516,000\n",
      "Aug 29, 2016 254.93 256.66 254.45 256.49 62,755,000\n",
      "Aug 26, 2016 256.17 256.76 255.02 256.23 68,304,000\n",
      "Aug 25, 2016 256.78 257.76 256.00 257.26 58,803,000\n",
      "Aug 24, 2016 258.40 258.65 256.54 257.30 54,461,000\n",
      "Aug 23, 2016 257.57 258.63 257.09 258.42 65,706,000\n",
      "Aug 22, 2016 258.54 258.63 256.92 257.27 62,921,000\n",
      "Aug 19, 2016 258.42 258.84 257.54 258.69 72,796,000\n",
      "Aug 18, 2016 256.62 258.23 255.80 258.11 64,012,000\n"
     ]
    }
   ],
   "source": [
    "for i in range(30):\n",
    "    k=4*i\n",
    "    print nodes[i].strip(), nodes2[k].strip(), nodes2[k+1].strip(), nodes2[k+2].strip(), nodes2[k+3].strip(), nodes3[i].strip()"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
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