# Start with coding!
## Start code but be aware of reproducibility

```{instructor-note}
```
```{Objectives}
   - We will get started with the coding
   - But also...
     - think about dependencies and work in an isolated environment
```

```{note} 
- For more background please confer 
  - [NBIS](https://nbis-reproducible-research.readthedocs.io/en/course_2104) 
  - [CodeRefinery](https://coderefinery.github.io/reproducible-research/)
``` 

```{discussion} Discuss in HackMD
Computer programs are expected to produce the same
output for the same inputs. Is
that true for research software?

Can you give some examples? What can we do about it?
```

## Create a virtual python environment with ``venv``
   
```{note}
There are several ways to make an isolated environment where you are sure what is needed by other users.
   - Conda is one way
   - `virtualenv` is an external package that has to be installed explicitely
     - uses pip to install within the isolated environment
   - We'll use ``venv``, which is standard library
```   

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
   
``````{challenge} Type-along
- We will need the python packages: ``numpy`` and ``matplotlib``
- Let's create an isolated environment with those packages and based on the python we have install, like 3.8.X. It is assumed that no-one uses python-2.X.X!   
- In the command-line, create and activate the environment ``planet-project``
```console
$ python -m venv planet-project
$ source planet-project/bin/activate
```
````{attention}
- In Windows, like from Git-bash, you activate instead with ``source planet-project/Scripts/activate`` 
````
- Note that your prompt is changing to start with (planet-project) to show that you are within that environment.   
- Now install the packages (leave out package versions so that ``python-<your-version>`` can choose by itself what suites)
```console
(planet-project) $ pip install numpy matplotlib  
```
- We won't deactivate the project environment now but for later, simply type ``deactivate`` in the console.
  - That's a good practice
   
``````   
## Create a first version of the python code

``````{challenge} Type-along
- Use you favorite editor and create the file ``planet.py``
- Use the linear code below. 
  - It plots the approximate orbit of earth with some eccentricity, and the distance during 2 years to the sun.
  - Later we will add Jupiter and make it more modular!

````{solution} Code
```python
#planet
import numpy as np
import matplotlib.pyplot as plt 

#constants
G=6.6743e-11
AU=149.597871e9 # 1 astronomical unit (AU) is the mean distance between sun and Earth
AU1=150.8e9
mj=5.97219e24
mJ=1.899e27
M=1.9891e30
day=86400;
year=31556926;
v0=AU*2*np.pi/year;
Fg=G*M*mj/AU**2
ag=Fg/mj
Fc=mj*v0**2/AU
ac=Fc/mj

L=2

x0=AU1;
y0=0;
u0=0;
x=np.zeros(365*L, dtype=float);
y=np.zeros(365*L, dtype=float);

x[0]=x0;
y[0]=y0;
u=u0;
v=v0;

for i in range(1,365*L):    
    print(i)
    x[i]=x[i-1]+day*u;
    y[i]=y[i-1]+day*v;
    ax=-G*M/(abs(x[i]**2+y[i]**2)**[3/2])*x[i];
    ay=-G*M/(abs(x[i]**2+y[i]**2)**[3/2])*y[i];
    u=u+ax*day;
    v=v+ay*day;

rj=(x**2+y**2)**.5
a=max(rj)
b=min(rj)
e=1-2/(a/b+1)
rel=(a/b-1)


fig=plt.figure(1,figsize=(12,5))
ax=fig.add_subplot(1,2,1)
ax.plot(x,y)
ax.plot (0,0,'o')
#axis equal

ax=fig.add_subplot(1,2,2)
ax.plot(range(0,365*2),rj)

plt.savefig('../Figures/planet_earth.png', dpi=100, bbox_inches='tight')
```
````
   
```{figure} img/planet_earth.png
:width: 100%
:class: with-border
```   

``````    

## What is Git, and what is a Git repository?

- Git is a version control system: can **record/save snapshots** and track the content of a folder as it changes over time.
- Every time we **commit** a snapshot, Git records a snapshot of the **entire project**, saves it, and assigns it a version.
- These snapshots are kept inside a sub-folder called `.git`.
- If we remove `.git`, we remove the repository and history (but keep the working directory!).
- `.git` uses relative paths - you can move the whole thing somewhere else and it will still work
- Git doesn't do anything unless you ask it to (it does not record anything automatically).
- Multiple interfaces to Git exist (command line, graphical interfaces, web interfaces).

  
```{admonition} Concepts in Git
- **repository**: The project, contains all data and history (commits, branches, tags).
- **add**: Stage you files (collect what to be added to the git record — a kind of middle step)
- **commit**: Snapshot of the project, gets a unique identifier (e.g. `c7f0e8bfc718be04525847fc7ac237f470add76e`).
- **cloning**: Copying the whole repository to your laptop - the first time. It is not necessary to download each file one by one.
- `git clone` copies everything: all commits and all branches.
- Branches on the remote appear as (read-only) local branches with a prefix, e.g. `origin/main`.
- We synchronize commits between local and remote with `git fetch`/`git pull` and `git push`.
```
   
### Before we start we need to configure Git

```{prereq}

   -  **Git and GITHUB should be configured prior to the course**
      following [https://coderefinery.github.io/installation](https://github.com/UPPMAX/programming_formalism/blob/main/setup.md)).
   -  Being comfortable with the command line. No expertise is required,
      but the lesson will be mostly taken from the command line.
   -  Students should be familiar with using a **text editor** on their
      system. Emacs and Vim are excellent choices if you know how to use
      them but Nano or Notepad on Windows are sufficient.
      
```    
   
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
$ git add .    # < -- "." means all files
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
   
   
## Make the code a part of the git record
   
``````{challenge} Type-along: Make your code part of git   

- Add you file to staging

```console
   git add planet.py
```
- Check the status. 
- The output should show the new changes since your work on GitHub  
```console
   git status
```
- Commit with the message "First commit of code"
```console
   git commit -m "First commit of code"
```
- Check the status   
- The output should show "Nothing to commit
```console
   git status
```

``````

## In-code documentation

- Comments, function docstrings, ...
- Advantages
  - Good for programmers
  - Version controlled alongside code
  - Can be used to auto-generate documentation for functions/classes
- Disadvantage
  - Probably not enough for users
   
````{exercise} Discussion
Let's take a look at two example comments (comments in python start with `#`):

**Comment A**
```python
# Now we check if temperature is larger then -50:
if temperature > -50:
    print('do something')
```

**Comment B**
```python
# We regard temperatures below -50 degrees as measurement errors
if temperature > -50:
    print('do something')
```
Which of these comments is best? Can you explain why?
````
```{solution} Solution
Comment A describes **what** happens in this piece of code,
whereas comment B describes **why** this piece of code is there, i.e. its **purpose**.
Comments in the form of B are much more useful, comments of form A are redundant and we should avoid them.
```

**Why and not how**

``````{challenge} Exercise
- Use your favourite editor
- Use the linear code below. 
  - Later we will make it more modular!

````{solution} 
```python
Coming...
```

``````


### Docstrings
A docstring is a structured comment associated to a segment of code (i.e. function or class)

```{note}
   - We will make docstrings in next session
```

````{keypoints}
- Comments should describe the why for your code not the what.
- Writing docstrings is an easy way to write documentation while you type code.
````

