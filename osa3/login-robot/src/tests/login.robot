*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Login With Incorrect Password
    Input Credentials    kalle    kalle321
    Output Should Contain    Invalid username or password

Login With Nonexistent Username
    Input Credentials    pekka    kalle123
    Output Should Contain    Invalid username or password

Register With Valid Username And Password 
    Create User   pekka   janne1234  
    Input Credentials    pekka    janne1234
    Output Should Contain    Logged in


Register With Already Taken Username And Valid Password
    Create User    kalle     kalle12345
    Output Should Contain    User with username kalle already exists

Register With Too Short Username And Valid Password
    Create User   aa  asdf1234
    #Should Be False  ${status}
    Output Should Contain    Username too short


Register With Enough Long But Invalid Username And Valid Password
    Create User  pekka1234  salasana123
    Output Should Contain    Username has forbidden symbols


Register With Valid Username And Too Short Password
    Create User   pekkaqwer  1234a
    Output Should Contain    Password too short


Register With Valid Username And Long Enough Password Containing Only Letters
    Create User  PekkaTammi    Salasanaontarpeeksipitka
    Output Should Contain    Password must contain special charachters


*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command

