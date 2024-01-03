# -*- coding: utf-8 -*-

from plone import api
from plonetheme.educorvi import _
from Products.Five.browser import BrowserView


class HomeView(BrowserView):

    def __call__(self):
        self.res_url = api.portal.get().absolute_url()+'/++plone++plonetheme.educorvi'
        return self.index()
        titleparts = self.context.title.split('@')[0]
        self.title_one = titleparts[0]
        self.title_two = ''
        if len(titleparts) > 1:
            self.title_two = titleparts[1]
        self.cat_one = self.context.service_categories[0]
        self.cat_two = self.context.service_categories[1]
        self.cat_three = self.context.service_categories[2]

    def get_header_content(self):
        title = self.context.title
