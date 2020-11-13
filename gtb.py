from git import Repo


def main():
    try:
        repo = Repo()
        print("Local Branches in this repo are: ")
        for each_item in repo.branches:
            print(f"\t {each_item}")
    except:
        print("No git repo found in this folder")


if __name__ == "__main__":
    main()
