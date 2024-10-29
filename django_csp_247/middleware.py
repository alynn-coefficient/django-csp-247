def injected_script(csp_nonce):
    return (
        f'<script type="text/javascript" nonce="{csp_nonce}">\n'
        'alert("Test!");\n'
        "</script>"
    ).encode("utf-8")


def csp_using_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        # Inject something into the response which uses the CSP nonce
        if response.headers.get("Content-Type") == "text/html":
            # Inject a script before the closing body tag
            response.content = response.content.replace(
                b"</body>", injected_script(str(request.csp_nonce)) + b"</body>"
            )
        return response

    return middleware
