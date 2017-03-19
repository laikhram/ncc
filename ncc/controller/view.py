from django.http import HttpResponse
from django.template import Template
from django.shortcuts import render
from django.template import Context
from django.shortcuts import redirect
import json

from ncc.ncc.docker_api.ContainerService import ContainerService
from ncc.model import Port
from ncc.model.LdapConnection import LdapConnection


# def index(request):
#     # return render(request, 'login.html', Context({'var': 'hello'}))
#     return HttpResponse("Hello")


def login(request):
    if request.method == 'POST':
        try:
            user = LdapConnection().getLdapConnection(request.POST['username'], request.POST['password'])
            request.session['user'] = user
            json_response = json.dumps({"error": False})
            # return render(request, 'userdetail.html', Context({'name': request.session['user']}))
            return HttpResponse(json_response)
        except Exception as ex:
            print ex
            json_response = json.dumps({"error": True, "message": "Worng username or password"})
            return HttpResponse(json_response)
            # return render(request, 'options.html', Context({'error': 'Worng username or password'}))



def ldap_authen(request):
    if request.method == 'POST':
        user = LdapConnection().getLdapConnection(request.POST['username'], request.POST['password'])
        request.session['user'] = user
        # return HttpResponse(user._User__userid)
        # print request.session['user']._User__userid
        return render(request, 'userdetail.html', Context({'name': request.session['user']}))


def container_prepare(request):
    userid = request.session['user'].userid
    alias_name = request.POST.getlist('container_name')
    image_name = request.POST['container_service']
    # env = 'MYSQL_ROOT_PASSWORD=' + request.POST['MYSQL_ROOT_PASSWORD']
    env_list = [u'MYSQL_ROOT_PASSWORD=root']
    container_name = userid + '_' + alias_name[0] + '_' + image_name
    container = ContainerService()
    if container.is_container_name_exist(container_name):
        pass
    else:
        container.create_container(image_name, container_name, environment=env_list)
        # ports = Port().get_ports(container_name)
        print 'Done!'
    return HttpResponse("Hello")


def home(request):
    return render(request, 'index.html')


def options(request):
    if request.method == 'POST':
        option = request.POST.getlist('option')
        print option
        if option == 'basic':
            return redirect('http://google.com')
        elif option == 'advance':
            return redirect('http://facebook.com')


def index(request):
    return render(request, 'options.html')


def container_basic(request):
    return render(request, 'basic.html')


def container_advance(request):
    return render(request, 'advance.html')


def container_detail(request):
    option = request.GET['option']
    print option
    if option == 'basic':
        return render(request, 'basic.html')
    elif option == 'advance':
        return render(request, 'advance.html')
