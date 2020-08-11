# import threading
#
# from wack import command
#
#
# @command()
# def make_pdf():
#     from pdfkit import from_url
#     from commandlib import Command
#
#     PORT = "5001"
#
#     flask = Command("flask", "run", "-p", PORT).with_env(
#         FLASK_ENV="development", FLASK_APP="jackwardell/app.py"
#     )
#
#     thread = threading.Thread(target=flask.run, daemon=True)
#     thread.start()
#     from_url(f"http://localhost:{PORT}/?for_pdf=True", "JACK_WARDELL_CV.pdf")
