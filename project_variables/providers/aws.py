class AWSProvider:
    def is_enabled(self):
        return True

    def dump(self, variables):
        stages = {
            "pull_request": "playground",
            "manual": "playground",
            "push": "development",
            "release_created": "staging",
            "release_published": "production",
        }

        stage = stages.get(variables.get("workflow", "manual"))

        return dict(
            stage=stage,
            aws_account_key=f"AWS_{stage}_ACCOUNT_ID".upper()
        )
