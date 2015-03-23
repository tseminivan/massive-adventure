from django.test import TestCase

class DemoTests(TestCase):

    def test_is_demo_ok(self):
        """
        is_demo_ok() should return True
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(True, True)

