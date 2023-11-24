# Planning phase

```{questions}
  - How to use UML and Pseudocode?
  - Can we learn it?
```

```{Objectives}
   - We will give an overview of UML diagrams
      - learn when to use
      - learn basic notations
   - We will see some examples of Pseudocode   
   
```

```{instructor-note}
```

## Some overview

```{admonition} The planning steps
1. Analysis
  - Get an overview of the project/program and goals
  - to state the problem and define inputs and outputs
  - Gather requirements
  - graphical tools like UML
1. Design
  - to find out the specific algorithms needed
  - pseudocode
```

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

## The Planet project

### Analysis

```{admonition} Planet project
Background
- The climate last about 1 million years has been largely determined but the change of the eccentricity (elongation) of Earth's orbit (One of the [Milankovitch cycles](https://climate.nasa.gov/news/2948/milankovitch-orbital-cycles-and-their-role-in-earths-climate/).
- The glacial cycles (daily speaking: ice ages) with a period of about 100 000 years are thought to be due to this.
Theory: The gravity form the other planets, especially Jupiter, causes the change of the eccentricity
- **Problem*: Reproduce Milankovitch cycle of eccentricity (100ka)
- **Method**: Use Python
  - Let's go for functional programming
- **Input**: Some initial positions of the planets but no external data
  - Perhaps also user input of length of simulation
- **Output**: Graph of orbits and a timeseries of an eccentricity parameter

**Development steps** (we extend the program with iterations)
1. Earth-sun system
2. Add Jupiter
3. Make modular
4. Add more planets?
```

### Let's make a flowchart of the program parts

``````{demo}
We want to make a activity diagram of these steps.

I will use <https://www.planttext.com/> for this

- define some parameters
- initialize earth (and Jupiter later on)
- repeat until simulation time is met
  - calculate acceleration
  - calculate velocity in two dimensions
- then plot figure 



````{solution}
```console
@startuml

start

:define some parameters;
:initialize earth (and Jupiter);

repeat
  :calculate acceleration;
  :calculate velocity in two dimensions;

repeat while (simulation time is met) is (no)
->yes;
:figure plotting;
stop

@enduml
```
````

```````


https://www.planttext.com/

## Design

- A way to visualize a system's architectural blueprints in a diagram, including elements such as:
  - any activities (jobs);
  - individual components of the system;
    - and how they can interact with other software components;
  - how the system will run;
  - how entities interact with others (components and interfaces);
  - external user interface.

- Although originally intended for object-oriented design documentation, UML has been extended to a larger set of design documentation, and been found useful in many contexts.



### Let's make a flowchart of the program parts

#### Syntax for algorithm flowchart
- [plantuml.com](https://plantuml.com/)

`````{admonition} PlantUML Cheat sheet

```{uml}
@startuml
start
:Hello world;
:This is defined on
several **lines**;
stop
@enduml
```

Start with 

```console
@startuml
start
:Hello world;
:This is defined on
several **lines**;
stop
@enduml

``` 
``````

#### Exercise
````{challenge} Test some psuedocode 10 min
- go to [plantuml server](https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000)
- try to make a flowchart of the program parts 
- have a look on examples, for help: [activity-diagram](https://plantuml.com/activity-diagram-beta)
````

### Do some pseudocode of the calculations

```{Challenge} Demo of Pseudocode

```{code}
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

```{note}
More practicals and UML Pseudocode later this week!
```

## Wrap-up

```{Discussion} If there is time
In Breakout-rooms 6-8 people:
- What are your impressions about
  - UML?
  - pseudocode?
- Experiences?
- Share in the end 1-3 inputs in HackMD
```


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
