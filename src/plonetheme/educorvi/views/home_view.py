# -*- coding: utf-8 -*-

from plone import api
from plonetheme.educorvi import _
from Products.Five.browser import BrowserView


class HomeView(BrowserView):

    def __call__(self):
        self.res_url = api.portal.get().absolute_url()+'/++plone++plonetheme.educorvi'
        return self.index()
