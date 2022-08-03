from config.database import db
from models.use_case import UseCase
from models.use_case_answer import UseCaseAnswer


class IncludeRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    use_case_answer = db.Column(UseCaseAnswer, nullable=False)
    connected_component_01 = db.Column(UseCase, nullable=False)
    connected_component_02 = db.Column(UseCase, nullable=False)
    plagiarism_count = db.Column(db.String(50), nullable=False)
    correctness_count = db.Column(db.String(50), nullable=False)
