Feature: Login page
  Scenario: Users Logs into Application
    Given Lunch Chrome Browser
    Then title should be "Login"

    When User Enters first "IbrahemCy21"
    And User Click on Login Button
    And User Enters "123qweASD!@#$"
    And User Click on Login Button
    And User click on CyberProtect Button
#    Then User should be navigated to Dashboard
#    And title should be "Cyber Protect Console"





