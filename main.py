import asyncio
import uuid

from agent.graph import Graph


async def main(thread_id: str = str(uuid.uuid4())):
    graph = await Graph.init()
    config = {"configurable": {"thread_id": thread_id}}
    final_state = await graph.ainvoke(
        input={
            "repo_owner": "Hard-Builds",
            "repo_name": "self-rag",
            "pr_number": 2
        },
        config=config
    )

    print("=== Analysis ===")
    print("Significant: ", final_state["is_significant"])
    print("Reasoning: ", final_state["reasoning"])
    print("Affected Components: ", final_state["affected_components"])

    # Ask for human approval
    approval = input("Proceed with updating architecture? (y/n): ")
    if approval.lower().strip() != "y":
        print("Aborted!")
        return

    final_state = await graph.ainvoke(
        input=None,
        config=config
    )

    print("Done.")
    return final_state


if __name__ == "__main__":
    asyncio.run(main())
