from django.contrib import admin

from django.db import models
from . import models as my_models

# Register your models here.
for key, val in my_models.__dict__.items():
    if (
        isinstance(val, type)
        and issubclass(val, models.Model)
        and not val._meta.abstract
    ):
        admin.site.register(val)
