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
This material is based on or inspired by the material from [NBIS](https://nbis-reproducible-research.readthedocs.io/en/course_2104/git/) and [CodeRefinery](https://coderefinery.github.io/git-intro/)



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

```{Attention}
- Start your terminal of choice
   - MAC terminal 
   - iTerm
   - WSL environment in
     - MobaxTerm
     - Visual Studio Code
   - Git BASH  
   - PowerShell

```

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

### Create repository 
We will create a repository (repo) called `Diagrams.

Be sure you are in a directory like "Programming_Formalisms" or similar (to have track of your work)

One of the basic principles of Git is that it is **easy to create repositories**:
```console
$ mkdir Diagrams
$ cd Diagrams
$ git init
```

That's it! With `git init` have now created an empty Git repository.

#### Check status

We will use `git status` a lot to check out what is going on:

```console
$ git status

On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

We will make sense of this information during this workshop.


```{admonition} A new repository from an existing project on own computer or HPC user account.

- Say you’ve got an existing project that you want to start tracking with git.

    - Go into the directory containing the project.
    - Type `git init`.
    - Type `git add` to add all of the relevant files.
    - You’ll probably want to create a `.gitignore` file right away, to indicate all of the files you don’t want to track. Use `git add .gitignore`, too.
    - Type `git commit`.

```

### Git everyday steps


Let us now **create two files**.

One file is called `class.puml` and contains:

```shell
@startuml
 class01 <|-- class02
 class03 *-- class04
 class05 o-- class06

 class01- class03 : knows >
 class class01 {
    -var01 : Integer
    Time : Date
    #method01()
    +get_var01()
    {method}Without paranteces or Qualifiers
 }
@enduml
```

The second file is called `activity.puml` and contains:

```shell
@startuml
start

if (Graphviz installed?) then (yes)
  :process all\ndiagrams;
else (no)
  :process only
  __sequence__ and __activity__ diagrams;
endif

stop
@enduml
```

#### Staging files


As mentioned above, in Git you can always check the status of files in your repository using
`git status`. It is always a safe command to run and in general a good idea to
do when you are trying to figure out what to do next:

```console
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        activity.puml
        class.puml

nothing added to commit but untracked files present (use "git add" to track)

```

The two files are untracked in the repository (directory). You want to **add the files** (focus the camera)
to the list of files tracked by Git. Git does not track
any files automatically and you need make a conscious decision to add a file. Let's do what
Git hints at and add the files:


```console
$ git add activity.puml
$ git add class.puml
$ git status

On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   activity.puml
        new file:   class.puml
```

Now this change is *staged* and ready to be committed.

#### Commit

Let us now commit the change to the repository:

```console
$ git commit -m "adding class and activity diagrams"

[master (root-commit) 8adee34] adding class and activity diagrams
 2 files changed, 26 insertions(+)
 create mode 100644 activity.puml
 create mode 100644 class.puml
```

Right after we query the status to get this useful command into our muscle memory:

```console
$ git status

On branch master
nothing to commit, working tree clean

```

What does the `-m` flag mean? Let us check the help page for that command:

```console
$ git help commit
```

You should see a very long help page as the tool is very versatile (press q to quit).
Do not worry about this now but keep in mind that you can always read the help files
when in doubt. Searching online can also be useful, but choosing search terms
to find relevant information takes some practice and discussions in some
online threads may be confusing.
Note that help pages also work when you don't have a network connection!


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
