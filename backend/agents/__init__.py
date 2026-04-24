# This file makes the 'agents' folder a Python package.
# By importing the agent functions here, other files can do:
#   from agents import researcher_agent
# instead of:
#   from agents.researcher import researcher_agent

from agents.researcher import researcher_agent
from agents.outliner import outliner_agent
from agents.writer import writer_agent
from agents.reviewer import reviewer_agent
