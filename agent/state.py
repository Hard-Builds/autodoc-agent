from typing import List

from langgraph.graph import MessagesState


MAX_ITERATIONS = 10


class AgentState(MessagesState):
    repo_owner: str
    repo_name: str
    pr_number: int

    raw_diff: str
    analysis: str

    is_significant: bool
    reasoning: str
    affected_components: List[str]

    iteration: int
