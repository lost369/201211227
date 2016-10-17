{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 국제학회 목록을 크롤링하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import lxml.html\n",
    "from lxml.cssselect import CSSSelector\n",
    "import requests\n",
    "r = requests.get('https://www.ieee.org/conferences_events/index.html')\n",
    "\n",
    "html = lxml.html.fromstring(r.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sel=CSSSelector('div.content-c > div:nth-child(1) > div >div>p>a')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
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
   "execution_count": 29,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "print len(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "collapsed": false,
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=39212&WT.mc_id=con_hi-poct_16\n",
      "2016 IEEE Healthcare Innovation Point-Of-Care Technologies Conference (HI-POCT)\n",
      "http://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=38831&WT.mc_id=con_sgc_16\n",
      "2016 IEEE International Conference on Smart Grid Communications (SmartGridComm) \n",
      "http://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=38386&WT.mc_id=con_itsc_16\n",
      "2016 IEEE 19th International Conference on Intelligent Transportation Systems (ITSC)\n",
      "http://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=39005&WT.mc_id=con_milcom_16\n",
      "MILCOM 2016 - 2016 IEEE Military Communications Conference (MILCOM)\n"
     ]
    }
   ],
   "source": [
    "for item in results:\n",
    "    print item.get('href')\n",
    "    print item.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sel=CSSSelector('div.content-c > div:nth-child(1) > div >div>p')"
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
    "results=sel(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "2016 IEEE Healthcare Innovation Point-Of-Care Technologies Conference (HI-POCT) Cancun, Mexico | 9 - 11 November 2016 \n",
      "2016 IEEE International Conference on Smart Grid Communications (SmartGridComm)  Sydney, Australia | 6 - 9 November 2016\n",
      "2016 IEEE 19th International Conference on Intelligent Transportation Systems (ITSC) Rio de Janeiro, Brazil | 1 - 4 November 2016\n",
      "MILCOM 2016 - 2016 IEEE Military Communications Conference (MILCOM)Baltimore, MD, USA | 1 - 3 November 2016\n"
     ]
    }
   ],
   "source": [
    "for item in results:\n",
    "    print item.text_content()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 프로야구 기록"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://www.kbreport.com/leader/main?rows=20&order=oWAR&orderType=DESC&teamId=1&defense_no=2&year_from=2015&year_to=2015&split01=&split02_1=&split02_2=&r_tpa_count=&tpa_count=0\n",
      "ZZ</li></a>\r\n",
      "\t\t\t\t\t<a href=\"depth.html\"><li>팀구성도</li></a>\r\n",
      "\t\t\t\t\t<a href=\"trade.html\"><li>선수이동내역</li></a>\r\n",
      "\t\t\t\t\t<a href=\"/leader/main\"><li>개인순위</li></a>\r\n",
      "\t\t\t\t\t<a href=\"team.html\"><li>팀순위</li></a>\r\n",
      "\t\t\t\t\t<a href=\"awards.html\"><li id=\"nav3\">명예의전당</li></a>\r\n",
      "\t\t\t\t\t<a href=\"/statDic/main\"><li id=\"nav4\">STAT Dic</li></a>\r\n",
      "\t\t\t\t\t<a href=\"/event/hitProbabilityPerGame\"><li>이벤트 STAT</li></a>\r\n",
      "\t\t\t\t\t -->\r\n",
      "\t\t\t\t</ul>\r\n",
      "\t\t\t</div>\r\n",
      "\t\t</div><!-- .nav end -->\r\n",
      "\t\t<div class=\"top-score-box\">\r\n",
      "\t\t<div class=\"top-score\">\r\n",
      "\t\t\t\t<div class=\"top-score-top\">\r\n",
      "\t\t\t\t\t<div class=\"tst-1\">\r\n",
      "\t\t\t\t\t\t<span class=\"tst-date\">2014.6.24</span>\r\n",
      "\t\t\t\t\t\t<span class=\"tst-day\">화</span>\r\n",
      "\t\t\t\t\t</div>\r\n",
      "\t\t\t\t\t<div class=\"tst-2\">\r\n",
      "\t\t\t\t\t\t<div class=\"tst-vs-score\">\r\n",
      "\t\t\t\t\t\t\t<p class=\"tst-stadium\">잠실</p>\r\n",
      "\t\t\t\t\t\t\t<p class=\"tst-team-1\"><span class=\"teamName\">삼성</span></p>\r\n",
      "\t\t\t\t\t\t\t<span class=\"tst-team-1-score\">7</span>\r\n",
      "\t\t\t\t\t\t\t<span class=\"tst-dash\">-</span>\r\n",
      "\t\t\t\t\t\t\t<span class=\"tst-team-2-score\">6</span>\r\n",
      "\t\t\t\t\t\t\t<p class=\"tst-team-2\"><span class=\"t\n"
     ]
    }
   ],
   "source": [
    "import urllib2\n",
    "import requests\n",
    "urlperson='http://www.kbreport.com/player/list?key=이대호'\n",
    "urlbase=\"http://www.kbreport.com/leader/main?\"\n",
    "url1=\"rows=20&order=oWAR&orderType=DESC&\"\n",
    "url2=\"teamId=1&defense_no=2&year_from=2015&year_to=2015&split01=&split02_1=&split02_2=&r_tpa_count=&tpa_count=0\"\n",
    "urlbaseball=urlbase+url1+url2\n",
    "print urlbaseball\n",
    "data=requests.get(urlbaseball).text\n",
    "#data=requests.get(urlperson).text\n",
    "print data[6000:7000]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6515\n",
      "8528\n"
     ]
    }
   ],
   "source": [
    "print data.find('top-score-top')\n",
    "print data.find('top-score end')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "mydata=data[6340:8353+len('top-score end')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import re\n",
    "p=re.compile(u'.승.+')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "res=p.findall(mydata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(승) 이호성 (패) 정수근 (세) 임창용 (홈런) 김바위</p>\r\n",
      "(승) 이호성 (패) 정수근 (세) 임창용 (홈런) 김바위</p>\r\n",
      "(승) 이호성 (패) 정수근 (세) 임창용 (홈런) 김바위</p>\r\n",
      "(승) 이호성 (패) 정수근 (세) 임창용 (홈런) 김바위</p>\r\n"
     ]
    }
   ],
   "source": [
    "for item in res:\n",
    "    print item"
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
