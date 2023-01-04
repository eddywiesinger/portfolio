import os

from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, Length, EqualTo

app = Flask(__name__, static_folder='static')
app.secret_key = os.environ['APP_SECRET']
Bootstrap4(app)

PRIMARY_COLOR = '#1f4eff'
SECONDARY_COLOR = '#ffd03c'


class ContactForm(FlaskForm):
    name_first = StringField('First Name',
                             [DataRequired()])
    name_last = StringField('Last Name',
                            [DataRequired()])
    email = StringField('Email Address', [DataRequired(),
                                          Email(), Length(min=6, max=50)])
    password = PasswordField('New Password', [DataRequired(), EqualTo('confirm',
                                                                      message='Passwords must match')
                                              ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Submit')


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Thank you for your message!')
        return redirect(url_for('hello'))
    return render_template('contact.html', form=form)


@app.route('/whatido')
def whatido():
    return render_template('whatido.html')


if __name__ == '__main__':
    app.run(debug=True)
