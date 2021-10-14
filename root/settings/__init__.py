import os
from root.constants import Environment

ENV = os.environ.get('ENV')

# raise exception if ENV is invalid (and show possible options)
if ENV not in Environment.VALID:
    env_options = ''.join([ f'\n\t{env}' for env in Environment.VALID ])
    raise Exception(
f"""
Environment variable 'ENV' is required to import '{__name__}'.
Possible values: {env_options}
"""
)


if ENV == Environment.DEV:
    from .dev import *
elif ENV == Environment.HEROKU:
    from .heroku import *
elif ENV == Environment.PROD:
    from .prod import *
