"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from polls import views
from django.urls import include
#from posts import views

urlpatterns = [
    # '^' denotes start with, and '/' denotes end-with
    re_path(r'^baba/settings/', admin.site.urls),
    
    re_path(r'index/', views.index),

    #二级路由
    re_path(r'^polls/', include('polls.urls'))
    #how did you catch it?

    # 函数中的question_id=’34’参数，是由(?P<question_id>[0-9]+)而来。
    # 在正则表达式中通过一个双圆括号，Django会捕获它匹配到的值并传递给对应的视图，作为视图的位置参数之一，
    # 而?P<question_id>则表示我要给这个捕获的值指定一个特殊的变量名，在视图中可以通过question_id这个变量名随意的引用它，形成一个关键字参数，
    # 不用考虑参数的位置。至于[0-9]+则是一个很简单的原生正则表达式，用于匹配一系列连续的数字，它匹配到的值也就是具体要传递的参数值。

]
