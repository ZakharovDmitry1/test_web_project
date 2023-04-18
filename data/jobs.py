import sqlalchemy
from flask_login import UserMixin

from data.db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase, UserMixin):
    __tablename__ = "jobs"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    title = sqlalchemy.Column(sqlalchemy.String)
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    def __repr__(self):
        return f'<{self.id}> team_leader:{self.team_leader}, title:{self.title}, job:{self.job}'
