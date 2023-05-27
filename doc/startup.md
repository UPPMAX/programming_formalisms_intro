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

**Reload your GitHub project website and - taa-daa - your commits should now be
online!**

What just happened? **Think of publishing a repository as uploading the `.git` part online**.

---

## Cloning a repository

Now other people can clone this repository and contribute changes. 

At this point only a brief demo - if you copy the SSH or HTTPS address, you can clone repositories like this
(again adapt the "namespace/repository.git" part):

```console
$ git clone git@github.com:<user>/project.git
```

This creates a directory called "project" unless it already exists. You can also specify the target directory
on your computer:

```console
$ git clone git@github.com:<user>/project.git myproject
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
- This is a summary.
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

## Create a first version of the python code

````{challenge} Type along
- Use you favorite editor
- Use the linear code below. 
  - Later we will make it more modular!

´´´python

```

````

## In-code documentation

- Comments, function docstrings, ...
- Advantages
  - Good for programmers
  - Version controlled alongside code
  - Can be used to auto-generate documentation for functions/classes
- Disadvantage
  - Probably not enough for users

**Why and not how**

````{challenge} Type along
- Use you favorite editor
- Use the linear code below. 
  - Later we will make it more modular!

´´´python

```

````


### Docstrings
A docstring is a structured comment associated to a segment of code (i.e. function or class)

Good docstrings describe:
   - What the function does
   - What goes in (including the type of the input variables)
   - What goes out (including the return type)
   - Python example: help(<function name>)
   
```{note}
   - We will make docstrings in next session
```

````{keypoints}
- Comments should describe the why for your code not the what.
- Writing docstrings is an easy way to write documentation while you type code.
````



