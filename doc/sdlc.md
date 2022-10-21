# The Software Development Lifecycle (SDLC)

```{questions}
- What are the different SDLC:s
- When to use which?
```

```{objectives}
- We will have an introduction to some the SDLC:s
- More on Wednesday!!
```

```{instructor-note}
- Lecture 15 min
```

- SDLC intro software development lifecycle 15 min


- A little deeper


```{todo}
Pair programming kommer testas
Continuous integration, delivery, deployment
Tests nivåer
Kostnad är en parameter också
Scrum inte relevant för ej jättestora teams
```


- sorting out the concepts
- Peer programming is QC/QA collab sharing
- Pair programming is real-time development teqch to increase algorithm implementation, pass off, introduction
- Agile development, the Agile manifest (Not a full process)
- OOSE-like Rational Unified Proces
- TDD

- development cycle?
  - ex. maintenance
  - code management plan!
  -	for project applications?

## Key steps

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

### Waterfall model
1.	Requirements
2.	Analysis and design
3.	Development
4.	Test
5.	Development and maintenance

- Problem:  error is spreading
- good approach for small and simple systems where the team knows the system and requirements very well. I

## Iterative models
### Spiral model: iterating waterfalls, quadrants

- Planning: reqs, identification: analysis
- Risk analysis: build prototypes to identify risks
- Engineering: software implementation
- Evaluation: stakeholder review, feedback, plan next iteration
- Each lab is new cycle: prototype--> RC --> aunch
- Risk driven

### Rational unified process (RUP) 
- created by IBM
- Framework, pool of knowledge, customizable
- Phases: Each containing 1 or more waterfall iterations
  - Inception (lifecycle objectives milestone
  - Elaboration (lifecycle architecture milestone)
  - Construction (initial operational capability, milestone)
  - Transition (production release milestone)
- Disciplines
  - Business modelling
  - Requirements
  - Analysis and design
  - Implementation
  - Test
  - Deployment
- Shortcomings: customizable but heavy, prescriptive, lacking test-driven development

- **Key takeaways**
  - RUP principles
  - Develop iteratively
  - Manage requirements, change
  - Continuously verify quality
  - Model visually, component-based architecture

## Early Agile methods
-	Dsdm: dynamic system development method
-	Feature-driven development (FDD)
-	Crystal methods

## Modern approaches
- Scrum 
- Lean
- Kanban
- Extreme Programming
  - pair programming
  - TDD
- Spotify
- DevOps
  - continous Integration, development and deployment
  - **DevOps aims to extend fast and frequent software feature development approach to build an efficient delivery pipeline.**
- CMMI (Capability maturity model integration)
- Six Sigma

## Conclusions
  - Each team unique requirements
  - Try out agile practices that make the most sense
  - Don’t be afraid of trial and error
  - Continuous learning


## Discussion about steps?

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
