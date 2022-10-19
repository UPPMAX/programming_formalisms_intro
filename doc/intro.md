# Introduction

```{questions}
- What is the Purpose of Formalism in Computer Science?
- What is software development life cycle
- There seem to be many concepts in this course. What do they mean?


```

```{objectives}
- We'll give an introducton to the week
- We'll give some introduction to concepts used in the course
- We'll give some introduction to tools
- We'll try to set up the mindset to find the rest of the week interesting and useful!
```

```{instructor-note}
- Lecture 15 min
- Discussions 10 min
```

## What is software?

### Some concepts
- program
- script
- tool
- model
- ---
- application software
- User-written software: End-user development
-----
- scripting vs programming
- Python is an interpreted language. Python uses an interpreter to translate and run its code. Hence Python is a scripting language.
- Programs written in C++ are compiled and then the compiled code runs to generate the output. C++ is thus a programming language and not a scripting language, since scripting languages are directly interpreted at run time and no prior compilation of the code takes place.

```{Note}
   We will use the word `program` for any code in this course!
```

### Your programming background
- Python	86%
-	Bash		80%
-	R		45%
-	C++		14%
-	C		12.5%
-	FORTRAN	12.5%
-	Julia 		5.5%
-	JAVA		4%
-	Perl		4%
-	MATLAB	4 %
-	HTML		4%
-	Javascript	4 %
-	Rest		1 person each
  -	AWK
  -	PHP
  -	Groovy
  -	SQL


## What is software development?

- Different types of Scientific software:
  - analysis of data
    - statistics
    - figures
    - visualization
  - tools for process data
    - refining data (formatting)
    - bioinformatics
  - workflows
  - modelling (mimic the reality)
      - simulations time-varying bahvour of a system
      - mathematical models of relationships among variables in a system 
  - decision assistance

### Icebreaker

What experience have you had?



## Development cycle

agile = characterized by the division of tasks into short phases of work and frequent reassessment and adaptation of plans.

### Basic models
- waterfall
  1.	Requirements
  2.	Analysis and design
  3.	Development
  4.	Test
  5.	Development and maintenance

- Spiral model: iterating waterfalls, quadrants
  -   Planning: reqs, identification: analysis
  -	Risk analysis: build prototypes to identify risks
  -	Engineering: software implementation
  -	Evaluation: stakeholder review, feedback, plan next iteration
  Each lab is new cycle: prototype --> RC --> Launch
  Risk driven

More about life cycles in next session and Day 3

### Parts from the life cycle model in this course

- **Day1** Intro
    - SDLC
        - waterfall
        - cont I and D:s
    - Analysis and design 
      - Pseudocode and flowcharts
        - Unified Modelling language
      - Top-down / Bottom-up 

    - source control
    - reproducibility
        - personal use to general use
        - dependencies
        - platforms
    - documentation
   
- **Day2** Algorithms+data structures
    - intro
    - storing
    - searching for things
    - sorting
    - BLAST
    - exercises
- **Day3-4** Paradigms: design patterns, modular code
    - How?
    - Programming paradigms
        - SDLC and the models for the development process
        - overview
    - Modular programming
        - design patterns introduction to element of reusable software modules
        - what is module
        - common interface design
- **Day4** TDD, testing
    - first look
    - types of tests
    - TDD in practice (afternoon 13:00-16:00)
        - Testing in Python with pytest
        - Automating testing with Github Actions
        - Putting it all together
        - "Advanced" topics
- **Day5** Optimization: halvdag...?


- Development
  - Algorithms
  - Optimization
    - Parallelism
- Test
  - Tests and test-drive development
- Development and maintenance
  - documentation

- Iterations
  - source control
  - reproducibility and sharing


- **iterative methodologies**
- **Agile**

## Object oriented modelling

- classes

{term}`class`

- objects
- generalizations, associations

### Languages
- C++
- Java
- Python 
- Julia
- OO features
  - Fortran 2003 
  - MATLAB
  - Perl
  - PHP
- OO object-based
  - Javascript


## Planning: Analysis and design

```{note}
- Planning step is to ...
   - get an overview of the project/program.
   - help planning writing the code
   - identify parts needed
- Can be devided into analysis and design
- Analysis part is to state the problem and define inputs and outputs
   - graphical tools like UML
- Design phase to find out the specific algorithms needed
   - pseudocode
```

### Top-down
1. Clearly state problem
2. Define inputs and outputs
3. Design the algorithm with `pseudocode`
4. Turn the algorithm into specific language statements
5. Test the resulting program
6. 

### Flowcharts or Unified Modeling Language

```{uml}
@startuml
!theme superhero
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
## Source and version control

- tool
- git
- branches

```{objectives}
   - [Source and version control](https://uppmax.github.io/programming_formalism_intro/sourcecontrol.html) aims to 
     - Introduce git and github
     - Get into working with git
     - Get into using GitHub as a remote repository
```

## Reproducibility and sharing

```{Discussion}
- One-time usage to distributed package
```

```{objectives}
   - [Reproducibility and sharing](https://uppmax.github.io/programming_formalism_intro/reproducible.html) aims to 
     - Introduce reproducibility and sharing, licensing and citation
     - Get into thinking about dependencies and solutions
     - Get into working more with GitHub for collaboration
     - Get into choosing license, citation and DOI
```
## Documentation


```{objectives}
   - [Documentation](https://uppmax.github.io/programming_formalism_intro/documentation.html) aims to 
     - Introduce motivation for documentation
     - Get tips for in-code documentation
     - Get tips for README files
     - Get tips for full documentation and tutorials
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
  - testing: test functions
  - Collaboration: GitHub
  - Documentation: READMEs and e.g. sphinx
```
