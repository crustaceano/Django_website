import uuid

import django.db.models
import sorl.thumbnail
from django.db import models
import django.core.validators
import catalog.validators
from django.utils.safestring import mark_safe


# from string import ascii_lowercase


def item_directory_path(instance, filename):
    return f'catalog/{instance.item.id}/{uuid.uuid4()}-{filename}'


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
        validators=[
            django.core.validators.MaxLengthValidator(200),
        ],
        blank=True,
    )
    weight = django.db.models.PositiveSmallIntegerField(
        validators=[
            django.core.validators.MinValueValidator(
                1,
                message='Значение должно быть больше 0',
            ),
            django.core.validators.MaxValueValidator(
                32767,
                message='Значение должно быть меньше 32678',
            )
        ],
        verbose_name='Вес',
        default=100,
    )

    class Meta:
        ordering = ('weight', 'id')
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name[:15]


class ItemManager(django.db.models.Manager):
    def published(self):
        (self.get_queryset()
         .filter(is_published=True)
         .select_related('category')
         .order_by('category')
         .prefetch_related(
            django.db.models.Prefetch(
                'tags',
                queryset=Tag.objects.all(),
            )
        )
         .only('name', 'text', 'category_id', 'category__name')
         )


class Item(AbstractModel):
    is_on_main = django.db.models.BooleanField(
        verbose_name='на главной странице',
        default=True,
    )
    text = django.db.models.TextField(
        verbose_name='Текст',
        help_text='Опишите объект',
        validators=[
            catalog.validators.custom_text_validator,
        ],
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        help_text='Выберите категорию',
        verbose_name='категория',
    )
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name[:15]

    def image_tmb(self):
        if self.main_image.image:
            return django.utils.safestring.mark_safe(
                f'<img src="{self.main_image.get_image_50x50.url}">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True


class ImageBaseModel(django.db.models.Model):
    image = models.ImageField(
        'изображение',
        upload_to=item_directory_path,
        default=None,
    )

    def get_image_300x300(self):
        return sorl.thumbnail.get_thumbnail(
            self.image,
            '300x300',
            crop='center',
            quality=51,
        )

    @property
    def get_image_50x50(self):
        return sorl.thumbnail.get_thumbnail(
            self.image,
            '50x50',
            crop='center',
            quality=51,
        )

    def __str__(self):
        return self.item.name

    class Meta:
        abstract = True


class MainImage(ImageBaseModel):
    item = django.db.models.OneToOneField(
        Item,
        on_delete=django.db.models.CASCADE,
        related_name='main_image',
    )

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = 'главное изображение'
        verbose_name_plural = 'главные изображения'


class Image(ImageBaseModel):
    item = django.db.models.ForeignKey(
        Item,
        on_delete=django.db.models.CASCADE,
        related_name='images',
    )

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

# class MyModel(models.Model):
#     upload = models.ImageField(upload_to='uploads/')
#
#     upload = models.ImageField(upload_to='uploads/% Y/% m/% d/')
