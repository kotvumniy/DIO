from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField, BooleanField, PasswordField, FloatField, URLField, \
    SelectField, EmailField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterUser(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, message="Password min length is 8")])
    repeat_password = PasswordField("Repeat password", validators=[DataRequired(), Length(min=8),
                                                                   EqualTo('password', message='Passwords must match')])
    phone_number = IntegerField("Phone Number", validators=[DataRequired()])
    country = SelectField("Your Country", choices=[('af', 'Afghanistan'),
                                                   ('ar', 'Argentina'),
                                                   ('am', 'Armenia'),
                                                   ('au', 'Australia'),
                                                   ('az', 'Azerbaijan'),
                                                   ('bd', 'Bangladesh'),
                                                   ('br', 'Brazil'),
                                                   ('ca', 'Canada'),
                                                   ('cn', 'China'),
                                                   ('cd', 'Democratic Republic of the Congo'),
                                                   ('eg', 'Egypt'),
                                                   ('et', 'Ethiopia'),
                                                   ('fr', 'France'),
                                                   ('de', 'Germany'),
                                                   ('ge', 'Georgia'),
                                                   ('gh', 'Ghana'),
                                                   ('in', 'India'),
                                                   ('id', 'Indonesia'),
                                                   ('ir', 'Iran'),
                                                   ('it', 'Italy'),
                                                   ('jp', 'Japan'),
                                                   ('ke', 'Kenya'),
                                                   ('kr', 'South Korea'),
                                                   ('lk', 'Sri Lanka'),
                                                   ('my', 'Malaysia'),
                                                   ('mx', 'Mexico'),
                                                   ('ma', 'Morocco'),
                                                   ('ng', 'Nigeria'),
                                                   ('pk', 'Pakistan'),
                                                   ('ph', 'Philippines'),
                                                   ('pl', 'Poland'),
                                                   ('ru', 'Russia'),
                                                   ('sa', 'Saudi Arabia'),
                                                   ('sg', 'Singapore'),
                                                   ('za', 'South Africa'),
                                                   ('es', 'Spain'),
                                                   ('lk', 'Sri Lanka'),
                                                   ('sd', 'Sudan'),
                                                   ('th', 'Thailand'),
                                                   ('tr', 'Turkey'),
                                                   ('tz', 'Tanzania'),
                                                   ('uk', 'United Kingdom'),
                                                   ('us', 'United States'),
                                                   ('uz', 'Uzbekistan'),
                                                   ('vn', 'Vietnam')])
    profile_picture = FileField("Your picture")
    submit = SubmitField("Submit")
    checkbox = BooleanField('Accept our rules?', validators=[DataRequired()])


class LoginUser(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, message="Password min length is 8")])
    checkbox = BooleanField('Accept our rules?')
    submit = SubmitField("Submit")


class AddProductClass(FlaskForm):
    name = StringField("Product name", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    text = StringField("Text", validators=[DataRequired()])
    category_id = IntegerField("Category ID", validators=[DataRequired()])
    image_url = URLField("Product picture", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddProductCategory(FlaskForm):
    category_name = StringField("Category name", validators=[DataRequired()])
    id = IntegerField("ID", validators=[DataRequired()])
    submit = SubmitField("Submit")
