import os
from pathlib import Path
from subprocess import PIPE, Popen

HERE = Path(__file__).parent


def echo_foo():  # type: ignore
    print("foo")


def fork_run():  # type: ignore
    process = Popen(
        ["/bin/bash", HERE.joinpath("run.sh")],
        cwd=str(HERE),
        env=os.environ.copy(),
        encoding="utf-8",
        stdout=PIPE,
        stderr=PIPE,
    )
    stdout, stderr = process.communicate()
    print(stdout)
    print(stderr)
    return process.returncode
