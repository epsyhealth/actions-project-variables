from os.path import isfile

import toml


class PoetryProvider:
    lock_file = "poetry.lock"
    project = "pyproject.toml"

    def is_enabled(self):
        return isfile(PoetryProvider.lock_file)

    def dump(self):
        lock = open(PoetryProvider.lock_file).read()
        packages = {
            package["name"]: package["version"]
            for package in toml.loads(lock).get("package")
        }

        library = False
        package_version = None
        if isfile(PoetryProvider.project):
            package = toml.loads(open(PoetryProvider.project).read())
            library = "library" in package.get("tool").get("poetry").get("keywords", [])
            package_version = package.get("tool").get("poetry").get("version")

        return dict(
            use_black=packages.get("black", 0),
            use_flake8=packages.get("flake8", 0),
            use_pytest=packages.get("pytest", 0),
            is_library=library,
            package_version=package_version,
        )
