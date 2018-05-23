from d0nut_sh.utils.controllers import web
from d0nut_sh.utils.security import Authorization

@web(route_name='home', authorization=Authorization.Guest)
def home_view(request):
    return {'project': 'd0nut_sh'}
