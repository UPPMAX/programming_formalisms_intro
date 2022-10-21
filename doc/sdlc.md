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

- Good approach for **small and simple systems** where the team knows the system and **requirements very well**.
- :warning:  Error is spreading 
  - small mistakes in the beginning will have large impact on the end result. 
    - e.g. bugs, architecture limiting extensions
  - large costs economically and timely

## Include iteration
### Spiral model

- Planning: reqs, identification: analysis
- Risk analysis: build prototypes to identify risks
- Engineering: software implementation
- Evaluation: stakeholder review, feedback, plan next iteration
- Each lab is new cycle: prototype--> RC --> launch
- Risk driven

IMAGE

- **Disadvantages**
  - Complexer than other SDLC models.
  - Expensive: Spiral Model is **not suitable for small projects**
  - Too much dependability on Risk Analysis
  - Difficulty in time management: Number of phases is unknown at the start of the project

### Rational unified process (RUP) 
- created by IBM
- Object-oriented software Engineering-like
- Framework, pool of knowledge, customizable
- **Phases**: Each containing **1 or more waterfall iterations**
  - Inception (lifecycle objectives milestone)
  - Elaboration (lifecycle architecture milestone)
  - Construction (initial operational capability, milestone)
  - Transition (production release milestone)
- Disciplines
  - Business modelling
  - Requirements
  - Analysis and design
  - Implementation
  - Test
  - Deployment
- Shortcomings: customizable but heavy, prescriptive, lacking test-driven developmen

- **Key takeaways**
  - RUP principles
    - **Develop iteratively**
    - Manage **requirements**, change
    - **Continuously verify quality**
    - **Model visually, component-based architecture**



```{todo}
Pair programming kommer testas
Continuous integration, delivery, deployment
Tests nivåer
Kostnad är en parameter också
Scrum inte relevant för ej jättestora teams
```

## Early Agile methods
### [The Agile manifest](https://agilemanifesto.org/)
**Values**

```{admonition}
**Individuals and interactions** over processes and tools
**Working software** over comprehensive documentation
**Customer collaboration** over contract negotiation
**Responding to change** over following a plan
```

Or:
"Agile = characterized by the division of tasks into short phases of work and frequent re-assessment and adaptation of plans."

### Some methods take aways
#### Dynamic system development method (DSDM)
- Timeboxing
-	Moscow prioritization
- Iterative and incremental approach

#### Feature-driven development (FDD)
- Feature teams
- Parallel development
- Tracking completion status (reporting, milestones, percentage completion)

#### Crystal methods
- People-centric
- Frequent delivery
- No one size fits all
- Modern principles: automated tests, frequent integration

### Modern approaches, key take-aways
#### Scrum 
- Business value-driven comprehensive framework
- Scrum roles
  - Owner (individual final authority): backlog (undone work)
  - development team: self-organizing and cross-functional developers
  - testers
  - documenters
  - DB admins 
  - scrum master: agile coach, servant leader, removes barriers, coaches and convinces; does not manage
- scrum workflow
  - sprint planning->sprint->review->retrospective
- Potentially shippable product increment each sprint

#### Lean
- **Minimize waste**, visualize production, look for bottlenecks, inefficiencies
- Decide as late as possible
  - Early in the process, what about change in technology, customers etc…?
  - **Last responsible moment**: wait ‘til we have enough facts
    - not make decisions based on preset timelines.
- Deliver as fast as possible: small iterations are easier to manage

#### Kanban
- Visualize your work, limit work in progress

#### Extreme Programming
-	[https://www.agilealliance.org/glossary/xp](https://www.agilealliance.org/glossary/xp)
-	Just In Time design

```{admonition} Branching and merging is not listed as a core XP practice
-	is generally not a favorable practice in Agile approaches. 
-	Branching has the potential for creating technical debt if changes are not merged frequently. 
-	The risks an be somewhat mitigated by merging frequently. 
-	In any case, branching and merging .
```

##### Pair programming
- Collaborate, continuous code inspection
- real-time development technique to increase algorithm implementation

##### Test-driven development
- Write test
- Write function to fail test
- Write code to pass test

#### Spotify
- Culture
  - Innovation: hackathons
  - Learning from each other
  - Failure-friendly culture
  - (internal) code repositories, visible and open for other teams
  - Minimize handoffs (help from other teams)
  - Bureaucracy minimized


#### DevOps
- **Dev**elopers and testers
- **Ops**: people working with release, servers, middleware, network, storage configs, monitoring techniques
- DevOps aims to extend fast and frequent software feature development approach to build an efficient delivery pipeline.
- **Continous**...
  - **Integration**: Central repo
  - **Development**: Ensuring stable product after every release
  - **Deployment**: automating updates to production

**And more...***











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
  - Each team unique requirements
  - Try out agile practices that make the most sense
  - Don’t be afraid of trial and error
  - Continuous learning

```{info}
More on Wednesday
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
