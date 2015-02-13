# Person Simulator - Object Specification [WIP]
**_Document subject to revision_**

## World
The `World` holds all the simulation's data and, on each tick, is reponsible for updating it and calling for it to be displayed.


## Person

Each `Person` must support the following methods:

1. `get_base_update(self:Person) -> iterable<Action>`  
   Returns a list of `Action` callables that perform standard tick updates to the self (e.g. increasing Hunger, drowsiness.) Called exactly once per tick.

2. `get_interaction(self:Person, others:iterable<Person>) -> (Action, Person)`  
   Returns an `Action` to be performed on another `Person` (e.g. slapping another player.) If the the second member of the returned tuple is None, the action is performed on all the other players. May be called several times per tick.
   
3. `get_id(self:Person) -> str`  
   Returns a unique identifier of this person. For small simulations, this can just be the first name, but should be a UUID for larger simulations.

4. `get_name(self:Person) -> str`  
   Returns the name of this `Person`.

Persons are added by creating `*.py` files in the `persons/` directory that contain a single class supporting this interface.


## Action
All `Action` objects must support the following methods:

1. `__call__(self:Action, actor:Person, target:Person) -> Person`  
   Returns the updated `target` due to the `actor` taking this `Action`. Required to make Action a callable.

2. `get_name(self:Action) -> str`
   Returns the name of this `Action`.

Actions are added by creating `*.py` files in the `actions/` directory that contain a single class supporting this interface.


## Display
`Display` objects are responsible for showing the `World` to the world. Each `Display` must support the following methods:

1. `render(self:Display, world:World, actions:iterable<Action>)`  
   Consumes the current `World` state and the actions that led to it. This method should create a representation of the `World` that the intended audience can easily interpret.

Displays are added by creating `*.py` files in the `display/` directory that contain a single class supporting this interface.

## To Do
- Define the relationship between 'simulation.py' and 'world.py' better. They're a little runny at the moment.
- Display.render() should get the whole World
  + Perhaps even the World before and after?
  + Would require standard ways to get the people for easy printouts
- Person classes should support a \_\_str\_\_ for world printouts
- For action printouts, Action should control the formatting
  + that method would need access to actor, target
- How should Person attributes be stored so they are clearly different from other attributes?
  + (e.g. hunger. Currently, stored as Person.hunger)
  + stored with an underscore, get named methods generated on \_\_init\_\_?
  + go into a dictionary? (but then what's the point of an object?)
  + have a defined and unlikely prefix? (e.g. \_pattr\_hunger?)
- Add interactions!
  + would require another player (at least another John Doe)
- Add Relationships
  + Even something as simple as relationship valence could work (e.g. valence \in [0, 100], where 100 is most positive and 0 is most negative)

## To Consider
- Standardize how players choose iteractions (e.g. have a Scheduler?)
  
