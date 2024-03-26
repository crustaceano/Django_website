from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FeedbackForm

from django.core.mail import send_mail
# Create your views here.
def description(request):
    template = 'about/description.html'
    context = {}
    return render(request, template, context)


def feedback_form(request):
    template = 'about/form_application.html'
    feedback_form = FeedbackForm()
    context = {
        'feedback_form': feedback_form,
    }
    if request.method == 'POST' and feedback_form.is_valid():
        name = request.POST.get('name')
        send_mail(
            'Subject here',
            name,
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
        return redirect('catalog:item_list')
    return render(request, template, context)
