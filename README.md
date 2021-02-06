# azdo-cli
A command-line interface client for Azure DevOps

## Requirements
* Python 3.x

## Installation
`pip install azdo-cli`

## Usage
Initialize your settings.ini file by typing in your terminal:
```
> azdocli init
```
When running the CLI application, make sure that you have this file in the working directory.  

---
To list the available commands:
```
> azdocli --help
```

---
Sample:
```
> azdocli projects getall

{
  'count': 2,
  'values': [
    {
      'id': '1234-5678-9101',
      'name': 'sample_project_01'
    },
    {
      'id': '2468-1012-1416',
      'name': 'sample_project_02'
    }
  ]
}
```

## Available Commands
```
projects getall 
  // lists all projects in the organization
projects get --projectname project_name 
  // gets the specific project

teams getall 
  // lists all teams in the organization
teams get --projectname project_name 
  // lists all teams in the project
teams get --projectname project_name --teamid team_id
  // gets the specific team
```

## Roadmap
```
list_runs(project_id, pipeline_id) -> pipelineruns get
  // lists the runs of the project

get_service_endpoints(project_id) -> svc get
  // list the service endpoints of the project

get_service_endpoint_details(project_id, endpoint_id) -> svc getone
  // gets the specific endpoint

list_pipelines(project_id) -> pipelines get
  // list the pipelines of the project

get_pipeline(project_id, pipeline_id) -> pipelines getone
  // gets the specific pipeline



get_run(project_id, pipeline_id, run_id) -> pipelineruns getone
  // gets the specific run

get_accounts(owner_id=None, member_id=None)

get_build(project_id, build_id) -> builds getone

get_builds(project_id) -> builds get




```