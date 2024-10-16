# polls/tests.py

from django.test import TestCase
from .models import Poll
from django.utils import timezone


class PollModelTest(TestCase):

    def test_poll_creation(self):
        """
        Test that a poll is created successfully.
        """
        poll = Poll.objects.create(question="Sample question?", pub_date=timezone.now())
        self.assertEqual(poll.question, "Sample question?")
