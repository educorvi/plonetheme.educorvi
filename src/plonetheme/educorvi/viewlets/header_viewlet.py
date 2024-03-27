# -*- coding: utf-8 -*-

from plone import api
from plonetheme.educorvi.utils import crop
from plone.app.layout.viewlets import ViewletBase
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class HeaderViewlet(ViewletBase):

    def update(self):
        self.portal_url = api.portal.get().absolute_url()
        self.logo_url = self.portal_url + '/++plone++plonetheme.educorvi/educorvi-logo.svg'
        self.items = self.get_formatted_items()

    def get_formatted_items(self):
        formatted_items = []
        portal = api.portal.get()
        portalid = portal.id
        contextpath = self.context.virtual_url_path().split('/')
        if contextpath[-1] == portalid:
            formatted_items.append({'title':'Startseite', 'url':self.portal_url, 'class':'nav-link mb-1 mb-lg-0 py-2 px-3 px-xl-4 active'})
        elif contextpath[-1] == portal.getDefaultPage():
            formatted_items.append({'title':'Startseite', 'url':self.portal_url, 'class':'nav-link mb-1 mb-lg-0 py-2 px-3 px-xl-4 active'})
        else:
            formatted_items.append({'title':'Startseite', 'url':self.portal_url, 'class':'nav-link mb-1 mb-lg-0 py-2 px-3 px-xl-4'})

        objroot = None
        if len(contextpath) == 1: 
            if contextpath[0] != portalid:
                objroot = contextpath[0]

        if len(contextpath) > 1:
            objroot = contextpath[1]

        items = self.get_items()
        for i in items:
            if objroot and objroot in i['url']:
                i['class'] = 'nav-link mb-1 mb-lg-0 py-2 px-3 px-xl-4 active'
            else:
                i['class'] = 'nav-link mb-1 mb-lg-0 py-2 px-3 px-xl-4'
            formatted_items.append(i)
        return formatted_items


    def check_displayed_types(self, item):
        """
        Check settings if content type should be displayed in navigation.
        """
        types = api.portal.get_registry_record(name='plone.displayed_types')
        if item.portal_type not in types:
            return True


    def check_filter_on_workflow(self, item):
        """
        Check workflow settings if item should be displayed in navigation.
        """
        filter = api.portal.get_registry_record(
            name='plone.filter_on_workflow',
        )
        states = api.portal.get_registry_record(
            name='plone.workflow_states_to_show',
        )
        if filter:
            state = api.content.get_state(obj=item.getObject())
            if state not in states:
                return True

    def contains_items(self, item):
        """
        Check if navigation will return items for folder
        """
        items = item.getObject().getFolderContents()
        for item in items:
            if self.check_item(item):
                return True
        return False


    def check_item(self, item):
        """
        Check if we want to have the given item in the navigation.
        """
        if self.check_displayed_types(item):
            return False
        if self.check_filter_on_workflow(item):
            return False
        if item.exclude_from_nav:
            return False
        try:
            if self.context.default_page == item.id:
                return False
        except AttributeError:
            pass
        return True


    def get_items(self):
        context = self.context
        context = api.portal.get_navigation_root(self.context)
        view_types = api.portal.get_registry_record(
            name='plone.types_use_view_action_in_listings')
        contents = list()
        try:
            contents = context.getFolderContents()
        except Exception:  # noqa: 902
            pass
        items = list()
        for item in contents:
            if self.check_item(item):
                item_type = 'link-item'
                url = item.getURL()
                if item.portal_type in view_types:
                    url = url + '/view'
                if item.is_folderish and self.contains_items(item):
                    item_type = 'link-folder'
                data = {
                    'title': item.Title,
                    'title_cropped': crop(item.Title, 100),
                    'url': url,
                    'type': item_type,
                }
                items.append(data)
        return items


    def index(self):
        return super(HeaderViewlet, self).render()
