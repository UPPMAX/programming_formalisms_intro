# Software Development Lifecycle (SDLC) tools

```{questions}
- What are the different SDLC:s
- When to use which?
```

```{objectives}
- We will have an introduction to some the SDLC:s
- More on Wednesday!!
```



```{instructor-note}
- Lecture 25 min
- Shorten to 15m
```


## The waterfall model

1.	Requirements
2.	Analysis and design
3.	Development
4.	Test
5.	Development and maintenance

```{graphviz}
digraph {
   rankdir=LR;
  "Requirements" -> "Analysis and design" -> "Development" -> Test -> "Development and maintenance";
}
```

- Good approach for **small and simple systems** where the team knows the system and **requirements very well**.
- |:warning:|  Error is spreading 
  - small mistakes in the beginning will have large impact on the end result. 
    - e.g. bugs, architecture limiting extensions
  - large costs economically and timely

## Include iteration
### Spiral model

1. Planning: reqs, identification: analysis
1. Risk analysis: build prototypes to identify risks
1. Engineering: software implementation
1. Evaluation: stakeholder review, feedback, plan next iteration
1. Each lab is new cycle: prototype--> RC --> launch
1. Risk driven

```{figure} img/spiral-1-1024x945.jpg
:alt: spiral
:width: 50%
```

- **Disadvantages**
  - Complexer than other SDLC models.
  - Expensive: Spiral Model is **not suitable for small projects**
  - **Too much dependability on Risk Analysis**
  - Difficulty in time management: Number of phases is unknown at the start of the project

### Rational unified process (RUP) 
- **Phases**: Each containing **1 or more waterfall iterations**
  - Inception (lifecycle objectives milestone)
  - Elaboration (lifecycle architecture milestone)
  - Construction (initial operational capability, milestone)
  - Transition (production release milestone)

- **Key takeaways**
  - RUP principles
    - Use cases
    - **Develop iteratively**
    - Manage **requirements**, change
    - **Continuously verify quality**
    - **Model visually, component-based architecture**
- Shortcomings: customizable but heavy, prescriptive, (lacking test-driven development)

## Take aways from other methods 
### [The Agile manifest](https://agilemanifesto.org/)

```{admonition} Values
- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan
```

Or:
"Agile = characterized by the division of tasks into short phases of work and frequent re-assessment and adaptation of plans."

**Most other models are Agile...**
see the extra reading section: https://uppmax.github.io/programming_formalisms_intro/SDLC_models.html

- Parallel development
- Modern principles: automated tests, frequent integration
- Deliver as fast as possible: small iterations are easier to manage
- Visualize your work, **limit work in progress**
- Extreme Programming
  - Pair programming
    - Collaborate, continuous code inspection
    - real-time development technique to increase algorithm implementation
  - Test-driven development
    - Write test
    - Write function to fail test
   - Write code to pass test
- DevOps (Development Operations)
  - **Dev**elopers and testers
  - **Ops**: people working with release, servers, network, storage configs etc...
  - DevOps aims to extend fast and frequent software feature development 
  - Phases: development --> test --> stage --> production
  - **Continous**...
    - **Integration**: Central repository
    - development + test
  - **Development**: Ensuring stable product after every release
    - development + test + stage
  - **Deployment**: automating updates to production
    - development + test + stage + production

**And more...**

## Key take aways
### Basic steps

1.	Plan/initiate
2.	Gather requirements
3.	Design
4.	Develop
5.	Test/validate
6.	Release/maintain
7.	Certification/accreditation
8.	Change and configuration management

```{graphviz}
digraph {
   rankdir=LR;
   "Plan" -> "Requirements" -> "Design" -> "Develop" -> Test -> Release -> Certification -> Change -> "Plan";
}
```

### Conclusions
  - Each team has unique requirements
  - Try out agile practices that make the most sense
  - Don’t be afraid of trial and error

```{info}
More on Wednesday
```

## Planning: Analysis and design

```{note}
"If I had nine hours to chop down a tree, I'd spend the first six sharpening my axe.
-	Modeling sharpens your axe since it helps you think about what you're going to build, how to seek feedback, and where to make improvements. It prepares you to build the real thing to reduce any potential risk of failure. "
```


```{note}
- Planning step is to ...
   - get an overview of the project/program.
   - help planning writing the code
   - identify parts needed
- Can be devided into analysis and design
- Analysis part is to state the problem and define inputs and outputs
   - graphical tools like UML
   - text
   - objects in OOP
- Design phase to find out the specific algorithms needed
   - pseudocode+UML
   - classes in OOP
   - functions/modules in functional programming
   
```

