from django.urls import re_path
from . import views

# used to register as a valid namespace in template system
app_name = 'polls'
urlpatterns = [

    # 函数中的question_id=’34’参数，是由(?P<question_id>[0-9]+)而来。
    # 在正则表达式中通过一个双圆括号，Django会捕获它匹配到的值并传递给对应的视图，作为视图的位置参数之一，
    # 而?P<question_id>则表示我要给这个捕获的值指定一个特殊的变量名，在视图中可以通过question_id这个变量名随意的引用它，形成一个关键字参数，
    # 不用考虑参数的位置。至于[0-9]+则是一个很简单的原生正则表达式，用于匹配一系列连续的数字，它匹配到的值也就是具体要传递的参数值。

    # ex: /polls/
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),       # detail is the namespace of the path in django template engine
    # ex: /polls/5/results/
    re_path(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),     #DetailView requires pk as parameter, therefore change
    # ex: /polls/5/vote/
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),       #why not use pk? In accordance with function param?
]