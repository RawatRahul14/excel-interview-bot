# === Python Module ===
import time

# === Streaming generator ===
def stream_text(
        text: str,
        delay: float = 0.05
):
    """
    Creates a streaming-like effect in Streamlit UI.
    Preserves line breaks while typing word by word.
    """
    for part in text.split(" "):  # split by spaces
        if "\n" in part:
            # handle words that contain line breaks
            lines = part.split("\n")
            for l in lines[:-1]:
                yield l + "\n"
                time.sleep(delay)
            yield lines[-1] + " "
        else:
            yield part + " "
        time.sleep(delay)
