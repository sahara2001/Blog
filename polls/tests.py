from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
# Create your tests here.


# testing the bug of was_published_recently()
class QuestionMethodTests(TestCase):
    def test_was_published_recently_wtih_future_question(self):
        """
        should return false for question published in the future 
        Can be used to buffer future posts
        """
        time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_true(self):
        """
        should return false for question published in the future 
        Can be used to buffer future posts
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)
    
    def test_was_published_recently_false(self):
        """
        should return false for question published in the future 
        Can be used to buffer future posts
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)