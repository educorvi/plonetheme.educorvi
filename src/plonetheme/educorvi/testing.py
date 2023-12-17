# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.educorvi


class PlonethemeEducorviLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plonetheme.educorvi)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.educorvi:default')


PLONETHEME_EDUCORVI_FIXTURE = PlonethemeEducorviLayer()


PLONETHEME_EDUCORVI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_EDUCORVI_FIXTURE,),
    name='PlonethemeEducorviLayer:IntegrationTesting',
)


PLONETHEME_EDUCORVI_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_EDUCORVI_FIXTURE,),
    name='PlonethemeEducorviLayer:FunctionalTesting',
)


PLONETHEME_EDUCORVI_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_EDUCORVI_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PlonethemeEducorviLayer:AcceptanceTesting',
)
