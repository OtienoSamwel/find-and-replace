import glob
from typing import Optional

import typer

from . import __app_name__, __version__

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    return


@app.command()
def fp(pattern: str, replacement: str):
    matched_files = glob.glob("*.txt")
    # the pattern you want to replace
    pattern = pattern
    # what you want to replace it with
    replacement = replacement
    change_map = {}

    # the read operation for each file
    for file in matched_files:
        f = open(file, "r")
        change_map[file] = f.readlines()

        # loop through all the lines in the file to find the pattern
        for x in range(len(change_map[file])):
            if pattern in change_map[file][x]:
                change_map[file][x] = change_map[file][x].replace(pattern, replacement)

        f.close()

    # the write operation
    for file in matched_files:
        f = open(file, "w")
        f.writelines(change_map[file])
        f.close()
        print(f"{file} has been successfully updated")
