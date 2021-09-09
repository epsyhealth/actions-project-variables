from project_variables.variables import comment_body, commit_message, event_action, event_name


class GithubProvider:
    def is_enabled(self):
        return True

    def dump(self, variables):
        local = {}
        deployable = True
        if event_name == "issue_comment" and comment_body.startswith("/build"):
            deployable = False
        if event_name == "push" and "/build" in commit_message:
            deployable = False
        local["deployable"] = deployable
        return local
