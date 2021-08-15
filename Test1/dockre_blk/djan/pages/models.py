from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if "/" in value and len(value.split("/")) and value.split("/")[1].isdigit():
            if int(value.split("/")[1])>=0 and int(value.split("/")[1])<33:
                if "." in value and len(value.split("."))==4:
                    ipDigit = value.split("/")[0].split(".")
                    for xTmp in ipDigit:
                        if not xTmp.isdigit():
                            raise ValidationError(
                                _('%(value)s is not an format x.x.x.x/x'),
                                params={'value': value},
                            )
                            return
                        if int(xTmp) < 0 or int(xTmp) > 255:
                            raise ValidationError(
                                _('%(value)s is not an format x.x.x.x/x'),
                                params={'value': value},
                            )
                            return
                    return
    raise ValidationError(
        _('%(value)s is not an format x.x.x.x/x'),
        params={'value': value},
    )

class Post(models.Model):
    title = models.CharField(max_length=18,validators=[validate_even])
    def __str__(self):
        return self.title
