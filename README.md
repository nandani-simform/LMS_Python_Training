This branch will demonstrate LMS git practical with git commands with proper description.

1. PULL and MERGE
    -> MERGE:   It is used to merge two branches locally. (suppose B is getting merged in A)
                For this checkout to branch A
                command:    git merge B

                            git checkout git_practical
                            git merge git_practical2
                            git push origin git_practical

    -> PULL REQUEST: Pull requests let you tell others about changes you've pushed to a branch in a repository on GitHub. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add follow-up commits before your changes are merged into the base branch.

                Some changes were made on git_practical2 and pushed on git_practical2
                            git push origin git_practical2

                On github, pull request is created from git_practical2 to git_practical compared ,review and then merge pull request.


2. Change commit message: Amending a commit is a way to modify the most recent commit we have made in our current branch. This can be helpful if yowe need to edit the commit message or if we forgot to include changes in the commit. 
                            git commit --amend
                Text editor will open, edit the commit messge then save it. To chow on github push it -
                            git push --force origin git_practical2


3. Cherry pick: cherry-pick means a commit on one branch to create a copy of the commit with the same changes on another branch. If we commit changes to the wrong branch or want to make the same changes to another branch, we can cherry-pick the commit to apply the changes to another branch.


                    
                    







                    