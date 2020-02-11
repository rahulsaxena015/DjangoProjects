from django.http import HttpResponse
from django.shortcuts import render
import operator


def wordcount(request):
    return render(request, 'home.html', {'myvar': 'This is context variable' })

def about_view(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['projectcount']
    word_list = fulltext.split()
    print(word_list)
    word_dict = {}

    for word in word_list:
        if word in word_dict:
            # Increase the number for specific word
            word_dict[word] += 1
        else:
            # Add the word to the dictionary
            word_dict[word] = 1
    sorted_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(word_list), 'worddict': sorted_dict})
