from django.views.generic import TemplateView
from survey_app.surveys.views import PublicStoryMixin


class Homepage(PublicStoryMixin, TemplateView):
    template_name = 'home.html'
