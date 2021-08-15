from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project_name):
        wd = self.app.wd
        self.go_to_manage_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::td[1]").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project_name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def delete(self, project_id):
        wd = self.app.wd
        self.go_to_manage_projects_page()
        project_name = self.find_name_by_id(project_id)
        wd.find_element_by_link_text(project_name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    def go_to_manage_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    project_cache = None

    def get_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.go_to_manage_projects_page()
            self.project_cache = []
            rows = wd.find_elements_by_xpath("//tr[contains(@class, 'row-')][not(contains(@class, 'category'))]"
                                             "[not(ancestor::a)]")
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("a").get_attribute("href").split("=", 1)[1]
                name = cells[0].find_element_by_tag_name("a").text
                self.project_cache.append(Project(id=id, name=name))
        return list(self.project_cache)

    def find_id_by_name(self, project_name):
        wd = self.app.wd
        rows = wd.find_elements_by_xpath(
            "//tr[contains(@class, 'row-')][not(contains(@class, 'category'))][not(ancestor::a)]")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].find_element_by_tag_name("a").text
            id = cells[0].find_element_by_tag_name("a").get_attribute("href").split("=", 1)[1]
            if name == str(project_name):
                return id

    def find_name_by_id(self, project_id):
        wd = self.app.wd
        rows = wd.find_elements_by_xpath(
            "//tr[contains(@class, 'row-')][not(contains(@class, 'category'))][not(ancestor::a)]")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].find_element_by_tag_name("a").text
            id = cells[0].find_element_by_tag_name("a").get_attribute("href").split("=", 1)[1]
            if id == str(project_id):
                return name






