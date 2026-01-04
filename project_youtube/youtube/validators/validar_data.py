from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from datetime import datetime

@deconstructible
class ValidarData:
    def __call__(self, value):
        if value is None:
            raise ValidationError("Data invalida")

        if value > datetime.today().date():
            raise ValidationError("Data não pode ser futura")
