class IPAddressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        try:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        except KeyError:
            pass
        else:
            ip = ip.split(',')[0]
            request.META['REMOTE_ADDR'] = ip
        return self.get_response(request, *args, **kwargs)
