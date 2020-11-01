from azdocli.strategies.strategy_context import StrategyContext
from azdocli.strategies.projects_list_strategy import ProjectsListStrategy
from azdocli.strategies.svc_list_strategy import SvcListStrategy


def execute_strategy(ctx):
    controller = ctx.obj['controller']
    operation = ctx.obj['operation']
    context = StrategyContext()

    if controller == 'projects' and operation == 'getall':
        context.strategy = ProjectsListStrategy(ctx)
        context.execute()
    elif controller == 'svc' and operation == 'getall':
        context.strategy = SvcListStrategy(ctx)
        context.execute()
    else:
        print("No strategies found")