# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s plonetheme.educorvi -t test_educorvi_homepage.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src plonetheme.educorvi.testing.PLONETHEME_EDUCORVI_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/plonetheme/educorvi/tests/robot/test_educorvi_homepage.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a educorvi Homepage
  Given a logged-in site administrator
    and an add educorvi Homepage form
   When I type 'My educorvi Homepage' into the title field
    and I submit the form
   Then a educorvi Homepage with the title 'My educorvi Homepage' has been created

Scenario: As a site administrator I can view a educorvi Homepage
  Given a logged-in site administrator
    and a educorvi Homepage 'My educorvi Homepage'
   When I go to the educorvi Homepage view
   Then I can see the educorvi Homepage title 'My educorvi Homepage'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add educorvi Homepage form
  Go To  ${PLONE_URL}/++add++educorvi Homepage

a educorvi Homepage 'My educorvi Homepage'
  Create content  type=educorvi Homepage  id=my-educorvi_homepage  title=My educorvi Homepage

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the educorvi Homepage view
  Go To  ${PLONE_URL}/my-educorvi_homepage
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a educorvi Homepage with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the educorvi Homepage title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
