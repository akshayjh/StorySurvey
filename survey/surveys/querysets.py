from django.db import models


class PublicStorySurveyQuerySet(models.QuerySet):
    """
    A custom queryset to return public surveys.
    """
    def is_public(self):
        return self.filter(is_public=True)
