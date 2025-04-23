from newspaper import Article
import random
import string
import nltk
from sklearn. feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore' )

import nltk
nltk.download('punkt')


article = Article('https://www.mayoclinic.org/diseases-conditions/kidney-cancer/symptoms-causes/syc-20352664')
article.download()
article.parse()
article.nlp()
corpus = article.text

print(corpus)


text = corpus
sentence_list = nltk.sent_tokenize(text) 

print(sentence_list)
def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    for i in range(length):
        for j in range(i + 1, length):
            if list_var[list_index[i]] < list_var[list_index[j]]:
                list_index[i], list_index[j] = list_index[j], list_index[i]

    return list_index


def bot_response(user_input):
    user_input = user_input. lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1],cm)
    similarity_scores_lists = similarity_scores.flatten()
    index = index_sort(similarity_scores_lists)
    index = index[1:]
    response_flag = 0

    j =0
    for i in range (len(index)):
        if similarity_scores_lists[index[i]] > 0.0:
            bot_response = bot_response +' '+sentence_list[index[i]]
            response_flag = 1
            j=j+1
        if j > 2:
            break

    if response_flag == 0 :
        bot_response = bot_response+' '+"I apologize , I dont understand ."
        sentence_list.remove(user_input)

    return bot_response

def greeting_response(text):
    text = text. lower()

   
    bot_greetings = ["hii","hey",'hello' ,'hola' ]
   
    user_greeting = ['hi','hey' ,'hello','hola' ,'greetings' ]

    for word in text.split():
        if word in user_greeting:
            return random. choice(bot_greetings)
        


print("Doc Bot : I am doc bot for your services for short time i will answer ypur questions")

exit_list = ['exit','see you later' ,'bye' ,'quit' ,'break' ]

while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print("Doc Bot : Chat with you later !")
        break
    else:
        if greeting_response(user_input) != None:
            print('Doc Bot: '+greeting_response(user_input))
        else:
            print('Doc Bot'+bot_response(user_input) )