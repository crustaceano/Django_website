import django.core.mail
from django.shortcuts import render
import django.urls
import django.conf
import feedback.forms
import feedback.models
import django.contrib.messages

def index(request):
    feedback_auther = feedback.forms.FeedbackAutherForm(request.Post or None)
    feedback_form = feedback.forms.FeedbackForm(request.Post or None)
    files_form = feedback.forms.FeedbackFileForm(request.Post or None)
    context = {
        'feedback_form': feedback_form,
        'files_form': files_form,
        'feedback_auther': feedback_auther,
    }

    forms = (feedback_form, files_form, feedback_auther)

    if request.method == 'POST' and all(form.is_valid() for form in forms):
        django.core.mail.send_mail(
            f'Hello {feedback_auther.cleaned_data["name"]}',
            f'{feedback_form.cleaned_data["text"]}',
            django.conf.settings.FEEDBACK_SENDER,
            [feedback_auther.cleaned_data['mail']],
            fail_silently=True,
        )
        feedback_item = feedback.models.Feedback.objects.create(
            **feedback_form.cleaned_data
        )
        feedback_item.save()
        feedback.models.FeedbackAuther.objects.create(
            feedback=feedback_item,
            **feedback_auther.cleaned_data,
        )
        for file in request.FILES.getlist(
            feedback.models.FeedbackFile.file.field.name,
        ):
            feedback.models.FeedbackFile.objects.create(
                file=file,
                feedback=feedback_item,
            )
        django.contrib.messages.success(
            request,
            'Фидбек отправлен, Спасибо!',
        )
        return django.shortcuts.redirect(
            django.urls.reverse('feedback:feedback'),
        )
    return django.shortcuts.render(
        request,
        'feedbacck/feedback.html',
        context,
    )
