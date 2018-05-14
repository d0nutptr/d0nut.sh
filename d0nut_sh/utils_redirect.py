from pyramid.response import Response
from pyramid.view import view_config


def _check_missing_params(request, required_params):
    missing_params = [param for param in required_params if param not in request.params]

    if missing_params:
        message = ""

        for param in missing_params:
            message += "Missing param: {}\n".format(param)

        resp = Response(message)
        resp.headers['Content-Type'] = 'text/plain'
        return resp
    return None


@view_config(route_name='utils_redirect_home', renderer='prettyjson')
def redirect_home(request):
    return {'routes': ['302', '307', 'get_to_post']}


@ view_config(route_name='redirect_302')
def redirect_302(request):
    missing_params = _check_missing_params(request, ['url'])

    if missing_params:
        return missing_params

    url = request.params['url']
    resp = Response(status=302)
    resp.headers['Location'] = url
    return resp


@view_config(route_name='redirect_307')
def redirect_307(request):
    missing_params = _check_missing_params(request, ['url'])

    if missing_params:
        return missing_params

    url = request.params['url']
    resp = Response(status=307)
    resp.headers['Location'] = url
    return resp


@view_config(route_name='redirect_get_to_post', request_method='GET')
def redirect_get_to_post(request):
    missing_params = _check_missing_params(request, ['url'])

    if missing_params:
        return missing_params

    action = request.current_route_url()
    resp = Response(r'''
    <html>
        <form action="{}" method="POST"/>
        <script>document.getElementsByTagName("form")[0].submit();</script>
    </html>'''.format(action), status=200)
    resp.headers['Content-Type'] = 'text/html'
    return resp


@view_config(route_name='redirect_get_to_post', request_method='POST')
def redirect_get_to_post_via_post(request):
    missing_params = _check_missing_params(request, ['url'])

    if missing_params:
        return missing_params

    url = request.params['url']

    resp = Response(status=307)
    resp.headers['Location'] = url
    return resp