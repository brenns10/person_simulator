# Person Simulator - Object Specification [WIP]
**_Document subject to revision_**

## World
The `World` holds all the simulation's data and, on each tick, is reponsible for updating it and calling for it to be displayed.

<!---
####Potential private attributes
`_persons:dict<str,Person>`
`_get_persons(self:World) -> list<persons>`
`_do(self:World, actor:Person, action:Action, target:Person)`  # responsible for tracking ticks
               
####Tick Overview
class World():
    ...

    def on_tick(self):
	   actions_this_tick = self.update()
       self.render(actions_this_tick)

    def update(self):
        persons = self._get_persons()[:]
	    persons.shuffle()

        # run base updates
        for person in persons:
            actions = person.get_base_update()
            for action in actions:
                self._do(person, action, person)

        # Poll for interactions.
        for person in persons:
            others = set(persons) - person
            action, target = person.get_interaction(person)

            if target is None:
                targets = others
            else:
                targets = [target]

            for target in others:
                self._do(person, action, target)

            
    def render(self):
       for display in world.displays:
           display.render(world)
    ...
   -->

## Person <!-- Entity? TBD based on ambition / time -->

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

## To Consider

Should we:

- Merge `Person.get_base_updates` and `Person.get_interaction` back into `Person.on_tick()`?
- Standardize how players choose iteractions (e.g. have a Scheduler?)
- Add a Relationship attribute that would track `Person`-`Person interaction over time (i.e. give the simulation memory?)
  + Even something as simple as a relationship valence (e.g. valence \in [0.0, 1.0], where 1 is most positive, 0.0 is most negative) could work.
  + Is (currently) easy to implement in `world.do()`.
  
