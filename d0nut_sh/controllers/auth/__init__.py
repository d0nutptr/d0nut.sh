from d0nut_sh.utils.controllers import web
from d0nut_sh.utils.security import Authorization


@web(route_name='auth/login', authorization=Authorization.Guest)
def login(request):
    return {'csrf': """<input type="hidden" value="CSRF_TOKEN_HERE" name="csrf">"""}