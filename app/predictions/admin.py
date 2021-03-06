# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Prediction
# Register your models here.


class PredictionAdmin(admin.ModelAdmin):
    list_display = (
            'user',
            'symbol',
            'choice',
            'result',
            'balance',
            'start_date',
            'end_date',
            )
    list_filter = (
        'user',
           )
    search_fields = (
            )
    readonly_fields = (
            )


admin.site.register(Prediction, PredictionAdmin)