### Top-down
1. Clearly state whole problem
2. Define inputs and outputs
3. Design the algorithm with `pseudocode`
4. Turn the algorithm into specific language statements
5. Test the resulting program

```{uml}
@startuml
start
:Clearly state whole problem;
:Define inputs and outputs;
:Design the algorithm with `pseudocode`'
  - Decomposition
  - Stepwise refinement;
:Turn the algorithm into specific language statements;
:Test the resulting program;

stop

@enduml
```


### Bottom-Up
Start with parts first and develop a bigger organization with time.

```{Discussion}
How do you program? Put "o" on you choice
- Top-down
- Bottom-up
```

### Flowcharts or Unified Modeling Language

```{uml}
@startuml
start
if (stuff) then (true) 
   :action 2;
endif

stop
@enduml
```

### Pseudocode

**Example**

```{code}
  algorithm ford-fulkerson is
    input: Graph G with flow capacity c, 
           source node s, 
           sink node t
    output: Flow f such that f is maximal from s to t

    (Note that f(u,v) is the flow from node u to node v, and c(u,v) is the flow capacity from node u to node v)

    for each edge (u, v) in GE do
        f(u, v) ← 0
        f(v, u) ← 0

    while there exists a path p from s to t in the residual network Gf do
        let cf be the flow capacity of the residual network Gf
        cf(p) ← min{cf(u, v) | (u, v) in p}
        for each edge (u, v) in p do
            f(u, v) ←  f(u, v) + cf(p)
            f(v, u) ← −f(u, v)

    return f
```

```{objectives}
   - [Planning phase section](https://uppmax.github.io/programming_formalism_intro/flowcharts.html) aims to 
     - Introduce flowcharts and UML expressions
     - Get into UML coding with PlantUML
```
## Source/version control and collaboration

