from pyramid.view import view_config
from pyramid.response import Response
from d0nut_sh.utils.security import Authorization


def web(route_name, renderer='', auth=Authorization.Guest):
    if renderer == '':
        # If we haven't set a renderer, we probably want to use the template with the name of the route
        renderer = 'templates/{route_name}.jinja2'.format(route_name=route_name)

    def wrapper(inner_func):
        @view_config(route_name=route_name, renderer=renderer, _depth=1)
        def handler(request):
            if auth.value ^ Authorization.Guest.value != 0:
                return Response("<html><h1>Unauthorized</h1></html>", status='401 Unauthorized')
            # Check authorization
            # 1. get session cookie
            # 2. look up user information to build authorization
            # 3. validate user meets minimum authorization requirements
            # 4. 401 if not, otherwise continue

            return inner_func(request)
        return handler

    return wrapper