from utils.utils import list_shedules,list_topics

from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,landscape
from reportlab.platypus import Image

from meetings.models import Meeting

def pdf_file(request,pk):

    meeting = Meeting.objects.get(id=pk)

    shedules = list_shedules()
    topics = list_topics()

    return render(request, 'pdfs/show_pdf.html',{'meeting': meeting,
                                                 'shedules':shedules,
                                                 'topics': topics})