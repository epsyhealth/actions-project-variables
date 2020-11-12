import os
import re


class ProjectProvider:
    def is_enabled(self):
        return True

    def dump(self):
        repository = os.getenv("GITHUB_REPOSITORY")

        if not repository:
            return {}

        org, name = repository.split("/")

        return dict(project_name=name, project_id=re.sub(r"\W+", "_", name))
