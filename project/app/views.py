from django.shortcuts import render
import numpy as np
from string import ascii_letters

from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'home.html'



def mainpage(request):
    global mat, row, col, ll, ul
    row = int(request.POST['Row'])
    col = int(request.POST['Column'])
    ll = int(request.POST['Lower_limit'])
    ul = int(request.POST['Upper_limit'])
    mat = np.random.randint(ll, ul + 1, size=(row, col))
    return render(request, "home.html", {"mat": mat, 'row':row,'col':col,'ll':ll,'ul':ul})

def Trans(request):
    tra = np.transpose(mat)
    return render(request, "home.html", {"mat": mat,'tra':tra,'row':row,'col':col,'ll':ll,'ul':ul})


