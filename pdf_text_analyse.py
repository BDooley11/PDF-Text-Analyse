import requests
import pdftotext
import nltk
import re

from nltk import word_tokenize

# ask user to type pdf they want to download and what to call it
url = input("Please enter URL of pdf you want to download:")
name = input("What do you want to call the download:")
print()

# gets pdf and saves it as name requested
request_object = requests.get(url)
with open(name+".pdf", "wb") as pdffile:
    pdffile.write(request_object.content)

# converts the pdf to a text file so it can be analysed.
with open(name+".pdf", "rb") as f:
    pdf = pdftotext.PDF(f)   
with open(name+".txt", 'w', encoding="utf-8") as f:
    f.write("\n\n".join(pdf))
 
selection = 0
while selection != 4:
    selection = int(input("What would you like to do next?\n1.Total sentence details\n2.Total word details\n3.Create dispersion plot\n4.Exit\n"))
    with open(name+".txt", 'rb') as f:
        text_content = f.read().decode('UTF-8')
    sentences = nltk.sent_tokenize(text_content)
    words = nltk.word_tokenize(text_content)
    if selection == 1:
        word_count = lambda sentence: len(word_tokenize(sentence))
        print("Number of sentences:", len(sentences))
        print("Smallest sentence:",len(min(sentences, key=word_count)))
        print("Largest sentence:",len(max(sentences, key=word_count))) 
        print()
    elif selection == 2:
        print("Number of words:", len(words))
        unique = text_content.split()
        myset= set(unique)
        print("Number of unique words:",len(myset))
        print("Ratio of unique words to total:","1 :",int((len(words)/len(myset))))
        text = nltk.Text(words)
        word_frequency = nltk.FreqDist(text)
        print("\nMost frequent top-20 words: ", word_frequency.most_common(20))
        print()
    elif selection == 3:
        nltkformat = nltk.Text(words)
        choice = 1
        mylist= list()
        while choice != "0":
            choice = input("Enter word for dispersion plot, press 0 to exit:")
            if choice != "0":
                mylist.append(choice)
        nltkformat.dispersion_plot(mylist)  
        print()
    elif selection == 4:
        print("Thanks, enjoy your results.")