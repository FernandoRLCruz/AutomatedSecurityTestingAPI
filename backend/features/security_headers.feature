
Feature: This feature check if the API is vulnerable to Security Headers.

       @wip
       Scenario Outline: Security Headers attack
        Given I verify api "<url>" using for following methods "<method>"
        When  I include the "<headers>" and "<body>" to request 
        And   I check result security headers scan response
            | attack_method        | parameter_1             | parameter_2 |
            | csp_check            | Content-Security-Policy | 
            | xss_protection_check | X-XSS-Protection        |
        #Then  I display report with results 
    
        Examples: security headers
        | url      | method | headers | body                                          |
        | /users/2 | POST   |  None   | {"first_name":"flipkart","last_name":"appsec"}|     