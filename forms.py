from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField,DateField
from wtforms.validators import DataRequired, EqualTo , length


class myform(FlaskForm):
   
    username=StringField('username',validators=[DataRequired()])
    email=StringField('email',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired(),length(min=8)])
    confirmpassword=PasswordField('confirmpassword',validators=[DataRequired(), EqualTo('password'),length(min=8)])
    firstname=StringField('firstname',validators=[DataRequired()])
    lastname=StringField('lastname',validators=[DataRequired()])
    user_id=IntegerField('user_id',validators=[DataRequired()])
    birthdate=DateField('birthdate',validators=[DataRequired()])
    submit=SubmitField('submit')
    
class get(FlaskForm):
    user_id=IntegerField('user_id',validators=[DataRequired()])
    submit=SubmitField('submit')
    
    

    
