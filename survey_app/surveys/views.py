from django.views.generic import TemplateView
from survey_app.surveys.models import Story


class StoryMixin(object):
    """
    A mixin class to include a survey in the
    page template context based on the page url.
    """

    def get_context_data(self, **kwargs):
        from django.shortcuts import get_object_or_404
        from django.http import Http404

        context = super(StoryMixin, self).get_context_data(**kwargs)

        survey_id = self.kwargs.get('pk', None)
        surveys = Story.public.is_public()

        if survey_id:
            context['story'] = get_object_or_404(surveys, pk=survey_id)

        return context


class PublicStoryMixin(object):
    """
    A mixin class to include the list of public surveys
    in the page template context.
    """

    def get_context_data(self, **kwargs):
        context = super(PublicStoryMixin, self).get_context_data(**kwargs)
        context['surveys'] = Story.public.is_public()
        return context


class SurveyDisclaimerView(StoryMixin, TemplateView):
    template_name = 'surveys/survey_disclaimer.html'


class SurveyInstructionView(StoryMixin, TemplateView):
    template_name = 'surveys/survey_instructions.html'


class SurveyPracticeView(StoryMixin, TemplateView):
    template_name = 'surveys/survey_practice.html'


class SurveyView(StoryMixin, TemplateView):
    template_name = 'surveys/survey.html'
