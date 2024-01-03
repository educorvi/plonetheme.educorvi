# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from plonetheme.educorvi.content.educorvi_homepage import IEducorviHomepage  # NOQA E501
from plonetheme.educorvi.testing import PLONETHEME_EDUCORVI_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class EducorviHomepageIntegrationTest(unittest.TestCase):

    layer = PLONETHEME_EDUCORVI_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_educorvi_homepage_schema(self):
        fti = queryUtility(IDexterityFTI, name='educorvi Homepage')
        schema = fti.lookupSchema()
        self.assertEqual(IEducorviHomepage, schema)

    def test_ct_educorvi_homepage_fti(self):
        fti = queryUtility(IDexterityFTI, name='educorvi Homepage')
        self.assertTrue(fti)

    def test_ct_educorvi_homepage_factory(self):
        fti = queryUtility(IDexterityFTI, name='educorvi Homepage')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IEducorviHomepage.providedBy(obj),
            u'IEducorviHomepage not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_educorvi_homepage_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='educorvi Homepage',
            id='educorvi_homepage',
        )

        self.assertTrue(
            IEducorviHomepage.providedBy(obj),
            u'IEducorviHomepage not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('educorvi_homepage', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('educorvi_homepage', parent.objectIds())

    def test_ct_educorvi_homepage_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='educorvi Homepage')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_educorvi_homepage_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='educorvi Homepage')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'educorvi_homepage_id',
            title='educorvi Homepage container',
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
