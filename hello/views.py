from django.http import HttpResponse
from django.views.generic import TemplateView


def hello(request):
    return HttpResponse('<h1>hello world</h1>')


class HelloView(TemplateView):
    template_name = 'hello.html'
