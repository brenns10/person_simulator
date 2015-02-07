# Person Simulator - Object Specification [WIP]
**_Document subject to revision_**

## World
The `World` holds all the simulation's data and is reponsible for updating it on a tick. The world will support the following methods:


1. `do(self:World, actor:Person, action:Action, target:Person) --> World`  
   Returns the world after `actor` applies the `action` to `target`. Intended for use in the `on_tick` method of `Person`.

2. `get_others(self:World, callee:Person) --> iterable<Person>`  
   Returns all other `Person` objects in the world besides the `callee`. Intended for use in the `on_tick` method of `Person`.

<!---
####Potential private attributes
`_persons:dict<str,Person>`
`_get_persons(self) -> list<persons>`

####Tick Overview
class World():
    ...
    def do(self, actor, action, target):
        ...
        self.actions_this_tick.append((actor, action, target))
        ...

    def on_tick(self):
	   self.update()
       self.render()

    def update(self):
        self.actions_this_tick = []
        persons = self._get_persons()[:]
	    persons.shuffle()

        for person in persons:
            person.on_tick(self)
            
    def render(self):
       for display in world.displays:
           display.render(world, self.actions_this_tick)

   -->

## Person <!-- Entity? TBD based on ambition / time -->

Each `Person` must support the following methods:

1. `on_tick(self:Person, world:World) -> Person`  
   Returns the updated self after the tick. This method should perform both updates (e.g. increasing hunger, drowsiness) and interactions (e.g. slapping another `Person`). Both types of updates should be done through the `world.do()`.

2. `get_id(self:Person) -> str`  
   Returns a unique identifier of this person. For small simulations, this can just be the first name, but should be a UUID for larger simulations.

3. `get_name(self:Person) -> str`  
   Returns the name of this `Person`.

Persons are added by creating `*.py` files in the `persons/` directory that contain a single class supporting this interface.


## Action
All `Action` objects must support the following methods:

1. `__call__(self:Action, actor:Person, target:Person) -> Person`  
   Returns the updated `target` due to the `actor` taking this `Action`. Required to make Action a callable.

2. `get_name(self:Person) -> str`
   Returns the name of this `Action`.


## Display
`Display` objects are responsible for showing the `World` to the world. They must support the following methods:

1. `render(self:Display, world:World, actions:iterable<Action>)`  
   Consumes the current `World` state and the actions that led to it. This method should create a representation of the `World` that the intended audience can easily interpret.

Displays are added by creating `*.py` files in the `display/` directory that contain a single class supporting this interface.

## To Consider

Should we:

- Split `Person.on_tick()` into two methods, one for updates and another for interactions?
- Standardize how players choose iteractions (e.g. have a Scheduler?)
- Add a Relationship attribute that would track `Person`-`Person interaction over time (i.e. give the simulation memory?)
  + Even something as simple as a relationship valence (e.g. valence \in [0.0, 1.0], where 1 is most positive, 0.0 is most negative) could work.
  + Is (currently) easy to implement in `world.do()`.
  
