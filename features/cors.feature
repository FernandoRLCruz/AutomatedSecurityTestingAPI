
Feature: This feature check if the API is vulnerable to Cross domain attack.

       Scenario Outline: Cross Domain attack with same origin policy
        Given I verify api "<url>" using for following methods "<method>"
        When  I include the "<header>" and "<body>" to request 
        #When  I check result response
        #Then  I display report with results 
    
        Examples: cors
        | url                          | method | header | body |
        | https:/reqres.in/api/users/2 | DELETE | teste  | teste|     