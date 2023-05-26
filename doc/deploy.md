# Deploy and document for usage

Make yor program or workflow work for others and yourself in the future


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

- podman

They are to some extent interoperable:

- podman is very close to Docker

- Docker images can be converted to Singularity/Apptainer images

- Singularity Python can convert Dockerfiles to Singularity definition files

https://coderefinery.github.io/reproducible-research/environments

## Reproducible publications
- Git (overleaf, authorea), hackmd, manuscripts.io, google docs
- Scholarly output reproducible: rrtools, jupyter, binder, research compendia
- Reprohack

```{keypoints}
  - Preserve the steps for re-generating published results.
  - Hundreds of workflow management tools exist.
  - Snakemake is a comparatively simple and lightweight option to create transferable and scalable data analyses.
  - Sometimes a script is enough.
```
## Documentation part 2

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

- [pkgdown](https://pkgdown.r-lib.org/)
  - Popular in the R community

- [MkDocs](https://www.mkdocs.org/)
- [GitBook](https://www.gitbook.com/)
- [Hugo](https://gohugo.io)
- [Hexo](https://hexo.io)
- [Zola](https://www.getzola.org/) **← this is what CodeRefinery use for their project website and workshop websites**

There are many more ...

### Deployment
                                        
GitHub, GitLab, and Bitbucket make it possible to serve HTML pages:
- [GitHub Pages](https://pages.github.com) (GH-pages) ← this is what we and CR use for some course material

- [Bitbucket Pages](https://pages.bitbucket.io/)
- [GitLab Pages](https://pages.gitlab.io)
- [Read the docs](http://readthedocs.org) ← this is what NBIS use for some course material

#### Github pages
- Easiest. everything is local to GitHub
- This lesson material

#### Read the Docs
- Somewhat more possibilities, like having several versions of documentation to switch between.
- Example
                                      
### Wikis

- Popular solutions (but many others exist):
  - [MediaWiki](https://www.mediawiki.org)
  - [Dokuwiki](https://www.dokuwiki.org)
- Advantage
  - Barrier to write and edit is low
- Disadvantages
  - Typically disconnected from source code repository (**reproducibility**)
  - Difficult to serve multiple versions
  - Difficult to check out a specific old version
  - Typically needs to be hosted and maintained

---

#### Demo These pages
``````{challenge} Make Documentation
``````
 

````{Admonition} Read more
   `CodeRefinery' <https://coderefinery.github.io/documentation/>`
````
