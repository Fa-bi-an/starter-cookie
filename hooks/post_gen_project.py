import os
import shutil
import sys
from pathlib import Path


def main() -> None:
    use_dvc = "{{ cookiecutter.use_dvc }}"
    precommit = "{{ cookiecutter.use_precommit }}"
    do_modelling = "{{ cookiecutter.do_modelling }}"
    print("********** POST GENERATION HOOK *************")

    if use_dvc == "no":
        print("Deleting DVC related files:")
        delete_entity(Path(".dvc"))
        delete_entity(Path(".dvcignore"))
        print("All DVC related files are deleted.")
    if precommit == "no":
        print("Deleting pre-commit config.")
        delete_entity(Path(".pre-commit-config.yaml"))
        print("Pre-commit config deleted.")
    if do_modelling == "no":
        print("Deleting models dir.")
        delete_entity(Path("models"))
        print("Models dir deleted.")


def delete_entity(entity: Path()) -> None:
    print(f"   {entity}")
    if entity.is_file():
        os.remove(entity)
    elif entity.is_dir():
        shutil.rmtree(entity)
    else:
        raise FileNotFoundError("File or directory does not exists.")


if __name__ == "__main__":
    main()
