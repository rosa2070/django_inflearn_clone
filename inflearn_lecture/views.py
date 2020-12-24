from django.shortcuts import render
from .models import myText
# Create your views here.
def home_list(request) :

    texts = myText.objects.filter()

    # texts = "1번 타이틀"
    # texts = "2번 타이틀"

    return render(request, 'inflearn_lecture/home_list.html', {'texts': texts})