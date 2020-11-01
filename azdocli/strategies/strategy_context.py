from abc import ABC, abstractmethod


class StrategyContext():

    def __init__(self, strategy=None):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def execute(self):
        result = self._strategy.run_strategy()
        return result


class Strategy(ABC):

    def __init__(self, ctx):
        self.ctx = ctx.obj
        self.org_name = self.ctx['org_name']
        self.org_pat = self.ctx['org_pat']

    @abstractmethod
    def run_strategy(self):
        pass