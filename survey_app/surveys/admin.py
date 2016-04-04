from django.contrib import admin
from survey_app.surveys.models import StorySurvey


class StorySurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_public')
    search_fields = ('title', )


admin.site.register(StorySurvey, StorySurveyAdmin)
