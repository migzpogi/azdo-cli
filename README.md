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
```

## Roadmap
```
get_team(project_id, team_id)
  // gets the specific team

get_service_endpoints()
  // list the service endpoints

get_service_endpoint_details(projet_id, endpoint_id)
  // gets the specific endpoint
```