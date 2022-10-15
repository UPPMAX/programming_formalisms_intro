
Programming formalisms: Introduction day
========================================

- “Turning scripters into computer scientists”
- Add theory to bolster already present practical skills

.. graphviz::

   digraph {
      "From" -> "To";
   }

.. uml:: external.uml


.. uml::

   @startuml
   user -> (use PlantUML)

   note left of user
      Hello!
   end note
   @enduml

.. admonition:: This course
   
   - This course aims to give life scientists, bioinformaticians, and other scientists with some experience in programming and scripting an understanding of the underlying principles of software development, design, and programming. 
   - The course aims to strengthen the understanding of:
      - more advanced programming concepts
      - ability to produce more reusable scripts through modular programming and to 
      - enable a better understanding of how to evaluate a script or programs performance.

.. admonition:: Content

   - We will cover an introduction to 
   
      - Algorithms and Data structures
      - Programming Paradigms
            - especially structured
            - functional programming
            - modular development
            - code reusability
            - testing
            - optimisation.
      - object oriented programming 
    
   - The modules will cover theory with bridging practical examples and applications to enhance the theoretical understanding of the principles.

.. prereq::

   -  A reasonably recent version of **Git is installed**
   -  **Git should be configured prior to the course**
   -  A `GitHub <https://github.com>`__ user account (but alternatives
      exist, see below).
   -  Being comfortable with the command line. 
   -  Students should be familiar with using a **text editor** on their
      system. Emacs and Vim are excellent choices if you know how to use
      them but Nano or Notepad on Windows are sufficient.

Some practicals
----------------
        
.. admonition:: Zoom

    - The course is run over Zoom. You should have gotten an email with the links
        
    - There will be a zoom for the lectures, a zoom for the HPC2N sessions, and a zoom for the UPPMAX sessions. 
        - The exercises will be done in the separate sessions.
   
    - When you join the Zoom meeting, use your REAL NAME.
    
    - The lectures and demos will be recorded, but NOT the exercises. If you ask questions during the lectures, you may thus be recorded. If you do not wish to be recorded, then please keep your microphone muted and your camera off during lectures and write your questions in the Q/A document (see below about HackMD collaboration document).
    
    - Please MUTE your microphone when you are not speaking and use the “Raise hand” functionality under the “Participants” window during the lecture. Please do not clutter the Zoom chat. Behave politely!

    - There may be breakout rooms used in the Zoom for the hands-ons. You will be randomly assigned to one of them.  
    
    
.. admonition:: Collabration document HackMD

    - Use the HackMD page for the workshop with your questions.
     
    - Depending on how many helpers there are we'll see how fast there are answers. 
        - Some answers may come after the workshop.
 
    - Type in the left frame 
        - "-" means new bullet and <tab> indents the level.
        - don't focus too much on the formatting if you are new to "Markdown" language!
    
    - **Have a try with the Icebreaker question**

.. admonition:: Exercises

   - Exercises will be mixed with group work and individual work.
   - We will use Git and Github as tools for version control and collaboration.
   
   
Schedule
--------------------

- Day1 Intro (Björn Claremar)
- Day2 Algorithms and data structures (Marcus Lundberg)
- Day3-4 Paradigms: design patterns, modular code (Lars Eklund)
- Day4 TDD, testing (Lars Eklund)
- Day5 Optimization (Marcus Lundberg)


The teachers 
------------

- Lars Eklund
- Marcus Lundberg
- Björn Claremar

.. admonition:: Learning outcomes of course

   - You will be able to:

      - understand the pros of having...


   
.. toctree::
   :maxdepth: 2
   :caption: Lesson:

   intro.md
   sdlc.md 
   flowcharts.md
   sourcecontrol.md
   reproducible.md
   documentation.md
   summary.md
   
.. toctree::
   :maxdepth: 2
   :caption: Reference:

   concepts.md
   exercises.md
   * :ref:`genindex`

Indices and tables
==================

* :ref:`genindex`

