from django.db import models
from django.utils import timezone
import datetime            
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
# makemigration create a 
# migrate create a table
# use command "CREATE DATABASE database_name;" to create database in databases other than SQLite 


# API会自动进行连表操作，通过双下划线分割关系对象。连表操作可以无限多级，一层一层的连接。
# 下面是查询所有的Choices，它所对应的Question的发布日期是今年。（重用了上面的current_year结果）
## >>> Choice.objects.filter(question__pub_date__year=current_year)
## <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

"""
# 显示所有与q对象有关系的choice集合，目前是空的，还没有任何关联对象。
>>> q.choice_set.all()
<QuerySet []>

# 看看我们自定义的方法用起来怎么样
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# 让我们试试主键查询
>>> q = Question.objects.get(pk=1)

# 创建3个choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
"""

# decorater makes compatible to python2
@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date =models.DateTimeField('date published')

    #make object readable
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return  now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'   #define teh order when filtering using this property
    was_published_recently.boolean = True       # set property to true to use official representation of true false?
    was_published_recently.short_description = 'Published recently?'    #description in admin site
    
class Choice(models.Model):
    """
        django support general data relationship:
        - one to one
        - many to one
        - many to many
    """
    #many to one relationship, Question as key and choices as many
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0) 

    def __str__(self):
        return self.choice_text
