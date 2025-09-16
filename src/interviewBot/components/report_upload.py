# === Python Modules ===
from pymongo import AsyncMongoClient
from datetime import datetime, timezone

## === Function to upload candidate's report ===
async def upload_report(
        user_id: str,
        answers_log: list,
        report: str,
        final_decision: str,
        mongo_uri: str,
        db_name: str,
        collection_name: str
):
    """
    Uploads the candidate's report to MongoDB
    """
    client = AsyncMongoClient(mongo_uri)

    try:
        # === Connecting to the collection ===
        collection = client[db_name][collection_name]

        # === Document structure ===
        doc = {
            "user_id": user_id,
            "timestamp": datetime.now(timezone.utc),
            "answers_log": answers_log,
            "report": report,
            "final_decision": final_decision
        }

        # === Insert into MongoDB ===
        await collection.insert_one(doc)

        return "Uploaded"

    except Exception as e:
        raise(e)

    finally:
        await client.aclose()