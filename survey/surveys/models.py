from django.db import models
from survey.surveys.managers import StorySurveyManager


class StorySurvey(models.Model):
    """
    A database model representing a survey.
    """
    title = models.CharField(
        max_length=90,
        help_text='The title of the survey.'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Determines if the survey is public for users to take.'
    )

    public = StorySurveyManager()
