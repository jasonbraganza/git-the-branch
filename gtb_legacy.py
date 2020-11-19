"""
First iteration of this program. Have kept it around to see progress :)
"""
from git import Repo


def main():
    """
    Uses GitPython to figure out local branches and print them out.
    Has a blanket catch for any exceptions
    """
    try:
        repo = Repo()
        print("Local Branches in this repo are: ")
        for each_item in repo.branches:
            print(f"\t {each_item}")
    except:
        print("No git repo found in this folder")


if __name__ == "__main__":
    main()
