from django.contrib import admin
from .models import Tutorial


class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]


admin.site.register(Tutorial, TutorialAdmin)
