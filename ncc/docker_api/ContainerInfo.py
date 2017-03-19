import docker

from model.Port import Port

client = docker.from_env()
user_id = '56130500059'
alias_name = 'web'
image_name = "nginx"
container_name = user_id+'_'+alias_name+'_'+image_name
ports = []
print client.containers.get(container_name).attrs


ports = []
list = client.containers.get(container_name).attrs.items()
listPorts = dict(list)[u'NetworkSettings'][u'Ports'].items()
print listPorts

for key, value in listPorts:
    for x in value:
        ports.append(Port(key.encode('ascii'), x[u'HostPort'], x[u'HostIp']))

print ports
