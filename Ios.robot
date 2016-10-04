*** Settings ***
Documentation    IOS DEMO APP TESTING Example test cases With IOS using the Appium and gherkin syntax.Developed By Wasey

...
...               This kind of _gherkin_ syntax has been made popular by
...               [http://cukes.info|Cucumber]. It works well especially when
...               tests act as examples that need to be easily understood also
...               by the business people.
Library           Ios.py
*** Test Cases ***


Test toolber in UiCatlog IOS APP.
  When user setup desirecapabolities
   Then test 010 element toolber
   Then user shutdown ios

Test Web in UiCatlog IOS APP.
    When user setup desirecapabolities
    Then test 008 element Web
    Then user shutdown ios

Test TextField in UiCatlog IOS APP.
    When user setup desirecapabolities
    Then test 005 element textview
    Then user shutdown ios
Test Control in UiCatlog IOS APP.
    When user setup desirecapabolities
    Then test 002 element control
    Then user shutdown ios

Test Image in UiCatlog IOS APP.

    When user setup desirecapabolities
    Then test 007 element Image
    Then user shutdown ios

Test Picker in UiCatlog IOS APP.

    When user setup desirecapabolities
    Then test 006 element Picker
    Then user shutdown ios

Test Searchfield in UiCatlog IOS APP.

   When user setup desirecapabolities
   Then test 004 element searchField
   Then user shutdown ios

Test Segmant in UiCatlog IOS APP.

    When user setup desirecapabolities
    Then test 009 element Segmant
    Then user shutdown ios

Test TextView in UiCatlog IOS APP.

  When user setup desirecapabolities
  Then test 005 element TextView
  Then user shutdown ios

*** Keywords ***
