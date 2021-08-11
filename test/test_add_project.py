import random
import string
from model.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    old_projects = app.project.get_list()
    project_name = random_string("name", 5)
    app.project.create(project_name)
    new_projects = app.project.get_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(Project(name=project_name, id=app.project.find_id_by_name(project_name)))
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
