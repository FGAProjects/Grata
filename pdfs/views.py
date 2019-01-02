import json

from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,landscape
from reportlab.platypus import Image

from meetings.models import Meeting

def pdf_file(request,pk):

    meeting = Meeting.objects.get(id=pk)

    with open("jsons/shedule.json", "r") as read_file:
        data = json.load(read_file)

    print(data)

    return render(request, 'pdfs/show_pdf.html',{'meeting': meeting, 'data':data})
