from django.db import models, transaction
from datetime import datetime


class BaseModel(models.Model):
    type = models.CharField(max_length=255, help_text='set the model name', default="")
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        with transaction.atomic():
            if not self.pk:
                self.type = self.__class__.__name__ if self.type == '' else self.type
            super(BaseModel,self).save()
