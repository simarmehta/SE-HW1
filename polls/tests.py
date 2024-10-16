# polls/tests.py

from django.test import TestCase
from django.utils import timezone
from .models import Question


class QuestionModelTest(TestCase):

    def test_question_creation(self):
        """
        Test that a Question is created successfully.
        """
        question = Question.objects.create(
            question_text="What's new?", pub_date=timezone.now()
        )
        self.assertEqual(question.question_text, "What's new?")
