# Recipes Without Testing:

The Recipes Without site was tested extensively, using the following processes:

# Table of Contents:

- [Chrome-Developer-Tools](#chrome-developer-tools)
- [W3c-Markup-Validation-Service](#W3C-markup-validation-service)
- [W3C-CSS-Validation-Service](#W3C-markup-validation-service)
- [JSHint](#jshint)
- [Testing the User Stories](#testing-the-user-stories)
  - [Create](#create)
  - [Read](#read)
  - [Update](#update)
  - [Delete](#delete)
  - [Book](#book)
  - [Map](#map)
  - [Contact](#contact)
- [Testing the Swedish Content](#testing-the-swedish-content)
- [Testing the Visitor Goals](#testing-the-visitor-goals)
  - [First Time Visitor Goals](#first-time-visitor-goals)
  - [Returning Visitor Goals](#returning-visitor-goals)
  - [Frequent Visitor Goals](#frequent-visitor-goals)
- [Testing the 404 error page](#testing-the-404-error-page)
- [Manual Browser Compatibility Testing](#Manual-browser-compatibility-testing)

## Chrome Developer Tools:

- Chrome developer tools was used regularly to check the layout, and to check the console for errors.

## W3C Markup Validation Service:

- The [W3C-Markup-Validation-Service](https://validator.w3.org/) was used to check that HTML used for the site was compliant with modern standards.
The code passed the validator's tests with no errors:

There was, however, a warning on all pages that display flash messages. This is because that section is empty until the flash images are created by the back end, so the validator thinks that it's an empty section.
![Screenshot of the W3 HTML validator results](assets/readme-images/html-validator-w3c-warning.jpg "Screenshot of the W3 HTML validator results") 

## W3C CSS Validation Service: 

- The [W3C-CSS-Validation-Service](https://jigsaw.w3.org/) was used to check that CSS used on the site was compliant with modern standards. The code passed the 
validator's tests with no errors or warnings. 
![Screenshot of the W3 CSS validator results](assets/readme-images/w3c-css-validator-results.jpg "Screenshot of the W3 HTML validator results")
