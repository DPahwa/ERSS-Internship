# import the necessary libraries
import nltk
import string
import re

#1 Text LowerCase

def text_lowercase(text):
	return text.lower()

input_str = "HELLO EVERYONE , WELCOME TO ERSS INTERNSHIP 2022"
text_lowercase(input_str)



#2 Removing the Numeric Digits

def remove_numbers(text):
	result = re.sub(r'\d+', '', text)
	return result

input_str = "There are 3 Black balls & 7 Cricket Bats in the bag."
remove_numbers(input_str)



#3 Removing Punctuation ( like . , ! $( ) * % @)

def remove_punctuation(text):
	translator = str.maketrans('', '', string.punctuation)
	return text.translate(translator)

input_str = "Hey, did you know that the summer break is coming? Amazing right !! It's only 5 more days !!"
remove_punctuation(input_str)




#4 Removing WhiteSpaces

def remove_whitespace(text):
	return " ".join(text.split())

input_str = "HELLO   EVERYONE       WELCOME TO ERSS   INTERNSHIP  2022"
remove_whitespace(input_str)




## !!!Currently Not Working!!! 
#5 Remove default stopwords 
      ## STOPWORDS (Stopwords are words that do not contribute to the meaning of a sentence. so, they can safely be removed without causing any change in the meaning of the sentence)
      ##  Ex- my , its , at , own , by , when etc.


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_stopwords(text):
	stop_words = set(stopwords.words("english"))
	word_tokens = word_tokenize(text)
	filtered_text = [word for word in word_tokens if word not in stop_words]
	return filtered_text

example_text = "This is a sample sentence and we are going to remove the stopwords from this."
remove_stopwords(example_text)



## !!!Currently Not Working!!! 
#6 Stemming 
    ## Stemming is the process of getting the root form of a word. Stem or root is the part to which inflectional affixes (-ed, -ize, -de, -s, etc.) are added. 
    ## Ex -> books      --->    book , denied     --->    deni etc.

from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()

def stem_words(text):
	word_tokens = word_tokenize(text)
	stems = [stemmer.stem(word) for word in word_tokens]
	return stems

text = 'data science uses scientific methods algorithms and many types of processes'
stem_words(text)

#7 Sorting Lines in the File

FileName = ("/Users/Daksh/Desktop/Sample.txt")
data=file(FileName).readlines()
data.sort()
for i in range(len(data)):
    print(data[i])

