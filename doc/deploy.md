# Deploy and document for usage

```{Objectives}
   - We will prepare for use of your code
   - Update the README
   - update a Doc Index
   - Revisit licence
   - But also...
     - some theory of packages
     - some theory of workflows
     - some theory of containers
     - some info about tutorials/reference/howTo guides
```

```{attention}
- Make your program or workflow work for others and yourself in the future.
- Let people understand how to use your program/tool
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
   -    Provide tools and services to **share packages**

[The tools](https://uppmax.github.io/programming_formalisms_intro/reproducible_deeper.html#the-tools)

**Course advertisment**
[Python for scientific computing](https://aaltoscicomp.github.io/python-for-scicomp/)

## Workflows

```{admonition} Learn more
<https://coderefinery.github.io/reproducible-research/workflow-management/>
<https://nbis-reproducible-research.readthedocs.io/en/course_2104/snakemake/>
```
## Containers

Popular container implementations:
- Docker
- Singularity (popular on high-performance computing systems)
- Apptainer (popular on high-performance computing systems, fork of Singularity)
- Docker images can be converted to Singularity/Apptainer images
- Singularity Python can convert Dockerfiles to Singularity definition files
https://coderefinery.github.io/reproducible-research/environments
https://uppmax.github.io/programming_formalisms_intro/reproducible_deeper.html#containers


```{keypoints}
  - Preserve the steps for re-generating published results.
  - Hundreds of workflow management tools exist.
  - Snakemake is a comparatively simple and lightweight option to create transferable and scalable data analyses.
  - Sometimes a script is enough.
```


## Documentation for tutorials
```{note} Documentation comes in different forms - what *is* documentation?
  - **Tutorials**: learning-oriented, allows the newcomer to get started
  - **How-to guides**: goal-oriented, shows how to solve a specific problem
  - **Explanation**: understanding-oriented, explains a concept
  - **Reference**: information-oriented, describes the machinery
  **Not to forget**
  - Project documentation:
    - requirements: what is the goal of the software, risks, platforms
    the analysis: pseusocode and UML
    - risk analysis
```

### HTML static site generators

   There are many tools that can turn RST or Markdown into beautiful HTML pages:

- [Sphinx](http://sphinx-doc.org) **← we will exercise this, this is how this lesson material is built**
  - Generate HTML/PDF/LaTeX from RST and Markdown.
  - Basically all Python projects use Sphinx but **Sphinx is not limited to Python**
  - [Read the docs](http://readthedocs.org)
    hosts public Sphinx documentation for free!
  - Also hostable anywhere else, like Github pages. **← this is what we use for this lesson 
  - API documentation possible
- [Jekyll](https://jekyllrb.com)
  - Generates HTML from Markdown.
  - GitHub supports this without adding extra build steps.
- [MkDocs](https://www.mkdocs.org/)

There are many more ...

### Deployment on servers
                                        
GitHub, GitLab, and Bitbucket make it possible to serve HTML pages:
- [GitHub Pages](https://pages.github.com) (GH-pages) ← this is what we and CR use for some course material

- [Bitbucket Pages](https://pages.bitbucket.io/)
- [GitLab Pages](https://pages.gitlab.io)
- [Read the docs](http://readthedocs.org) ← this is what NBIS use for some course material

#### Github pages
- Easiest. Everything is local to GitHub
- This lesson material

#### Read the Docs
- Somewhat more possibilities, like having several versions of documentation to switch between.
                                      
### Wikis
- Popular solutions (but many others exist):
  - [MediaWiki](https://www.mediawiki.org)
  - [Dokuwiki](https://www.dokuwiki.org)
  - Also on GitHub!
  - Typically needs to be hosted and maintained
 
````{Admonition} Read more
   `CodeRefinery' <https://coderefinery.github.io/documentation/>`
````


## Last hands on your documentation
- Some inspiration [Beagle](https://github.com/yampelo/beagle)

```{admonition} A little more about licensing

Copyleft is the legal technique of granting certain freedoms over copies of copyrighted works with the requirement that the same rights be preserved in derivative works.

1. Custom/closed/proprietary
    Derivative work typically not possible
2. Permissive (MIT, BSD, Apache)
    Derivative work does not have to be shared
    Permissive: gives the public permission to use, modify, and share, without any condition for downstream licensing
    If the licenses of components are permissive, one may use any open license they want.
3. Weak copyleft share-alike (LGPL, MPL)
    Derivative work is free software but is limited to the component
4. Strong copyleft share-alike (GPL, AGPL)
    Derivative work is free software and derivative work extends to the combined project
    If the licenses of components are strong copyleft, one must use the same license
```

```{admonition} Citation bullets    
   - Creator
   - Title
   - Publication venue
   - Date
   - Version
   - Type
```

``````{challenge} Update your documentation
- Revisit your README and update it with info after all our commits
  - About
  - Installation
  - Citing

``````


