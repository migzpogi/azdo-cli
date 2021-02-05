from azdocli.strategies.strategy_context import Strategy
from azdocli.lib.core import CoreAPI


class TeamsGetStrategy(Strategy):
    def run_strategy(self):
        coreapi = CoreAPI(self.org_name, self.org_pat)
        if self.ctx['team_id'] == '':
            return coreapi.get_teams(self.ctx['project_name'])
        else:
            return coreapi.get_team(self.ctx['project_name'], self.ctx['team_id'])