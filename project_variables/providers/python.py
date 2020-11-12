from os.path import isfile


class PythonProvider:
    def is_enabled(self):
        return True

    def dump(self):
        python_version = "3.7"
        if isfile(".python-version"):
            python_version = open(".python-version").read().strip()

        return dict(python_version=python_version)
