# -*- encoding: utf-8 -*-
# Python Libs
from __future__ import absolute_import
from django.shortcuts import redirect
from django.template.response import TemplateResponse

# Main View
def main(request):
    ctx = {}
    return TemplateResponse(request, 'home.html', ctx)
