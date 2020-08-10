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
    def __init__(self, institution, location, description, date=None, degree=None):
        self.institution = institution
        self.date = date
        self.location = location
        self.description = description
        self.degree = degree


class Personal:
    def __init__(self, name, description, skills_used=None):
        self.name = name
        self.description = description
        self.skills_used = skills_used


class CurriculumVitae:
    name = "Jack Wardell"
    job_title = "Data Engineer / Software Engineer"
    nationality = "British National"
    links = [
        ("https://www.jackwardell.co.uk", "Home"),
        ("https://github.com/jackwardell", "Github"),
        ("https://www.linkedin.com/in/jack-wardell-london/", "LinkedIn"),
        # ("https://medium.com/@jackwardell", "Medium"),
        ("https://www.antipodecoefficient.com/", "Antipode Coefficient"),
    ]

    # personal summary
    summary = """I am an enthusiastic software developer who genuinely derives pleasure from
    learning and building. I am motivated by an innate curiosity and a desire to master my technologies.
    I believe in agile delivery and as such, that customer collaboration is key to
    developing a successful product and delivering value to both the customer and business."""

    _values = [
        "Simplicity",
        "Courage",
        "Respect",
        "Compassion",
        "Curiosity",
        "Transparency",
        "Customer collaboration",
        "Feedback & adapting to change",
    ]
    values = ", ".join(_values)

    looking_for = [
        "Building software mainly in Python",
        "A highly collaborative, cross-functional agile team",
        "A non-hierarchical and psychologically safe working environment",
        "An exciting product",
    ]

    offering = [
        "My broad spectra of data and software engineering skills",
        "Loyalty and kindness towards my colleagues",
        "Dedication to delivering value to the customer and therefore the business",
        "A desire for regular customer engagements",
        "Knowledge sharing / training within the team",
    ]

    specific_expertise = [
        "Flask (have contributed 3 times to source code and have my own pip installable flask library)",
        "SQLAlchemy & Postgres",
        "Bootstrap4",
    ]

    # job history
    jobs = [
        Job(
            "AI Engineer",
            "Shell",
            "Dec 2019",
            "Present",
            "London",
            Description(
                lines=[
                    """I changed roles in the new year into a new team but in the same product.
                    The new role is similar to my previous role as a Data Engineer, but with a greater
                    focus on modeling, productionising machine learning work in kubernetes and building pipelines.""",
                    # "During this time I completed the Udacity course: Introduction to Machine Learning",
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
                    weekly to understand their pain and therefore their requirements.
                    We used this instruction to build features they actually wanted.""",
                    "Business aims:",
                    [
                        "To optimise internal customer decision making by applying machine learning",
                        "To improve business decision making by 10%",
                        "To consolidate various discrete signals from multiple sources into a single view",
                    ],
                    "Customer pain points:",
                    [
                        "I can't predict what's going to happen to X",
                        "I don't have a clear understanding of the effects of A on X",
                        "I can't consolidate the effects of numerous features on X into a single view",
                    ],
                    "Delivered:",
                    [
                        "A CI/CD pipeline",
                        "Data ingestion from multiple sources and processing",
                        "Deployed models to the cloud",
                        "A website / tool frontend",
                        "Migration from monolithic codebase to microservices in kubernetes",
                    ],
                    "Skills used:",
                    [
                        "Backend: Python, including Flask, SQLAlchemy, Pandas, Numpy, Scikit-learn",
                        "CI: Git, Jenkins",
                        "CD: Azure Web App, Kubernetes, VMs",
                        "Databases: PostgreSQL, Redis, Azure Datalake Store",
                        "Cloud: Azure",
                        "Front End: HTML, CSS, Jinja2, Javascript, JQuery, Bootstrap4",
                        "Agile: Scrum, Kanban (ScrumBan), Lean Startup, Mutual Learning",
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
            "Present",
            "London",
            Description(
                lines=[
                    """For 4 months I was rigorously trained on-site in the
                    discipline of big data engineering. In this bootcamp I
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
            # "2018",
            "London",
            Description(
                lines=[
                    """3rd Year dissertation on ‘Structural Defects in Metal–Organic Frameworks’ under Prof. Ben Slater""",
                    """4th Year advanced chemical project on ‘Synthesis and Study of Exotic Magnets – Engineering New Quantum States’ under Prof. Andrew Wills""",
                ]
            ),
            degree="MSci Chemistry, 2.1",
        ),
        Education(
            "Abingdon School",
            # "2013",
            "Oxford",
            Description(lines=["Chemistry A*, Maths A*, Further Maths B, Art A"]),
        ),
    ]

    # languages
    languages = ["English"]

    # skills
    # todo: better formatting
    # initial intention was a star rating
    # however haven't decided on its implementation yet
    _skills = {
        "Key Skills": [
            ("Data Engineering", 5),
            ("Software Engineering", 5),
            ("AI/ML Engineering", 4),
            ("Full Stack Development", 4),
            ("Data Analysis", 4),
            ("Data Modelling", 4),
            ("Machine Learning", 4),
            ("Data Ingestion", 5),
            ("Back End Engineering", 5),
            ("Front End Engineering", 3),
        ],
        "Languages": [
            ("Python", 5),
            ("SQL", 5),
            ("HTML", 5),
            ("CSS", 4),
            ("Javascript", 3),
        ],
        "Frameworks & Libraries": [
            ("Flask", 5),
            ("JQuery", 3),
            ("Vue.js", 2),
            ("Bootstrap4", 5),
            ("Jinja2", 5),
            ("Pandas", 5),
            ("Numpy", 4),
            ("Scikit-learn", 4),
        ],
        "Software Engineering": [
            ("TDD", 4),
            ("SOLID", 4),
            ("APIs", 5),
            ("Linux", 4),
            ("Git", 5),
            ("Docker", 5),
            ("AWS", 4),
            ("Azure", 5),
            ("Heroku", 5),
            ("Kubernetes", 3),
        ],
        "Agile & Other Methodologies": [
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
    skills = {i: [k[0] for k in j] for i, j in _skills.items()}

    personal = [
        Personal(
            "Antipode Coefficent",
            """Built a small website to calculate the antipode coefficient
            between two points. The basic idea is that two points can be
            described with a number between 0 and 1 where 1 represents a place
            being perfectly opposite on the globe.""",
            [
                "Flask",
                "SQLAlchemy",
                "Alembic",
                "PostgreSQL",
                "Heroku",
                "Mapbox",
                "geopy",
                "gunicorn",
                "click",
                "Bootstrap4",
                "pytest",
                "TDD",
                "Github",
                "JQuery",
            ],
        ),
        Personal(
            "Udacity Course On ML",
            """Completed multiple projects on supervised and unsupervised
            learning, with sklearn and pytorch.""",
            [
                "Ensemble models",
                "Bayesian models",
                "SVMs",
                "Image classifiers",
                "PCA",
                "scikit-learn",
                "pytorch",
                "matplotlib",
                "seaborn",
                "pandas",
                "numpy",
            ],
        ),
        Personal(
            "Open source contributor",
            """A few packages on pip, contributions to Flask, many repos and projects on GitHub""",
        ),
        Personal(
            "Gardening, Botany, Horticulture & Bonsai",
            """I enjoy growing plants and identifying trees. Currently growing
            multiple flowers, plants and trees. This summer I went wild tree hunting, potting up saplings from the forest, in preparation to bonsai.""",
        ),
        # Personal(
        #     "History",
        #     """I love learning and reading about history, particularly human
        #     history, ancient history and English history.""",
        # ),
    ]


# @app.route("/")
# def curriculum_vitae():
#     return render_template("curriculum_vitae.html", cv=CurriculumVitae)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
