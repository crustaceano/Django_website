import django.forms
import feedback.models


class BootstrapForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class FeedbackAutherForm(BootstrapForm):
    class Meta:
        model = feedback.models.FeedbackAuther
        fields = (
            feedback.models.FeedbackAuther.name.field.name,
            feedback.models.FeedbackAuther.mail.field.name,
        )
        labels = {
            feedback.models.FeedbackAuther.name.field.name: 'Name',
            feedback.models.FeedbackAuther.mail.field.name: (
                'Mail adress',
            ),
        }
        help_texts = {
            feedback.models.FeedbackAuther.name.field.name: 'Write down your name',
            feedback.models.FeedbackAuther.mail.field.name: (
                'Write down your mail adress'
            ),
        }


class FeedbackFileForm(BootstrapForm):
    class Meta:
        model = feedback.models.FeedbackFile

        fields = (feedback.models.FeedbackFile.file.field.name,)
        help_texts = {
            feedback.models.FeedbackFile.file.field.name: (
                'Upload files if you need',
            ),
        }
        widgets = {
            feedback.models.FeedbackFile.file.field.name: (
                django.forms.FileInput(
                    attrs={
                        'class': 'form-control',
                        'type': 'file',
                        'multiple': True,
                    },
                )
            ),
        }


class FeedbackForm(BootstrapForm):
    class Meta:
        model = feedback.models.Feedback
        exclude = (
            feedback.models.Feedback.id.field.name,
            feedback.models.Feedback.created.field.name,
            feedback.models.Feedback.status.field.name,
        )
        labels = {
            feedback.models.Feedback.text.field.name: 'feedback text',
        }
        help_texts = {
            feedback.models.Feedback.text.field.name: 'Write feedback text',
        }
