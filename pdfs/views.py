import json

from utils.utils import list_shedules
from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,landscape
from reportlab.platypus import Image

from meetings.models import Meeting

def pdf_file(request,pk):

    meeting = Meeting.objects.get(id=pk)

    shedules = list_shedules()
    print(type(shedules))
    print(len((shedules)))

    # shedules_list = {}
    #
    # for aux in range(len(list_shedules)):
    #     introduction = \
    #         list_shedules[aux].get('Shedules').get('introduction')

    for aux in range(len(shedules)):
        x = shedules.get('introduction')
        print(x)
    return render(request, 'pdfs/show_pdf.html',{'meeting': meeting,'shedules':shedules})
