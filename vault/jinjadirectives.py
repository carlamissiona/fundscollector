from datetime import datetime
from jinja2 import Environment
...
env = Environment()
env.globals.update(
  strftime=lambda fmt: datetime.now().strftime(fmt)
)
