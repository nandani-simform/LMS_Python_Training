This branch will demonstrate LMS git practical with git commands with proper description.

1. PULL and MERGE:
    -> MERGE: It is used to merge two branches locally. (suppose B is getting merged in A) For this checkout to branch A then run, git merge B

                    git checkout git_practical
                    git merge git_practical2
                    git push origin git_practical

    -> PULL REQUEST: Pull requests let you tell others about changes you've pushed to a branch in a repository on GitHub. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add follow-up commits before your changes are merged into the base branch.

                Some changes were made on git_practical2 and pushed on git_practical2
                    git push origin git_practical2

                On github, pull request is created from git_practical2 to git_practical compared ,review and then merge pull request.


2. AMEND: Amending a commit is a way to modify the most recent commit we have made in our current branch. This can be helpful if yowe need to edit the commit message or if we forgot to include changes in the commit. 
                    
                    git commit --amend
                Text editor will open, edit the commit message then save it. To show on github push it -
                    git push --force origin git_practical2


3. CHERRY-PICK: cherry-pick means a commit on one branch to create a copy of the commit with the same changes on another branch. If we commit changes to the wrong branch or want to make the same changes to another branch, we can cherry-pick the commit to apply the changes to another branch.

                Go to that branch from where we want to create copy-
                    git checkout git_practical

                Then run 'git log' command to display the most recent commits and the status of the head-
                    git log 

                Copy commit id which we want to copy
                Go to that branch where we want to create copy and run following commands-

                    git checkout git_practical2
                    git cherry-pick 4ca6d68a7320d857185a0ac9bb29752c799c6303
                    git push --force origin git_practical

4. RESET: It is used to delete commit from a branch.

                    git reset --hard HEAD~1 (delete latest commit)
                    git reset --hard HEAD~N (delete N-th latest commit)
                    git reset --hard <commit-id> (delete by hash code)

                Then run-
                    git push origin git_practical


5. REBASE: We can take all the changes that were committed on one branch and replay them on a different branch.
            
                commit changes in git_practical branch
                    git checkout git_practical2

                commit changes in git_practical2 branch
                    git checkout git_practical
                    git rebase git_practical2 (resolve merge conflicts in merge editor if have)

                This command is used to continue with the changes we made
                    git rebase --continue  

                If we want to skip the change, we can skip also
                    git rebase --skip



