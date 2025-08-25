"""This module provides example tools for web scraping and search functionality.

It includes a basic Tavily search function (as an example)

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""

from typing import Any, Callable, List, Optional, cast, Tuple

from langchain_tavily import TavilySearch
from langgraph.runtime import get_runtime

from react_agent.context import Context


async def search(query: str) -> Optional[dict[str, Any]]:
    """Search for general web results.

    This function performs a search using the Tavily search engine, which is designed
    to provide comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events.
    """
    runtime = get_runtime(Context)
    wrapped = TavilySearch(max_results=runtime.context.max_search_results)
    return cast(dict[str, Any], await wrapped.ainvoke({"query": query}))

def draw_card(count: int):
    """Draw N cards from a tarot deck.

    This function simulates drawing a card from a tarot deck, returning a random integer
    between 1 and 78, inclusive.
    """
    import random
    deck = list(range(1, 79))
    rng = random.Random()
    rng.shuffle(deck)
    cards = deck[:count]
    result = []
    for c in cards:
        result.append({"card": c, "position": random.choice(["upright", "reversed"])})
    return result

TOOLS: List[Callable[..., Any]] = [search, draw_card]

