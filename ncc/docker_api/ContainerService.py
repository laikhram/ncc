import docker
from ContainerService import *


class ContainerService(object):
    def __init__(self):
        self.client = docker.from_env()

    def is_image_exist(client, image_name):
        try:
            client.images.get(image_name)
            print ("Image is Exist")
        except:
            print ("Image is Not Exist")
            client.images.pull(image_name)

    def is_container_name_exist(self, container_name):
        try:
            self.client.containers.get(container_name)
            return True
        except docker.errors.NotFound as ex:
            print ex
            print "Container '" + container_name + "' is not exist."
            return False

    def create_container(self, image_name, container_name, environment=None):
        try:
            container_info = self.client.containers.run(image_name, detach=True, environment=environment,
                                                        name=container_name, publish_all_ports=True)
            print container_info
            print "create_container method is running."
        except docker.errors.APIError as ex:
            print "Container '" + container_name + "' is already exist... Try to start this container. ---v"
            print self.client.containers.get(container_name).start()
            print "Container '" + container_name + "' is started."

    def containerStart(self, container_name):
        self.client.containers.get(container_name).start()
        print "Container '" + container_name + "' is started."

    def containerStop(self, container_name):
        self.client.containers.get(container_name).stop()
        print "Container '" + container_name + "' is stop."

    def main():
        # client = docker.from_env()
        # user_id = '56130500059'
        # alias_name = 'web'
        # image_name = "nginx"
        # container_name = user_id + '_' + alias_name + '_' + image_name
        # print container_name
        c = ContainerService()
        c.is_container_name_exist('hello')

    if __name__ == "__main__":
        main()
