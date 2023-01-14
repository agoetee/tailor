from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import CourseForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dd38f17bfaab5a77c9586314e01e63769627cec9dbd6ba36'


course_list = [{
    'title' : 'Purple Hibiscus',
    'description' : 'A lovely Novel set in Nigeria',
    'price' : 45,
    'available' : True,
    'level' : 'Intermediate'
}]

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=('POST', 'GET'))
def index():
    form = CourseForm()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=1)