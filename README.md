# Rom-Com Audience Analysis Overtime
Sentiment analysis and word cloud for "how to lose a guy in 10 days" overtime
Zayna Sayyed - KWK Data Science Challenge

# The Question: How and why has viewer attitude changed over time toward this rom-com?
focusing on WORDS

# WEB SCRAPING
RottenTomatoes → Selenium
Letterboxd → BeautifulSoup

What: Review and Year Posted
Pandas → save to CSV
Old Reviews (2009-2012)
Middle Reviews (2013-2016)
New Reviews (2017-2025)
About 400 reviews for each period

*used gen ai for help with some selenium, used youtube video for help with bs4

# ANALYSIS
Sentiment Analysis with nltk.sentiment (aka VADER) 
Word Cloud using wordcloud library
Visualization with matplotlib library

data cleanup using stop words like "the" "and", lemmetization, translating everything into english, and removing duplicat reviews

# INSIGHTS  - SENTIMENT
The "Nostalgia Peak" Pattern (2013-2017)
The Letterboxd Effect

Why?

Cultural Evolution:
Generational Shift

Action
Future of film: authentic relationship building
Analysis of film: benchmark for how the genre has changed.

# INSIGHTS  - WORD CLOUD
Old reviews: Focus on basic enjoyment
Middle reviews: Maintain positive sentiment with analytics
New reviews: Dramatically shift toward analytical language

# INSIGHTS - OVERALL

uncritical enjoyment → nostalgic appreciation → analytical deconstruction.


The shift from "funny" to "character" suggests audiences now prioritize character development and authentic relationship dynamics over comedic situations or star chemistry.

# FUTURE RESEARCH
This project:
Small scale and one movie
Timeout
Limited review sites (website culture confounding)
Help of Generative AI

In the future:
More romcoms
More data
Wider range
More review sites

# MY THOUGHTS
I expected mainly insights about nostalgia, where there is more criticism in the past due to prevalency and predictability of this romcom style, and in recent times, there is more positive receptions due to this style becoming classic and a comfort, a srt of time capsule perspective.

Instead, got insights about movie reviewing culture and the shift in online reviewing habits.

Yes, the data shows recent criticism, but
at the end of the day, it depends on your taste

A lot of us miss this classic rom-com style



