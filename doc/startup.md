# Start the coding and documentation

# Reproducible research

```{Objectives}
   - We will give an overview of 
      - recording dependencies
   - Get short intro to tools:
       - Pip and PyPI
       - Conda
       - Environments
       - Tools for other languages than Python
    
```

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

```{figure} img/repro-pyramid.png
:alt: Reproducibility pyramid
:width: 100%
```

```{figure} img/turing-way/39-reproducible-replicable-robust-generalisable.jpg
:alt: Reproducible, replicable, robust, generalisable
:width: 100%
```

(This image was created by [Scriberia](http://www.scriberia.co.uk) for [The
Turing Way](https://the-turing-way.netlify.com) community and is used under a
CC-BY licence. The image was obtained from [https://zenodo.org/record/3332808](https://zenodo.org/record/3332808).)


```{discussion} Discuss in HackMD, with your neighbors, or among all participants
Computer programs are expected to produce the same
output for the same inputs. Is
that true for research software?

Can you give some examples? What can we do about it?
```


## First things: order your files!

- Directory structure: Different projects should have separate folders
  - Readme file
  - Data		(version controlled)(.gitignore)
  - Processed data	intermediate
  - Manuscript	
  - Results		data, tables, figures (version controlled, git tags for manus version)
  - Src		version controlled code
    - License 
    - Requirements.txt
  - Doc
    - index
```{note}
If software is reused in several projects it can make sense to put them in own repo
```

## Project documentation

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

**Recall a typical directory structure from last section**

  - Readme file
  - Data		(version controlled)(.gitignore)
  - Processed data	intermediate
  - Manuscript	
  - Results		data, tables, figures (version controlled, git tags for manus version)
  - Src		version controlled code
    - License 
    - Requirements.txt
  - Doc
    - index

## In-code

- Comments, function docstrings, ...
- Advantages
  - Good for programmers
  - Version controlled alongside code
  - Can be used to auto-generate documentation for functions/classes
- Disadvantage
  - Probably not enough for users

**Why and not how**

### Docstrings
A docstring is a structured comment associated to a segment of code (i.e. function or class)

Good docstrings describe:
   - What the function does
   - What goes in (including the type of the input variables)
   - What goes out (including the return type)
   - Python example: help(<function name>)

````{keypoints}
- Comments should describe the why for your code not the what.
- Writing docstrings is an easy way to write documentation while you type code.
````

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

