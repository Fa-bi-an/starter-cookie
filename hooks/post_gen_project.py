import sys, os, shutil
from pathlib import Path

def main() -> None:
    use_dvc = "{{ cookiecutter.use_dvc }}"
    have_examples = "{{ cookiecutter.have_examples }}"
    project = "{{ cookiecutter.project_slug }}"
    print("********** POST GENERATION HOOK *************")
    
    if use_dvc == 'no':
        print("Deleting DVC related files:")
        delete_entity(Path(".dvc"))
        delete_entity(Path(".dvcignore"))
        print("All DVC related files are deleted.")
             

def delete_entity(entity:Path()) -> None:
    print(entity)
    if entity.is_file():
        os.remove(entity)
    elif entity.is_dir():
        shutil.rmtree(entity)
    else:
        raise FileNotFoundError("File or directory does not exists.")


if __name__ == '__main__':
    main()

