# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import requests,pdb,json,hashlib,os,pdfkit
from django.template.loader import render_to_string
from django.http import HttpResponse

def render_to_pdf3(template_src, context_dict):
   date = datetime.datetime.now()
   printDate = "%s/%s/%s  %s:%s:%s - Page [page]/[topage]"%(date.day,date.month,date.year,date.hour,date.minute,date.second)
   options = {
      'footer-font-size':'6',
      'footer-right': printDate,
     }
   rendered = render_to_string(template_src, context_dict)
   pdf = pdfkit.from_string(rendered,False,options=options)
   return HttpResponse(pdf, content_type='application/pdf')
