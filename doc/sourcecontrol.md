# The iterations and Git
```{questions}
  - Why should you use source/version control?
```

```{Discussion} Have you used Git (locally) in your own work?
Answer in HackMD
```

```{Objectives}
   - We will
      - work with the basic commands in git
      - go through branching and merging
```

```{instructor-note}
```
This material is based on or inspired by the material from [NBIS](https://nbis-reproducible-research.readthedocs.io/en/course_2104/git/) and [CodeRefinery](https://coderefinery.github.io/git-intro/)

```{note}
- We will cover the most basic things with Git such that you can use it this week.
- For deeper understanding and hands-on on branching etcetera, please confer the course material of [NBIS](https://nbis-reproducible-research.readthedocs.io/en/course_2104/git/) and [CodeRefinery](https://coderefinery.github.io/git-intro/).
```

## Git

- We will start with our own repository.
- branching and merging (locally)
- and a brief introduction to pushing to remotes.
- In the separate collaborative Git lesson, we teach more use of remote repositories and good collaborative workflows. 


```{prereq}

   -  **Git and GITHUB should be configured prior to the course**
      following [https://coderefinery.github.io/installation](https://github.com/UPPMAX/programming_formalism/blob/main/setup.md)).
   -  Being comfortable with the command line. No expertise is required,
      but the lesson will be mostly taken from the command line.
   -  Students should be familiar with using a **text editor** on their
      system. Emacs and Vim are excellent choices if you know how to use
      them but Nano or Notepad on Windows are sufficient.
      
```

## Start with pushing your changes in the local Git to GitHub

 ```console
  $ git push
  ```

You should now see something like:

```text
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 846 bytes | 846.00 KiB/s, done.
Total 7 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To github.com:bclaremar/Formalisms.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

```

``````{admonition} If you get errors
---
class: warning, dropdown
---
If you instead get something like the below, your SSH keys are not correctly configured. 
```text
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```
If `ssh -T git@github.com` gives an error, this is the case.


- [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- Approximate steps
```console
ssh-keygen -t ed25519 -C "email address"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```
- [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
- Hope you can **fix this in Lunch Break**. **Follow the rest by listening for now.**

``````

**Reload your GitHub project website and - taa-daa - your commits should now be
online!**

What just happened? **Think of publishing a repository as uploading the `.git` part online**.

---

## Alternative way to initialize Git

```{admonition} A new repository from an existing project on own computer or HPC user account.

- Say you’ve got an existing project that you want to start tracking with git.

    - Go into the directory containing the project.
    - Type `git init`.
    - Type `git add` to add all of the relevant files.
    - You’ll probably want to create a `.gitignore` file right away, to indicate all of the files you don’t want to track. Use `git add .gitignore`, too.
    - Type `git commit`.

```

## Make the next iteration of the planet project

``````{challenge} Type-along: Add Jupiter
- We will add some lines to count with the effects from the gravity of Jupiter on Earth

```python



```

- Do **not** stage (add) yet!
``````

### git diff

When you are done editing the files, try `git diff`:

```console
  $ git diff
```

You will see (can you identify in there the two added lines?):

```diff

```

Now first stage and then commit (what happens when we leave out the `-m` flag?):

```console
  $ git add python.puml     # <-- we can state exactly which file to stage as well
  $ git commit                   # <-- we have left out -m "..."
```

  When you leave out the `-m` flag, Git should open an editor where you can edit
  your commit message. This message will be associated and stored with the
  changes you made. This message is your chance to explain what you've done and
  convince others (and your future self) that the changes you made were
  justified.  Write a message and save and close the file.

  When you are done committing the changes, experiment with these commands:

  ```console
  $ git log
  $ git log --stat
  $ git log --oneline
  ```
``````

(gitignore)=

## Ignoring files and paths with .gitignore

```{discussion}
- Should we add and track all files in a project?
- How about generated files?
- Why is it considered a bad idea to commit compiled binaries to version control?
- What types of generated files do you know?
```

## Branching and merging

- A branch is a division unit of work, to be merged with other units of work.
- A tag is a pointer to a moment in the history of a project.

```{figure} img/git-collaborative.svg
:alt: Isolated tracks
:width: 50%

Isolated tracks of work.
```


### Typical workflows

There are two typical workflows:

```console
$ git checkout -b new-feature  # create branch, switch to it
$ git commit                   # work, work, work, ..., and test
$ git checkout master          # once feature is ready, switch to master
$ git merge new-feature        # merge work to master
$ git branch -d new-feature    # remove branch
```

## Let's make our code modular (test in branch)

```{challenge} 

```console
$ git checkout -b wild-idea    # create branch, switch to it, work, work, work ...
$ git checkout master          # realize it was a bad idea, back to master
$ git branch -D wild-idea      # it is gone, off to a new idea
```

No problem: we worked on a branch, branch is deleted, `master` is clean.

```{note}
[More about branches](https://coderefinery.github.io/git-intro/branches/)
```


---


## Summary

Now we know how to save snapshots:

```console
$ git add <file(s)>
$ git commit
```

And this is what we do as we program.

Every state is then saved and later we will learn how to go back to these "checkpoints"
and how to undo things.

```console
$ git init    # initialize new repository
$ git add     # add files or stage file(s)
$ git commit  # commit staged file(s)
$ git status  # see what is going on
$ git log     # see history
$ git diff    # show unstaged/uncommitted modifications
$ git show    # show the change for a specific commit
$ git mv      # move tracked files
$ git rm      # remove tracked files
```

Git is not ideal for large binary files
(for this consider [http://git-annex.branchable.com](http://git-annex.branchable.com)).

### Docstrings
A docstring is a structured comment associated to a segment of code (i.e. function or class)

Good docstrings describe:
   - What the function does
   - What goes in (including the type of the input variables)
   - What goes out (including the return type)
   - Python example: help(<function name>)
   

```{Keypoints}
- Initializing a Git repository is simple: git init.
- Commits should be used to tell a story.
- Git uses the .git folder to store the snapshots.
- Don’t be afraid to stage and commit often. Better too often than not often enough.
- A branch is a division unit of work, to be merged with other units of work.
- A tag is a pointer to a moment in the history of a project.
- A repository can have one or multiple remotes (we will revisit these later).
- Local branches often track remote branches.
- A remote serves as a full backup of your work.
```
