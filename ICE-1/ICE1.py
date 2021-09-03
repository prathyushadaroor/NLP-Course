import urllib.request
from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

#reading spaceex wikipedia page by using urllib

response = urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html =  response.read()

#Using Beautiful Soup to parse raw html data
soup = BeautifulSoup(html, "html5lib")
text = soup.get_text(strip = True)
tokens = [t for t in text.split()]
clean_tokens = tokens[:]

#Obtaining high frequency words using NLP Frequency distribution
frequency = nltk.FreqDist(tokens)
keys =[]
values = []

for key,val in frequency.items():
    # Obtaining values with word frequency greater than5
    if val>5:
        print(str(key) + ':' +str(val))
        keys.append(key)
        values.append(val)
    else:
        tokens.remove(key)
        
#Graph with stopwords
frequency.plot(20,cumulative= False)

#Ignoring stop words
for token in tokens:
    #Ignoring integers
    if str(token).isdigit():
        clean_tokens.remove(token)
    #Ignoring Stopwords
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

#Calculating Frequency after removing stopwords
final = nltk.FreqDist(clean_tokens)


#Calculating Frequency after removing stopwords
final.plot(10,cumulative= False)


#Plotting first 10 high distribution words
plt.bar(keys[0:10], values[0:10], color='green')
plt.show()



