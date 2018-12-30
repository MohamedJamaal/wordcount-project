from django.http import HttpResponse
from django.shortcuts import render
import operator



def home(request):
    return render(request , 'home.html')

def count(request):
    fulltext = request.GET['fulltext'] # da 3mltlo get 3shan ageb el klam mn el text area
    countwords = fulltext.split()

    worddictionary = {} # new empty dictionary use to count the words

    for word in countwords:
        if word in worddictionary:
            #increase the count
            worddictionary[word] += 1
        else:
            # add to dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1) , reverse = True)
    # sorted function hia kda bttktbn 3la b3dha :D  # items to put dictionary values in a list
    # operator lazm t3mlha import fo2

    return render(request , 'count.html' , {'fulltext' : fulltext ,
    'countwords' :len(countwords),# a3mlha call b2a fel count html
     'sortedwords': sortedwords})



def about(request):
    return render(request , 'about.html')
