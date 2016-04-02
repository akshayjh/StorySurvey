from django.views.generic import TemplateView
from survey.surveys.models import StorySurvey


class SurveyMixin(object):
    """
    A mixin class to include a survey in the
    page template context based on the page url.
    """

    def get_context_data(self, **kwargs):
        context = super(SurveyMixin, self).get_context_data(**kwargs)
        context['survey'] = StorySurvey.public.get(pk=self.kwargs['pk'])
        return context


class SurveyListView(TemplateView):
    template_name = 'surveys/survey_list.html'

    def get_context_data(self, **kwargs):
        context = super(SurveyListView, self).get_context_data(**kwargs)
        context['surveys'] = StorySurvey.public.all()
        return context


class SurveyInstructionView(SurveyMixin, TemplateView):
    template_name = 'surveys/survey_instructions.html'


class SurveyPracticeView(SurveyMixin, TemplateView):
    template_name = 'surveys/survey_practice.html'


class SurveyView(SurveyMixin, TemplateView):
    template_name = 'surveys/survey.html'
