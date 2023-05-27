# Start the coding and documentation

```{Objectives}
   - We will get started with the coding
   - But also...
     - think about structure of the files and folders for the project
     - think about dependencies and work in an isolated environment
     - think about docuemtation already

```

```{note}
- Many projects/scripts starts as something for personal use, but expands to be distributed.
- Let's start i nthat end and be preperad.
- The following steps can be very valuable for you in a couple of months as well as you revisit your code and don't know what it does or why you did this and that.
```

## First things: order your files!

- Think that **everything is worth to be part of documentation** (like Github directory tree)
- The parts from the software development cycle
  - The planning parts
      - Requirements: 
        - what should the program deliver
        - dependencies
        - OS platforms
      - Risk analysis
  - Design documentation
      - Analysis: pseudo code and UML
  - Source code
    - with in-code deocumentation
  - README
  - (Full documentation)
  - (Tutorial)

- Directory structure: Different projects should have separate folders
  - Readme file
  - Data		(version controlled)(.gitignore)
  - Processed data	intermediate
  - (Manuscript)	
  - Results		data, tables, figures (version controlled, git tags for manus version)
  - Src		version controlled code
    - License (here or in the 1st level)
    - Requirements.txt
  - Doc
    - index

```{note}
- If software is reused in several projects it can make sense to put them in own repo.
- We will revisit this structure in the coming sessions as well!
```

## Start with a new GitHub project

```{discussion}
- For the course porject we do it in this order, but that is not necessary in all cases.
- Typically you may start locally in  Git repository and later push to a GitHub repository (more next session about Git)
- The reason for starting here is that we can get our PlantUML render in the browser!
```

### Type-along: Create a new repository on GitHub

Make sure that you are **logged into GitHub**.

```{figure} img/New_repo.png
:width: 60%
:class: with-border

To create a repository we either click the green button "New" (top left corner).
```

```{figure} img/new-top-right.png
:width: 60%
:class: with-border

Or if you see your profile page, there is a "+" menu (top right corner).
```

---

On this page choose a project name, e.g. ``planets-<username>`` 
  - the name there so there are noe clahes when you collaborate and fork other repositories)
   
For the sake of this exercise **do select**
"Initialize this repository with a README"
and
"Choose a license"
- Let's choose MIT (we may discuss this later on

```{figure} img/New_repo_formalisms.png
:width: 100%
:class: with-border
```

**Done!**

Let's view the license!
- There are prewritten text for the different types.
- More info at https://uppmax.github.io/programming_formalisms_intro/sharing_deeper.html#licensing

## README files

   - Advantage
  - Versioned (goes with the code development)
  - It is often good enough to have a `README.md` or `README.rst` along with your code/script
- If you use README files, use either
  [RST](http://docutils.sourceforge.net/rst.html) or
  [Markdown](https://commonmark.org/help/)
- A great guide to README files: [MakeaREADME](https://www.makeareadme.com/)

   
````{keypoints}
README file should include:

  - A descriptive project title

  - Motivation (why the project exists)

  - How to setup

  - Copy-pastable quick start code example

  - Recommended citation
````

**We are ready to**
- extend the README file
- Make some folders according to the above list
- Put the planning documents in a docs folder

````{challenge}
1. Extend the README file a little bit with an **About section** in Markdown format describing the project.
  - Use the **Pencil** button
  - Use the goals stated in last session). 
  - Get inspiration from https://www.makeareadme.com/ and a favorite Git repo or https://github.com/yampelo/beagle. 


```markdown
**Cheat sheet**
# This is a section in Markdown   

## This is a subsection           

Nothing special needed for        
a normal paragraph.               

    This is a code block          


**Bold** and *emphasized*.       

A list:                           
- this is an item                 
- another item                   
               
```

2. Create the planning document in markdown **Add file** button and choose "Create file".
  - Call the file ``doc/plan.md``
  - Copy paste the example code found in the last session for plantUML and pseudocode.
  - Add some suitable headings for the code sections

````
---


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
---

## Cloning a repository

Now you and other people can clone this repository and contribute changes. 

At this point only a brief demo - if you copy the SSH or HTTPS address, you can clone repositories like this
(again adapt the "namespace/repository.git" part):

```console
$ git clone git@github.com:<user>/planet-<user>.git
```

This creates a directory called "planet-<user>" unless it already exists. You can also specify the target directory
on your computer, in this case just "planet":

```console
$ git clone git@github.com:<user>/planet-<user>.git planet
```

What just happened? **Think of cloning as downloading the `.git` part to your
computer**. After downloading the `.git` part the branch pointed to by HEAD is
automatically checked out.

```{keypoints}
- A repository can have one or multiple remotes (we will revisit these later).
- Local branches often track remote branches.
- A remote serves as a full backup of your work.
```
## Working on GitHub

- You can do basically the same work at GitHub as in your local git repo
- The graphical view makes it easier to work with in everyday editing work at least.
  - Depends on your own preferences of course.
- Here your commit each file at a time with the "commit button". No staging that is.
- GitHub Actions are workflows defined by you, like:
  - for automatic testing after each commit (Used on Thursday)
  - for GitHub Pages, briefly covered in last session today.

## Start code but be aware of dependencies

```{instructor-note}
- Lecture+discussions 25 min
- Sharing moved to own page
- Time required, 20?
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
There are seveal ways to make an isolated environment where you are sure what is needed by other users.
   - Conda is one way
   - virtualenv is an extarnal package that has to be installed explicitely
     - uses pip to install within the isolated environment
   - We'll use ´venv´, which is standard library
```   

   
``````{challenge} Type-along
- We will need the python packages: numpy and matplotlib
- Let's create an isolated environment with those packages and based on the python we have install, like 3.8.X. It is assumed that no-one uses python-2.X.X!   
- In the command-line, create and activate the environment ``planet-project``
```console
$ pyton -m venv planet-project
$ source planet-project/bin/activate
```
- Note that your prompt is changing to start with (planet-project) to show that you are within that environment.   
- Now install the packages
```console
(planet-project) $ pip install --no-cache-dir --no-build-isolation numpy==1.15.4 matplotlib==2.2.2   
```
- we won't deactivate the project environment now but for later, simply type ``deactivate`` in the console.
   
``````   
## Create a first version of the python code

``````{challenge} Type-along
- Use you favorite editor and create the file ``planet.py``
- Use the linear code below. 
  - It plots the approximate orbit of earth with some eccentricity, and the distance during 2 years to the sun.
  - Later we will add Jupiter and make it more modular!

````{solution} `planet.py`
```python
#planet
import numpy as np
import matplotlib.pyplot as plt 

#constants
G=6.6743e-11
AU=149.597871e9
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

plt.savefig('planet_earth.png', dpi=100, bbox_inches='tight')

```
````
   
```{figure} img/planet_earth.png
:width: 100%
:class: with-border
```   

``````    
## Make the code a part of the git record

```{admonition} Concepts in Git
- **repository**: The project, contains all data and history (commits, branches, tags).
- **add**: Stage you files (collect what to be added to the git record — a kind of middle step)
- **commit**: Snapshot of the project, gets a unique identifier (e.g. `c7f0e8bfc718be04525847fc7ac237f470add76e`).
- **cloning**: Copying the whole repository to your laptop - the first time. It is not necessary to download each file one by one.
- `git clone` copies everything: all commits and all branches.
- Branches on the remote appear as (read-only) local branches with a prefix, e.g. `origin/main`.
- We synchronize commits between local and remote with `git fetch`/`git pull` and `git push`.
```
   
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
- Use you favorite editor
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



