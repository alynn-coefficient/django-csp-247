from django.http import HttpResponse


def example_view(request):
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Test page</title>
        </head>
        <body>
            <h1>Test page</h1>
        </body>
    </html>
    """
    return HttpResponse(html, content_type="text/html")
