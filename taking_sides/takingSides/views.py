# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
 
# 引入我们创建的表单类
# from .forms import AddForm
 
# def index(request):
#     if request.method == 'POST':# 当提交表单时
     
#         form = AddForm(request.POST) # form 包含提交的数据
         
#         if form.is_valid():# 如果提交的数据合法
#             a = form.cleaned_data['a']
#             b = form.cleaned_data['b']
#             return HttpResponse(str(int(a) + int(b)))
     
#     else:# 当正常访问时
#         form = AddForm()
#     return render(request, 'index.html', {'form': form})
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
class IndexView(generic.ListView):
      model = Question
      template_name = 'polls/index.html'
      context_object_name='latest_question_list'
      # def get_queryset(self):
      #     return Question.objects.order('-pub_date')[:5]
class DetailView(generic.View):
      model = Question
      template_name = 'polls/detail.html'

class ResultsView(generic.View):
      model = Question
      template_name = 'polls/results.html'
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls: results', args=[question.id, ]))

