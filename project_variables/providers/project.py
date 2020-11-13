import os
import re


class ProjectProvider:
    def is_enabled(self):
        return True

    def dump(self, variables):
        repository = os.getenv("GITHUB_REPOSITORY")

        if repository:
            org, name = repository.split("/")
        else:
            name = os.getcwd().split("/")[-1]

        return dict(project_name=name, project_id=re.sub(r"\W+", "_", name))
