import django.db.models
from django.db import models
import django.core.validators
import django.core.exceptions
from string import ascii_lowercase


def custom_text_validator(value):
    if ('превосходно' not in value) and ('роскошно' not in value):
        raise django.core.exceptions.ValidationError(
            'В тексте должно быть слово превосходно или роскошно!!',
        )


def custom_slug_validator(value):
    value = value.lower()
    Slug_alphabet = list(map(str, range(10))) + list(ascii_lowercase) + ['-', '_']
    for elem in value:
        if elem not in Slug_alphabet:
            raise django.core.exceptions.ValidationError(
                'В тексте могут использоваться только цифры, буквы латиницы, символы - и _',
            )


# class AbstractModel(django.db.models.Model):
#     name = django.db.models.TextField()
#
#     class Meta:
#         abstract = True
#
#
# class Category(AbstractModel):
#     pass
#
#
# class Tag(AbstractModel):
#     pass
#
#
# class ExtendItem(AbstractModel):
#     pass
class AbstractModel(django.db.models.Model):
    is_published = django.db.models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
    )
    name = django.db.models.TextField(
        verbose_name='Название',
        validators=[
            django.core.validators.MaxLengthValidator(150),
        ],
        blank=True,
    )

    class Meta:
        abstract = True


class Tag(AbstractModel):
    slug = django.db.models.SlugField(
        verbose_name='Слаг',
        unique=True,
        validators=[
            django.core.validators.MaxLengthValidator(200),
        ],
        blank=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name[:15]


class Category(AbstractModel):
    slug = django.db.models.SlugField(
        verbose_name='Слаг',
        unique=True,
        validators=[
            django.core.validators.MaxLengthValidator(200),
        ],
        blank=True,
    )
    weight = django.db.models.PositiveSmallIntegerField(
        verbose_name='Вес',
        default=100,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name[:15]


class Item(AbstractModel):
    text = django.db.models.TextField(
        verbose_name='Текст',
        help_text='Опишите объект',
        validators=[
            custom_text_validator,
        ],
        blank=True,
    )
    # category = django.db.models.ForeignKey(
    #     'category',
    #     on_delete=django.db.models.CASCADE,
    #     related_name='catalog_items',
    # )
    # tags = django.db.models.ManyToManyField(Tag)
    # extend = django.db.models.OneToOneField(ExtendItem)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name[:15]
