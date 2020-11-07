from azdocli.strategies.strategy_context import Strategy
from azdocli.lib.core import CoreAPI


class ProjectsGetStrategy(Strategy):
    def run_strategy(self):
        coreapi = CoreAPI(self.org_name, self.org_pat)
        return coreapi.get_project(self.ctx['project_name'])