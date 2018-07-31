# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from .function import render_to_pdf3
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
import time,pdb,json,requests,urllib
from django.views.decorators.http import require_GET,require_POST
from documents.models import Extrait
from django.views.decorators.csrf import csrf_exempt
from annoying.functions import get_object_or_None

@csrf_exempt
@require_GET
def extraitPDF(request):
   data = request.GET
   numero = data["numero"]
   extrait = get_object_or_None(Extrait,num_extrait=numero)
   if not extrait:  return HttpResponse("numero extrait inconnu")
   return render_to_pdf3("pdf/extrait.html",{"extraits":extrait})

