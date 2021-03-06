from flask import render_template, redirect, url_for, request
from models import db, Project, app
from datetime import datetime


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def new_project():
    projects = Project.query.all()
    if request.form:
        date = datetime.strptime(request.form['date'], '%Y-%m')
        new_project = Project(
        title = request.form['title'],
        description = request.form['desc'],
        completion_date = date,
        skills = request.form['skills'],
        github = request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=projects)


@app.route('/projects/<id>')
def project(id):
    project = Project.query.get_or_404(id)
    date = project.completion_date.strftime('%B %Y')
    skills = project.skills.split(', ')
    return render_template('detail.html', project=project, date=date, skills=skills)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    date = project.completion_date.strftime('%Y-%m')
    if request.form:
        project.title = request.form['title']
        project.completion_date = datetime.strptime(request.form['date'], '%Y-%m')
        print(project.completion_date)
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.github = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editform.html', projects=projects, project=project, date=date)


@app.route('/projects/<id>/delete')
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    projects = Project.query.all()
    return render_template('404.html', projects=projects, msg=error), 404



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')