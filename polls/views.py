from django.shortcuts import HttpResponse, get_object_or_404, render, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.urls import reverse
# Create your views here.

"""
PAGES:
    - index: latest polls
    - detail: detail of a poll, a table
    - result: the polling result of a questionare
    - vote: voting for a specific choice in a question
"""
def index(request):
    #member of Question shows in runtime visiting databases
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    data = {"latest_question_list": latest_question_list}

    # difference?
    #return HttpResponse(template.render(data,request))
    return render(request,"template/polls/index.html", data)

"""
    use get_object_or_404() to replace the try catch clause,
    similarly, we have get_list_or_404() method with similar functionality

    1. request.POST是一个类似字典的对象，允许你通过键名访问提交的数据。
            本例中，request.POST[’choice’]返回被选择选项的ID，并且值的类型永远是string字符串，那怕它看起来像数字！同样的，你也可以用类似的手段获取GET请求发送过来的数据，一个道理。
    2. request.POST[’choice’]有可能触发一个KeyError异常，如果你的POST数据里没有提供choice键值，在这种情况下，上面的代码会返回表单页面并给出错误提示。PS：通常我们会给个默认值，防止这种异常的产生，例如request.POST[’choice’,None]，一个None解决所有问题。
    3. 在选择计数器加一后，返回的是一个HttpResponseRedirect而不是先前我们常用的HttpResponse。HttpResponseRedirect需要一个参数：重定向的URL。这里有一个建议，当你成功处理POST数据后，应当保持一个良好的习惯，始终返回一个HttpResponseRedirect。这不仅仅是对Django而言，它是一个良好的WEB开发习惯。
    4. 我们在上面HttpResponseRedirect的构造器中使用了一个reverse()函数。它能帮助我们避免在视图函数中硬编码URL。它首先需要一个我们在URLconf中指定的name，然后是传递的数据。例如'/polls/3/results/'，其中的3是某个question.id的值。重定向后将进入polls:results对应的视图，并将question.id传递给它。白话来讲，就是把活扔给另外一个路由对应的视图去干。
"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'template/polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id) 
    return render(request, 'template/polls/results.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)   
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #error finding choice, return to table page and give error message
        return render(request, 'template/polls/detail.html',{
            'question': question,
            'error_message': "You did't select a choice or there is a problem with the choice you select.",
        })
    #else has replace final?
    else:
        selected_choice.votes +=1
        selected_choice.save()
        #save counts and jump back to the results page
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


