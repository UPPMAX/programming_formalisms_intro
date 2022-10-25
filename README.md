# programming_formalism_intro

Main course page is found here: https://uppsala.instructure.com/courses/69215

Topics

  - Day1 Intro https://uppmax.github.io/programming_formalism_intro/index.html
  - Day2 Algorithms+data structures
  - Day3-4 Paradigms: design patterns, modular code
  - Day4 Test-driven Development, testing
  - Day5 Optimization

```mermaid
classDiagram

Animal <|-- Duck
Animal <|-- Fish
Animal <|-- Zebra
Animal : +int age
Animal : +String gender
Animal: +isMammal()
Animal: +mate()
class Duck{
  +String beakColor
  +swim()
  +quack()
}
class Fish{
  -int sizeInFeet
  -canEat()
}
class Zebra{
  +bool is_wild
  +run()
}
 
```    

```mermaid
sequenceDiagram 
a->>b:a

```


