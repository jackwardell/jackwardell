import threading

import pdfkit
from commandlib import Command

if __name__ == "__main__":
    PORT = "5003"
    HOST = "127.0.0.1"
    flask = Command("flask", "run", "-p", PORT, "-h", HOST).with_env(
        FLASK_ENV="development", FLASK_APP="app/__init__.py"
    )
    thread = threading.Thread(target=flask.run, daemon=True)
    thread.start()
    pdfkit.from_url(
        f"http://{HOST}:{PORT}/?for_pdf=True",
        "JACK_WARDELL_CV.pdf",
        options={"zoom": 0.95},
    )
