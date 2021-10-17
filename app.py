from flask import render_template, redirect, url_for, request
from models import db, Project, app
import datetime

@app.route('/')
def index():
    projects = Project.query.all()
    print(projects)
    return render_template('index.html', projects=projects)


@app.route('/projects/new')
def new_project():
    pass


@app.route('/projects/<id>')
def project(id):
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project)


@app.route('/projects/<id>/edit')
def edit_project(id):
    pass


@app.route('/projects/<id>/delete')
def delete_project(id):
    pass


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')