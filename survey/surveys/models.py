from django.db import models


class StorySurvey(models.Model):
    """
    A database model representing a survey.
    """

    title = models.CharField(
        max_length=90,
        help_text='The title of the survey.'
    )
