# flight-finder

It's my capstone project. And I'm going to be using a combination of different APIs to create a cheap flight finder. 
Part one, my program is going to find amazing flight deals just for myselves. And in part two, I turn this project into a fully-fladged product where I can start 
signing up users to use my service. 

First, I have a Google sheet which keeps track of the locations that I want to visit and a price cutoff. So a historical low price. I take this data from Google sheet 
with lots of different locations and their lowest prices and I feed that into a flight search API, which is going to run every day, searching through all of the 
locations looking for the cheapest flight in the next six months. When it comes up with a hit and it finds a flight that's actually cheaper than my predefined price, 
then it's going to send that date and price via Twilio SMS model to my mobile phone so that I can book it right there.
