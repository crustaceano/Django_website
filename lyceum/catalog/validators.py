import django.core.exceptions


def custom_text_validator(value):
    value = value.lower()
    if ('превосходно' not in value) and ('роскошно' not in value):
        raise django.core.exceptions.ValidationError(
            'В тексте должно быть слово превосходно или роскошно!!',
        )
