import django.db.models
import time


class Feedback(django.db.models.Model):
    class Status(django.db.models.TextChoices):
        NEW = 'new', 'New'
        WIP = 'wip', 'Work in progress'
        ANSWERED = 'ans', 'Answered'

    text = django.db.models.TextField('текст')
    created = django.db.models.DateTimeField(
        'время создания',
        auto_now_add=True,
    )
    status = django.db.models.CharField(
        max_length=3,
        choices=Status.choices,
        default=Status.NEW,
    )


class FeedbackAuther(django.db.models.Model):
    feedback = django.db.models.OneToOneField(
        Feedback,
        related_name='auther',
        on_delete=django.db.models.CASCADE,
    )
    name = django.db.models.CharField('имя', max_length=150)
    mail = django.db.models.EmailField('mail adress')


class FeedbackFile(django.db.models.Model):
    def get_path(self, filename):
        return f'uploads/{self.feedback_id}/{time.time()}_{filename}'

    feedback = django.db.models.ForeignKey(
        Feedback,
        related_name='files',
        on_delete=django.db.models.CASCADE,
    )
    file = django.db.models.FileField(
        'file',
        upload_to=get_path,
        blank=True,
    )
