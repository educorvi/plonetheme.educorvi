# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api

class BannerViewlet(ViewletBase):

    def update(self):
        self.imageurl = api.portal.get().absolute_url() + '/++plone++plonetheme.educorvi'


    def index(self):
        return super(BannerViewlet, self).render()
