from azdocli.strategies.strategy_context import Strategy
from azdocli.lib.pipelines import PipelinesAPI


class PipelinerunsGetStrategy(Strategy):
    def run_strategy(self):
        pipelinesapi = PipelinesAPI(self.org_name, self.org_pat)
        return pipelinesapi.get_pipelineruns(self.ctx['project_name'], self.ctx['pipeline_id'])