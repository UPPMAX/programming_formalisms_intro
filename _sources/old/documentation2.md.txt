# Documentation part 2

## HTML static site generators

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

## Deployment
                                        
GitHub, GitLab, and Bitbucket make it possible to serve HTML pages:
- [GitHub Pages](https://pages.github.com) (GH-pages) ← this is what we and CR use for some course material

- [Bitbucket Pages](https://pages.bitbucket.io/)
- [GitLab Pages](https://pages.gitlab.io)
- [Read the docs](http://readthedocs.org) ← this is what NBIS use for some course material

### Github pages
- Easiest. everything is local to GitHub
- This lesson material

### Read the Docs
- Somewhat more possibilities, like having several versions of documentation to switch between.
- Example
                                      
## Wikis

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

## Other generators
### LaTeX/PDF
- Advantage
  - Popular and familiar in the physics and mathematics community
- Disadvantages
  - PDF format is not ideal for copy-paste ability of examples
  - Possible, but not trivial to automate rebuilding documentation after every Git push

### Doxygen (C, C++, Java atc...)
- Auto-generates API documentation
- Documented directly in the source code
  see [Doxygen Github Repo](https://github.com/doxygen/doxygen)
- Can be deployed to GiHub/GitLab/Bitbucket Pages

### For Fortran 
- [Fortran Documenter (FORD)](https://github.com/Fortran-FOSS-Programmers/ford)

### For Julia
- [Franklin](https://franklinjl.org/): static site generator
- [Documenter.jl](https://juliadocs.github.io/Documenter.jl/stable/)

### For Markdown
- [Quarto](https://quarto.org/) converts markdown to websites, pdfs, ebooks and many other things

---

## Demo These pages
``````{challenge} Demo: Git repo -  Sphinx - GitHub - GitHub Actions - GH-pages
                                        
- We will go behind the scenes of this documentation.
- You can do this checkout whenever you want.

**The basic steps are:**
(also presented [here](https://coderefinery.github.io/documentation/sphinx/)               
- Start locally in repo with name describing the project
- You can generate Sphinx documentation in an existing code project (may be a git repo)
- Install python package: `sphinx`
- `sphinx-quickstart` to generate directories and files
- `index.rst` is first page and includes the Table of contents (TOC) to be seen in a menu and the *.md and/or *.rst files to make up your web pages.
- `config.py`contains configurations like Sphinx extensions. (these python packages may have to be installed as well)
- You can build locally and view results in a web browser
---
**To use GH-pages**
- push to the GitHub remote wnd continue working from there.
- Add the GitHub Action
- Create a new file at `.github/workflows/documentation.yaml`
- Enable GitHub Pages:
  - Go to `[https://github.com/myuser/word-count/settings/pages](https://github.com/UPPMAX/programming_formalism_intro)` 
  - In the “Source” section, choose “gh-pages” in the dropdown menu and click save 
- That’s it! Your site should now be live on [https://uppmax.github.io/programming_formalism_intro/index.html](https://uppmax.github.io/programming_formalism_intro/index.html).
   
**Everytime you commit the GH Actions will render your source code to html and deploy it to your new web page!**
``````
   

````{Admonition} Read more
   `CodeRefinery' <https://coderefinery.github.io/documentation/>`
````
