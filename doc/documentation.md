# Documentation

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


## In-code

- Why and not how

### Docstrings
A docstring is a structured comment associated to a segment of code (i.e. function or class)

Good docstrings describe:

    What the function does

    What goes in (including the type of the input variables)

    What goes out (including the return type)
    
    python example: help(<function name>)


````{keypoints}
- Comments should describe the why for your code not the what.
- Writing docstrings is an easy way to write documentation while you type code.
````

## README files

````{keypoints}
README file should include:

  - A descriptive project title

  - Motivation (why the project exists)

  - How to setup

  - Copy-pastable quick start code example

  - Recommended citation
````

## Sphinx and Markdown/Restructured text

```{discussion} This lesson is built with Sphinx
- [Source code](https://raw.githubusercontent.com/coderefinery/documentation/main/content/sphinx.md)
- Try to compare the source code and the result side by side
```

- Make use of Spinx to render markdown or reStructuredText to HTML
- Markdown easier, but rst have more possibilities.
- With 

````{keypoints}
  - Lightweight options for writing full documentation.
````


## Deploy
- Make use of free web platforms to put your full documentation!

- GH-pages
- ReadTheDocs

- Input from you?

### Github pages
- Easiest. everything is local to uithub

### Read the Docs
- Somewhat more possibilities, like having several versions of documentation to switch between.

## Exercise

````{Admonition} Read more
   `Code refinery <https://coderefinery.github.io/documentation/>`
````

## Summary

````{Keypoints}
  - Document in code, answering why, not how.
  - Make a README.txt for an overview of the software. Make use of Markdown on Github for easier formatting. It should include:
    - Overview
    - How to install and setup
    - Quick setup
    - Licensing and how to cite
  - Documentation should be tracked with the corresponding code in the same repository.
  - Full documentation or tutorial
    - Make use of Sphinx to render standard markup languages like markdown or reStructuredText to HTML.
  - Deploy at GH-pages or ReadTheDocs
    
```` 
