import docker

class ImageSearch() :
    def main():
        client = docker.from_env()
        print client.images.search("ubuntu")


    if __name__ == "__main__":
        main()