# Start the project
```{Objectives}
   - think about structure of the files and folders for the project
   - think about documentation already
```

```{note}
- Many projects/scripts start as something for personal use, but expands to be distributed.
- Let's start in that end and be prepared.
- The following steps can be very valuable for you in a couple of months as well as you revisit your code and don't know what it does or why you did this and that.
```

## First things: order your files!

- Think that **everything is worth to be part of documentation** (like GitHub directory tree)
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
    - with in-code documentation
  - README
  - (Full documentation)
  - (Tutorial)

```{admonition} Directory structure
Different projects should have separate folders
  - ReadMe file
  - Data		(version controlled)(.gitignore)
  - Processed data	intermediate
  - (Manuscript)	
  - Results		data, tables, figures (version controlled, git tags for manuscript version)
  - Src		version controlled code
    - License (here or in the 1st level)
    - Requirements.txt
  - Doc
    - index
```

```{note}
- If software is reused in several projects it can make sense to put them in own repo.
- We will revisit this structure in the coming sessions as well!
```

## Start with a new GitHub project

```{discussion}
- For the course project we do it in this order, but that is not necessary in all cases.
- Typically you may start locally in Git repository and later push to a GitHub repository (more next session about Git)
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
  - the name there so there are no clashes when/if you collaborate and fork other repositories)
   
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

**Let's view the license!**
- There are prewritten text for the different types.
- More info at [Licensing](https://uppmax.github.io/programming_formalisms_intro/sharing_deeper.html#licensing)

## README files

**Advantages**
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
  - Copy paste the example code found in the last session for PlantUML and pseudocode.
  - Add some suitable headings for the code sections

````
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

What just happened?
- **Think of cloning as downloading the `.git` part to your
computer**. 
- After downloading the `.git` part the branch pointed to by HEAD is
automatically checked out.

## Working on GitHub

- You can do basically the same work at GitHub as in your local git repo
- The graphical view makes it easier to work with in everyday editing work at least.
  - Depends on your own preferences of course.
- Here your commit each file at a time with the "commit button". 
  - No staging that is.
  - Be aware of that feature!
- GitHub Actions are workflows defined by you, like:
  - for automatic testing after each commit (Used in the test lessons)
  - for GitHub Pages, briefly covered in last session today or Extra reading: [Documentation](https://uppmax.github.io/programming_formalisms_intro/documentation_deeper.html).

```{keypoints}
- A repository can have one or multiple remotes (we will revisit these later).
- A remote (GitHub) in this case serves as a full backup of your work.
```
