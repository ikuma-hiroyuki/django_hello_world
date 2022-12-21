from django.http import HttpResponse


def top_view(request):
    return HttpResponse('<h1>Top Page</h1>')
