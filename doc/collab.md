# Collaboration

```{discussion}
**Optional**
- Have you downloaded programs/tools from GitHub?
- Have you uploaded your own programs/tools and believe that people are using your tool?
```

```{instructor-note}
- GitHub Lecture+discussion 25 min

```

Different types of remotes:
- If you have a server you can ssh to, you can use that as a remote.
- [GitHub](https://github.com) is a popular, closed-source commercial site.
- [GitLab](https://about.gitlab.com) is a popular, open-core
  commercial site.  Many universities have their own private GitLab servers
  set up.
- [Bitbucket](https://bitbucket.org) is yet another popular commercial site.
- Another option is [NotABug](https://notabug.org)
-
  
## Github
There are two more ways to create “copies” of repositories into your user space:

    A repository can be marked as template and new repositories can be generated from it, like using a cookie-cutter. The newly created repository will start with a new history, only one commit, and not inherit the history of the template.

## Commits, branches, repositories, forks, clones

- **repository**: The project, contains all data and history (commits, branches, tags).
- **commit**: Snapshot of the project, gets a unique identifier (e.g. `c7f0e8bfc718be04525847fc7ac237f470add76e`).
- **branch**: Independent development line, often we call the main development line `master` or `main`.
- **tag**: A pointer to one commit, to be able to refer to it later. Like a [commemorative plaque](https://en.wikipedia.org/wiki/Commemorative_plaque)
  that you attach to a particular commit (e.g. `phd-printed` or `paper-submitted`).
- **cloning**: Copying the whole repository to your laptop - the first time. It is not necessary to download each file one by one.
- **forking**: Taking a copy of a repository (which is typically not yours) - your
  copy (fork) stays on GitHub and you can make changes to your copy.

- `git clone` copies everything: all commits and all branches.
- Branches on the remote appear as (read-only) local branches with a prefix, e.g. `origin/master`.
- We synchronize commits between local and remote with `git fetch`/`git pull` and `git push`.
- Repositories that are shared online often synchronize via pull requests or merge requests.
- Repositories that are forked or cloned do not automatically synchronize themselves.

## Centralized workflow
```{figure} img/centralized.svg
:alt: Centralized layout
:width: 50%

Centralized layout. **Red** is the repository on GitHub.  **Blue** is
where all contributors work on their own computers.
```

- Centralized workflow is often used for remote collaborative work.
- `origin` refers to where you cloned from (but you can relocate it).
- `origin/mybranch` is a read-only pointer to branch `mybranch` on `origin`.
- These read-only pointers only move when you `git fetch`/`git pull` or `git push`.

## Distributed version control and Forking workflow

```{figure} img/forking-overview.svg
:alt: Centralized layout
:width: 50%

Forking workflow.  **Red** is the central repository, where only
owners have access.  **Green** are *forks* on Github (copy for a
single user to work on).  **Blue** are local copies where contributors
work on their own computer.
```

In the forking layout described above we work with **multiple remotes**,
in this case **two remotes**: One remote refers to the "central" repository, and the other
remote refers to the fork.


- Working with multiple remotes is not as scary as it might look.
- `origin` is just an alias/placeholder.
- We can add and remove remotes.
- We can call these aliases/placeholders as we like.
- We typically synchronize/updates remotes via the local clone.
- To see all remotes use `git remote -v`.
- If you are more than one person contributing to a project, consider using code review.

## How to contribute changes to somebody else's project

- Avoid frustration and surprises by first discussing and then coding.

### Contributing very minor changes

- Fork repository
- Create a branch
- Commit and push change
- File a pull request or merge request


### If you observe an issue and have an idea how to fix it

- Open an issue in the repository you wish to contribute to
- Describe the problem
- If you have a suggestion on how to fix it, describe your suggestion
- Possibly **discuss and get feedback**
- If you are working on the fix, indicate it in the issue so that others know that somebody is working on it and who is working on it
- Submit your fix as pull request or merge request which references/closes the issue

```{keypoints}
- Communicate and discuss before coding massive changes.
- **Cross-reference discussions, proposals, and code changes**.
```
