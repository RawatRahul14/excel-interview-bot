# === Python Modules ===
from typing import List
from pathlib import Path
import random

# === Utils ===
from interviewBot.utils.common import load_yaml

# === Gets Topics from YAML ===
async def get_topic(
        used_topics: List[str]
):
    """
    Returns the name, description of a topic and updated used_topics list
    """
    # === Calling the yaml file ===
    topics_data = load_yaml(
        path = Path("src/interviewBot/data/questions.yaml")
    )

    # === Checking for the available topics ===
    available_topics = [t for t in topics_data if t["topic"] not in used_topics]

    # === Choosing one randomly ===
    chosen = random.choice(available_topics)
    topic, description = chosen["topic"], chosen["description"]

    # === Updating the used_topics list ===
    updated_used_topics = used_topics + [chosen["topic"]]

    return topic, description, updated_used_topics