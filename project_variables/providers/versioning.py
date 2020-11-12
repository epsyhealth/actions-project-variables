import os


class VersionProvider:
    def is_enabled(self):
        return True

    def dump(self):
        github_ref = os.getenv("GITHUB_REF", "")
        github_sha = os.getenv("GITHUB_SHA", "")

        if "ref/tag" in github_ref:
            package_version = github_ref.replace("ref/tag", "")
        else:
            package_version = github_sha[0:8]

        return dict(package_version=package_version)
