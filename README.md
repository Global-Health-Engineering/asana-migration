# asana-migration

The simple script `src/remove-incomplete-tasks.py` removes lines in all files in `data/proj-with-incomplete-tasks/*.csv` where tasks have completed date in `Completed At` column.

The script saves the dataframes to `data/proj-with-complete-tasks-only`. Those files can be then imported to asana without completed tasks.

To make it work:
1. add all `csv` files (each of them is a project from old asana space) to `data/proj-with-incomplete-tasks`
2. run `python src/remove-incomplete-tasks.py`
3. Import projects to from `data/proj-with-complete-tasks-only` to new asana space, one csv at a time, manually setting the name of the project (potentially the same as the old one).