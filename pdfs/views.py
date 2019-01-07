from jsons.utils import list_shedules,list_topics

from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from meetings.models import Meeting

def pdf_file(request,pk):

    meeting = Meeting.objects.get(id=pk)
    shedules = list_shedules()
    topics = list_topics()

    # for aux in shedules:
    #     for aux2 in topics:
    #         print(aux.introduction)
    #         print(aux2.topic_name)

    pdf_file_name = 'Relatório_da Reunião Número: '+ str(meeting.id) + '.pdf'
    generate_report(shedules,topics,pdf_file_name,pk)

    return render(request, 'pdfs/show_pdf.html',{'meeting': meeting,
                                             'shedules':shedules,
                                             'topics': topics})

def generate_report(shedules,topics,pdf_file_name,pk):

    meeting = Meeting.objects.get(id=pk)
    pdf = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))
    dimension_y = 100
    image = 'projeto-grata/static/images/naruto.jpg'

    pdf.setFont('Helvetica', 35, leading=None)
    pdf.drawCentredString(400, 550, 'Relatório da Reunião Número: ' + str(meeting.id))
    pdf.setFont('Helvetica', 30, leading=None)
    pdf.drawCentredString(400, 500, 'Informações Sobre a Reunião')
    pdf.setLineWidth(.3)
    pdf.setFont('Helvetica', 20)

    pdf.drawString(dimension_y, 450, 'Título da Reunião: ' + meeting.subject_matter)
    pdf.drawString(dimension_y, 420, 'Projeto: ' + meeting.project)
    pdf.drawString(dimension_y, 390, 'Líder da Reunião: ' + meeting.meeting_leader)
    pdf.drawString(dimension_y, 360, 'Documentador: ' + meeting.documentary)
    pdf.drawString(dimension_y, 330, 'Local: ' + meeting.local)
    pdf.drawString(dimension_y, 300, 'Data de Ínicio: ' + meeting.project)
    pdf.drawString(dimension_y, 270, 'Data de Encerramento: ' + meeting.final_date)
    pdf.drawString(dimension_y, 240, 'Hora de Ínicio: ' + meeting.first_hour)
    pdf.drawString(dimension_y, 210, 'Hora de Encerramento: ' + meeting.final_hour)
    pdf.drawImage(image,330,50,width=150,height=100)
    pdf.showPage()

    pdf.setFont('Helvetica', 30, leading=None)
    pdf.drawCentredString(400, 550, 'Pauta da Reunião')
    pdf.setLineWidth(.3)
    pdf.setFont('Helvetica', 20)

    pdf.drawImage(image, 330, 50, width=150, height=100)

    pdf.save()