###  The essence of version control
Summarized from [Code refinery](https://coderefinery.github.io/git-intro/motivation/)

- System which records snapshots of a project
- Implements branching:
  - You can work on several feature branches and switch between them
  - Different people can work on the same code/project without interfering
  - You can experiment with an idea and discard it if it turns out to be a bad idea
- Implements merging:
  - Person A and B’s simultaneous work can be easily combined

### What we typically like to snapshot

- Software (this is how it started but Git/GitHub can track a lot more)
- Scripts
- Documents (plain text files much better suitable than Word documents)
- Manuscripts (Git is great for collaborating/sharing LaTeX or Quarto manuscripts)
- Configuration files
- Website sources
- tool

###  Why version control
- Roll-back functionality
   - Mistakes happen - without recorded snapshots you cannot easily undo mistakes and **go back to a working version**.
- Branching
  - Often you need to work on **several issues/features in one code** - without branching this can be messy and confusing.
  - You can simulate branching by copying the entire code to multiple places but also this will be messy and confusing.
- Collaboration
  - With version control, none of these are needed anymore (or have much simpler answers):
    - *"I will just finish my work and then you can start with your changes."*
    - *"Can you please send me the latest version?"*
    - *"You never got the code I send by email? Maybe the spam filter marked it as malicious?"*
    - *"Where is the latest version?"*
    - *"Which version are you using?"*
   - *"Which version have the authors used in the paper I am trying to reproduce?"*
- Reproducibility
  - How do you indicate which version of your code you have used in your paper?
  - When you find a bug, how do you know **when precisely** this bug was introduced
  (Are published results affected? Do you need to inform collaborators or users of your code?).
- Compare with Dropbox or Google Drive
  - Document/code is in one place, no need to email snapshots.
  - How can you use an old version? Possible to get old versions but in a much less useful way - snapshots of files, not directories.
  - What if you want to work on multiple versions at the same time? Do you make a copy? How do you merge copies?
  - What if you don't have internet?

```{discussion} Why Git?
We will use [Git](https://git-scm.com) to record snapshots of our work:
- **Easy to set up**: no server needed.
- **Very popular**: chances are high you will need to contribute to somebody else's code which is tracked with Git.
- **Distributed**: good backup, no single point of failure, you can track and
  clean-up changes offline, simplifies collaboration model for open-source
  projects.
- Important **platforms** such as [GitHub](https://github.com), [GitLab](https://gitlab.com), and [Bitbucket](https://bitbucket.org)
  build on top of Git.

However, any version control is better than no version control and it is OK to prefer a different tool than Git.

Other tools:
- [Subversion](https://subversion.apache.org)
- [Mercurial](https://www.mercurial-scm.org)
- [Pijul](https://pijul.org/)
```
### Sharing Online

- What if the hard disk fails?
- What if somebody steals my laptop?
- How can we collaborate with others across the web?

#### Remotes

To store your git data on another server, you use remotes. A remote is a repository on its own, with its own branches We can push changes to the remote and pull from the remote.

You might use remotes to:

 - Back up your own work.

 - To collaborate with other people.

There are different types of remotes:

- If you have a server you can ssh to, you can use that as a remote.
- [GitHub](https://github.com) is a popular, closed-source commercial site.
- [GitLab](https://about.gitlab.com) is a popular, open-core
  commercial site.  Many universities have their own private GitLab servers
  set up.
- [Bitbucket](https://bitbucket.org) is yet another popular commercial site.
- Another option is [NotABug](https://notabug.org)


```{attention}
**Also workflows!**
```

```{objectives}
   - [Source and version control](https://uppmax.github.io/programming_formalism_intro/sourcecontrol.html) aims to
      - Introduce git and github
      - Get into working with git
      - Get into using GitHub as a remote repository
   ```

## Collaboration

- Let's say that someone has given you access to a repository online and you want to contribute to it.
- It is quite easy to make a copy and send a change back.
- First, we do this a relatively simple way: get repository, make a change
  locally, and send the change directly back.
- Then, we make a "pull request" that allows a review.
- Once we know how code review works, we will be able to propose changes
  to repositories of others and review changes submitted by external
  contributors.

```{objectives}
   - [Collaboration](https://uppmax.github.io/programming_formalism_intro/collab.html) aims to 
     - Get into working more with GitHub for collaboration
     - Centralized workflow
     - Forking
     - Contributing to other's projects
```

## Reproducibility and sharing

### Reproducible research

- Have you ever spent days trying to repeat the results that took you hours to do the first time last week?  - Or you have to do paper revisions, but you just can’t get the results to match up? Nothing is a worse feeling - either for you or for science itself.

In this lesson we will discuss different methods and tools for better reproducibility in research software and data. We will demonstrate how version control, workflows, containers, and package managers can be used to record reproducible environments and computational steps.

```{objectives}
   - [Reproducibility and sharing](https://uppmax.github.io/programming_formalism_intro/reproducible.html) aims to 
     - Get a short overview of recording dependencies
     - Get short intro to tools:
       - Pip and PyPI
       - Conda
       - Environments
       - Tools for other languages than Python

```
  
 ### Sharing and licensing and citations
  
  
```{Discussion}
- One-time usage to distributed package
```

```{objectives}
   - [Reproducibility and sharing](https://uppmax.github.io/programming_formalism_intro/reproducible.html) aims to 
     - Introduce reproducibility and sharing, licensing and citation
     - Get into thinking about dependencies and solutions
     - Get into choosing license, citation and DOI
```
## Documentation

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

**There is no one size fits all**: often for small projects a `README.md` or
`README.rst` can be enough (more about these formats later).

```{objectives}
   - [Documentation](https://uppmax.github.io/programming_formalism_intro/documentation.html) aims to 
     - Introduce motivation for documentation
     - Get tips for in-code documentation
     - Get tips for README files
     - Get tips for full documentation and tutorials
```

## Testing

Does it work for all legal input data sets??

1. Unit testing 
2. Integration tests

**Typical testing process**

```{uml}
@startuml
start
:Unit testing of individual subtasks;
-> subtasks validated sperately;
repeat: Successive builds \n - adding subtasks to the program;
backward:As many times as necessary;
repeat while
-> subtasks combined into program;
repeat: Alpha release;
backward:As many times as necessary;
repeat while
-> worst bugs fixed;

repeat: Beta release;
backward:As many times as necessary;
repeat while
-> minor bugs fixed;
:Finished program;

stop

@enduml


```


```{keypoints}
- Typical workflow:
  - Requirements
  - Analysis and design
  - Development
  - Test
  - Development and maintenance
- Iteration!
- Important to identify problem in beginning and add for flexibility

```

## Summary of Introduction
- Now after the overview you are ready to dig deeper in the topics and try it out yourself!

```{Keypoints}
- Software development is both series of steps: 
     1.	Requirements
     2.	Analysis and design
     3.	Development
     4.	Test
     5.	Development and maintenance
- ... and iteration of these
- Planning for reproducibility, modularity and documentation should be started in the beginning
- Tools for the developer
  - Planning: UML and pseudocode
  - Development iteration: git
  - Testing: test functions (Covered on Thursday)
  - Collaboration: GitHub, licenses, citation
  - Documentation: READMEs and e.g. sphinx
```