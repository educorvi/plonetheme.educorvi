# -*- coding: utf-8 -*-
from plone import api
from plone.app.layout.viewlets import ViewletBase


class BannerViewlet(ViewletBase):

    def update(self):
        portal_url = api.portal.get().absolute_url()
        self.imageurl = portal_url + '/++plone++plonetheme.educorvi'
        self.consulting_url = f'{portal_url}/consulting'
        self.development_url = f'{portal_url}/development'
        self.education_url = f'{portal_url}/education'
        self.consulting = 'consulting' in self.context.id
        self.development = 'development' in self.context.id
        self.education = 'education' in self.context.id

    def index(self):
        return super(BannerViewlet, self).render()
