from d0nut_sh.utils import web

@web(route_name='home')
def home(request):
    return {'project': 'd0nut_sh'}
