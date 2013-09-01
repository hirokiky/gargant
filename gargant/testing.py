from webob import Request


def request_factory(path):
    env = {'PATH_INFO': path,
           'REQUEST_METHOD': 'GET',
           'SERVER_PROTOCOL': 'HTTP/1.0',
           'HTTP_HOST': 'test.com:8000',
           'wsgi.url_scheme': 'http'}
    return Request(env)
