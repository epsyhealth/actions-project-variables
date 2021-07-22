import os
import re
from project_variables.variables import repository


class ProjectProvider:
    def is_enabled(self):
        return True

    def dump(self, variables):
        if repository:
            org, name = repository.split("/")
        else:
            name = os.getcwd().split("/")[-1]

        return dict(project_name=name, project_id=re.sub(r"\W+", "_", name))
