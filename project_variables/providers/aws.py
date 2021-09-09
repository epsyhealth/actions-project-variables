STAGES = {
    "pull_request": "playground",
    "manual": "playground",
    "push": "development",
    "release_created": "staging",
    "release_published": "production",
}

ENV_NAME_TO_SHORT = {
    "playground": "play",
    "development": "dev",
    "production" : "prod",
}


class AWSProvider:
    def is_enabled(self):
        return True

    def dump(self, variables):
        local = {}
        stage = variables.get("stage")
        if "stage" not in variables:
            stage = STAGES.get(variables.get("workflow", "manual"))
            local["stage"] = stage

        if "stage_short" not in variables:
            local["stage_short"] = ENV_NAME_TO_SHORT.get(stage, stage)

        local["aws_account_key"] = f"AWS_{stage}_ACCOUNT_ID".upper()

        return local
