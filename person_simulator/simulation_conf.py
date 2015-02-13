from person import Person
from actions.increment_hunger import IncrementHunger

CONF = {
    'tick_sleep_time': 5,
    'persons': [
        Person('John Doe', base_updates=[IncrementHunger()], interactions=[], hunger=0)
    ],
}
