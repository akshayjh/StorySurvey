from django.views.generic import TemplateView
from survey_app.surveys.views import PublicSurveyMixin


class Homepage(PublicSurveyMixin, TemplateView):
    template_name = 'home.html'
