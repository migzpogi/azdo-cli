from azdocli.strategies.strategy_context import StrategyContext
from azdocli.strategies.projects_list_strategy import ProjectsListStrategy
from azdocli.strategies.projects_get_strategy import ProjectsGetStrategy
from azdocli.strategies.svc_list_strategy import SvcListStrategy
from azdocli.strategies.teams_list_strategy import TeamsListStrategy
from azdocli.strategies.teams_get_strategy import TeamsGetStrategy
from azdocli.strategies.pipelineruns_get_strategy import PipelinerunsGetStrategy


def execute_strategy(ctx):
    controller = ctx.obj['controller']
    operation = ctx.obj['operation']
    context = StrategyContext()

    if controller == 'projects' and operation == 'getall':
        context.strategy = ProjectsListStrategy(ctx)
        return context.execute()
    elif controller == 'projects' and operation == 'get':
        context.strategy = ProjectsGetStrategy(ctx)
        return context.execute()
    elif controller == 'svc' and operation == 'getall':
        context.strategy = SvcListStrategy(ctx)
        return context.execute()
    elif controller == 'teams' and operation == 'getall':
        context.strategy = TeamsListStrategy(ctx)
        return context.execute()
    elif controller == 'teams' and operation == 'get':
        context.strategy = TeamsGetStrategy(ctx)
        return context.execute()
    elif controller == 'pipelineruns' and operation == 'get':
        context.strategy = PipelinerunsGetStrategy(ctx)
        return context.execute()
    else:
        print("No strategies found")
        return None