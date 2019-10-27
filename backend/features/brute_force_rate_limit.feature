
Feature: This feature check if the API is vulnerable to Brute Force.

       @wip
       Scenario Outline: Brute Force attack
        Given I verify api "<url>" using for following methods "<method>"
        When  I include the "<headers>" and "<body>" to request 
        And   I check result brute force response
        #Then  I display report with results 
    
        Examples: brute force
        | url        | method | headers | body                                                      | attack           |
        | /api/login | POST   |  None   | {"email":"eve.holt@reqres.in","password":"cityslicka"}    | brute force      |