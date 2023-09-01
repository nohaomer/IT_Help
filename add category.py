import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("ithelp-2f67c-firebase-adminsdk-ckc7c-57cd35c507.json")
firebase_admin.initialize_app(cred)

# Get a Firestore client instance
db = firestore.client()

# Add a new collection and document to Firestore
collection_name = "my_collection"
document_data = {
    "field1": "value1",
    "field2": "value2"
}

# Add the document to the collection
doc_ref = db.collection(collection_name).document()
doc_ref.set(document_data)

# Retrieve the auto-generated document ID
document_id = doc_ref.id
print("New document ID:", document_id)
