# Software Development Lifecycle (SDLC) tools

```{questions}
- What are the key concepts and steps in the SDLC
- What are the tools for a project?

```

```{objectives}
- We will have an introduction to some SDLC key features
- We will get some theory of project tools and thinking.
```



```{instructor-note}
- Lecture 45 min
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
- :warning:  Error is spreading 
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
  - Expensive: Spiral Model is **not suitable for small projects**
  - **Too much dependability on Risk Analysis**


## Take aways from other methods 
### [The Agile manifest](https://agilemanifesto.org/)

"Agile = characterized by the division of tasks into short phases of work and frequent re-assessment and adaptation of plans."

```{admonition} Values
- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan
```

**Most other models are Agile...**
see the extra reading section: https://uppmax.github.io/programming_formalisms_intro/SDLC_models.html

- Modern principles: 
  - automated tests, continuous integration
- Deliver as fast as possible: small iterations are easier to manage
- Extreme Programming
  - Pair programming
    - Collaborate, continuous code inspection
    - real-time development technique to increase algorithm implementation
  - Test-driven development
    - Write test
    - Write function to fail test
   - Write code to pass test

```{admonition} Conclusion
  - Each team has unique requirements
  - Try out agile practices that make the most sense
  - Don’t be afraid of trial and error
```

## The tools/concepts for Developing a programming project

- Planning
  - Pseudocode
  - Unified Modelling Language
- Testing
  - Different levels
- Source/version control
  - Git etc
- Collaboration
  - Github
- Reproducibility (for you and others)
  - Dependencies
  - (Workflows)
  - Containers (deployment)
- Sharing
  - open science
  - citation
  - licensing  
- Documentation
  - Tutorials
  - How-to guides
  - Explanation
  - Reference 

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
   - (risk analysis)
- Can be divided into analysis and design
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

<https://en.wikipedia.org/wiki/List_of_Unified_Modeling_Language_tools>

- Modeling
  - Code generation
  -	Reverse engineering
  - Analyze code complexity
  -	Other metrics

```{graphviz}
digraph{
"UML diagrams"
Structure, Behaviour
"UML diagrams" -> Structure
"UML diagrams" -> Behaviour
Structure -> Class, Component, Object, composite
Behaviour -> "Use case", Activity, Interaction
Interaction -> Sequence, Communication, Timing, "Interaction overview"
}
```

``{admonition} We will use
  - Sequence
  - Activity/algorithm flowchart
``

##### Sequence

```{uml} puml/external.uml
```

```console
@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response

Alice -> Bob: Another authentication Request
Alice <-- Bob: Another authentication Response
@enduml
```

##### Activity

A flowchart that shows the process and its correlating decisions, including an **algorithm**  or a business process.

```{uml} puml/activity.puml
```

```console
@startuml

start

if (Graphviz installed?) then (yes)
  :process all\ndiagrams;
else (no)
  :process only
  __sequence__ and __activity__ diagrams;
endif

stop

@enduml
```

##### Algorithm flowchart
```{uml}
@startuml
start
if (stuff) then (true) 
   :action 2;
endif

stop
@enduml
```


#### Tools
- PlantUML
  - Open-source
  -	Can be integrated with IDE:s, Java documentation, Word
  -	Scripts rather than drawing tools
  -	<http://www.plantuml.com/plantuml>
- Graphviz
  - Graphviz is open source graph visualization software. 
  - Graph visualization is a way of representing structural information as diagrams of abstract graphs and networks. 
  - It has important applications in networking, bioinformatics, software engineering, database and web design, machine learning, and in visual interfaces for other technical domains.
  - https://graphviz.org/
- Mermaid
  - Open-source
  - Not as many diagrams
  - renders in browser
  - https://mermaid.js.org/

##### Class

 A diagram that shows the system classes and relationships between them.

```{uml} puml/class.puml
```

```console
@startuml
node foo
foo --> bar : normal
foo --> bar1 #line:red;line.bold;text:red  : red bold
foo --> bar2 #green;line.dashed;text:green : green dashed 
foo --> bar3 #blue;line.dotted;text:blue   : blue dotted
@enduml
```

```{uml}
@startuml
class Car

Driver - Car : drives >
Car *- Wheel : have 4 >
Car -- Person : < owns
@enduml
```

```console
@startuml
class Car

Driver - Car : drives >
Car *- Wheel : have 4 >
Car -- Person : < owns
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
## Testing

Does it work for all legal input data sets??

1. Unit testing 
2. Integration tests (test modeuls together as a whole)

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

```{note}

   **More about testing day 2-3**

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

- Have you ever spent days trying to repeat the results that took you hours to do the first time last week?  
- Or you have to do paper revisions, but you just can’t get the results to match up? 
- Nothing is a worse feeling - either for you or for science itself.

- Some theory will be given in the [Extra material](https://uppmax.github.io/programming_formalisms_intro/reproducible_deeper.html)
- We will integrate this topic in the hands-on.
- We will discuss different methods and tools for better reproducibility in research software and data.
  - virtual environments with ``pip install`` (venv/vuirtualenv) will be covered in the hands-on.
  - Conda environment is referred to in the extra material. 
- We will demonstrate how version control, workflows, containers, and package managers can be used to record reproducible environments and computational steps.

```{objectives}
   - [More about reproducibility](https://uppmax.github.io/programming_formalism_intro/reproducible_deeper.html) aims to 
     - Get a short overview of recording dependencies
     - Get short intro to tools:
       - Pip and PyPI
       - Conda
       - Environments
       - Tools for other languages than Python
   - We will develop our code in a virtualenvironment with the python tool ``venv ``   
  
```
  
 ### Sharing and licensing and citations
 
```{Discussion}
- One-time usage towards distributed package
```
#### Open science

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

### Licencing
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

### Software Citation

- Think the same as for a scientific paper
- [Software citation](https://uppmax.github.io/programming_formalisms_intro/sharing_deeper.html#software-citation)

```{keypoints}
- Share your code! Eventually others will probably use it anyway.
- Licence your software and do it early. Default is “no one can make copies or derivative works”.
- Get DOI or at least state how to cite your software
```

```{objectives}
   - [More about sharing](https://uppmax.github.io/programming_formalism_intro/sharing_deeper.html) aims to 
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
  - Testing: test functions (Covered later)
  - Collaboration: GitHub, licenses, citation
  - Documentation: In-code, READMEs and e.g. sphinx
```
