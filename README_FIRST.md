# Template repository #
A generic template repository from which you can create other standard repositories.

The files included are this README_FIRST.md, a generic README.md and a standard .gitignore.

Fill in the README.md with the client details as needed.

Rename the main branch (master) as needed; for example Odoo repositories use braches named as the target version (16.0, etc) while other types of repositories may use the classic master, testing convention.
```
 $ git branch -m <new_name>
 $ git push origin -u <new_name>
 # Delete the <old_name> remote branch:
 $ git push origin --delete <old_name>
```
