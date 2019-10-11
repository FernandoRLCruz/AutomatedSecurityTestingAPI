
Feature: This feature check if the API is vulnerable to sql injection attack.

       
       Scenario Outline: Sql injection attack
        Given I verify api "<url>" using for following methods "<method>"
        When  I include the "<headers>" and "<body>" to request 
        And   I check result <attack> response
        #Then  I display report with results 
    
        Examples: sqli
        | url        | method | headers                                | body                                                     | attack |
        | /api/login | POST   | {"Content-type" : "application/json"}  | {"email": "eve.holt@reqres.in","password": "cityslicka"} | sqli   |