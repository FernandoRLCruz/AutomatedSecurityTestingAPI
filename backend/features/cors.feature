
Feature: This feature check if the API is vulnerable to Cross domain attack.

       @wip
       Scenario Outline: Cross Domain attack with same origin policy
        Given I verify api "<url>" using for following methods "<method>"
        When  I include the "<headers>" and "<body>" to request 
<<<<<<< HEAD
        And   I check result cors scan response
=======
        And   I check result response
>>>>>>> parent of 01150fc... commit estrutural
        #Then  I display report with results 
    
        Examples: cors
        | url      | method | headers                                                              | body                                          |
        | /users/2 | POST   |  {"Content-type" : "application/json", "access_token" : "X123B12DF"} | {"first_name":"flipkart","last_name":"appsec"}|     