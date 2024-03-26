import django.contrib.admin

import feedback.models


class FeedbackAuther(django.contrib.admin.TabularInline):
    model = feedback.models.FeedbackAuther
    fields = (
        feedback.models.FeedbackAuther.name.field.name,
        feedback.models.FeedbackAuther.mail.field.name,
    )
    can_delete = False


class FeedbackFiles(django.contrib.admin.TabularInline):
    model = feedback.models.FeedbackFile
    fields = (feedback.models.FeedbackFile.file.field.name,)


@django.contrib.admin.register(feedback.models.Feedback)
class FeedbackAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        feedback.models.Feedback.text.field.name,
        feedback.models.Feedback.status.field.name,
    )
    inlines = (
        FeedbackFiles,
        FeedbackAuther,
    )
