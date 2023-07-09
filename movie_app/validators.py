from django.core.exceptions import ValidationError


def check_len(value):
    if len(value) < 3:
        raise ValidationError('za krutkie')