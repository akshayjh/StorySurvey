from django.views.generic import TemplateView


class SurveyView(TemplateView):
    template_name = 'surveys/survey.html'
