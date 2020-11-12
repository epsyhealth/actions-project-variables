import os

import click

from project_variables.providers.docker import DockerProvider
from project_variables.providers.github import GithubProvider
from project_variables.providers.poetry import PoetryProvider
from project_variables.providers.project import ProjectProvider
from project_variables.providers.python import PythonProvider
from project_variables.providers.versioning import VersionProvider
from project_variables.providers.workflow import WorkflowProvider


@click.command()
@click.option("--debug", is_flag=True)
@click.option("--work-dir", default=os.getcwd())
def run(debug, work_dir):
    os.chdir(work_dir)
    providers = (
        WorkflowProvider(),
        ProjectProvider(),
        PoetryProvider(),
        PythonProvider(),
        DockerProvider(),
        GithubProvider(),
        VersionProvider(),
    )

    variables = {}
    for provider in [p for p in providers if p.is_enabled()]:
        variables.update(provider.dump())

    for k, v in variables.items():
        if debug:
            click.secho(f"{k}::{v}", fg="green")

        click.echo(f"::set-output name={k}::{v if type(v) != bool else str(v).lower()}")
