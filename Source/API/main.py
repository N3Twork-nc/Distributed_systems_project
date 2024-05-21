from App import app
import uvicorn
import signal


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)