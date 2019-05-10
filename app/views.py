from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def result(request):
    text = request.GET['text']
    word_list = text.split(' ')
    word_dic = {}
    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1 
    
    context={
        "word_dic":word_dic,
        "text":text,
    }

    return render(request,'result.html',context)

def about(request):

    return render(request,'about.html')

# Create your views here.
