from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *


class AddJob(FlaskForm):
    title = StringField("Job Title", validators=[DataRequired()])
    team_leader = StringField('Team Leader id', validators=[DataRequired()])
    work_size = StringField('Work size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is finished', validators=[])
    submit = SubmitField('Add')
