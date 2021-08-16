from django.test import TestCase

from authorities.models import Authority


class AnimalTestCase(TestCase):
    def sample_test(self):

        self.assertEqual(1, 1)
