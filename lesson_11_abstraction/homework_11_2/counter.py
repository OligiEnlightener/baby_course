class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start:int):
        self.current = start

    def set_max(self, max_max:int):
        self.max_value = max_max

    def set_min(self, min_min: int):
        self.min_value = min_min

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Max reached")

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Min reached")

    def get_current(self):
        return self.current
