# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Region, Centre, Mairie, Distict

admin.site.register(Mairie)
admin.site.register(Centre)