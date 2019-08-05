
Feature: This feature check if the API is vulnerable to Broken Authentication.

       
       Scenario Outline: Broken Authentication attack
        Given I verify broken api "<url>" using for following methods "<method>"
        When  I include the "<headers>" and "<body>" to request 
        And   I check result response
        #Then  I display report with results 
    
        Examples: Authentication
        | url                           | method | headers | body                                                      |
        | https://reqres.in/api/login   | POST   |  blank  | {"email": "eve.holt@reqres.in", "password": "cityslicka"} |     