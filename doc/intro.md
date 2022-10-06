# Introduction

## Learning outcomes

“Turning scripters into computer scientists”
Add theory to bolster already present practical skills


## Software development

- Different types of software:
  - Your analysis of data
    - statistics
    - figures
  - tools for process data
  - workflows
  - modelling
  - more? 

## What is the Purpose of Formalism in Computer Science

## Development cycle

agile = characterized by the division of tasks into short phases of work and frequent reassessment and adaptation of plans.

## Flowcharts

## Source control

## Reproducible research
### Sharing


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
