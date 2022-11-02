# Reproducible research and sharing

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

## Versioning systems 

### Semantic (SemVer)
Given a version number MAJOR.MINOR.PATCH, increment the:
1.	MAJOR version when you make incompatible API changes
2.	MINOR version when you add functionality in a backwards compatible manner
3.	PATCH version when you make backwards compatible bug fixes
Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

```{figure} img/SemVer.jpg
:alt: Isolated tracks
:width: 50%

<https://nehckl0.medium.com/semver-and-calver-2-popular-software-versioning-schemes-96be80efe36
>
```

### Calender ([CalVer](https://calver.org/))

```{figure} img/CalVer.png
:alt: Isolated tracks
:width: 50%

<https://nehckl0.medium.com/semver-and-calver-2-popular-software-versioning-schemes-96be80efe36
>
```

## Recording dependencies
-	**Reproducibility**: We can control our code but how can we control dependencies?
-	**10-year challenge**: Try to build/run your own code that you have created 10 (or less) years ago. Will your code from today work in 5 years if you don’t change it?
-	**Dependency hell**: Different codes on the same environment can have conflicting dependencies.

### Conda, Anaconda, pip, Virtualenv, Pipenv, pyenv, Poetry, requirements.txt …

**These tools try to solve the following problems:**
-	**Defining a specific set of dependencies**, possibly with well defined versions
-	**Installing those dependencies** mostly automatically
-	**Recording the versions** for all dependencies
-	**Isolated environments**
  -	On your computer for projects so they can use different software.
  -	Isolate environments on computers with many users (and allow self-installations)
-	Using **different Python/R versions** per project??
- Provide tools and services to **share packages**

### The tools
- Python
  -	PyPI
    -pip freeze > requirements.txt
  -	Conda: any language, also compiled code and libraries.
    -	conda-forge is a GitHub organization containing repositories of conda recipes.
	  - Export the requirements into requirements.txt with conda list --export > requirements.txt.
	  - Export the full environment using conda env export > environment.yml, and compare the .yml file format to the .txt file format.
  -	Virtualenv
	- Pipenv
	- Poetry
	- Pyenv
	- Mamba (faster conda)
-	R
  - Packrat, jetpack, rsuite, renv, automagic, deplearning, devtools
-	C/C+
	- CMake
	- Conan
	- Conda
-	Fortran
  - Fortran package manager
- Julia
  - Pkg.jl
    -	designed around using isolated environments with independent sets of packages. Environments can either be local to a particular project or shared and selected by name.

