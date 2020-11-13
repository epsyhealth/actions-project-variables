from os.path import isfile


class DockerProvider:
    def is_enabled(self):
        return isfile("Dockerfile")

    def dump(self, variables):
        return dict(use_dockerlint=isfile("Dockerfile"))
