from actions.increment_hunger import IncrementHunger
from person import Person


class JohnDoe(Person):
    def __init__(self):
        super().__init__('John Doe', base_updates=[IncrementHunger()], interactions=[], hunger=0)

    def __str__(self):
        return '%s (hunger=%s)' % (self.get_name(), self.hunger)
