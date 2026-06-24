from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from agent import node
from agent.state import AgentState
from integrations import GithubClient


class Graph:
    @classmethod
    async def init(cls):
        builder = StateGraph(AgentState)

        file_explorer_node = ToolNode(await GithubClient.get_tools())

        builder.add_node("fetch", node.fetch_pr_details)
        builder.add_node("analysis", node.analyzer)
        builder.add_node("output", node.output)
        builder.add_node("tools", file_explorer_node)

        builder.add_edge(START, "fetch")
        builder.add_edge("fetch", "analysis")
        builder.add_conditional_edges(
            "analysis",
            lambda state: "output" if state["is_significant"] else END
        )
        builder.add_conditional_edges("output", tools_condition)
        builder.add_edge("tools", "output")

        checkpointer = InMemorySaver()
        graph = builder.compile(
            checkpointer=checkpointer,
            interrupt_after=["analysis"]
        )

        return graph