### Course advertisment
[Python for scientific computing](https://aaltoscicomp.github.io/python-for-scicomp/)


## Recording computational steps

```{questions}
- How can we create a reproducible workflow?
- When to use scientific workflow management systems.
```

```{objectives}
- Discuss pros/cons of GUI vs. manual steps vs. scripted vs. workflow tools.
```

**4 ways (from CodeRefinery)**

### Graphical user interface (GUI)
Imagine we have programmed a GUI with a nice interface with icons where you can select scripts and input files by clicking:
- Click on counting script
- Select book txt file
- Give a name for the dat file
- Click on a run symbol
- Click on plotting script
- Select book dat file
- Give a name for the image file
- Click on a run symbol
- ...
- Go to next book ...
- Click on counting script
- Select book txt file
- ...

Disclaimer: not all GUIs behave this way - there exist very good GUI solutions which enable
reproducibility and automation.

---
### Solution 2: Manual steps
It is not too much work for four files:
```{code-block} console
---
emphasize-lines: 1-2, 13
---

$ python source/wordcount.py data/abyss.txt processed_data/abyss.dat
$ python source/plotcount.py processed_data/abyss.dat processed_data/abyss.png

$ python source/wordcount.py data/isles.txt processed_data/isles.dat
$ python source/plotcount.py processed_data/isles.dat processed_data/isles.png

$ python source/wordcount.py data/last.txt processed_data/last.dat
$ python source/plotcount.py processed_data/last.dat processed_data/last.png

$ python source/wordcount.py data/sierra.txt processed_data/sierra.dat
$ python source/plotcount.py processed_data/sierra.dat processed_data/sierra.png

$ python source/zipf_test.py processed_data/abyss.dat processed_data/isles.dat processed_data/last.dat processed_data/sierra.dat
```

This is **imperative style**: first do this, then to that, then do that, finally do ...

---
### Solution 3: Script
Let’s express it more compactly with a shell script (Bash). Let’s call it script.sh:
```shell
#!/usr/bin/env bash

# loop over all books
for title in abyss isles last sierra; do
    python source/wordcount.py data/${title}.txt processed_data/${title}.dat
    python source/plotcount.py processed_data/${title}.dat processed_data/${title}.png
done

# this could be done using variables but nevermind
python source/zipf_test.py processed_data/abyss.dat processed_data/isles.dat processed_data/last.dat processed_data/sierra.dat
```
We can run it with:
```console
bash script.sh
```
### Solution 4: Using [Snakemake](https://snakemake.readthedocs.io/en/stable/index.html) or other workflow manager

```{figure} img/snakemake_dag.png
:alt: Isolated tracks
:width: 50%

Isolated tracks of work.
```

````{discussion} Discussion
Discuss the pros and cons of these different approaches. Which are reproducible? Which scale to hundreds of books and which can it be automated?

```{solution}
- GUIs may or may not be reproducible.
- Some GUIs can be automated, many cannot.
- Typing the same series of commands for 100 similar inputs is tedious and error prone.
- Imperative scripts are reproducible and great for automation.
- Declarative workflows such as Snakemake are great for longer multi-step analyses.
- Declarative workflows are often easy to parallelize without you changing anything.
- With declarative workflows it is no problem to add/change things late in the project.
- Interesting modern alternative to Make/Snakemake: [https://taskfile.dev](https://taskfile.dev)
- Many [specialized frameworks](https://github.com/common-workflow-language/common-workflow-language/wiki/Existing-Workflow-systems) exist.
```
````

```{admonition} Learn more
<https://coderefinery.github.io/reproducible-research/workflow-management/>
<https://nbis-reproducible-research.readthedocs.io/en/course_2104/snakemake/>
```

```{keypoints}
  - Preserve the steps for re-generating published results.
  - Hundreds of workflow management tools exist.
  - Snakemake is a comparatively simple and lightweight option to create transferable and scalable data analyses.
  - Sometimes a script is enough.
```

## Reproducible publications
- Git (overleaf, authorea), hackmd, manuscripts.io, google docs
- Scholarly output reproducible: rrtools, jupyter, binder, research compendia
- Reprohack


## Sharing

The Open Science movement encourages researchers
to share research output beyond the contents of a
published academic article (and possibly supplementary information).

```{figure} img/Open_Science_Principles.png
:alt: Research comic
:width: 90%
```

- **Open-source license** is a type of license for computer software and other products that allows the **source code, blueprint or design to be used, modified and/or shared under defined terms and conditions**.


Arguments in favor [(from Wikipedia)](https://en.wikipedia.org/wiki/Open_science):
- Open access publication of research reports and data allows for rigorous peer-review
- Science is publicly funded so all results of the research should be publicly available
- Open Science will make science more reproducible and transparent
- Open Science has more impact
- Open Science will help answer uniquely complex questions

Arguments against [(from Wikipedia)](https://en.wikipedia.org/wiki/Open_science):
- Too much unsorted information overwhelms scientists
- Potential misuse
- The public will misunderstand science data
- Increasing the scale of science will make verification of any discovery more difficult
- Low-quality science

```{figure} img/36-data-research-cycle.jpg
:width: 100%

(This image was created by Scriberia for The Turing Way community and is used under a CC-BY licence. The image was obtained from https://zenodo.org/record/3332808.)
```

```{admonition} Read more

[CodeRefinery](https://coderefinery.github.io/reproducible-research/sharing/)

### FAIR
**“FAIR”** is the current buzzword for data management. You may be asked about it in, for example, making data management plans for grants:

- Findable
  - Will anyone else know that your data exists?
  - Solutions: put it in a standard repository, or at least a description of the data. Get a digital object identifier (DOI).
- Accessible
   - Once someone knows that the data exists, can they get it?
   - Usually solved by being in a repository, but for non-open data, may require more procedures.
- Interoperable
   - Is your data in a format that can be used by others, like csv instead of PDF?
   - Or better than csv. Example: 5-star open data
- Reusable
   - Is there a license allowing others to re-use?




### Social coding

-  Our work depends on outputs from others. Research of others depends on our outputs.

- Whether you can share your output depends on how you obtained your input.
- A repository that is private today might become public one day.
- Sometimes “OTHERS” are you yourself in the future in a different group/job.
- Software licenses matter. And this is what we will discuss in the next episode.

```{info}
More on Wednesday!
```
    
## Licensing
[For more details](https://coderefinery.github.io/social-coding/licensing/#)

### Copyright

- Protects creative expression
- Automatically created
- **Derivative works** usually inherit copyright of the thing derived
- Time frame: essentially forever (lifetime + X years)

When can you use:
- When there is a **license** saying you can
- Limited other cases (private use, fair use: context dependent)
- In practice: people do many things, but then can't share their
  output if license does not allow it or is not clarified

**When we write or use software then copyright, licenses, and derivative works are important concepts**


### Derivative work: Changing, remixing, covering

```{figure} img/rubik.jpg
:alt: Images of Bob Marley and Mona Lisa made out of Rubik cubes
:width: 60%

Images of Bob Marley and Mona Lisa made out of Rubik cubes. 
Is this derivative work? ["Distillery District 26"](https://www.flickr.com/photos/dgriebeling/3851273590) CC-BY.
```

### If you build on something, you form a derivative work

- The original creator may have rights to what you make
- The whole point of this talk is to make sure that **you can make and publish derivative works**
  and **others can make and publish derivative works from you**
- **You cannot ignore licensing**: default is “no one can make copies or derivative works”.
- License your code very early in the project: ideally develop publicly accessible open source code from day one.
- Start with a README.md and a LICENSE file.
- Use GitHub recommendation or/and <https://choosealicense.com/>.


### Licensing and ownership

**Who can decide about or change a license?**
- The copyright holder if a separate "Contributor License Agreement" is signed. Otherwise
  copyright holder provided they secure express consent from all the contributors.

**Who owns the copyright for software you write?**
- **Intellectual property depends on the country and the employer!**
- So-called works made for hire.

**If you own your software:**
- You can change the license.
- You can dual-license (e.g. GPL for anyone, but you can pay for commercial non-GPL).

**If you do not own your software, you can:**
- Request open-sourcing directly (preserves your rights!).
- Request a transfer of ownership (check with your university).

**If you accept contributions (pull requests), you may not be the only owner anymore!**
- Clarify licensing strategy **before** - otherwise you won't have
  all rights to your code.
  
### What is free software?

#### Software freedom is the freedom to ...

- ... run the software for **any purpose**: new applications
- ... **study** how the software works and to adapt it to your needs: new applications, less reinventing wheels
- ... **redistribute** copies of the software: more users, more citations
- ... **improve** the software and distribute your improvements to the public: fix bugs, new science

#### Typical confusion

- Free software does not mean that software is for free
- Open source license does not mean you need to share everything immediately (share main branch, put unpublished code on a fork)
- Open source does not mean public domain: software in the public domain has no owner
- Open source does not mean non-commercial: plenty of companies produce and support it

### Taxonomy of software licenses

- Copyleft is the legal technique of granting certain freedoms over copies of copyrighted works with the requirement that the same rights be preserved in derivative works.



**1. Custom/closed/proprietary**

- Derivative work typically not possible

**2. Permissive (MIT, BSD, Apache)**

- Derivative work does not have to be shared
- Permissive: gives the public permission to use, modify, and share, without any condition for downstream licensing
- If the licenses of components are permissive, one may use any open license they want.

```{figure} img/MIT.png
:alt: Permissions, conditions, and limitations of the MIT license

Example: Permissions, conditions, and limitations of the MIT license. Unchanged from <https://choosealicense.com/>.
```

**3. Weak copyleft share-alike (LGPL, MPL)**

- Derivative work is free software but is limited to the component

```{figure} img/GNU_LGPL_v3.png
:alt: Permissions, conditions, and limitations of the LGPL license

Example: Permissions, conditions, and limitations of the LGPL license. Unchanged from <https://choosealicense.com/>.
```

**4. Strong copyleft share-alike (GPL, AGPL)**

- Derivative work is free software and derivative work extends to the combined project
- If the licenses of components are strong copyleft, one must use the same license

```{figure} img/GNU_GPL_v3.png
:alt: Permissions, conditions, and limitations of the GPL license

Example: Permissions, conditions, and limitations of the GPL license. Unchanged from <https://choosealicense.com/>.
```

### Creative Commons licenses 
```{figure} ./img/Cc.logo.circle.svg.png
:alt: Creative Commons
:width: 100px
:align: left
``` 

- Creative Commons licenses give everyone a standardized way to grant the public permission to use their creative work under copyright law.
- From the reuser’s perspective, the presence of a Creative Commons license on a copyrighted work answers the question, “What can I do with this work?” 
<https://creativecommons.org/about/cclicenses/>
- More often used for images and text.
- For software, Creative Commons includes three free licenses created by other institutions: the BSD License, the GNU LGPL, and the GNU GPL. See above.

- 4 rights:
  - BY – Attribution - Credit must be given to the creator <img src="./img/Cc-by_new.svg.png" alt="CC-by" width="50"/>
  ```{image} ./img/Cc-by_new..svg.png
:alt: CC-BY
:width: 50pxt
``` 

    - User may copy, distribute, display, perform and make derivative works and remixes based on it only if they give the author or licensor the credits
  - SA - Share alike - Allows remix culture ![Cc-sa](./img/Cc-sa.svg.png =50x)
    - distribute derivative works only under a license identical to ("not more restrictive than") the license that governs the original work.(Share alike)
  - NC - Non-commercial ![Cc-nc](./img/113px-Cc-nc.svg.png =50x)
    - Licensees may copy, distribute, display, perform the work and make derivative works and remixes based on it only for non-commercial purposes. 
  - ND - No derivative work ![Cc-nd](./img/Cc-nd.svg.png =50x)
    - Licensees may copy, distribute, display and perform only verbatim copies of the work, not derivative works and remixes based on it. Since version 4.0, derivative works are allowed but must not be shared. 
  - CC0 (aka CC Zero) - No attribution required
    - not recommended to release software into the public domain because it lacks a patent grant.

If you would like to learn more about licenses, check out our slide deck ["Software licensing
and open source explained with
cakes"](https://cicero.xyz/v3/remark/0.14.0/github.com/coderefinery/social-coding/main/licensing-and-cakes.md/).

```{note}
Also covered on the third day
```

## Software Citation

- Think the same as for a scientific paper

**Our practical recommendations**:
- Get a [DOI](https://en.wikipedia.org/wiki/Digital_object_identifier) using [Zenodo](https://zenodo.org) or similar services.
- Open source license can't demand citation, but it is required by science ethics anyway.
- Make it as easy as possible! Clearly say what you want cited.
- Make it easy for scripts and tools, use the [Citation File Format](https://citation-file-format.github.io).
- [GitHub now supports CITATION.cff files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)

This is an example of a simple `CITATION.cff` file:
```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/0000-0003-4925-7248
title: "My Research Software"
version: 2.0.4
doi: 10.5281/zenodo.1234
date-released: 2021-08-11
```

Recommended format for software citation is to ensure the following information
is provided as part of the reference [Katz, Chue Hong, Clark, 2021](https://doi.org/10.12688/f1000research.26932.2):
- Creator
- Title
- Publication venue
- Date
- Identifier
- Version
- Type

    
- Digital object identifiers (DOI) are the backbone of the academic reference and metrics system. 
- CodeRefinery has an exercise to see how to make a GitHub repository citable by archiving it on the Zenodo archiving service. If you are interested,  have a look [here](https://coderefinery.github.io/reproducible-research/sharing/#exercise-connecting-repositories-to-zenodo)
- For Services for sharing and collaboration on RESEARCH DATA, click [here](https://coderefinery.github.io/reproducible-research/sharing/#exercise-connecting-repositories-to-zenodo)


```{keypoints}
  - Share your code! Eventually others will probably use it anyway.
  - Licence your software and do it early. Default is “no one can make copies or derivative works”.
  - Get DOI or at least state how to cite your software
```
