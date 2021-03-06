"""
Course info page
"""
from edxapp_acceptance.pages.lms.course_info import CourseInfoPage
from regression.pages.lms import BASE_URL


class CourseInfoPageExtended(CourseInfoPage):
    """
    This class is an extended class of CourseInfoPage,
    where we add methods that are different or not used in CourseInfoPage
    """
    @property
    def url(self):
        """
        Construct a URL to the page within the course.
        """
        return BASE_URL + "/courses/" + self.course_id + "/" + self.url_path

    def click_resume_button(self):
        """
        Clicks Resume button of the course selected
        """
        self.q(css='.last-accessed-link').first.click()

    def get_page_names_in_tab(self):
        """
        Get names of all pages in tab

        Returns
            list: A list of names of all pages
        """
        tab_pages = self.q(css='.tabs.course-tabs .tab').text
        # There is an extra text 'Current location' along
        # the page's name of selected(active) tab. It is
        # not required, so removing it.
        return [page.replace('\n, current location', "") for page in tab_pages]
