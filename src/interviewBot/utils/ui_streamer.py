# === Python Module ===
import time

# === Streaming generator ===
def stream_text(
        text: str,
        delay: float = 0.1
):
    """
    Creates a streaming-like effect in Streamlit UI.
    Preserves line breaks while typing word by word.
    """
    ## === Iterating over the text split by spaces ===
    for part in text.split(" "):

        ## === If there is a line break in the word ===
        if "\n" in part:

            # Split the part into lines
            lines = part.split("\n")

            # Stream each line (except the last one) with newline preserved
            for l in lines[:-1]:
                yield l + "\n"
                time.sleep(delay)

            # Stream the last segment of the line with a space
            yield lines[-1] + " "

        ## === If no line break, stream normally ===
        else:
            yield part + " "

        ## === Apply delay after each streamed part ===
        time.sleep(delay)
