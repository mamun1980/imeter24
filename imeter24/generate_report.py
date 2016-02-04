from django import http
from django.template.loader import get_template
from django.template import Context
import ho.pisa as pisa
import cStringIO as StringIO
import cgi

def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(
        html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), mimetype='application/pdf')
    return http.HttpResponse('Gremlin\'s ate your pdf! %s' % cgi.escape(html))

def article(request, id):
    article = get_object_or_404(Article, pk=id)

    return write_pdf('dtd/pdf/template.html',{
        'pagesize' : 'A4',
        'article' : article})