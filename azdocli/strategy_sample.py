from abc import ABC, abstractmethod


class Context():

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

    @abstractmethod
    def run_strategy(self):
        pass


class StrategyA(Strategy):
    def run_strategy(self):
        return 1


class StrategyB(Strategy):
    def run_strategy(self):
        return 2


if __name__ == "__main__":
    context = Context()
    context.strategy = StrategyA()
    print(context.execute())
    context.strategy = StrategyB()
    print(context.execute())