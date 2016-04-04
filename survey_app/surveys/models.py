from django.db import models
from survey_app.surveys.querysets import PublicStorySurveyQuerySet


class Story(models.Model):
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

    start = models.TextField(
        blank=True,
        help_text='The beginning of a story that will be provided to the user.'
    )

    end = models.TextField(
        blank=True,
        help_text='The end of a story that will be provided to the user.'
    )

    public = PublicStorySurveyQuerySet.as_manager()


class StoryEvent(models.Model):
    """
    A database model that represents a single event in a story.
    """

    survey = models.ForeignKey(
        'surveys.Story',
        related_name='events'
    )

    text = models.TextField(
        help_text='The text of one event in the story.'
    )

    #order
