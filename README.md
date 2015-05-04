# BoulderCrime
Scrapes the Boulder, CO police call logs for the past two weeks.

Introduction
------------
After a recent burglary in my neighborhood, I became interested in learning more about crime in Boulder, CO.  I learned that spotcrime.com was getting its data for the area formatted like "https://bouldercolorado.gov/pages/call-log-april-30-2015" so I used scrapy to scrape the crime data from the past two weeks.  The contents of this directory are my scrapy files.

How To
------
If you want to use these files, you have to install [Scrapy](http://doc.scrapy.org/en/latest/index.html) then call "scrapy crawl call" from the spiders directory to retrieve the existing data for the past two weeks.  I have used "scrapy crawl call -o calls.json" to export the calls to a .json file.
