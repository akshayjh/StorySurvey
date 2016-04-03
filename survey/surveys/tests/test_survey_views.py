from django.test import TestCase
from django.core.urlresolvers import reverse
from survey.surveys.factories import StorySurveyFactory


class SurveyViewTests(TestCase):

    def setUp(self):
        super(SurveyViewTests, self).setUp()

        self.survey = StorySurveyFactory()

        self.survey_url = reverse(
            'surveys:survey',
            kwargs={
                'pk': self.survey.id,
            }
        )

    def test_get_public_survey(self):
        """
        Test that a user can go to a survey page.
        """
        response = self.client.get(self.survey_url)

        self.assertEqual(response.status_code, 200)

    def test_get_non_public_survey(self):
        """
        Test that a user can not go to a survey
        page for a survey that is not public.
        """
        self.survey.is_public = False
        self.survey.save()

        response = self.client.get(self.survey_url)

        self.assertEqual(response.status_code, 404)
