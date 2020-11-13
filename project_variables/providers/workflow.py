import os


class WorkflowProvider:
    def is_enabled(self):
        return True

    def dump(self, variables):
        trigger = "manual"
        event_name = os.getenv("GITHUB_EVENT_NAME")
        event_action = os.getenv("GITHUB_EVENT_ACTION")
        comment_body = os.getenv("GITHUB_EVENT_COMMENT")

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
