from flask import Flask
from flask import render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "<replace with a secret key>"
toolbar = DebugToolbarExtension(app)


class Description:
    content = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
        "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut"
        "enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor "
        "in reprehenderit in voluptate velit esse cillum dolore eu fugiat "
        "nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt "
        "in culpa qui officia deserunt mollit anim id est laborum."
    )


class Job:
    def __init__(
        self, job_title, employer, start_date, end_date, location, description
    ):
        self.job_title = job_title
        self.employer = employer
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.description = description


class Education:
    def __init__(self, institution, date, location, description, degree=None):
        self.institution = institution
        self.date = date
        self.location = location
        self.description = description
        self.degree = degree


class CurriculumVitae:
    name = "Jack Wardell"
    email_address = "jackwardell@me.com"
    phone_number = "+44 7868 118 271"
    job_title = "Data Engineer / Software Engineer / AI Engineer / Technologist"

    # personal summary
    summary = "I am an enthusiastic software developer who genuinely derives pleasure from learning and building."

    # job history
    jobs = [
        Job("AI Engineer", "Shell", "Dec 2019", "Jun 2020", "London", Description),
        Job("Data Engineer", "Shell", "Jun 2018", "Dec 2019", "London", Description),
        Job(
            "Big Data Engineer",
            "Kubrick Group",
            "Feb 2018",
            "Jun 2020",
            "London",
            Description,
        ),
    ]

    # education history
    education = [
        Education("UCL", "2018", "London", Description, "MSci Chemistry"),
        Education("Abingdon School", "2013", "Oxford", Description),
    ]

    languages = ["English"]


@app.route("/")
def curriculum_vitae():
    return render_template("curriculum_vitae.html", cv=CurriculumVitae)


if __name__ == "__main__":
    app.run()
