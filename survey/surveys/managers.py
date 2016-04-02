from django.db import models


class StorySurveyManager(models.Manager):
    """
    A custom manager to overide the default
    manager for the StorySurvey model.
    """
    def get_queryset(self):
        queryset = super(StorySurveyManager, self).get_queryset()
        return queryset.filter(is_public=True)
