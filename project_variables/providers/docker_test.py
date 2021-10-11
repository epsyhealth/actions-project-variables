from os.path import isfile


class DockerTestProvider:
    def is_enabled(self):
        return isfile("Dockerfile.tests")

    def dump(self, variables):
        return dict(run_docker_tests=isfile("Dockerfile.tests"))
