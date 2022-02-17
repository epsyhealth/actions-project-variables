import configparser
import time
from os.path import isfile

from project_variables.variables import github_ref, github_sha


class VersionProvider:
    def is_enabled(self):
        return True

    def dump(self, variables):
        if "refs/tags" in github_ref:
            package_version = github_ref.replace("refs/tags/", "")
        elif github_sha:
            package_version = github_sha[0:8]
        else:
            package_version = f"build-{int(time.time())}"

        current_version = None
        if isfile(".bumpversion.cfg"):
            config = configparser.ConfigParser()
            config.read(".bumpversion.cfg")
            current_version = config["bumpversion"]["current_version"]

        return dict(package_version=package_version, current_version=current_version)
