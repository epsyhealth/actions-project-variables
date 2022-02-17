import io
import os
from collections import OrderedDict
from os.path import isfile

import click
import yaml
from actions_toolkit import core

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from project_variables.providers.aws import AWSProvider
from project_variables.providers.docker import DockerProvider
from project_variables.providers.docker_test import DockerTestProvider
from project_variables.providers.github import GithubProvider
from project_variables.providers.poetry import PoetryProvider
from project_variables.providers.project import ProjectProvider
from project_variables.providers.python import PythonProvider
from project_variables.providers.versioning import VersionProvider
from project_variables.providers.workflow import WorkflowProvider

CONFIG_FILE = ".github/config.yml"


@click.command()
@click.option("--debug", is_flag=True)
@click.option("--export", is_flag=True, default=False)
@click.option("--save", is_flag=True, default=False)
@click.option("--work-dir", default=os.getcwd())
def run(debug, work_dir, export, save):
    os.chdir(work_dir)
    providers = [
        WorkflowProvider(),
        ProjectProvider(),
        VersionProvider(),
        PoetryProvider(),
        PythonProvider(),
        DockerProvider(),
        DockerTestProvider(),
        GithubProvider(),
        AWSProvider(),
    ]

    variables = OrderedDict()

    variables["project_config"] = {}
    if isfile(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as stream:
            variables["project_config"] = yaml.safe_load(stream)

    variables["is_library"] = False
    variables["aws_account_group"] = "main"
    for provider in [p for p in providers if p.is_enabled()]:
        variables.update(provider.dump(variables))

    del variables["project_config"]

    buffer = io.StringIO()

    for k, v in variables.items():
        if debug:
            click.secho(f"{k}::{v}", fg="green")

        value = v if type(v) != bool else str(v).lower()
        core.set_output(k, value)
        if export:
            core.export_variable(f"project_{k}", value)

        if save:
            buffer.write(f"echo 'project_{k}={value}' >> $GITHUB_ENV\n")

    if save:
        with open(".variables", "w+") as f:
            buffer.seek(0)
            f.write(buffer.read())
