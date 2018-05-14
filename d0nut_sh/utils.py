from pyramid.view import view_config


@view_config(route_name='utils_home', renderer='prettyjson')
def my_view(request):
    return {'routes': ['redirect']}