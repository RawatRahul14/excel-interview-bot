# === Python Modules ===
from pymongo import AsyncMongoClient

## === Function to verify whether the ID is valid or not ===
async def verify_id(
        user_id: str,
        mongo_uri: str,
        db_name: str,
        collection_name: str
) -> bool:
    """
    Verifies whether the id is valid or not
    """
    client = AsyncMongoClient(mongo_uri)

    try:
        # === Connecting to the collection ===
        collection = client[db_name][collection_name]

        # === Checking if user exists ===
        doc = await collection.find_one({
            "user_id": user_id
        })

        ## === If the user exists ===
        if doc:
            return "True"

        ## === If user does not exists ===
        else:
            return "False"

    except Exception as e:
        raise(e)

    finally:
        await client.aclose()