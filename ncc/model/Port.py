import docker
from Port import *


class Port(object):
    __client = docker.from_env()

    def __init__(self, port=None, hostport=None, hostIP=None):
        self.__port = port
        self.__hostport = hostport
        self.__hostIP = hostIP

    def __str__(self):
        return self.__hostIP + ":" + self.__hostport + '->' + self.__port

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def get_ports(container_name):
        ports = []
        container_detail = Port.__client.containers.get(container_name).attrs.items()
        ports_object = dict(container_detail)[u'NetworkSettings'][u'Ports'].items()

        for key, value in ports_object:
            for x in value:
                ports.append(Port(key.encode('ascii'), x[u'HostPort'], x[u'HostIp']))

        print ports

    def main():
        Port().get_ports('database_phpmyadmin_1')

    if __name__ == '__main__':
        main()
