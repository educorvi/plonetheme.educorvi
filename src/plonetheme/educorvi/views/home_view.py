# -*- coding: utf-8 -*-

from plonetheme.educorvi import _
from Products.Five.browser import BrowserView
from plone import api

class HomeView(BrowserView):

    def __call__(self):
        self.res_url = api.portal.get().absolute_url()+'/++plone++plonetheme.educorvi'
        return self.index()
