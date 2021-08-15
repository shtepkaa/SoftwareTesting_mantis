import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def check_empty_filling(app):
    if len(app.soap.get_projects_list(username=app.config['webadmin']['username'],
                                      password=app.config['webadmin']['password'])) == 0:
        app.project.create(random_string("name", 5))


def test_del_project(app):
    check_empty_filling(app)
    old_projects = app.soap.get_projects_list(username=app.config['webadmin']['username'],
                                              password=app.config['webadmin']['password'])
    random_project = random.choice(old_projects)
    app.project.delete(random_project.id)
    new_projects = app.soap.get_projects_list(username=app.config['webadmin']['username'],
                                              password=app.config['webadmin']['password'])
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(random_project)
    assert old_projects == new_projects
