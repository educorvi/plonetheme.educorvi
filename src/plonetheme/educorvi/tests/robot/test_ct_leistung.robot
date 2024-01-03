# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s plonetheme.educorvi -t test_leistung.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src plonetheme.educorvi.testing.PLONETHEME_EDUCORVI_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/plonetheme/educorvi/tests/robot/test_leistung.robot
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

Scenario: As a site administrator I can add a Leistung
  Given a logged-in site administrator
    and an add educorvi Homepage form
   When I type 'My Leistung' into the title field
    and I submit the form
   Then a Leistung with the title 'My Leistung' has been created

Scenario: As a site administrator I can view a Leistung
  Given a logged-in site administrator
    and a Leistung 'My Leistung'
   When I go to the Leistung view
   Then I can see the Leistung title 'My Leistung'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add educorvi Homepage form
  Go To  ${PLONE_URL}/++add++educorvi Homepage

a Leistung 'My Leistung'
  Create content  type=educorvi Homepage  id=my-leistung  title=My Leistung

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Leistung view
  Go To  ${PLONE_URL}/my-leistung
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Leistung with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Leistung title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
