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

        local = {}
        stage = variables.get("stage")
        if "stage" not in variables:
            stage = stages.get(variables.get("workflow", "manual"))
            local["stage"] = stage

        local["aws_account_key"] = f"AWS_{stage}_ACCOUNT_ID".upper()

        return local
