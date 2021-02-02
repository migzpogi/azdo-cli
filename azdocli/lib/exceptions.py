from azure.devops.exceptions import AzureDevOpsServiceError, AzureDevOpsAuthenticationError
import functools


def exception_handler(func):
    @functools.wraps(func)
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AzureDevOpsServiceError as e:
            print(e, "Invalid PAT provided.")
            exit(1)
        except AzureDevOpsAuthenticationError as e:
            print(e, "Wrong PAT provided.")
            exit(2)

    return inner_function
