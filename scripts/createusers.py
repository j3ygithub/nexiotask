import json

from models import User, db

if __name__ == "__main__":
    charles_data = {
        "name": "Charles",
        "job_title": "SRE",
        "communicate_information": json.dumps(
            {
                "email": "charles@gmail.com",
                "mobile": "09xx-xxx-xxx",
            }
        ),
    }
    charles = User(**charles_data)
    db.session.add(charles)
    allen_data = {
        "name": "Allen",
        "job_title": "Backend Engineer",
        "communicate_information": json.dumps(
            {
                "email": "allen@gmail.com",
                "mobile": "09xx-xxx-xxx",
            }
        ),
    }
    allen = User(**allen_data)
    db.session.add(allen)
    db.session.commit()
