from pathlib import Path
import typing as T
import subprocess


def list_wheel_files(project_dir: Path) -> T.List[Path]:
    listing = subprocess.check_output(
        ["unzip", "-t", "dist/*.whl"], stderr=subprocess.STDOUT, cwd=project_dir
    )
    flist = []
    for raw in listing.split(b"\n"):
        line = raw.decode("ascii")
        if line.startswith("    testing: "):
            fic = Path(line[13:-2].strip())
            flist.append(fic)
    return flist


def test_template_no_c_no_obfusc(copie):
    log_pth = Path("toto_no_c_no_obfusc.txt")
    log_pth.unlink(missing_ok=True)

    result = copie.copy(
        extra_answers={
            "project_name": "foo",
            "project_description": "tmp test project",
            "author_name": "Elon Musk",
            "author_email": "elon.musk@spacex.com",
            "is_c_extension": False,
            "is_obfuscated": False,
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    assert (result.project_dir / "README.md").exists()
    # with open(log_pth,'w') as f:
    #     f.write(str(result.project_dir))
    subprocess.check_call(["pdm", "run", "pytest"], subprocess.STDOUT, cwd=result.project_dir)
    subprocess.check_call(["pdm", "build"], cwd=result.project_dir)
    flist = list_wheel_files(result.project_dir)
    assert any([p.suffix == ".py" for p in flist])


def test_template_c_no_obfusc(copie):
    log_pth = Path("toto_c_no_obfusc.txt")
    log_pth.unlink(missing_ok=True)

    result = copie.copy(
        extra_answers={
            "project_name": "foo",
            "project_description": "tmp test project",
            "author_name": "Elon Musk",
            "author_email": "elon.musk@spacex.com",
            "is_c_extension": True,
            "is_obfuscated": False,
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    assert (result.project_dir / "README.md").exists()
    #     with open(log_pth,'w') as f:
    #         f.write(str(result.project_dir))
    subprocess.check_call(["pdm", "run", "pytest"], cwd=result.project_dir)
    subprocess.check_call(["pdm", "build"], cwd=result.project_dir)
    flist = list_wheel_files(result.project_dir)
    assert any([p.suffix == ".so" for p in flist])


def test_template_no_c_obfusc(copie):
    log_pth = Path("toto_no_c_obfusc.txt")
    log_pth.unlink(missing_ok=True)

    result = copie.copy(
        extra_answers={
            "project_name": "foo",
            "project_description": "tmp test project",
            "author_name": "Elon Musk",
            "author_email": "elon.musk@spacex.com",
            "is_c_extension": False,
            "is_obfuscated": True,
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    assert (result.project_dir / "README.md").exists()
    #     with open(log_pth,'w') as f:
    #         f.write(str(result.project_dir))
    subprocess.check_call(["pdm", "run", "pytest"], cwd=result.project_dir)
    subprocess.check_call(["pdm", "build"], cwd=result.project_dir)
    flist = list_wheel_files(result.project_dir)
    assert all([p.suffix != ".py" for p in flist])


def test_template_c_obfusc(copie):
    log_pth = Path("toto_c_obfusc.txt")
    log_pth.unlink(missing_ok=True)

    result = copie.copy(
        extra_answers={
            "project_name": "foo",
            "project_description": "tmp test project",
            "author_name": "Elon Musk",
            "author_email": "elon.musk@spacex.com",
            "is_c_extension": True,
            "is_obfuscated": True,
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    assert (result.project_dir / "README.md").exists()
    #     with open(log_pth,'w') as f:
    #         f.write(str(result.project_dir))
    subprocess.check_call(["pdm", "run", "pytest"], cwd=result.project_dir)
    subprocess.check_call(["pdm", "build"], cwd=result.project_dir)
    flist = list_wheel_files(result.project_dir)
    assert all([p.suffix != ".py" for p in flist])
    assert all([p.suffix != ".cpp" for p in flist])
    assert all([p.suffix != ".hpp" for p in flist])
    assert all([p.suffix != ".c" for p in flist])
    assert all([p.suffix != ".h" for p in flist])
