from django.contrib import admin
from .models import Question, Choice
# Register your models here to manage them in admin site


# equivalent to manage choice under question
# StackedInline takes more space than TabularInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3     # 4 slots for extra to edit

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pubdate', 'question_text']

    #cut the table as teh set of some text pieces
    fieldsets= [
        (None,  {'fields': ['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # to display things besides __str__() method return value
    # we can add properties to method to revise the display effect (from False to graphic ...)
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    search_fields =['question_text']    #adding a searching field, but using SQL like grammar

    list_filter = ['pub_date']  
    
    
    # and the split pages function with 100 item per page by default is on by default


# keep the line at the end since python is not static type language
admin.site.register(Question,QuestionAdmin)