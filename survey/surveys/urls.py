from django.conf.urls import url
from survey.surveys import views as survey_views

urlpatterns = [
    url(
        r'^(?P<pk>[0-9]+)',
        survey_views.SurveyView.as_view(),
        name='survey'
    ),
]
