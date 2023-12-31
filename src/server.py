import uvicorn
from dotenv import load_dotenv
import os
dotenv_path = os.path.join(os.path.dirname(__file__), '.', '.env')
load_dotenv(dotenv_path)

PORT=os.getenv('PORT')
PORT=int(PORT) if PORT else 8888
HOST=os.getenv('HOST')
HOST=HOST if HOST else '127.0.0.1'

if __name__ == "__main__":
    # uvicorn.run("app:app", host=HOST, port=PORT, workers=4)
    uvicorn.run("app:app", host=HOST, port=PORT, reload=True)