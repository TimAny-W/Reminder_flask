from datetime import datetime
from uuid import uuid4

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")
app.secret_key = f'{uuid4()}'  # secret key

reminders = []


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        reminder_text = request.form['text']
        reminder_date = request.form['date']
        reminder_time = request.form['time']

        date_str = f'{reminder_date} {reminder_time}'
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M')

        reminders.append(
            {
             'text': reminder_text,
             'date': date_obj
             }
        )
        return redirect(url_for('home'))
    now = datetime.now()
    upcoming_reminders = []
    for index, reminder in enumerate(reminders):
        if reminder['date'] > now:
            reminder['index'] = index

            upcoming_reminders.append(reminder)

    return render_template(r'home.html',upcoming_reminders=upcoming_reminders)


@app.route('/joke', methods=['GET'])
def joke_page():
    return render_template(r'joke_page.html')


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, True)
