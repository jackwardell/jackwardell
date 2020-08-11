import threading

from commandlib import Command
from git import Repo
from pdfkit import from_url

if __name__ == "__main__":
    PORT = "5000"
    HOST = "127.0.0.1"

    git = Command("git", "status")
    git.run()

    if (
        "modified:   JACK_WARDELL_CV.pdf"
        in git.output().split("Changes not staged for commit").pop()
    ):
        flask = Command("flask", "run", "-p", PORT, "-h", HOST).with_env(
            FLASK_ENV="development", FLASK_APP="app/__init__.py"
        )
        thread = threading.Thread(target=flask.run, daemon=True)
        thread.start()
        from_url(f"http://{HOST}:{PORT}/?for_pdf=True", "JACK_WARDELL_CV.pdf")
        thread.join()

    else:
        print("NOT NESC")
