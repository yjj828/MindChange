from django.http import HttpResponse
from django.shortcuts import render
from thoughtReverse.models import Thought
import random

# Create your views here.

def index(request):
    t = random.choice(Thought.objects.all())
    context_dict = {'NegativeThought': t.negative, 'PositiveThought': t.positive}
    return render(request, 'thoughtReverse/index.html', context=context_dict)

