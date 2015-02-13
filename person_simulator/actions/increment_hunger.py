from action import Action


class IncrementHunger(Action):
    def __init__(self, increment_amount=1, max_hunger=100):
        super().__init__('IncrementHunger(+%d, max=%d)' % (increment_amount, max_hunger))
        self._increment_amount = increment_amount
        self._max_hunger = max_hunger

    def __call__(self, actor, target):
        target.hunger = min(target.hunger + self._increment_amount, self._max_hunger)
        return target
