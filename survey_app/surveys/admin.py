from django.contrib import admin
from survey_app.surveys.models import Story, StoryEvent


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_public', )
    search_fields = ('title', )


class StoryEventAdmin(admin.ModelAdmin):
    list_display = ('survey', 'order')
    search_fields = ('survey__title', )


admin.site.register(Story, StoryAdmin)
admin.site.register(StoryEvent, StoryEventAdmin)
