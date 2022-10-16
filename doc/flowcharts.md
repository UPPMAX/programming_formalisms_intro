# Unified Modeling Language

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
-	Structure 
  -	Class
  -	Component
  -	Object
  -	Composite structure
  -	Package
  -	deployment
-	Behavior
  -	Use case 
  - Activity
  - State machine
  - Interaction within/outside system
    - Sequence
    -	Communication
    -	Timing
    -	Interaction overview

```{graphviz}
digraph{
"UML diagrams"
Structure, Behaviour
"UML diagrams" -> Structure
"UML diagrams" -> Behaviour
Structure -> Class, Component,	Object,	Composite-structure,	Package,	deployment
Behaviour -> Use-case ,	Activity,	State-machine,	Interaction
Interaction -> Sequence,	Communication, Timing,	Interaction-overview
}
```

```{graphviz}
digraph{
"UML diagrams"
Structure, Behaviour, Class, Component,	Object,	Composite-structure,	Package,	deployment,	Behavior,	Use-case ,	Activity,	State-machine,	Interaction, Sequence,	Communication, Timing,	Interaction-overview

"UML diagrams" -> Structure
"UML diagrams" -> Behaviour
Structure -> Class, Component,	Object,	Composite-structure,	Package,	deployment
Behaviour -> Use-case ,	Activity,	State-machine,	Interaction
Interaction -> Sequence,	Communication, Timing,	Interaction-overview
}
```

UML diagrams -> Structure
UML diagrams -> Behaviour
Structure -> Class, Component,	Object,	Composite-structure,	Package,	deployment
Behaviour -> Use-case ,	Activity,	State-machine,	Interaction
Interaction -> Sequence,	Communication, Timing,	Interaction-overview


### Class

```{uml}
@startuml
abstract        abstract
abstract class  "abstract class"
annotation      annotation
circle          circle
()              circle_short_form
class           class
diamond         diamond
<>              diamond_short_form
entity          entity
enum            enum
interface       interface
protocol        protocol
struct          struct
@enduml
```

###  Sequence

```{uml}
   
@startuml
user -> (use PlantUML)

note left of user
   Hello!   
end note
@enduml
```


### Activity
```{uml}
@startuml
if( HAS AN
OWNER AND IS OPEN) then(yes)
 if (CAN I RESOLVE) then
 if (waiting user input) then
 elseif (condition D) then (yes)
  :Text 4;
else ()
  :Text else;
endif
@stopuml
```



### Other
#### Use case 

```{uml}
@startuml
left to right direction
actor Guest as g
package Professional {
  actor Chef as c
  actor "Food Critic" as fc
}
package Restaurant {
  usecase "Eat Food" as UC1
  usecase "Pay for Food" as UC2
  usecase "Drink" as UC3
  usecase "Review" as UC4
}
fc --> UC4
g --> UC1
g --> UC2
g --> UC3
@enduml
```


#### Object

```{uml}
@startuml
object Object01
object Object02
object Object03
object Object04
object Object05
object Object06
object Object07
object Object08

Object01 <|-- Object02
Object03 *-- Object04
Object05 o-- "4" Object06
Object07 .. Object08 : some labels
@enduml

```
#### GRAPHVIZ

```{graphviz} external.dot
```

   
```{graphviz} puml/external.dot
```

```{uml} puml/external.uml
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
