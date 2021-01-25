# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Text Analytics in Python: An Introduction
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business
# University of Central Florida
#
# January 25, 2021
# 
# This script follows a set of examples written by 
# Dhilip Subramanian, a Data Scientist and AI Enthusiast 
# called *Text Mining in Python: Steps and Examples*
# https://www.kdnuggets.com/2020/05/text-mining-python-steps-examples.html
# https://medium.com/towards-artificial-intelligence/
#   text-mining-in-python-steps-and-examples-78b3f8fd913b
#
##################################################
"""


##################################################
# Import Modules.
##################################################

# We will see over the next several weeks that 
# you can import python modules to perform many tasks 
# for business analytics.

# These libraries are often used with such projects 
# and we will learn about them later.

# import os
# import pandas as pd
# import numpy as np


# This module is used to plot graphs. 
import matplotlib.pyplot as plt

# This module is the Natural Language Toolkit, 
# designed for building Python programs to work with 
# human language data. 
import nltk

# When running the commands below, 
# you often have to download additional resources.
# You will see a message such as:
# 
# Please use the NLTK Downloader to obtain the resource:
nltk.download('punkt')
# For more information see: https://www.nltk.org/data.html
# 
# This command downloads additional software for use with 
# the nltk package. 



#--------------------------------------------------
### Tokenization
#--------------------------------------------------

# Tokenization is the process of breaking strings into 
# tokens, which are small structures or units.

import nltk.corpus
# sample text for performing tokenization
text = "In Brazil they drive on the right-hand side of the road. Brazil has a large coastline on the Eastern side of South America"
# importing word_tokenize from nltk
from nltk.tokenize import word_tokenize
# Passing the string text into word tokenize for breaking the sentences
token = word_tokenize(text)
token



#--------------------------------------------------
### Finding the frequency distinct in the tokens
#--------------------------------------------------

# A first step is to create a bar chart of the frequencies of words.

# Importing FreqDist library from nltk and passing token into FreqDist
from nltk.probability import FreqDist
fdist = FreqDist(token)
fdist


# Frequency Distribution Plot
fdist.plot(30,cumulative=False)
plt.show()




# To find the frequency of top 10 words
fdist1 = fdist.most_common(10)
fdist1


#--------------------------------------------------
### Stemming
#--------------------------------------------------

# Stemming is the process of categorizing words into 
# the root form.

# Approach 1: Importing Porterstemmer from nltk library
# Checking for the word ‘giving’ 
from nltk.stem import PorterStemmer
pst = PorterStemmer()
pst.stem("waiting")

# Categorizing the list of words
stm = ["waited", "waiting", "waits"]
for word in stm :
   print(word+ ":" +pst.stem(word))


# Approach 2: Importing LancasterStemmer from nltk
from nltk.stem import LancasterStemmer
lst = LancasterStemmer()
stm = ["giving", "given", "given", "gave"]
for word in stm :
    print(word + ":" + lst.stem(word))

# Note that Lancaster is more aggressive than Porter stemmer:
# it separates the past tense "gave" from the present tense "give".




#--------------------------------------------------
### Lemmatization
#--------------------------------------------------

# Lemmatization is a more sophisticated approach to stemming:
# it considers the context and categorizes words according to meaning. 

# Importing Lemmatizer library from nltk

# Please use the NLTK Downloader to obtain the resource:
# import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() 
 
print("rocks :", lemmatizer.lemmatize("rocks")) 
print("corpora :", lemmatizer.lemmatize("corpora"))


#--------------------------------------------------
### Stop Words
#--------------------------------------------------

# Stop Words are words such as “the”, “a”, “at”, “for”, “above”, “on”, 
# “is”, or “all”. These words do not provide any meaning and are usually 
# removed from texts. 

# importing stopwords from nltk library
from nltk import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
a = set(stopwords.words('english'))
text = "Cristiano Ronaldo was born on February 5, 1985, in Funchal, Madeira, Portugal."
text1 = word_tokenize(text.lower())
print(text1)
stopwords = [x for x in text1 if x not in a]
print(stopwords)


#--------------------------------------------------
### Part-of-speech tagging (POS)
#--------------------------------------------------

# Part-of-speech tagging assigns parts of speech (such as nouns, 
# verbs, pronouns, adverbs, conjunction, adjectives, and interjections) 
# to each word of a given text  based on its definition and its context. 

text = "vote to choose a particular man or a group (party) to represent them in parliament"
#Tokenize the text
nltk.download('averaged_perceptron_tagger')
tex = word_tokenize(text)
for token in tex:
    print(nltk.pos_tag([token]))

# The text is assiggned to nouns (NN) prepositions (PRP)
# conjunctions (CC) and so on. 



#--------------------------------------------------
### Named entity recognition
#--------------------------------------------------

# Named entity recognition is a term for identifying the entities 
# referred to in text, such as those in the subject and object of 
# a sentence.

text = "Google’s CEO Sundar Pichai introduced the new Pixel at Minnesota Roi Centre Event"
#importing chunk library from nltk
from nltk import ne_chunk
nltk.download('maxent_ne_chunker')
nltk.download('words')
# tokenize and POS Tagging before doing chunk
token = word_tokenize(text)
tags = nltk.pos_tag(token)
chunk = ne_chunk(tags)
chunk



#--------------------------------------------------
### Chunking
#--------------------------------------------------

# Chunking is the process of assigning individual terms
# into sets with larger meaning, such as phrases. 

text = "We saw the yellow dog"
token = word_tokenize(text)
tags = nltk.pos_tag(token)
reg = "NP: {<DT>?<JJ>*<NN>}"
a = nltk.RegexpParser(reg)
result = a.parse(tags)
print(result)


# These examples illustrate only the pieces of the puzzle.
# We need to lewarn a good deal more to make full use of these tools. 


##################################################
# End.
##################################################
