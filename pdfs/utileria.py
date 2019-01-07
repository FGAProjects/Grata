from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

from meetings.models import Meeting
from jsons.utils import list_shedules,list_topics

def render_pdf(url_template,pk):

    meeting = Meeting.objects.get(id=pk)
    shedules = list_shedules()
    topics = list_topics()

    template = get_template(url_template)

    contexto = {
        'meeting': meeting,
        'shedules': shedules,
        'topics': topics
    }

    html = template.render(contexto)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')),result)

    if not pdf.err:

        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None