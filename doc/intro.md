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
  -	Each lab is new cycle: prototypeRCLaunch
  -	Risk driven


### Parts in course

Analysis and design 
  - Unified Modelling language
Development
  - Algorithms
  - Optimization
    - Parallelism
Test
  - Tests and test-drive development


## Unified Modelling language

## Source control

## Reproducible research
Discussion
•	One-time usage to distributed package

### Sharing

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
