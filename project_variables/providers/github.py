from project_variables.variables import event_name, event_action, comment_body, commit_message

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