from d0nut_sh.utils.security import (
    Authorization,
    AuthorizationException,
    AuthorizationLevel,
)
from pyramid.request import Request
from pyramid.view import view_config
from typing import Any, Callable, Optional


def web(route_name: str,
        template_name: Optional[str] = None,
        authorization: AuthorizationLevel=Authorization.Admin) -> Callable:
    # Clean up arguments
    if template_name is None:
        template_name = route_name

    def wrapper(func: Callable) -> Callable:
        @view_config(route_name=route_name, renderer='templates/{}.jinja2'.format(template_name), _depth=1)
        def web_wrapper(request: Request) -> Any:
            # Check Authorization for request
            if not _check_authorization(request, authorization):
                raise AuthorizationException()

            return func(request)
        return web_wrapper
    return wrapper


def ajax(route_name: str) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def ajax_wrapper(request: Request) -> Any:

            return func(request)
        return ajax_wrapper
    return wrapper


def _check_authorization(request: Request, expected_authorization: AuthorizationLevel) -> bool:
    # TODO: Grab authorization for current request
    # Assume it's Guest at the moment
    presented_authorization: AuthorizationLevel = Authorization.Guest

    return Authorization.is_authorized(expected_authorization=expected_authorization, presented_authorization=presented_authorization)
