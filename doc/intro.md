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
  - decision assistance

ALT:
  - computational
    - simulations time-varying bahvour of a system
  - analytical
    - mathematical models of relationships among variables in a system 
  - non-analytical/descritptive
    - components and their relationships in as system    

  

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
  - Planning: reqs, identification: analysis
  -	Risk analysis: build prototypes to identify risks
  -	Engineering: software implementation
  -	Evaluation: stakeholder review, feedback, plan next iteration
  -	Each lab is new cycle: prototype --> RC --> Launch
  -	Risk driven

More about life cycles in next session and Day 3

### Parts from the life cycle model in this course

- Day1 Intro
    - SDLC
        - waterfall
        - cont I and D:s
    - planning: UML
    - source control
    - reproducibility
        - personal use to general use
        - dependencies
        - platforms
    - documentation
   

- Day2 Algorithms+data structures
    - intro
    - storing
    - searching for things
    - sorting
    - BLAST
    - exercises
- Day3-4 Paradigms: design patterns, modular code
    - How?
    - Programming paradigms
        - SDLC and the models for the development process
        - overview
    - Modular programming
        - design patterns introduction to element of reusable software modules
        - what is module
        - common interface design
- Day4 TDD, testing
    - first look
    - types of tests
    - TDD in practice (afternoon 13:00-16:00)
        - Testing in Python with pytest
        - Automating testing with Github Actions
        - Putting it all together
        - "Advanced" topics
- Day5 Optimization: halvdag...?


- Analysis and design 
  - Unified Modelling language
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
- objects
- generalizations, associations

## Unified Modelling language

- Key refernces
  - UML 2.5
  - UML distilled
  - Applying UML and Patterns

## Source control

tool
git
branches

## Reproducibility and sharing
Discussion
•	One-time usage to distributed package

## Documentation


## Concepts

## Exercises

````{exercise} In-code-1: Comments
Let's take a look at two example comments (comments in python start with `#`):

**Comment A**
```python
# Now we check if temperature is larger then -50:
if temperature > -50:
    print('do something')
```

**Comment B**
```python
# We regard temperatures below -50 degrees as measurement errors
if temperature > -50:
    print('do something')
```
Which of these comments is best? Can you explain why?
````
```{solution} Solution
Comment A describes **what** happens in this piece of code,
whereas comment B describes **why** this piece of code is there, i.e. its **purpose**.
Comments in the form of B are much more useful, comments of form A are redundant and we should avoid them.
```
