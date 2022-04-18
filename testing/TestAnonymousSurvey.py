import unittest
from AnonymousSurvey import AnonymousSurvey
from UseAnonymousSurvey import getHobbiesResponses

# test file for class AnonymousSurvey from testClass.py
# make sure that a single response to the question is stored properly

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What's your hobby?"
        my_survey = AnonymousSurvey(question)
        hobbies = getHobbiesResponses()
        for h in hobbies:
            my_survey.addResponse(h)

        # test whether every element in list hobbies has been added to my_survey's responses
        # using setUp() method from unittest.TestCase is a better alternative

        # what if we want to test multiple cases? creating one method for each test is way to lousy
        for h in hobbies:
            self.assertIn(h, my_survey.responses)

    # will be run before any method start with test_
    # put all test here
    def setUp(self):
        question = "What's your hobby?"
        my_survey = AnonymousSurvey(question)
        hobbies = getHobbiesResponses()
        for h in hobbies:
            my_survey.addResponse(h)

        # test first hobby is in my_survey.responses
        self.assertIn(hobbies[0], my_survey.responses)

        # test all hobbies are in my_survey.responses
        for h in hobbies:
            self.assertIn(h, my_survey.responses)




unittest.main()