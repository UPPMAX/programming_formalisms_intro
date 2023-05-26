# Planning phase

```{questions}
  - How to use UML and Pseudocode?
  - Can we learn it?
```

```{Objectives}
   - We will give an overview of UML diagrams
      - learn when to use
      - learn basic notations
      - (Test with graphical interface)
      - (Test with the script based plantUML)
   - We will see some examples of Pseudocode   
   
```

```{instructor-note}
- Lecture + Discussions 45 min
- Perhaps OK length
```

## Some overview

### The planning steps
- get an overview of the project/program.
- help planning writing the code
- identify parts needed

Lifecycle steps, example
1.	Plan/initiate
2.	Gather requirements
3.	Design

or

1. Analysis
  - to state the problem and define inputs and outputs
    - graphical tools like UML
2. Design
  - to find out the specific algorithms needed
    - pseudocode

### Analysis step
- UML Diagrams
  - Flowchart 
- Object-orientation programming
  - Identify objects
- Functional programming
  - Identify functions  
- Text can also work here, describing the problem as a whole

### Design step

- Pseudocode
- Object-orientation programming
  - Identify classes that objects can belong to
  - UML
- Functional programming
  - Identify algorithms 

## Analysis

### State our project goal

```{note}
**Planet project**
The climate last about 1 million years has been largely determined but the change of the eccentricity (elongation) of Earth's orbit (One of the [Milankovitch cycles](https://climate.nasa.gov/news/2948/milankovitch-orbital-cycles-and-their-role-in-earths-climate/).
The glacial cycles (daily speaking: ice ages) with a period of about 100 000 years are thought to be due to this.
Theory: The gravity form the other planets, especially Jupiter, causes the change of the eccentricity
- **Problem*: Reproduce Milankovitch cycle of eccentricity (100ka)
- **Method**: Use Python
  - Let's go for functional programming
- **Input**: Some initial positions of the planets but no external data
  - Perhaps also user input of lenght of simulation
- **Output**: Graph of orbits and a timeseries of an eccentricity parameter
```

## Unified Modeling Language

First iteration in planning can be paper or whiteboard 
Then there are benefits with digital tools 


### Design

- A way to visualize a system's architectural blueprints in a diagram, including elements such as:
  - any activities (jobs);
  - individual components of the system;
    - and how they can interact with other software components;
  - how the system will run;
  - how entities interact with others (components and interfaces);
  - external user interface.

- Although originally intended for object-oriented design documentation, UML has been extended to a larger set of design documentation, and been found useful in many contexts.

### Activity

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
### Syntax for algorithm flowchart

Start and stop

```{uml}
@startuml
start
stop
@enduml
```

```{uml}
@startuml
start
:Hello world;
:This is defined on
several **lines**;
stop
@enduml
```

Computation

Input output

Choice

Direction of program flow
Iterative or counting loop


### PlantUML

- PlantUML is an open-source tool allowing users to create diagrams from a plain text language. 
- uses Graphviz software to lay out its diagrams
- More info and examples at <https://plantuml.com/>

#### Syntax
- https://plantuml.com/

## Pseudocode

- Pseudocode generally does not obey the syntax rules of any particular language
   - there is no systematic standard form. 
- Some writers borrow style and syntax from control structures from some conventional programming language, although this is discouraged.
- Some syntax sources include Fortran, Pascal, BASIC, C, C++, Java, Lisp, and ALGOL. 
- Variable declarations are typically omitted. 
- Function calls and blocks of code, such as code contained within a loop, are often replaced by a one-line natural language sentence.

- Depending on the writer, pseudocode may therefore vary widely in style, 
  - from a near-exact imitation of a real programming language at one extreme
  - to a description approaching formatted prose at the other. 

### Mathematical style pseudocode
- Used in numerical computation

```{math}
\sum_{k\in S} x_k
```

```{Discussion}
In Breakout-rooms 6-8 people:
- What are your impressions about
  - UML?
  - pseudocode?
- Experiences?
- Share in the end 1-3 inputs in HackMD
```

```{note}
More practicals and UML Pseudocode later this week!
```

```{Challenge} Demo of Pseudocode
Define constants
Define initial values
	positions
	velocity (balance of gravity and centrifugal force
(Allocate (book) space for long vectors	plan iteration)
Iteration
	Change of positions
	Calc acc (gravity)
	Calc new velocity
Plot resulting ellipses
Calculate orbit parameters
Plot time series of parameter change
´´´

## Summary

````{Keypoints}
  - UML is good in several conditions
    - Structural overviews
    - Planning
    - Problem solving
    - Designing phase of programming
  - Pseudocode gives a more detailed description what you want the program to do.
    - Can be highly personal or very language-like
```` 
