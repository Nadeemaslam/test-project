
from django.shortcuts import render

from .models import Question




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'blog/index.html', context)
