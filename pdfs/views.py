from django.views.generic import View
from django.http import HttpResponse

from pdfs.utileria import render_pdf

class PDF(View):

    def get(self, request, *args, **kwargs):

        pk = self.kwargs['pk']
        pdf = render_pdf('pdfs/pdf.html',pk)

        return HttpResponse(pdf, content_type='application/pdf')
