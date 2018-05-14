from pyramid.config import Configurator
from pyramid.renderers import JSON


def utils_redirect(config):
    config.add_route('utils_redirect_home', '')
    config.add_route('redirect_302', '302')
    config.add_route('redirect_307', '307')
    config.add_route('redirect_get_to_post', 'get_to_post')

def utils(config):
    config.add_route('utils_home', '')
    config.include(utils_redirect, route_prefix='/redirect')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_renderer('prettyjson', JSON(indent=4))
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    config.include(utils, route_prefix='/utils')

    config.scan()
    return config.make_wsgi_app()
