# Unified Modeling language

```{questions}
  - How to use UML?
  - Can I learn it?
```

```{Objectives}
   - We will give an overview of UML diagrams
      - learn when to use
      - learn basic notations
      - Test with graphical interface
      - Test with the script based plantUML
```


- UML is not a programming language. It's a graphical notation for drawing diagrams to visualize object oriented systems.
-  UML includes over a dozen different types of structural and behavioral diagrams. 

- caveats 
  - UML has been marketed for many contexts.[24][31]
  - It has been treated, at times, as a design silver bullet, which leads to problems. 
  - UML misuse includes overuse (designing every part of the system with it, which is unnecessary) and assuming that novices can design with it.[32]
  - It is considered a large language, with many constructs. Some people (including Jacobson) feel that UML's size hinders learning (and therefore, using) it

class diagrams and use case diagrams 

 "These diagrams should be a quick, useful communication tool. A support system for your brain, not the other way around!"
 
paper or whiteboard --> digital toools 

https://en.wikipedia.org/wiki/List_of_Unified_Modeling_Language_tools

## Object orientation
{term}`class`

## Design

## Diagrams

```{markmap}
# Types of UML models
## Structure
## Behaviour
### Interaction
```
- Class
-	Use case 
- Activity
- Sequence
- Communication
- Object

```{uml}
   
   @startuml
   user -> (use PlantUML)

   note left of user
      Hello!   
   end note
   @enduml
```

```{uml}
User -> Authenticator : request
Authenticator -> User : respond <token>
```

## Tools
- Computer-Aided Software Engineering tools
  -	Modeling
  - Code generation
  -	Reverse engineering
  - Analyze code complexity
  -	Other metrics
- PlantUML
  - Open-source
  -	Can be integrated with IDE:s, Java documentation, Word
  -	Scripts rather than drawing tools
  -	http://www.plantuml.com/plantuml


## Graphical tools

## PlantUML


## Exercise


## Summary

````{Keypoints}
  - UML is good several coditions
    - Structural overviews
    - Planning
    - Problem solving
    - Designing phase of programming
  - The most important diagrams for software development are: 
    - class
    - sequence 
    - aktivitetsdiagram
  - There are plenty of tools out there
    - some can produce code directly
    - some are script-vased and well integrated in Markdown tools like Sphinx and HackMD
      - perfect for sharing
```` 
