"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from xblock.core import XBlock
from xblock.fields import Integer, Scope,String
from xblock.fragment import Fragment


class TableCreaterXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    # count = Integer(
    #     default=0, scope=Scope.user_state,
    #     help="A simple counter, to show something happening",
    # )

    csv_url = String(display_name="CSV URL",default="",scope=Scope.settings,help="upload the csv and input its url")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the TableCreaterXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/tablecreater_view.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/tablecreater.css"))
        frag.add_javascript(self.resource_string("static/js/src/tablecreater.js"))

        # frag.add_javascript(self.resource_string("static/js/src/tablecreater_edit.js"))

        frag.initialize_js('TableCreaterXBlock')
        return frag


    def studio_view(self,context=None):

        context = {
            'csv_url':self.csv_url
        }

        html = self.resource_string('static/html/tablecreater_edit.html')
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/tablecreater.css"))
        frag.add_javascript(self.resource_string("static/js/src/tablecreater_edit.js"))
        frag.initialize_js('TableMakerXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
        

    @XBlock.json_handler
    def getHtml(self, data, suffix=''):
        self.csv_url = "baidu"
        return {"csv":self.csv_url}


    @XBlock.json_handler
    def save_tablecreater(self,data,suffix=''):
        self.csv_url = data['csv_url']

        return {"result":"success"}

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("TableCreaterXBlock",
             """<tablecreater/>
             """),
            ("Multiple TableCreaterXBlock",
             """<vertical_demo>
                <tablecreater/>
                <tablecreater/>
                <tablecreater/>
                </vertical_demo>
             """),
        ]
