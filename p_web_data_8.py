
# coding: utf-8

# In[20]:

import os


# In[56]:

os.chdir('C:\\Users\yesun')


# In[59]:

os.chdir('spiders')
os.getcwd()


# In[16]:

get_ipython().run_cell_magic(u'writefile', u'ds_web_data_paging.py', u'import scrapy\n\n\nclass QuotesSpider(scrapy.Spider):\n    name = "quotes"\n    start_urls = [\n        \'http://quotes.toscrape.com/page/1/\',\n    ]\n\n    def parse(self, response):\n        for quote in response.css(\'div.quote\'):\n            yield {\n                \'text\': quote.css(\'span.text::text\').extract_first(),\n                \'author\': quote.css(\'span small::text\').extract_first(),\n                \'tags\': quote.css(\'div.tags a.tag::text\').extract(),\n            }\n\n        next_page = response.css(\'li.next a::attr(href)\').extract_first()\n        if next_page is not None:\n            next_page = response.urljoin(next_page)\n            yield scrapy.Request(next_page, callback=self.parse)')


# In[60]:

get_ipython().system(u'scrapy runspider quotes_spider.py -o quotes_spider.json -t json --logfile quotes_spider.logfile')


# In[ ]:

2016-10-11 22:58:52 [scrapy] INFO: Spider opened
2016-10-11 22:58:52 [scrapy] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2016-10-11 22:58:52 [scrapy] DEBUG: Telnet console listening on 127.0.0.1:6023
2016-10-11 22:58:53 [scrapy] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)
2016-10-11 22:58:54 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
2016-10-11 22:58:54 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': u'\u201cThe world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.\u201d', 'tags': [u'change', u'deep-thoughts', u'thinking', u'world'], 'author': u'Albert Einstein'}
2016-10-11 22:58:54 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': u'\u201cIt is our choices, Harry, that show what we truly are, far more than our abilities.\u201d', 'tags': [u'abilities', u'choices'], 'author': u'J.K. Rowling'}
2016-10-11 22:58:54 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': u'\u201cThere are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.\u201d', 'tags': [u'inspirational', u'life', u'live', u'miracle', u'miracles'], 'author': u'Albert Einstein'}
2016-10-11 22:58:54 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': u'\u201cThe person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.\u201d', 'tags': [u'aliteracy', u'books', u'classic', u'humor'], 'author': u'Jane Austen'}
2016-10-11 22:58:54 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': u"\u201cImperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.\u201d", 'tags': [u'be-yourself', u'inspirational'], 'author': u'Marilyn Monroe'}
2016-10-11 22:58:54 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': u'\u201cTry not to become a man of success. Rather become a man of value.\u201d', 'tags': [u'adulthood', u'success', u'value'], 'author': u'Albert Einstein'}
2016-10-11 22:58:54 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': u'\u201cIt is better to be hated for what you are than to be loved for what you are not.\u201d', 'tags': [u'life', u'love'], 'author': u'Andr\xe9 Gide'}
2016-10-11 22:58:54 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': u"\u201cI have not failed. I've just found 10,000 ways that won't work.\u201d", 'tags': [u'edison', u'failure', u'inspirational', u'paraphrased'], 'author': u'Thomas A. Edison'}
2016-10-11 22:58:54 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': u"\u201cA woman is like a tea bag; you never know how strong it is until it's in hot water.\u201d", 'tags': [u'misattributed-eleanor-roosevelt'], 'author': u'Eleanor Roosevelt'}
2016-10-11 22:58:54 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': u'\u201cA day without sunshine is like, you know, night.\u201d', 'tags': [u'humor', u'obvious', u'simile'], 'author': u'Steve Martin'}
2016-10-11 22:58:55 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/2/> (referer: http://quotes.toscrape.com/page/1/)
2016-10-11 22:58:55 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': u"\u201cThis life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.\u201d", 'tags': [u'friends', u'heartbreak', u'inspirational', u'life', u'love', u'sisters'], 'author': u'Marilyn Monroe'}
2016-10-11 22:58:55 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': u'\u201cIt takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.\u201d', 'tags': [u'courage', u'friends'], 'author': u'J.K. Rowling'}
2016-10-11 22:58:55 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': u"\u201cIf you can't explain it to a six year old, you don't understand it yourself.\u201d", 'tags': [u'simplicity', u'understand'], 'author': u'Albert Einstein'}
2016-10-11 22:58:55 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': u"\u201cYou may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? She's not perfect\u2014you aren't either, and the two of you may never be perfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break\u2014her heart. So don't hurt her, don't change her, don't analyze and don't expect more than she can give. Smile when she makes you happy, let her know when she makes you mad, and miss her when she's not there.\u201d", 'tags': [u'love'], 'author': u'Bob Marley'}
2016-10-11 22:58:55 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': u'\u201cI like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.\u201d', 'tags': [u'fantasy'], 'author': u'Dr. Seuss'}
2016-10-11 22:58:55 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': u'\u201cI may not have gone where I intended to go, but I think I have ended up where I needed to be.\u201d', 'tags': [u'life', u'navigation'], 'author': u'Douglas Adams'}
2016-10-11 22:58:55 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': u"\u201cThe opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.\u201d", 'tags': [u'activism', u'apathy', u'hate', u'indifference', u'inspirational', u'love', u'opposite', u'philosophy'], 'author': u'Elie Wiesel'}
2016-10-11 22:58:55 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': u'\u201cIt is not a lack of love, but a lack of friendship that makes unhappy marriages.\u201d', 'tags': [u'friendship', u'lack-of-friendship', u'lack-of-love', u'love', u'marriage', u'unhappy-marriage'], 'author': u'Friedrich Nietzsche'}
2016-10-11 22:58:55 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': u'\u201cGood friends, good books, and a sleepy conscience: this is the ideal life.\u201d', 'tags': [u'books', u'contentment', u'friends', u'friendship', u'life'], 'author': u'Mark Twain'}
2016-10-11 22:58:55 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': u'\u201cLife is what happens to us while we are making other plans.\u201d', 'tags': [u'fate', u'life', u'misattributed-john-lennon', u'planning', u'plans'], 'author': u'Allen Saunders'}
2016-10-11 22:58:56 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/3/> (referer: http://quotes.toscrape.com/page/2/)
2016-10-11 22:58:56 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/3/>
{'text': u'\u201cI love you without knowing how, or when, or from where. I love you simply, without problems or pride: I love you in this way because I do not know any other way of loving but this, in which there is no I or you, so intimate that your hand upon my chest is my hand, so intimate that when I fall asleep your eyes close.\u201d', 'tags': [u'love', u'poetry'], 'author': u'Pablo Neruda'}
2016-10-11 22:58:56 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/3/>
{'text': u'\u201cFor every minute you are angry you lose sixty seconds of happiness.\u201d', 'tags': [u'happiness'], 'author': u'Ralph Waldo Emerson'}
2016-10-11 22:58:56 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/3/>
{'text': u'\u201cIf you judge people, you have no time to love them.\u201d', 'tags': [u'attributed-no-source'], 'author': u'Mother Teresa'}
2016-10-11 22:58:56 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/3/>
{'text': u'\u201cAnyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.\u201d', 'tags': [u'humor', u'religion'], 'author': u'Garrison Keillor'}
2016-10-11 22:58:56 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/3/>
{'text': u'\u201cBeauty is in the eye of the beholder and it may be necessary from time to time to give a stupid or misinformed beholder a black eye.\u201d', 'tags': [u'humor'], 'author': u'Jim Henson'}
2016-10-11 22:58:56 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/3/>
{'text': u'\u201cToday you are You, that is truer than true. There is no one alive who is Youer than You.\u201d', 'tags': [u'comedy', u'life', u'yourself'], 'author': u'Dr. Seuss'}
2016-10-11 22:58:56 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/3/>
{'text': u'\u201cIf you want your children to be intelligent, read them fairy tales. If you want them to be more intelligent, read them more fairy tales.\u201d', 'tags': [u'children', u'fairy-tales'], 'author': u'Albert Einstein'}
2016-10-11 22:58:56 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/3/>
{'text': u'\u201cIt is impossible to live without failing at something, unless you live so cautiously that you might as well not have lived at all - in which case, you fail by default.\u201d', 'tags': [], 'author': u'J.K. Rowling'}
2016-10-11 22:58:56 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/3/>
{'text': u'\u201cLogic will get you from A to Z; imagination will get you everywhere.\u201d', 'tags': [u'imagination'], 'author': u'Albert Einstein'}
2016-10-11 22:58:56 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/3/>
{'text': u'\u201cOne good thing about music, when it hits you, you feel no pain.\u201d', 'tags': [u'music'], 'author': u'Bob Marley'}
2016-10-11 22:58:57 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/4/> (referer: http://quotes.toscrape.com/page/3/)
2016-10-11 22:58:57 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/4/>
{'text': u"\u201cThe more that you read, the more things you will know. The more that you learn, the more places you'll go.\u201d", 'tags': [u'learning', u'reading', u'seuss'], 'author': u'Dr. Seuss'}
2016-10-11 22:58:57 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/4/>
{'text': u'\u201cOf course it is happening inside your head, Harry, but why on earth should that mean that it is not real?\u201d', 'tags': [u'dumbledore'], 'author': u'J.K. Rowling'}
2016-10-11 22:58:57 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/4/>
{'text': u'\u201cThe truth is, everyone is going to hurt you. You just got to find the ones worth suffering for.\u201d', 'tags': [u'friendship'], 'author': u'Bob Marley'}
2016-10-11 22:58:57 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/4/>
{'text': u'\u201cNot all of us can do great things. But we can do small things with great love.\u201d', 'tags': [u'misattributed-to-mother-teresa', u'paraphrased'], 'author': u'Mother Teresa'}
2016-10-11 22:58:57 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/4/>
{'text': u'\u201cTo the well-organized mind, death is but the next great adventure.\u201d', 'tags': [u'death', u'inspirational'], 'author': u'J.K. Rowling'}
2016-10-11 22:58:57 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/4/>
{'text': u"\u201cAll you need is love. But a little chocolate now and then doesn't hurt.\u201d", 'tags': [u'chocolate', u'food', u'humor'], 'author': u'Charles M. Schulz'}
2016-10-11 22:58:57 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/4/>
{'text': u"\u201cWe read to know we're not alone.\u201d", 'tags': [u'misattributed-to-c-s-lewis', u'reading'], 'author': u'William Nicholson'}
2016-10-11 22:58:57 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/4/>
{'text': u'\u201cAny fool can know. The point is to understand.\u201d', 'tags': [u'knowledge', u'learning', u'understanding', u'wisdom'], 'author': u'Albert Einstein'}
2016-10-11 22:58:57 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/4/>
{'text': u'\u201cI have always imagined that Paradise will be a kind of library.\u201d', 'tags': [u'books', u'library'], 'author': u'Jorge Luis Borges'}
2016-10-11 22:58:57 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/4/>
{'text': u'\u201cIt is never too late to be what you might have been.\u201d', 'tags': [u'inspirational'], 'author': u'George Eliot'}
2016-10-11 22:58:58 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/5/> (referer: http://quotes.toscrape.com/page/4/)
2016-10-11 22:58:58 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/5/>
{'text': u'\u201cA reader lives a thousand lives before he dies, said Jojen. The man who never reads lives only one.\u201d', 'tags': [u'read', u'readers', u'reading', u'reading-books'], 'author': u'George R.R. Martin'}
2016-10-11 22:58:58 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/5/>
{'text': u'\u201cYou can never get a cup of tea large enough or a book long enough to suit me.\u201d', 'tags': [u'books', u'inspirational', u'reading', u'tea'], 'author': u'C.S. Lewis'}
2016-10-11 22:58:58 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/5/>
{'text': u'\u201cYou believe lies so you eventually learn to trust no one but yourself.\u201d', 'tags': [], 'author': u'Marilyn Monroe'}
2016-10-11 22:58:58 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/5/>
{'text': u'\u201cIf you can make a woman laugh, you can make her do anything.\u201d', 'tags': [u'girls', u'love'], 'author': u'Marilyn Monroe'}
2016-10-11 22:58:58 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/5/>
{'text': u'\u201cLife is like riding a bicycle. To keep your balance, you must keep moving.\u201d', 'tags': [u'life', u'simile'], 'author': u'Albert Einstein'}
2016-10-11 22:58:58 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/5/>
{'text': u'\u201cThe real lover is the man who can thrill you by kissing your forehead or smiling into your eyes or just staring into space.\u201d', 'tags': [u'love'], 'author': u'Marilyn Monroe'}
2016-10-11 22:58:58 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/5/>
{'text': u"\u201cA wise girl kisses but doesn't love, listens but doesn't believe, and leaves before she is left.\u201d", 'tags': [u'attributed-no-source'], 'author': u'Marilyn Monroe'}
2016-10-11 22:58:58 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/5/>
{'text': u'\u201cOnly in the darkness can you see the stars.\u201d', 'tags': [u'hope', u'inspirational'], 'author': u'Martin Luther King Jr.'}
2016-10-11 22:58:58 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/5/>
{'text': u'\u201cIt matters not what someone is born, but what they grow to be.\u201d', 'tags': [u'dumbledore'], 'author': u'J.K. Rowling'}
2016-10-11 22:58:58 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/5/>
{'text': u'\u201cLove does not begin and end the way we seem to think it does. Love is a battle, love is a war; love is a growing up.\u201d', 'tags': [u'love'], 'author': u'James Baldwin'}
2016-10-11 22:58:59 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/6/> (referer: http://quotes.toscrape.com/page/5/)
2016-10-11 22:58:59 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/6/>
{'text': u'\u201cThere is nothing I would not do for those who are really my friends. I have no notion of loving people by halves, it is not my nature.\u201d', 'tags': [u'friendship', u'love'], 'author': u'Jane Austen'}
2016-10-11 22:58:59 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/6/>
{'text': u'\u201cDo one thing every day that scares you.\u201d', 'tags': [u'attributed', u'fear', u'inspiration'], 'author': u'Eleanor Roosevelt'}
2016-10-11 22:58:59 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/6/>
{'text': u'\u201cI am good, but not an angel. I do sin, but I am not the devil. I am just a small girl in a big world trying to find someone to love.\u201d', 'tags': [u'attributed-no-source'], 'author': u'Marilyn Monroe'}
2016-10-11 22:58:59 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/6/>
{'text': u'\u201cIf I were not a physicist, I would probably be a musician. I often think in music. I live my daydreams in music. I see my life in terms of music.\u201d', 'tags': [u'music'], 'author': u'Albert Einstein'}
2016-10-11 22:58:59 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/6/>
{'text': u'\u201cIf you only read the books that everyone else is reading, you can only think what everyone else is thinking.\u201d', 'tags': [u'books', u'thought'], 'author': u'Haruki Murakami'}
2016-10-11 22:58:59 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/6/>
{'text': u'\u201cThe difference between genius and stupidity is: genius has its limits.\u201d', 'tags': [u'misattributed-to-einstein'], 'author': u'Alexandre Dumas fils'}
2016-10-11 22:58:59 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/6/>
{'text': u"\u201cHe's like a drug for you, Bella.\u201d", 'tags': [u'drug', u'romance', u'simile'], 'author': u'Stephenie Meyer'}
2016-10-11 22:58:59 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/6/>
{'text': u'\u201cThere is no friend as loyal as a book.\u201d', 'tags': [u'books', u'friends', u'novelist-quotes'], 'author': u'Ernest Hemingway'}
2016-10-11 22:58:59 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/6/>
{'text': u'\u201cWhen one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.\u201d', 'tags': [u'inspirational'], 'author': u'Helen Keller'}
2016-10-11 22:58:59 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/6/>
{'text': u"\u201cLife isn't about finding yourself. Life is about creating yourself.\u201d", 'tags': [u'inspirational', u'life', u'yourself'], 'author': u'George Bernard Shaw'}
2016-10-11 22:59:00 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/7/> (referer: http://quotes.toscrape.com/page/6/)
2016-10-11 22:59:00 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/7/>
{'text': u"\u201cThat's the problem with drinking, I thought, as I poured myself a drink. If something bad happens you drink in an attempt to forget; if something good happens you drink in order to celebrate; and if nothing happens you drink to make something happen.\u201d", 'tags': [u'alcohol'], 'author': u'Charles Bukowski'}
2016-10-11 22:59:00 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/7/>
{'text': u'\u201cYou don\u2019t forget the face of the person who was your last hope.\u201d', 'tags': [u'the-hunger-games'], 'author': u'Suzanne Collins'}
2016-10-11 22:59:00 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/7/>
{'text': u"\u201cRemember, we're madly in love, so it's all right to kiss me anytime you feel like it.\u201d", 'tags': [u'humor'], 'author': u'Suzanne Collins'}
2016-10-11 22:59:00 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/7/>
{'text': u'\u201cTo love at all is to be vulnerable. Love anything and your heart will be wrung and possibly broken. If you want to make sure of keeping it intact you must give it to no one, not even an animal. Wrap it carefully round with hobbies and little luxuries; avoid all entanglements. Lock it up safe in the casket or coffin of your selfishness. But in that casket, safe, dark, motionless, airless, it will change. It will not be broken; it will become unbreakable, impenetrable, irredeemable. To love is to be vulnerable.\u201d', 'tags': [u'love'], 'author': u'C.S. Lewis'}
2016-10-11 22:59:00 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/7/>
{'text': u'\u201cNot all those who wander are lost.\u201d', 'tags': [u'bilbo', u'journey', u'lost', u'quest', u'travel', u'wander'], 'author': u'J.R.R. Tolkien'}
2016-10-11 22:59:00 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/7/>
{'text': u'\u201cDo not pity the dead, Harry. Pity the living, and, above all those who live without love.\u201d', 'tags': [u'live-death-love'], 'author': u'J.K. Rowling'}
2016-10-11 22:59:00 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/7/>
{'text': u'\u201cThere is nothing to writing. All you do is sit down at a typewriter and bleed.\u201d', 'tags': [u'good', u'writing'], 'author': u'Ernest Hemingway'}
2016-10-11 22:59:00 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/7/>
{'text': u'\u201cFinish each day and be done with it. You have done what you could. Some blunders and absurdities no doubt crept in; forget them as soon as you can. Tomorrow is a new day. You shall begin it serenely and with too high a spirit to be encumbered with your old nonsense.\u201d', 'tags': [u'life', u'regrets'], 'author': u'Ralph Waldo Emerson'}
2016-10-11 22:59:00 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/7/>
{'text': u'\u201cI have never let my schooling interfere with my education.\u201d', 'tags': [u'education'], 'author': u'Mark Twain'}
2016-10-11 22:59:00 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/7/>
{'text': u"\u201cI have heard there are troubles of more than one kind. Some come from ahead and some come from behind. But I've bought a big bat. I'm all ready you see. Now my troubles are going to have troubles with me!\u201d", 'tags': [u'troubles'], 'author': u'Dr. Seuss'}
2016-10-11 22:59:01 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/8/> (referer: http://quotes.toscrape.com/page/7/)
2016-10-11 22:59:01 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/8/>
{'text': u'\u201cIf I had a flower for every time I thought of you...I could walk through my garden forever.\u201d', 'tags': [u'friendship', u'love'], 'author': u'Alfred Tennyson'}
2016-10-11 22:59:01 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/8/>
{'text': u'\u201cSome people never go crazy. What truly horrible lives they must lead.\u201d', 'tags': [u'humor'], 'author': u'Charles Bukowski'}
2016-10-11 22:59:01 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/8/>
{'text': u'\u201cThe trouble with having an open mind, of course, is that people will insist on coming along and trying to put things in it.\u201d', 'tags': [u'humor', u'open-mind', u'thinking'], 'author': u'Terry Pratchett'}
2016-10-11 22:59:01 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/8/>
{'text': u'\u201cThink left and think right and think low and think high. Oh, the thinks you can think up if only you try!\u201d', 'tags': [u'humor', u'philosophy'], 'author': u'Dr. Seuss'}
2016-10-11 22:59:01 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/8/>
{'text': u"\u201cWhat really knocks me out is a book that, when you're all done reading it, you wish the author that wrote it was a terrific friend of yours and you could call him up on the phone whenever you felt like it. That doesn't happen much, though.\u201d", 'tags': [u'authors', u'books', u'literature', u'reading', u'writing'], 'author': u'J.D. Salinger'}
2016-10-11 22:59:01 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/8/>
{'text': u'\u201cThe reason I talk to myself is because I\u2019m the only one whose answers I accept.\u201d', 'tags': [u'humor', u'insanity', u'lies', u'lying', u'self-indulgence', u'truth'], 'author': u'George Carlin'}
2016-10-11 22:59:01 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/8/>
{'text': u"\u201cYou may say I'm a dreamer, but I'm not the only one. I hope someday you'll join us. And the world will live as one.\u201d", 'tags': [u'beatles', u'connection', u'dreamers', u'dreaming', u'dreams', u'hope', u'inspirational', u'peace'], 'author': u'John Lennon'}
2016-10-11 22:59:01 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/8/>
{'text': u'\u201cI am free of all prejudice. I hate everyone equally. \u201d', 'tags': [u'humor', u'sinister'], 'author': u'W.C. Fields'}
2016-10-11 22:59:01 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/8/>
{'text': u"\u201cThe question isn't who is going to let me; it's who is going to stop me.\u201d", 'tags': [], 'author': u'Ayn Rand'}
2016-10-11 22:59:01 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/8/>
{'text': u"\u201c\u2032Classic\u2032 - a book which people praise and don't read.\u201d", 'tags': [u'books', u'classic', u'reading'], 'author': u'Mark Twain'}
2016-10-11 22:59:01 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/9/> (referer: http://quotes.toscrape.com/page/8/)
2016-10-11 22:59:02 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/9/>
{'text': u'\u201cAnyone who has never made a mistake has never tried anything new.\u201d', 'tags': [u'mistakes'], 'author': u'Albert Einstein'}
2016-10-11 22:59:02 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/9/>
{'text': u"\u201cA lady's imagination is very rapid; it jumps from admiration to love, from love to matrimony in a moment.\u201d", 'tags': [u'humor', u'love', u'romantic', u'women'], 'author': u'Jane Austen'}
2016-10-11 22:59:02 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/9/>
{'text': u'\u201cRemember, if the time should come when you have to make a choice between what is right and what is easy, remember what happened to a boy who was good, and kind, and brave, because he strayed across the path of Lord Voldemort. Remember Cedric Diggory.\u201d', 'tags': [u'integrity'], 'author': u'J.K. Rowling'}
2016-10-11 22:59:02 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/9/>
{'text': u'\u201cI declare after all there is no enjoyment like reading! How much sooner one tires of any thing than of a book! -- When I have a house of my own, I shall be miserable if I have not an excellent library.\u201d', 'tags': [u'books', u'library', u'reading'], 'author': u'Jane Austen'}
2016-10-11 22:59:02 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/9/>
{'text': u'\u201cThere are few people whom I really love, and still fewer of whom I think well. The more I see of the world, the more am I dissatisfied with it; and every day confirms my belief of the inconsistency of all human characters, and of the little dependence that can be placed on the appearance of merit or sense.\u201d', 'tags': [u'elizabeth-bennet', u'jane-austen'], 'author': u'Jane Austen'}
2016-10-11 22:59:02 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/9/>
{'text': u'\u201cSome day you will be old enough to start reading fairy tales again.\u201d', 'tags': [u'age', u'fairytales', u'growing-up'], 'author': u'C.S. Lewis'}
2016-10-11 22:59:02 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/9/>
{'text': u'\u201cWe are not necessarily doubting that God will do the best for us; we are wondering how painful the best will turn out to be.\u201d', 'tags': [u'god'], 'author': u'C.S. Lewis'}
2016-10-11 22:59:02 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/9/>
{'text': u'\u201cThe fear of death follows from the fear of life. A man who lives fully is prepared to die at any time.\u201d', 'tags': [u'death', u'life'], 'author': u'Mark Twain'}
2016-10-11 22:59:02 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/9/>
{'text': u'\u201cA lie can travel half way around the world while the truth is putting on its shoes.\u201d', 'tags': [u'misattributed-mark-twain', u'truth'], 'author': u'Mark Twain'}
2016-10-11 22:59:02 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/9/>
{'text': u'\u201cI believe in Christianity as I believe that the sun has risen: not only because I see it, but because by it I see everything else.\u201d', 'tags': [u'christianity', u'faith', u'religion', u'sun'], 'author': u'C.S. Lewis'}
2016-10-11 22:59:02 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/10/> (referer: http://quotes.toscrape.com/page/9/)
2016-10-11 22:59:03 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/10/>
{'text': u'\u201cThe truth." Dumbledore sighed. "It is a beautiful and terrible thing, and should therefore be treated with great caution.\u201d', 'tags': [u'truth'], 'author': u'J.K. Rowling'}
2016-10-11 22:59:03 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/10/>
{'text': u"\u201cI'm the one that's got to die when it's time for me to die, so let me live my life the way I want to.\u201d", 'tags': [u'death', u'life'], 'author': u'Jimi Hendrix'}
2016-10-11 22:59:03 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/10/>
{'text': u'\u201cTo die will be an awfully big adventure.\u201d', 'tags': [u'adventure', u'love'], 'author': u'J.M. Barrie'}
2016-10-11 22:59:03 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/10/>
{'text': u'\u201cIt takes courage to grow up and become who you really are.\u201d', 'tags': [u'courage'], 'author': u'E.E. Cummings'}
2016-10-11 22:59:03 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/10/>
{'text': u'\u201cBut better to get hurt by the truth than comforted with a lie.\u201d', 'tags': [u'life'], 'author': u'Khaled Hosseini'}
2016-10-11 22:59:03 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/10/>
{'text': u'\u201cYou never really understand a person until you consider things from his point of view... Until you climb inside of his skin and walk around in it.\u201d', 'tags': [u'better-life-empathy'], 'author': u'Harper Lee'}
2016-10-11 22:59:03 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/10/>
{'text': u'\u201cYou have to write the book that wants to be written. And if the book will be too difficult for grown-ups, then you write it for children.\u201d', 'tags': [u'books', u'children', u'difficult', u'grown-ups', u'write', u'writers', u'writing'], 'author': u"Madeleine L'Engle"}
2016-10-11 22:59:03 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/10/>
{'text': u'\u201cNever tell the truth to people who are not worthy of it.\u201d', 'tags': [u'truth'], 'author': u'Mark Twain'}
2016-10-11 22:59:03 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/10/>
{'text': u"\u201cA person's a person, no matter how small.\u201d", 'tags': [u'inspirational'], 'author': u'Dr. Seuss'}
2016-10-11 22:59:03 [scrapy] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/10/>
{'text': u'\u201c... a mind needs books as a sword needs a whetstone, if it is to keep its edge.\u201d', 'tags': [u'books', u'mind'], 'author': u'George R.R. Martin'}
2016-10-11 22:59:03 [scrapy] INFO: Closing spider (finished)
2016-10-11 22:59:03 [scrapy] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 2873,
 'downloader/request_count': 11,
 'downloader/request_method_count/GET': 11,
 'downloader/response_bytes': 24788,
 'downloader/response_count': 11,
 'downloader/response_status_count/200': 10,
 'downloader/response_status_count/404': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2016, 10, 11, 13, 59, 3, 117000),
 'item_scraped_count': 100,
 'log_count/DEBUG': 112,
 'log_count/INFO': 7,
 'request_depth_max': 9,
 'response_received_count': 11,
 'scheduler/dequeued': 10,
 'scheduler/dequeued/memory': 10,
 'scheduler/enqueued': 10,
 'scheduler/enqueued/memory': 10,
 'start_time': datetime.datetime(2016, 10, 11, 13, 58, 52, 289000)}
2016-10-11 22:59:03 [scrapy] INFO: Spider closed (finished)

