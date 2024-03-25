import subprocess


def test_template_no_c_no_obfusc(copie):
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
    # with open('/home/yannbdt/repos/python-tas-template/toto_no_c_no_obfusc.txt','w') as f:
    #     f.write(str(result.project_dir))
    subprocess.check_call(["pdm", "run", "pytest"], cwd=result.project_dir)


def test_template_c_no_obfusc(copie):
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
    #     with open('/home/yannbdt/repos/python-tas-template/toto_c_no_obfusc.txt','w') as f:
    #         f.write(str(result.project_dir))
    subprocess.check_call(["pdm", "run", "pytest"], cwd=result.project_dir)


def test_template_no_c_obfusc(copie):
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
    #     with open('/home/yannbdt/repos/python-tas-template/toto_no_c_obfusc.txt','w') as f:
    #         f.write(str(result.project_dir))
    subprocess.check_call(["pdm", "run", "pytest"], cwd=result.project_dir)


def test_template_c_obfusc(copie):
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
    #     with open('/home/yannbdt/repos/python-tas-template/toto_c_obfusc.txt','w') as f:
    #         f.write(str(result.project_dir))
    subprocess.check_call(["pdm", "run", "pytest"], cwd=result.project_dir)
