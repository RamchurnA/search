from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

projectsList = [
            {
                'id': '1',
                'title': "Movies",
                'description' : 'list of all the different movies'
            },
            {
                'id' : '2',
                'title' : 'the hell',
                'description' : 'no clue what i am ding'
            },
            {
                'id' : '3',
                'title' : 'from dusk till dawn',
                'description' : 'vampires'
            },

]

def projects(request):
    page = 'Projects'
    number = 10
    context = {'page' : page, 'number' : number, 'pro': projectsList} # we access projectsList, via any name and a colon to say thats the dictionary
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None

    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-projects.html', {'pro' : projectObj})
