from typing import List, Optional
import rich 
import typer

Term = typer.Typer()


@Term.command("show runngin containers")
def show_running_containers(conatiners):
    for _ in conatiners:
        rich.print("[magenta][b]Running Containers |")


if __name__ == '__main__':
    typer.run(show_running_containers)