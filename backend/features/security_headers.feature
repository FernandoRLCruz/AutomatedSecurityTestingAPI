
Feature: This feature check if the API is vulnerable to Security Headers.

       
       Scenario Outline: Security Headers attack
        Given I verify api "<url>" using for following methods "<method>"
        When  I include the "<headers>" and "<body>" to request 
        And   I check result security headers response
            | attack_method                | parameters                             |
            | csp_check                    | Content-Security-Policy                | 
            | xss_protection_check         | X-XSS-Protection, 0, 1;mode=block      |
            | x_frame_options_check        | X-Frame-Options                        |
            | x_content_type_options_check | X-Content-Type-Options                 |
            | hsts_check                   | Strict-Transport-Security              |
            | cookies_check                | HttpOnly                               |
            | check_version_disclosure     | Server, X-Powered-By, X-AspNet-Version |
        #Then  I display report with results 
    
        Examples: security headers
        | url      | method | headers | body                                          | attack           |
        | /users/2 | POST   |  None   | {"first_name":"flipkart","last_name":"appsec"}| security headers |