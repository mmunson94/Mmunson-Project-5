from django.shortcuts import render

# Create your views here.


def get_fit_list():
    return render(request, 'fit/fit_list.html')
