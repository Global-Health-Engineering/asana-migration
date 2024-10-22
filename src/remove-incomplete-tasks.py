import os
import git
import numpy as np
import pandas as pd


def get_git_root(path):
    git_repo = git.Repo(path, search_parent_directories=True)
    return git_repo.working_dir


def main():
    orig_dir = os.path.join(get_git_root(os.getcwd()),
                            "data",
                            "proj-with-incomplete-tasks")
    new_dir = os.path.join(get_git_root(os.getcwd()),
                           "data",
                           "proj-with-complete-tasks-only")

    for csv_name in os.listdir(orig_dir):
        if csv_name.split(".")[1].lower() == "csv":
            df = pd.read_csv(os.path.join(orig_dir, csv_name),
                             sep=",",
                             index_col="Task ID")
            df = df[df["Completed At"].isnull()]
            df.to_csv(os.path.join(new_dir, csv_name))
        else:
            print(f"{csv_name} not converted")


if __name__ == "__main__":
    main()
