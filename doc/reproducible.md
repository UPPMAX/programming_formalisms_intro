# Reproducible research and sharing

```{questions}
  - Should research software and data be reproducible?
  - Are they?
```

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
- Lecture 15 min
- Discussions 15 min
```


- https://nbis-reproducible-research.readthedocs.io/en/course_2104/git/
- NBIS: Making projects reproducible

- kort om workflow connecta med moduler!
- Snakemake

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

:Note: If software is reused in several projects it can make sense to put them in own repo

## Reproducible publications
- Git (overleaf, authorea), hackmd, manuscripts.io, google docs
- Scholarly output reproducible: rrtools, jupyter, binder, research compendia
- Reprohack

## Recording dependencies
-	Reproducibility: We can control our code but how can we control dependencies?
-	10-year challenge: Try to build/run your own code that you have created 10 (or less) years ago. Will your code from today work in 5 years if you don’t change it?
-	Dependency hell: Different codes on the same environment can have conflicting dependencies.
Conda, Anaconda, pip, Virtualenv, Pipenv, pyenv, Poetry, requirements.txt …
-	Defining a specific set of dependencies, possibly with well defined versions
-	Installing those dependencies mostly automatically
-	Recording the versions for all dependencies
-	Isolated environments
  -	On your computer for projects so they can use different software.
  -	Isolate environments on computers with many users (and allow self-installations)
-	Using different Python/R versions per project??


### Provide tools and services to share packages
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

## Semantic versioning: 
Given a version number MAJOR.MINOR.PATCH, increment the:
1.	MAJOR version when you make incompatible API changes
2.	MINOR version when you add functionality in a backwards compatible manner
3.	PATCH version when you make backwards compatible bug fixes
Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.


## Recording dependencies

- Jupyter?

- containers
  - Docker
  - Singularity
- makefile

## Sharing

```{Objectives}
   - We will give an overview of 
      - recording dependencies
   - Get short intro to tools:
       - Pip and PyPI
       - Conda
       - Environments
       - Tools for other languages than Python    - Introduce reproducibility and sharing, licensing and citation
     - Get into thinking about dependencies and solutions
     - Get into choosing license, citation and DOI
``` 

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


## Social coding


>    Our work depends on outputs from others. Research of others depends on our outputs.

    Whether you can share your output depends on how you obtained your input.

    A repository that is private today might become public one day.

    Sometimes “OTHERS” are you yourself in the future in a different group/job.

    Software licenses matter. And this is what we will discuss in the next episode.
    
    

### Open source

> Enable derivative work

    Do not lock yourself out of own code

    Attract developers who want to be able to show the coding work on their CVs

    Tightly regulated domains require open source

    Open-source software (OSS) can lead to more engagement from industry which may lead to more impact

    If it’s not open, it is not likely to become standard
    
Types of things that can be reused:

    Main libraries (e.g. NumPy, SciPy)

    Special scientific libraries

    Random code from website

    Copying from Stack Overflow



## Licensing

> You cannot ignore licensing: default is “no one can make copies or derivative works”.

> License your code very early in the project: ideally develop publicly accessible open source code from day one.

> Start with a README.md and a LICENSE file.

> Use GitHub recommendation or/and https://choosealicense.com/.


### Licensing and ownership

Who can decide about or change a license?

    The copyright holder if a separate “Contributor License Agreement” is signed. Otherwise copyright holder provided they secure express consent from all the contributors.

Who owns the copyright for software you write?

    Intellectual property depends on the country and the employer!

    So-called works made for hire.

If you own your software:

    You can change the license.

    You can dual-license (e.g. GPL for anyone, but you can pay for commercial non-GPL).

If you do not own your software, you can:

    Request open-sourcing directly (preserves your rights!).

    Request a transfer of ownership (check with your university).

If you accept contributions (pull requests), you may not be the only owner anymore!

    Clarify licensing strategy before - otherwise you won’t have all rights to your code.


### Taxonomy of software licenses

1. Custom/closed/proprietary

    Derivative work typically not possible

2. Permissive (MIT, BSD, Apache)

    Derivative work does not have to be shared

    Permissive: gives the public permission to use, modify, and share, without any condition for downstream licensing

    If the licenses of components are permissive, one may use any open license they want.

Permissions, conditions, and limitations of the MIT license

Example: Permissions, conditions, and limitations of the MIT license. Unchanged from https://choosealicense.com/.

3. Weak copyleft share-alike (LGPL, MPL)

    Derivative work is free software but is limited to the component

Permissions, conditions, and limitations of the LGPL license

Example: Permissions, conditions, and limitations of the LGPL license. Unchanged from https://choosealicense.com/.

4. Strong copyleft share-alike (GPL, AGPL)

    Derivative work is free software and derivative work extends to the combined project

    If the licenses of components are strong copyleft, one must use the same license

Permissions, conditions, and limitations of the GPL license

Example: Permissions, conditions, and limitations of the GPL license. Unchanged from https://choosealicense.com/.

If you would like to learn more about licenses, check out our slide deck “Software licensing and open source explained with cakes”.


## Citation

Think the same as for a scientific paper

Our practical recommendations:

    Get a DOI using Zenodo or similar services.

    Open source license can’t demand citation, but it is required by science ethics anyway.

    Make it as easy as possible! Clearly say what you want cited.

    Make it easy for scripts and tools, use the Citation File Format.

    GitHub now supports CITATION.cff files

Recommended format for software citation is to ensure the following information is provided as part of the reference Katz, Chue Hong, Clark, 2021:

    Creator

    Title

    Publication venue

    Date

    Identifier

    Version

    Type
    
 ### DOI/Zenodo
    
````{Admonition} Read more
   [Code refinery: social-coding/](https://coderefinery.github.io/social-coding/)
````

## Exercise ??

```{keypoints}
  - Share your code! Eventually others will probably use it anyway.
  - Licence your software and do it early. Default is “no one can make copies or derivative works”.
  - Get DOI or at least state how to cite your software
```
