from django.views.generic import TemplateView
from survey.surveys.models import StorySurvey


class SurveyMixin(object):
    """
    A mixin class to include a survey in the
    page template context based on the page url.
    """

    def get_context_data(self, **kwargs):
        context = super(SurveyMixin, self).get_context_data(**kwargs)

        survey_id = self.kwargs.get('pk', None)

        if survey_id:
            context['survey'] = StorySurvey.public.get(pk=survey_id)

        return context


class PublicSurveyMixin(object):
    """
    A mixin class to include the list of public surveys
    in the page template context.
    """

    def get_context_data(self, **kwargs):
        context = super(PublicSurveyMixin, self).get_context_data(**kwargs)
        context['surveys'] = StorySurvey.public.all()
        return context


class SurveyDisclaimerView(SurveyMixin, TemplateView):
    template_name = 'surveys/survey_disclaimer.html'


class SurveyInstructionView(SurveyMixin, TemplateView):
    template_name = 'surveys/survey_instructions.html'


class SurveyPracticeView(SurveyMixin, TemplateView):
    template_name = 'surveys/survey_practice.html'


class SurveyView(SurveyMixin, TemplateView):
    template_name = 'surveys/survey.html'
