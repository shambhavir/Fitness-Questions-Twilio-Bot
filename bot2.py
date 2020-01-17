import flask 
from flask import Flask, request 
from twilio.twiml.messaging_response import MessagingResponse
import json
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
nltk.download('all')

with open('intents2.json') as file: 
	data2 = json.load(file)
with open('intents3.json') as file:
	data3 = json.load(file)
with open('intents4.json') as file:
	data4 = json.load(file)
with open('intents5.json') as file:
	data5 = json.load(file)
with open('intents6.json') as file:
	data6 = json.load(file)

#intents2 organization - Greetings 
words = []
#labels = []
docs_x = []
docs_y = []

for intent in data2["intents"]: #going to loop through all the dictionaries for us
	for pattern in intent["patterns"]: #stemming takes any of our words and brings it down to the root word 
		wrds = nltk.word_tokenize(pattern)
		words.extend(wrds)
		docs_x.append(wrds)
		docs_y.append(intent["tag"]) #shows what intent/tag it is a part of 
#if intent["tag"] not in labels:
			#labels.append(intent["tag"])
words = [stemmer.stem(w.lower()) for w in words if  w not in "?"]
words = sorted(list(set(words)))
#labels = sorted(labels)

#intents3 organization - Goodbye
words2 = []
#labels2 = []
docs_x2 = []
docs_y2 = []

for intent in data3["intents"]: #going to loop through all the dictionaries for us
	for pattern in intent["patterns"]: #stemming takes any of our words and brings it down to the root word 
		wrds = nltk.word_tokenize(pattern)
		words2.extend(wrds)
		docs_x2.append(wrds)
		docs_y2.append(intent["tag"])
#if intent["tag"] not in labels2:
			#labels2.append(intent["tag"])
words2 = [stemmer.stem(w.lower()) for w in words2 if  w not in "?"]
words2 = sorted(list(set(words2)))
#labels2 = sorted(labels2)

#intents4 organization - thanks
words3 = []
#labels3 = []
docs_x3 = []
docs_y3 = []

for intent in data4["intents"]: #going to loop through all the dictionaries for us
	for pattern in intent["patterns"]: #stemming takes any of our words and brings it down to the root word 
		wrds = nltk.word_tokenize(pattern)
		words3.extend(wrds)
		docs_x3.append(wrds)
		docs_y3.append(intent["tag"])
#if intent["tag"] not in labels3:
			#labels3.append(intent["tag"])
words3 = [stemmer.stem(w.lower()) for w in words3 if  w not in "?"]
words3 = sorted(list(set(words3)))
#labels3 = sorted(labels3)

#intents5 organization - query
words4 = []
#labels4 = []
docs_x4 = []
docs_y4 = []

for intent in data5["intents"]: #going to loop through all the dictionaries for us
	for pattern in intent["patterns"]: #stemming takes any of our words and brings it down to the root word 
		wrds = nltk.word_tokenize(pattern)
		words4.extend(wrds)
		docs_x4.append(wrds)
		docs_y4.append(intent["tag"])
#if intent["tag"] not in labels4:
			#labels4.append(intent["tag"])
words4 = [stemmer.stem(w.lower()) for w in words4 if  w not in "?"]
words4 = sorted(list(set(words4)))
#labels4 = sorted(labels4)

#intents6 organization - diet tips
words5 = []
#labels5 = []
docs_x5 = []
docs_y5 = []

for intent in data6["intents"]: #going to loop through all the dictionaries for us
	for pattern in intent["patterns"]: #stemming takes any of our words and brings it down to the root word 
		wrds = nltk.word_tokenize(pattern)
		words5.extend(wrds)
		docs_x5.append(wrds)
		docs_y5.append(intent["tag"])
#if intent["tag"] not in labels5:
			#labels5.append(intent["tag"])
words5 = [stemmer.stem(w.lower()) for w in words5 if  w not in "?"]
words5 = sorted(list(set(words5)))
#labels5 = sorted(labels5)


app = Flask(__name__)
@app.route('/bot', methods = ['POST'])

def bot():
	incoming_msg = request.values.get('Body', '').lower()
	resp = MessagingResponse()
	msg = resp.message()
	responded = False
	data100 = {}
	if incoming_msg in words:
		r = requests.get('https://api.quotable.io/random')
		if r.status_code == 200:
			data100 = r.json()
			response100 = str(data100)
			msg.body(response100)
			responded = True
	elif incoming_msg in words2:
		r = requests.get('https://api.quotable.io/random')
		if r.status_code == 200:
			data100 = r.json()
			response100 = str(data100)
			msg.body(response100)
			responded = True
	elif incoming_msg in words3:
		r = requests.get('https://api.quotable.io/random')
		if r.status_code == 200:
			data100 = r.json()
			response100 = str(data100)
			msg.body(response100)
			responded = True
	elif incoming_msg in words4:
		r = requests.get('https://www.livestrong.org/')
		if r.status_code == 200:
			data100 = r.json()
			response100 = str(data100)
			msg.body(response100)
			responded = True
	elif incoming_msg in words5:
		r = requests.get('https://www.webmd.com/diet/ss/slideshow-best-diet-tips-ever')
		if r.status_code == 200:
			data100 = r.json()
			response100 = str(data100)
			msg.body(response100)
			responded = True
print str(resp)

	








	






