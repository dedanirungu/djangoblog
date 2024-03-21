from django.shortcuts import render

# Create your views here.

def handler404(request, *args, **argv):

    # Render the HTML template index.html with the data in the context variable
    return render(request, '404.html', context=RequestContext(request))


def handler500(request, *args, **argv):

    # Render the HTML template index.html with the data in the context variable
    return render(request, '500.html', context=RequestContext(request))
