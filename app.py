from flask import Flask
from flask import render_template

app = Flask(__name__)


class Description:
    def __init__(self, lines):
        self.lines = lines


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
    nationality = "British National"
    links = [
        ("https://www.jackwardell.co.uk", "Home"),
        ("https://github.com/jackwardell", "Github"),
        ("https://www.linkedin.com/in/jack-wardell-london/", "LinkedIn"),
        ("https://medium.com/@jackwardell", "Medium"),
        ("https://www.antipodecoefficient.com/", "Antipode Coefficient"),
    ]

    # personal summary
    summary = """I am an enthusiastic software developer who genuinely derives pleasure from 
    learning and building. I am motivated by an innate curiosity and a desire to master my technologies.
    I believe in agile delivery and as such that customer collaboration is key to 
    developing a successful product."""

    # job history
    jobs = [
        Job(
            "AI Engineer",
            "Shell",
            "Dec 2019",
            "Jun 2020",
            "London",
            Description(
                lines=[
                    """A continuation of my previous role as a Data Engineer with a greater 
                    focus on modeling and productionising data science work.""",
                    "During this time I completed the Udacity course: Introduction to Machine Learning",
                ]
            ),
        ),
        Job(
            "Data Engineer",
            "Shell",
            "Jun 2018",
            "Dec 2019",
            "London",
            Description(
                lines=[
                    """On-site consultant at Shell working as a data engineer. 
                    During this time, in a team, we delivered a tool for internal customers.
                    Using ScrumBan and a lean startup approach, I interacted with customers 
                    weekly to understand their pain and to build features they actually wanted.""",
                    "Delivered:",
                    [
                        "A CI/CD pipeline",
                        "Data ingestion from multiple sources and processing",
                        "Deployed models to the cloud",
                        "A website / tool frontend",
                        "Migration from monolithic codebase to kubernetes",
                    ],
                    "Skills used:",
                    [
                        "Backend: Python, including Flask, SQLAlchemy, Pandas, Numpy, Scikit-learn",
                        "CI: Git, Jenkins",
                        "CD: Azure Web App, Kubernetes, VMs",
                        "Databases: PostgreSQL, Redis, Azure Datalake Store",
                        "Cloud: Azure",
                        "Front End: HTML, CSS, Javascript, JQuery, Bootstrap4",
                        "Agile: Lean Startup, Mutual Learning, Scrum, Kanban",
                        "Other: Jira, Slack, ACT, RFT",
                    ],
                    "Internally awarded prizes within Shell:",
                    [
                        "Code Masters Award",
                        "Downstream Directors Award",
                        "Chemicals: Increasing profitability in our base business",
                    ],
                ]
            ),
        ),
        Job(
            "Big Data Engineer",
            "Kubrick Group",
            "Feb 2018",
            "Jun 2020",
            "London",
            Description(
                lines=[
                    """For 4 months I was rigorously trained on - site in the
                    discipline of big data engineering.In this bootcamp I
                    learnt technical skills and soft skills for business.
                    Including but not limited to:""",
                    [
                        "Python",
                        "SQL (T-SQL, Microsoft SQL Server)",
                        "NoSQL (MongoDB)",
                        "Spark (Hadoop, Hive)",
                        "Excel",
                    ],
                    """I was then placed at Shell on client site for 2 years where I am now.""",
                ]
            ),
        ),
    ]

    # education history
    education = [
        Education(
            "UCL",
            "2018",
            "London",
            Description(
                lines=[
                    """3rd Year dissertation on ‘Structural Defects in Metal–Organic Frameworks’ under Prof. Ben Slater""",
                    """4th Year advanced chemical project on ‘Synthesis and Study of Exotic Magnets – Engineering New Quantum States’ under Prof. Andrew Wills""",
                ]
            ),
            "MSci Chemistry",
        ),
        Education("Abingdon School", "2013", "Oxford", Description),
    ]

    # languages
    languages = ["English"]

    # skills
    skills = {
        "Key Skills": [
            ("Data Engineering", 5),
            ("Software Engineering", 5),
            ("AI Engineering", 4),
            ("Data Analysis", 4),
            ("Data Modelling", 4),
            ("Machine Learning", 4),
            ("Data Ingestion", 5),
        ],
        "Languages": [
            ("Python", 5),
            ("Javascript", 3),
            ("HTML", 5),
            ("CSS", 4),
            ("SQL", 5),
        ],
        "Frameworks": [("Flask", 5), ("JQuery", 3), ("Vue.js", 2), ("Bootstrap4", 5),],
        "Libraries": [("Pandas", 5), ("Numpy", 4), ("Scikit-learn", 4),],
        "Software Engineering": [
            ("TDD", 4),
            ("SOLID", 4),
            ("APIs", 5),
            ("Linux", 4),
            ("Git", 5),
            ("Docker", 5),
            ("AWS", 4),
            ("Azure", 5),
            ("Kubernetes", 3),
        ],
        "Agile & Other methodologies": [
            ("Scrum", 4),
            ("Kanban", 5),
            ("Lean Startup", 4),
            ("XP", 4),
            ("OKR", 4),
            ("Mutual Learning", 5),
            ("DevOps", 5),
        ],
        "Other skills": [("Chemistry", 5), ("Public Speaking", 4),],
    }


@app.route("/")
def curriculum_vitae():
    return render_template("curriculum_vitae.html", cv=CurriculumVitae)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
