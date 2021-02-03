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
projects get --name project_name
projects getall

teams getall
```