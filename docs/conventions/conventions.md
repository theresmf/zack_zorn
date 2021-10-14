# Conventions

## File structure
- project
    - .git
    - .venv
    - <app>
        - management/commands/
        - migrations/
        - miniapps/
            - fakeapp/
        - models/
            - model_a.py
            - model_b.py
        - views/
            - view_a.py
            - view_b.py
        - tests/
        - admin.py
        - apps.py
        - urls.py
        - views.py
    - root/
        - settings/
            - base.py
            - prod.py
            - dev.py
            - heroku.py
        - urls.py
    - .env
    - .gitignore
    - manage.py
    - Pipfile
    - Procfile
    - README.md
    - runtime.txt

## Models
Each model gets a file inside the module 'app.models'
> remember to import everything in __init__.py



## Urls
Scope paths by defining `app_name` inside `urls.py`

## Templates
Extend a `base.html`


### Component
Create components when possible.


### Structure
Templates must be scoped to folders within the `templates` folder.

- templates/
    - some_app/
        - index.html
    - other_app/
        - index.html


## Documentation
Write:
- why
- how to install and configure
- usage

## Imports
- Start with `# imports`
- End with `# End: imports -----------------------------------------`
- Sort by:
    - increasing length by codeword `import`
- Order:
    - python modules
    - installed modules
    - _space_
    - django modules
    - _space_
    - project modules
    
Example:
```python
# imports
import os
import numpy as np

from django.shortcuts import reverse

from info_screens import modules as infoscreen_models
# End: imports -----------------------------------------------------------------
```

## Naming
Python is a typical snake_case language.
Classes are CamelCase.
Variables and methods prefixed with underscore indicate `private` and should only be used within the scope they are defined.


## Constants
Separate constants to a common file
Use classes (possibly as Enum) when suitable to scope variables.

## Tests
Create tests inside a `tests` module.
