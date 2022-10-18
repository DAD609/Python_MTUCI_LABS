from django.shortcuts import render


from django.http import HttpResponse


def home(request):
    message = 'Gigachat'
    return render(request, 'firstwebpage/index.html', {'message': message})
    
def nehome(request):
    message = 'Gigachat'
    return render(request, 'firstwebpage/static_handler.html', {'message': message})
    

