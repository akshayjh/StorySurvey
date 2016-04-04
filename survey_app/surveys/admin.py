from django.contrib import admin
from survey_app.surveys.models import Story


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_public')
    search_fields = ('title', )


admin.site.register(Story, StoryAdmin)
