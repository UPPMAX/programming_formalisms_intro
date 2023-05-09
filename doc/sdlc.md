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
