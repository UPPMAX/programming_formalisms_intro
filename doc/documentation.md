# Documentation

```{instructor-note}
- Lecture 20.0 min
```

```{discussion} Motivation: Why should we document code?

- **Use the collaborative document**.
- Is project documentation important? Why?
- How would you describe a useful documentation?
```

```{Objectives}
   - We will give an overview of different levels of documentation
      - in-code
      - README:s
      - Full documentation/tutorials
   - We will give examples where to deploy a documenation page.
```

## Project documentation

- Think that everything is worth to be part of documentation (like Github directory tree)
- The parts from the software development cycle
  - The planning parts
      - Requirements: 
        - what should the program deliver
        - dependencies
        - OS platforms
      - Risk analysis
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
## reStructuredText and Markdown

- Two of the most popular lightweight markup languages.
- reStructuredText (RST) has more features than Markdown but the choice is a matter of taste.
- Markdown convenient for smaller documents,
  but for larger and more complicated documents RST may be a better option.
- There are (unfortunately) [many flavors of Markdown](https://github.com/jgm/CommonMark/wiki/Markdown-Flavors).

```markdown
# This is a section in Markdown   This is a section in RST
                                  ========================

## This is a subsection           This is a subsection
                                  --------------------

Nothing special needed for        Nothing special needed for
a normal paragraph.               a normal paragraph.

                                  ::

    This is a code block          This is a code block


**Bold** and *emphasized*.        **Bold** and *emphasized*.

A list:                           A list:
- this is an item                 - this is an item
- another item                    - another item

There is more: images,            There is more: images,
tables, links, ...                tables, links, ...
```
   
Experiment with Markdown:
- [Learn Markdown in 60 seconds](http://commonmark.org/help/)
- [https://dillinger.io](http://dillinger.io)
- [https://stackedit.io](https://stackedit.io)

To convert between MD and RST (and many other formats):
- [Pandoc](https://pandoc.org/)

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

## Summary

````{Keypoints}
  - Think that everything is worth to be part of documentation (like Github directory tree)
  - Document in code, answering why, not how.
  - Make a README.txt for an overview of the software. Make use of Markdown on Github for easier formatting. It should include:
    - Overview
    - How to install and setup
    - Quick setup
    - Licensing and how to cite
  - Documentation should be tracked with the corresponding code in the same repository.
  - Full documentation or tutorial
    - Make use of Sphinx or MkDocs to render standard markup languages like markdown or reStructuredText to HTML.
  - Deploy wat GH-pages or ReadTheDocs or other.
    
```` 
