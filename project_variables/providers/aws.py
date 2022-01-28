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
    "production": "prod",
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

        account_group = variables["aws_account_group"]
        if "project_config" in variables:
            config_account_group = variables.get("project_config", {}).get("aws", {}).get("accountGroup")
            if config_account_group:
                account_group = config_account_group
                local["aws_account_group"] = account_group

        account_id_stage = stage
        if stage in ["staging", "production"] and account_group == "dataScience":
            account_id_stage += "_DS"
        local["aws_account_key"] = f"AWS_{account_id_stage}_ACCOUNT_ID".upper()

        return local
