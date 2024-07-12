import os
import sys
from typing import Generator

import pytest


@pytest.fixture(scope="session", autouse=True)
def reset_argv() -> Generator[None, None, None]:
    original_argv = sys.argv[:]
    sys.argv = ["sapporo"]

    yield

    sys.argv = original_argv


@pytest.fixture(scope="session", autouse=True)
def reset_os_env() -> Generator[None, None, None]:
    original_os_env = os.environ.copy()
    os.environ.clear()

    yield

    os.environ.clear()
    os.environ.update(original_os_env)
