Specifications for this project are as follows:

For this project, you will design and build a knowledge-based intelligent system that collects
user preferences and reasons about them.

1 Requirements
  1. The system should have an easy-to-use GUI (using the Python Tkinter module1
  ) for
  collecting names of attributes and their values, hard constraints, and preferences. The
  system also should allow reading in these input from files. (See section 3 for formats
  of these files.)
    • Attributes (A) in this project are going to be binary.
    • Hard constraints (H) are represented as propositional formulas in the Conjunctional Normal Form (CNF).
    • The system should support preferences (T) in the preference language of penalty
    logic. Formulas involved in the preference theories are of CNF as well.
  2. The system should support the following reasoning tasks:
    • Existence of feasible objects: decide whether there are feasible objects w.r.t H,
  that is, whether there are models of H that are truth assignments making H true.
    • Exemplification: generate, if possible, two random feasible objects, and show the
  preference between the two (strict preference or equivalence) w.r.t T.
    • Optimization: find an optimal object w.r.t T.
    • Omni-optimization: find all optimal objects w.r.t T.
  3. The system should take advantage of the clasp system, a SAT solver that takes a propositional formula in CNF and computes its models. 
  It can be used to compute feasible objects for H, check if a truth assignment satisfies a formula, etc. The short tutorial is on Canvas.
  4. For testing, the system should solve an instance, developed by you, that contains at
  least 6 hard constraints and at least 6 preference rules over at least 8 attributes. Also
  use this instance when demonstrating your system.
  5. By Mar. 15 midnight, you will need to email me to discuss your progress. In your
  email, you will describe what you have done for this project and what you plan to do,
  and your questions if any. You will send me a screen shot of your GUI or at least a
  design of it, in case you will not have implemented in Python. Once I read your emails,
  I will respond with my comments to help you towards completing this project. Failure
  of this will result in deduction in the project grade. (See rubrics.)

2 Deliverables
  Zip the following to name [your-last-name] Project3.zip and submit to Canvas.
    1. A text file with description of the instance (attributes and their values, hard constraints,
    and preferences) you used for testing.
    2. A directory that contains all your source codes.
    3. A README file that contains instructions to build and run your system.
    4. A PDF report that describes how your system works and shows the testing results using
    the test instance (e.g., screen shots of various steps).

3 File Formats
  3.1 Attributes File
  appetizer: soup, salad
  entree: beef, fish
  drink: beer, wine
  dissert: cake, ice-cream
  ...
  3.2 Hard Constraints File
  NOT soup OR NOT beer
  NOT soup OR NOT wine
  ...
  3.3 Preferences File
  fish AND wine, 10
  wine OR cake, 6
  beer AND beer OR beef AND NOT soup, 7
