# GitHub setup
Local `.git` exists. At inspection it had no commits, no remote, and all source files were untracked. GitHub CLI reports no authenticated hosts; VS Code account sign-in does not establish CLI authentication. Repository URL/name is pending user input.

No remote repository was created and no code was uploaded in this resumed session.

```bash
gh auth login
cd /home/luke/Projects/nucaloric-site
git status
```

Choose the intended repository and configure your actual author identity before the first commit. Then commit the reviewed files and attach the supplied remote. For a new repository, prefer private visibility unless explicitly requested otherwise. `.gitignore` excludes dependencies, dotenv files, and logs.

Documentation and review artifacts are prepared locally. Do not commit credentials or the private conversation archive to a public repository.
