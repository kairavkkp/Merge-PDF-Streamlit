from dotenv import load_dotenv
load_dotenv('../.env')

if not firebase_admin._apps:
    # Use a service account
    cred = credentials.Certificate('../firebase.json')
    firebase_admin.initialize_app(cred)

db = firestore.client()
