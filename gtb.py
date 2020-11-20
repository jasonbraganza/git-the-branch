from collections import namedtuple
from datetime import datetime

from git import Repo, objects


def main():
    r = Repo()

    head_list = r.heads

    printlog = {}
    collect_log_details = namedtuple(
        "collect_log_details",
        ["branch_name", "committer_name", "sha_num", "commit_message"],
    )

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

    print_date_format = "%a, %Y-%m-%d %H:%M"
    print_header = f'{"Date":<20s}\t{"Commit Hash":<15s}{"Branch":<20s}\t{"Author Name":<25s}{"Commit Message"}\n'

    print(print_header)

    for key in reversed(sorted(printlog)):
        print_date = key.strftime(print_date_format)
        print(
            f"{print_date:<20s}\t{printlog[key].sha_num[:7]:<15s}{printlog[key].branch_name:<20s}\t{str(printlog[key].committer_name):<25s}{printlog[key].commit_message}"
        )


if __name__ == "__main__":
    main()