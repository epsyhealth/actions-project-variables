from project_variables.variables import event_action, comment_body, event_name


class WorkflowProvider:
    def is_enabled(self):
        return True

    def dump(self, variables):
        trigger = "manual"
        local = {}
        if event_name == "issue_comment" and comment_body.startswith("/deploy"):
            trigger = "manual"
            stage = comment_body.replace("/deploy", "").strip() or "playground"
            local["stage"] = stage
        elif event_name == "push":
            trigger = "push"
        elif event_name == "release" and event_action == "created":
            trigger = "release_created"
        elif event_name == "release" and event_action == "released":
            trigger = "release_published"

        local["workflow"] = trigger

        return local
