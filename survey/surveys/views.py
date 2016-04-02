from django.views.generic import TemplateView
from survey.surveys.models import StorySurvey


class SurveyListView(TemplateView):
    template_name = 'surveys/survey_list.html'

    def get_context_data(self, **kwargs):
        context = super(SurveyListView, self).get_context_data(**kwargs)
        context['surveys'] = StorySurvey.public.all()
        return context


class SurveyView(TemplateView):
    template_name = 'surveys/survey.html'

    def get_context_data(self, **kwargs):
        context = super(SurveyView, self).get_context_data(**kwargs)
        #context['survey'] = StorySurvey.objects.get(pk=)
        return context
