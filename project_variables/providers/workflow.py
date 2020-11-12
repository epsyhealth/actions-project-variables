import os


class WorkflowProvider:
    def is_enabled(self):
        return True

    def dump(self):
        trigger = "unknown"
        event_name = os.getenv("GITHUB_EVENT_NAME")
        event_action = os.getenv("GITHUB_EVENT_ACTION")
        comment_body = os.getenv("GITHUB_EVENT_COMMENT")

        if event_name == "issue_comment" and comment_body == "/deploy":
            trigger = "manual"
        elif event_name == "push":
            trigger = "push"
        elif event_name == "release" and event_action == "created":
            trigger = "release_created"
        elif event_name == "release" and event_action == "released":
            trigger = "release_published"

        return {"workflow": trigger}
