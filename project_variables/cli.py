import os
from collections import OrderedDict
from os.path import isfile

import click
import yaml
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
@click.option("--work-dir", default=os.getcwd())
def run(debug, work_dir):
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
            variables["project_config"] = yaml.load(stream, Loader)

    variables["is_library"] = False
    variables["aws_account_group"] = "main"
    for provider in [p for p in providers if p.is_enabled()]:
        variables.update(provider.dump(variables))

    del variables["project_config"]

    for k, v in variables.items():
        if debug:
            click.secho(f"{k}::{v}", fg="green")

        click.echo(f"::set-output name={k}::{v if type(v) != bool else str(v).lower()}")
