import os
import smtplib

from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__, static_folder='static')
app.secret_key = os.environ['APP_SECRET']
Bootstrap4(app)

PRIMARY_COLOR = '#1f4eff'
SECONDARY_COLOR = '#ffd03c'


class ContactForm(FlaskForm):
    name = StringField('Your Name',
                             [DataRequired()])
    email = StringField('Your Email', [DataRequired(),
                                          Email(), Length(min=6, max=50)])
    body = TextAreaField(
        'Your Message',
        [
            DataRequired(),
            Length(min=4,
                   message='Your message is too short.'),
            Length(max=1000, message='Your message exceeds maximum length of 1000.')
        ],
    )
    submit = SubmitField('Submit')


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            msg = ("From: %s (%s)\r\nMessage: %s\r\n\r\n"
                   % (form.name.data, form.email.data, form.body.data))
            connection.starttls()
            connection.login(user=os.environ.get("MAIL_SENDER"), password=os.environ.get("GMAIL_APP_PASSWORD"))
            connection.sendmail(from_addr=os.environ.get("MAIL_SENDER"), to_addrs=os.environ.get("MAIL_RECIPIENT"), msg=f"Subject:New Message for Eddy Wi!\n\n{msg}")
            #print("Successfully sent email")
        flash('Thank you for your message!')
        return redirect(url_for('hello'))
    return render_template('contact.html', form=form)


@app.route('/whatido')
def whatido():
    return render_template('whatido.html')





#if __name__ == '__main__':
#    app.run(debug=True)
