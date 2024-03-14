import subprocess
from typing import List
from pathlib import Path


def run_command(cmd: List[str], check: bool = True):
    out = subprocess.run(cmd, stdout=subprocess.PIPE, check=check)
    print(out.stdout.decode("utf-8"))


def initialize_git():
    git_dir = Path(".git")
    if not git_dir.exists():
        run_command(["git", "init"])
    run_command(["git", "add", "--all"])
    run_command(["git", "commit", "-am", "Initial commit"])


def update_venv():
    venv_dir = Path(".venv")
    if not venv_dir.exists():
        run_command(["pdm", "venv", "create"])
        run_command(["pdm", "use", "--venv", "in-project"])
    run_command(["pdm", "lock"], check=False)
    initialize_git()
    run_command(["pdm", "install"], check=False)


def update_commit_hooks():
    run_command([".venv/bin/pre-commit", "install"])


def main():
    update_venv()
    update_commit_hooks()


if __name__ == "__main__":
    main()
