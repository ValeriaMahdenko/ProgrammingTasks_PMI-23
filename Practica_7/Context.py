from Strategy import *

class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def __str__(self):
        return ''+ str(self._strategy)

    def execute(self, list: Double_List, position) -> None:
        return self._strategy.execute(list, position)
