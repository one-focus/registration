# Created by Alex Kardash at 24/07/2021
Feature: Check google.com

  @monitor_italy @retry1000
  Scenario: montor germany
    When open url: "https://prenotami.esteri.it/"
    Then page italy consulate is opened
    Then click on language en link
    Then enter "stelmashuk_vova@mail.ru" in email field
    Then enter "Visa2020!" in password field
    Then click on login button
    Then click on language en link
    When click on book tab
    When enter "Schengen" in search field
    When click on book schengen button
    When click on privacy checkbox
    When click on forward button
    When accept alert
    When send dates