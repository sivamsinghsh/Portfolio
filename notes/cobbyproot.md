where I edit files, the staging area where git add prepares changes,
my local repository where git commit saves a permanent snapshot, and
the remote on GitHub that only updates when I push. I noticed this
because git status reported the same file as "modified" before
staging and "ready to commit" after, which showed me the working
directory and the index are separate places. Understanding this made
the pull request cycle make sense, my commits were safe locally the
whole time, but invisible to my teammate until git push copied them
to the remote.