import os
github_ref = os.getenv("GITHUB_REF", "")
github_sha = os.getenv("GITHUB_SHA", "")
event_name = os.getenv("GITHUB_EVENT_NAME")
event_action = os.getenv("GITHUB_EVENT_ACTION")
comment_body = os.getenv("GITHUB_EVENT_COMMENT")
commit_message = os.getenv('GITHUB_COMMIT_MESSAGE', "")
repository = os.getenv("GITHUB_REPOSITORY")