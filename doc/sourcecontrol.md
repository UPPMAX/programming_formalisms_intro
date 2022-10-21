# Source/version control (Git)
```{questions}
  - Why should you use source/version control?
```

```{Discussion} Have you used Git (locally) in your own work?
Answer in HackMD
```

```{Objectives}
   - We will
      - introduce the use of git
      - work with the basic commands in git
      - go through branching and merging
      - present and use sharing online
```

```{instructor-note}
- Git Lecture+typealong 25 min
- Git Exercise 15 min
- Github locally + type along 15
```
This material is based on or inspired by the material from {NBIS](https://nbis-reproducible-research.readthedocs.io/en/course_2104/git/) and [CodeRefinery](https://coderefinery.github.io/git-intro/)



## Git

- We will start with our own repository.
- branching and merging (locally)
- and a brief introduction to pushing to remotes.
- In the separate collaborative Git lesson, we teach more use of remote repositories and good collaborative workflows. 


.. prereq::

   -  A reasonably recent version of **Git is installed**
      (`installation
      instructions <https://coderefinery.github.io/installation/>`__).
   -  **Git should be configured prior to the course**
      following `our installation
      instructions <https://coderefinery.github.io/installation/>`__.
   -  A `GitHub <https://github.com>`__ user account (but alternatives
      exist, see below).
   -  Being comfortable with the command line. No expertise is required,
      but the lesson will be mostly taken from the command line.
   -  Students should be familiar with using a **text editor** on their
      system. Emacs and Vim are excellent choices if you know how to use
      them but Nano or Notepad on Windows are sufficient.

### What is Git, and what is a Git repository?

- Git is a version control system: can **record/save snapshots** and track the content of a folder as it changes over time.
- Every time we **commit** a snapshot, Git records a snapshot of the **entire project**, saves it, and assigns it a version.
- These snapshots are kept inside a sub-folder called `.git`.
- If we remove `.git`, we remove the repository and history (but keep the working directory!).
- `.git` uses relative paths - you can move the whole thing somewhere else and it will still work
- Git doesn't do anything unless you ask it to (it does not record anything automatically).
- Multiple interfaces to Git exist (command line, graphical interfaces, web interfaces).

### Recording a snapshot with Git

- Git takes snapshots only if we request it.
- We will record changes always in two steps (we will later explain why this is a recommended practice).
- Example (we don't need to type yet):

  ```console
  $ git add somefile.txt
  $ git commit

  $ git add file.txt anotherfile.txt
  $ git commit
  ```

- We first focus (`git add`, we "stage" the change), then shoot (`git commit`):

### Before we start we need to configure Git

If you haven't already configured Git, please follow the instructions in the
[installation instructions](https://coderefinery.github.io/installation/shell-and-git/#configuration).

```console
$ git config --global user.name "Your Name"
$ git config --global user.email yourname@example.com
$ git config --global core.editor nano
```

Verify with:
```console
$ git config --list
```


## Type-along



#### Create repo

#### Git workflow

#### Staging files

#### Commit

#### Check status


#### Exercise




### Branching and merging

#### Exercise
```{challenge} Make changes
  - 
```
```{solution}
6
 ```
## Working remotely and sharing (github)

### Create Create a remote repository
Create a remote repository

    Log in to your GitHub account and press the New button on the left:
        Make sure you are listed as the owner
        Add a repository name, e.g. git_tutorial
        You can keep the repo private or make it public, as you wish
        Skip including a README, a .gitignore and licence
        
### GH actions

Just briefly



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
