# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import ViewletBase
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class HeaderViewlet(ViewletBase):

    def update(self):
        self.message = self.get_message()
        self.portal_url = api.portal.get().absolute_url()
        self.logo_url = self.portal_url + '/++plone++plonetheme.educorvi/educorvi-logo.svg'

    def get_message(self):
        return u'My message'

    def index(self):
        return super(HeaderViewlet, self).render()
