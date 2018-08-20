# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns,include,url

urlpatterns = patterns('',
   #url('inscriptions/$','tickets.views.ticket',name="edition de ticket"),
   #url('recu-des-preinscriptions-en-ligne-2014/$','tickets.views.ticket2014',name="edition de ticket 2014"),
   url('extrait/$','parametres.views.extraitPDF',name="appercu extrait"),
)
