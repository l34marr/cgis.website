# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import cgis.website


class CgisWebsiteLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=cgis.website)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cgis.website:default')


CGIS_WEBSITE_FIXTURE = CgisWebsiteLayer()


CGIS_WEBSITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CGIS_WEBSITE_FIXTURE,),
    name='CgisWebsiteLayer:IntegrationTesting'
)


CGIS_WEBSITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CGIS_WEBSITE_FIXTURE,),
    name='CgisWebsiteLayer:FunctionalTesting'
)


CGIS_WEBSITE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CGIS_WEBSITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CgisWebsiteLayer:AcceptanceTesting'
)
