# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question
from users.models import User
from django import forms
from django.contrib.auth.decorators import login_required


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def rankByUpTime(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def rankByDownTime(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def rankByAppreciation(request):
    latest_question_list = Question.objects.order_by('-question_appreciation')[:]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        now_user = User.objects.get(username=request.user.username)
        votedQuestions = now_user.voted_questions.split(',')
        if str(question_id) in votedQuestions:
            return render(request, 'polls/results.html', {
                'question': question,
                'error_message': "你已投过票，请勿重复投票！",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            votedQuestions.append(str(question_id))
            now_user.voted_questions = ','.join(votedQuestions)
            now_user.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)), {'error_message':"You vote successfully!"})
            return render(request, 'polls/results.html', {
                'question': question,
                'error_message': "投票成功!",
            })


def search(request):
    q = request.GET.get('q')
    error_msg = '未找到'

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'polls/search.html', {'error_msg': error_msg})

    post_list = Question.objects.filter(question_text__icontains=q)
    return render(request, 'polls/search.html', {'post_list': post_list})


def appreciate(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    now_user = User.objects.get(username=request.user.username)
    likedQuestions = now_user.liked_questions.split(',')
    if str(question_id) in likedQuestions:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You have already appreciated this question!",
        })
    else:
        question.question_appreciation += 1
        question.save()
        likedQuestions.append(str(question_id))
        now_user.liked_questions = ','.join(likedQuestions)
        now_user.save()
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))


class QuestionForm(forms.Form):
    question_text = forms.CharField(label='问题标题', max_length=50)
    question_detail = forms.CharField(label='问题内容', max_length=500)
    choice_text1 = forms.CharField(label='选项1', max_length=200)
    choice_text2 = forms.CharField(label='选项2', max_length=200)


@login_required
def questionRaise(request):
    if request.method == "POST":
        questionform = QuestionForm(request.POST)
        if questionform.is_valid():
            question_text = questionform.cleaned_data['question_text']
            question_detail = questionform.cleaned_data['question_detail']
            choice_text1 = questionform.cleaned_data['choice_text1']
            choice_text2 = questionform.cleaned_data['choice_text2']
            q = Question(question_text=question_text, question_detail=question_detail,
                         questioner_name=request.user.username)
            q.save()
            q.choice_set.create(choice_text=choice_text1)
            q.choice_set.create(choice_text=choice_text2)
            return HttpResponseRedirect('/polls/')
    else:
        questionform = QuestionForm()
    return render(request, 'polls/raiseQuestion.html', {'questionform': questionform})
