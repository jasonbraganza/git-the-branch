from collections import namedtuple
from datetime import datetime

from git import Repo


def main():

    # Set up house. Creating a dict to hold the details we need, and a named tuple for easy access
    printlog = {}
    collect_log_details = namedtuple(
        "collect_log_details",
        ["branch_name", "committer_name", "sha_num", "commit_message"],
    )

    # Check if a repo exists in the current folder, otherwise bounce down to exception handler.
    try:
        # create a git repo object (of the current folder) and get a list of local branches
        r = Repo()
        head_list = r.heads

        # loop throught the branches, pull out details (branch name, commit date, author, commit sha, and the commit message) and then put them all in a dictionary with the date as key.
        for each_head in head_list:
            head_name = each_head.name
            get_last_commit_details = each_head.log()[-1]
            commit_date_utc = datetime.fromtimestamp(get_last_commit_details.time[0])
            commit_date_local = commit_date_utc.astimezone()
            commit_author_name, commit_sha, commit_details = (
                get_last_commit_details.actor,
                get_last_commit_details.newhexsha,
                get_last_commit_details.message,
            )
            log_details = collect_log_details(
                branch_name=head_name,
                committer_name=commit_author_name,
                sha_num=commit_sha,
                commit_message=commit_details,
            )
            printlog[commit_date_local] = log_details

        # Templates to generate time (in sane, readable terms) and output.
        print_date_format = "%a, %Y-%m-%d %H:%M"
        print_header = f'{"Date":<20s}\t{"Commit Hash":<15s}\t{"Author Name":<25s}{"Branch":<40s}{"Commit Message"}\n'

        # Finally present what we fished from the repo, to the user.
        print(print_header)

        for key in reversed(sorted(printlog)):
            print_date = key.strftime(print_date_format)
            print(
                f"{print_date:<20s}\t{printlog[key].sha_num[:7]:<15s}\t{str(printlog[key].committer_name):<25s}{printlog[key].branch_name:<40s}{printlog[key].commit_message}"
            )
    except:
        print("No git repo found in this folder")


if __name__ == "__main__":
    main()