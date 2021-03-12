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
- [Testing the Visitor Goals](#testing-the-visitor-goals)
  - [First Time Visitor Goals](#first-time-visitor-goals)
  - [Returning Visitor Goals](#returning-visitor-goals)
  - [Frequent Visitor Goals](#frequent-visitor-goals)
- [Testing the 404 error page](#testing-the-404-error-page)
- [Manual Browser Compatibility Testing](#Manual-browser-compatibility-testing)

## Chrome Developer Tools:

- Chrome developer tools was used regularly to check the layout, and to check the console for errors.

## W3C Markup Validation Service:

- The [W3C Markup Validation Service](https://validator.w3.org/) was used to check that HTML used for the site was compliant with modern standards.
The code passed the validator's tests with no errors:

There was, however, a warning on all pages that display flash messages. This is because that section is empty until the flash images are created by the back end, so the validator thinks that it's an empty section.
![Screenshot of the W3 HTML validator results](assets/readme-images/html-validator-w3c-warning.jpg "Screenshot of the W3 HTML validator results") 

## W3C CSS Validation Service: 

- The [W3C CSS Validation Service](https://jigsaw.w3.org/) was used to check that CSS used on the site was compliant with modern standards. The code passed the 
validator's tests with no errors or warnings. 
![Screenshot of the W3 CSS validator results](assets/readme-images/w3c-css-validator-results.jpg "Screenshot of the W3 HTML validator results")

## PEP8 Python Validation:

- The [PEP8 Online Checker](http://pep8online.com/checkresult) was used to check that the Python code was compliant with modern standards.
The code passed witn no errors or warnings.
![Screenshot-of-the-PEP8-validator-results](assets/readme-images/pep8.jpg "Screenshot of the W3 HTML validator results")

## JSHint:

- JSHint was used to test the validity of the Javascript code in the project. 'Let' was flagged as a warning, but once it was told to
recognise ECMAScript 6 features by adding: '/*jshint esversion: 6 */' at the top, all Javascript code passed with no errors or warnings. 
Undefined and unused vairables are noted however, but these are all either defined in other files, 
or in the case of the '$' sign, necessary for jquery - which has been used extensively in the project.

- Screenshot of JSHint warning about the use of 'let'.

![Screenshot of JSHint warning about the use of and 'let'](assets/readme-images/jshint-warning.jpg)

- Screenshot of JSHint with /*jshint esversion: 6 */ added to the top of the file, and with no warnings.

![Screenshot of JSHint with no warnings](assets/images/readme-images/jshint-no-warning.jpg)

## Testing the User Stories:

- The following user stories are listed in the README.md file. Images have been inserted below each of them to show how their requirements 
have been fulfilled, and how they relate to the CRUD functionality.

### **READ:** The first 3 user stories are concerned with being able to read data found on the site. This stage of user story testing 
is concerned with users who are not logged in:

1. I have an allergy or intolerance to gluten, dairy or eggs and would like to find some appropriate recipes so that 
I can prepare myself a tasty meal that is also safe for me to eat.
2. I have a friend or relative who has an allergy or intolerance to gluten, dairy or eggs, and I would like to find some 
recipes so that I can safely cook them a tasty meal. 
3. I am a restaurant or cafe owner, and I would like to find inspiration for dishes that I can add to my menu that would
be suitable for diners with intolerances to gluten, dairy or eggs.

- Scroll down the homepage to where a slection of recipe cards are shown:
    
    - **Test Case 1**
    - Ensure that the all recipe cards render as expected, with title, image, 'view recipe' button, number of upvotes, 
    and number of downvotes displayed on them. 
    - **Expected Result**: Recipe cards should render as described above.
    - **Actual Result**: Recipe cards render as described above.
    - **Pass/Fail**: Pass.

![Screenshot of recipe cards on homepage](assets/readme-images/recipe-cards-home.jpg)

- Click on the 'view recipe' card to find and read the entire recipe:

 - **Test Case 2**
    - Ensure that the 'view recipe' button-link takes the user to the 'recipe.html' page. Ensure that on the 'recipe.html' 
    page, the recipe renders as expected, with the recipe title, image, equipment needed, ingredients, method, portions, added by,
    added on, number of upvotes, number of downvotes, and a link back to the homepage.
    and number of downvotes displayed on them. . 
    - **Expected Result**: recipe.html page should render as described above.
    - **Actual Result**: recipe.html page renders as described above.
    - **Pass/Fail**: Pass.

![Screenshot of top section of recipe card on recipe.html](assets/readme-images/recipepage-top-section.jpg)
![Screenshot of middle section of recipe card on recipe.html](assets/readme-images/recipepage-middle-section.jpg)
![Screenshot of lower middle section of recipe card on recipe.html](assets/readme-images/recipepage-lower-middle-section.jpg)
![Screenshot of bottom section of recipe card on recipe.html](assets/readme-images/recipepage-bottom-section.jpg)

- Navigate to 'gluten-free.html' by clicking the link on the 'recipes' navbar link, and choosing 'Gluten Free' from the dropdown. 

 - **Test Case 3**
    - Ensure that the all recipe cards render as expected, with title, image, 'view recipe' button, number of upvotes, 
    and number of downvotes displayed on them.
    - **Expected Result**: gluten_free.html page should render as described above.
    - **Actual Result**: gluten_free.html page renders as described above.
    - **Pass/Fail**: Pass.

![Screenshot of recipe cards on gluten_free.html](assets/readme-images/gluten-free-recipe-cards.jpg)

- Navigate to 'dairy-free.html' by clicking the link on the 'recipes' navbar link, and choosing 'Dairy Free' from the dropdown. 

 - **Test Case 3**
    - Ensure that the all recipe cards render as expected, with title, image, 'view recipe' button, number of upvotes, 
    and number of downvotes displayed on them.
    - **Expected Result**: dairy_free.html page should render as described above.
    - **Actual Result**: dairy_free.html page renders as described above.
    - **Pass/Fail**: Pass.

![Screenshot of recipe cards on dairy free.html](assets/readme-images/dairy-free-recipe-cards.jpg)

- Navigate to 'egg-free.html' by clicking the link on the 'recipes' navbar link, and choosing 'Egg Free' from the dropdown. 

 - **Test Case 4**
    - Ensure that the all recipe cards render as expected, with title, image, 'view recipe' button, number of upvotes, 
    and number of downvotes displayed on them.
    - **Expected Result**: egg_free.html page should render as described above.
    - **Actual Result**: egg_free.html page renders as described above.
    - **Pass/Fail**: Pass.

![Screenshot of recipe cards on egg free.html](assets/readme-images/egg-free-recipe-cards.jpg)

- Navigate to Gluten Free, Egg Free or Dairy Free pages

- **Test Case 5**
    - Ensure that the view recipe button on each card navigates the user to 'gluten_free_recipe.html', 'egg_free_recipe.html' or 'dairy_free_recipe.html',
    - **Expected Result**: 'view recipe' button should operate as described above.
    - **Actual Result**: 'view recipe' button operates as described above.
    - **Pass/Fail**: Pass.

### **Create:** User stories 4 and 5 are concerned with being able to create data on the site. This stage of user story testing is 
concerned with logged in and registered users:

4. I am any of the above users, and I would like to be able to upload, edit and delete my own recipes, without other 
users being able to tamper with them.
5. I am a user who enjoys cooking, and I would like to have all of my favourite recipes easily accessible in a digital format, 
so that I can access them from anywhere.

- Navigate to 'register' by clicking the 'register' link on the navbar or on the footer. 

 - **Test Case 6**
    - Ensure that the the register card panel is rendered in front of the background image. The following fields should be displayed:
    username, email address, memorable name, password, and compare password.
    - **Expected Result**: register.html page should render as described above.
    - **Actual Result**: register.html page renders as described above.
    - **Pass/Fail**: Pass.

![Screenshot of register card panel on register.html](assets/readme-images/register-card-panel.jpg)

- Complete the 'Register' form.
    - **Test Case 7*
    - Ensure that submit button takes the user to 'my_recipes.html' when clicked. Ensure that form validation is present when the expected format
    is not followed.
    - **Expected Result**: register.html page should render as described above, form validation should be present, and submit button should take the user to 'my_recipes.html' when clicked.
    - **Actual Result**: register.html page renders as described above, form validation is present, and submit button takes the user to 'my_recipes.html' when clicked.
    - **Pass/Fail**: Pass.

- Navigate to 'Add Recipes' by clicking on the navbar link, or on the 'Add Recipe' button that is displayed when the 'My Recipes' page shows no recipes.

- **Test Case 8**
    - Ensure that the the Add Recipes card panel is rendered in front of the background image. The following fields should be displayed:
    username, email address, memorable name, password, and compare password.
    - **Expected Result**: register.html page should render as described above.
    - **Actual Result**: register.html page renders as described above.
    - **Pass/Fail**: Pass.

![Screenshot of top half of 'Add Recipes' card panel on add_recipes.html](assets/readme-images/add-recipe-top-screenshot.jpg)
![Screenshot of bottom half of 'Add Recipes' card panel on add_recipes.html](assets/readme-images/add-recipe-bottom-screenshot.jpg)

- Complete the 'Add Recipe' form.
    - **Test Case 9**
    - Ensure that submit ('Add Recipe') button takes the user to 'my_recipes.html' when clicked. Ensure that form validation is present when the expected format
    is not followed, and that the 'Add Recipe' button takes the user to the 'my recipes' page, where the newly added recipe is displayed.
    - **Expected Result**: 'add_recipes.html' page should render as described above, form validation should be present, and submit button should take the user to 'my_recipes.html' when clicked, 
    where the newly uploaded recipe is displayed.
    - **Actual Result**: 'add_recipes.html' page renders as described above, form validation is present, and submit button takes the user to 'my_recipes.html' when clicked, 
    where the newly uploaded recipe is displayed.
    - **Pass/Fail**: Pass.

- Navigate to 'My Recipes' by submitting the 'Add Recipes' form, registering, logging in, or by clicking the navbar link:
    - **Test Case 10**
    - Ensure that if the user has uploaded any recipes, all user recipe cards render as expected, with title, image, date recipe was added, 'view recipe', 'edit recipe' and 'delete' button, number of upvotes, 
    and number of downvotes displayed on them.
    - **Expected Result**: my_recipes.html page should render as described above.
    - **Actual Result**: my_recipes.html page renders as described above.
    - **Pass/Fail**: Pass.

![Screenshot of recipe cards on my_recipes.html](assets/readme-images/my-recipes-cards-screenshot.jpg)

### **Update:** User stories 4, 6 and 7 are concerned with being able to update data on the site. This stage of user story testing is 
concerned with logged in and registered users:

- Navigate to 'Edit Recipe' by clicking on one of the 'edit recipe' buttons located on recipe cards on the 'My Recipes' page.
    - **Test Case 11**
    - Ensure that the 'Edit Recipe' on the recipe cards button take the user to 'edit_recipes.html' when clicked. Ensure that form validation is present when the expected format
    is not followed, and that the 'Edit Recipe' button displays the flash message ' the user to the 'my recipes' page, where the newly added recipe is displayed.
    - **Expected Result**: 'edit_recipes.html' page should render as described above, form validation should be present, and submit button should take the user to 'my_recipes.html' when clicked, 
    where the newly uploaded recipe is displayed, and the flash message is displayed.
    - **Actual Result**: 'edit_recipes.html' page renders as described above, form validation is present, and submit button takes the user to 'my_recipes.html' when clicked, 
    where the newly edited recipe is displayed.
    - **Pass/Fail**: Pass.

- Navigate to 'My Recipes' by submitting the 'Add Recipes' form, registering, logging in, or by clicking the navbar link. From there, click on 
'view recipe' in order to navigate to 'recipe.html' 
    - **Test Case 12:**
    - Ensure that thumbs up (upvote) and thumbs down (downvote) buttons are present at the bottom of the card panel. Ensure that when clicked they increment the upvotes/downvotes 
    displayed on the page.
    - **Expected Result:** 'Upvote' and 'downvote' buttons are present at the bottom of the card panel. When clicked they increment the upvotes/downvotes 
    displayed on the page.
    - **Actual Result:** 'Upvote' and 'downvote' buttons are present at the bottom of the card panel. When clicked they increment the upvotes/downvotes 
    displayed on the page.
    - **Pass/Fail**: Pass.

![Screenshot of upvotes/downvotes on recipe.html](assets/readme-images/votes.jpg)

- Navigate to 'My Recipes' by submitting the 'Add Recipes' form, registering, logging in, or by clicking the navbar link.
    - **Test Case 13:**
    - Ensure that a 'delete' button is present on each recipe card, and that when clicked it opens a modal, which says: 'Confirm Delete
    Are you sure you want to delete this recipe?'. Below are these options: 'Yes I'm Sure' and ' Cancel'. Ensure that when clicked, 'cancel' 
    closes the modal and returns the user back to their 'my recipe' page, 
    and that when 'yes I'm sure' is clicked, the recipe is deleted, and a flash message is displayed confirming this.
    - **Expected Result:** A modal is triggered when 'delete' is clicked, which invites the user to cancel the action, or confirm that they want to delete the recipe.
    - **Actual Result:** A modal is triggered when 'delete' is clicked, which invites the user to cancel the action, or confirm that they want to delete the recipe.
    - **Pass/Fail**: Pass.

## **Delete:** User stories 7 and 8 are concerned with being able to delete data from the site:

7. I am a user who no longer wants to use the site, so I would like to be able to delete my account.
8. I am the site owner, and I would like to be able to edit or delete other users recipes if I decide that they are inappropriate 
or offensive.

- Navigate to 'Manage Account' by clicking the navbar link.
    - **Test Case 14:**
    - Ensure that when clicked, the 'Manage Account' link takes the user to their 'manage account' page, where a card panel is displayed with 'my recipes' and 
    'delete account' buttons are displayed. Ensure that when 'my recipes' is clicked, it takes the user to their 'my recipes' page. Ensure that when 
    'delete account' is clicked, a modal opens which asks: 'Confirm Delete Are you sure you want to delete your account?' When 'cancel' is clicked,
    ensure that the modal is closed, and the user is returned to their 'manage account' page. Ensure that when 'Yes I'm Sure' is clicked, the account is deleted.
    - **Expected Result:** Actions taken are as detailed above.
    - **Actual result: ** Actions taken are as detailed above.
    - **Pass/Fail**: Pass.

### **If the site owner is logged in:** 

- Navigate to 'Admin Section' via the navbar.
    - **Test Case 15:**
    - Ensure that when clicked, the 'Admin Section' link takes the user to 'admin.html', and that the card panel at the top of the page says
    'Admin Section', with a button that links to all of the site owner's recipes. Ensure that below, all user accounts are displayed on separate card panels
    with button-links to 'User's Recipes' and 'Delete Account'.
    - **Expected Result:** 'admin.html' will display card panels for each user, with links to all their recipes, and a delete button.
    - **Actual Result:** 'admin.html' displays card panels for each user with links to all their recipes, and a delete button.
    - **Pass/Fail**: Pass.

![Screenshot of card panels on admin.html](assets/readme-images/admin-section.jpg)

    - **Test Case 16:**
    - Ensure that when clicked, the 'Admin's Recipes' and 'User Recipes' cards navigate the user to 'user_recipes.html' 
    - **Expected Result:** 'Admin's Recipes' and 'User Recipes' buttons navigate the user to 'user_recipes.html'
    - **Actual Result:** ''Admin's Recipes' and 'User Recipes' buttons navigate the user to 'user_recipes.html'.
    - **Pass/Fail**: Pass.

    - **Test Case 17:** 
    - Ensure that when clicked, the 'delete account' button opens a modal that says: 'Confirm Delete Are you sure you want to delete this account?'
    Ensure that 'yes I'm sure' and 'cancel' buttons are displayed. Ensure that when 'yes I'm sure' is clicked, the account is deleted, and that when 
    'cancel' is clicked, the modal will close, and return the site owner to 'admin.html'.
    - **Expected Result:** The buttons will perform as described above.
    - **Expected Result:** The buttons perform as described above.
    - **Pass/Fail**: Pass.

![Screenshot of confirm delete modal](assets/readme-images/confirm-delete-modal.jpg)  
![Screenshot of admin section with deleted account removed](assets/readme-images/account-deleted.jpg) 

## User story 9 is concerned with being able to read data that has been uploaded to the site. It is also concerned with one 
of the business owner's goals:

9. I am the site owner and I would like to collect recipes uploaded by users so that I can create a book to sell. 

'The site has one main goal, which is to collect recipies in order to publish them in a physical book at a later date.
The site will be populated by recipes uploaded by users, using the CRUD functionality.'

The fact that the recipes will be used to create a book is explained in the welcome text on the homepage

![Screenshot of welcome text sentence](assets/readme-images/publication-text.jpg) 

- **Test Case 18:** 
    - Ensure that registered and logged in users are able to upload recipes to the site.
    - **Expected Result:** registered and logged in users are able to upload recipes to the site.
    - **Actual Result:** registered and logged in users are able to upload recipes to the site.
    - **Pass/Fail**: Pass.


## Contact: user story 10 is concerned with being able to contact the site owner:

10. I want to be able to get in touch with the site owner so that I can share any comments or criticisms about the site.

- Navigate to the contact page, by clicking the link on the navbar or the footer.
- **Test Case 19:** 
    - Ensure that any user is able to contact the site user via the contact form.
    - **Expected Result:** When the contact form is submitted, the site owner's email (recipetest579@gmail.com) 
    recieves an email from the site, and a flash message on the contact page confirms that an email has been sent.
    - **Actual Result:** When the contact form is submitted, the site owner's email (recipetest579@gmail.com) 
    recieves an email from the site, and a flash message on the contact page confirms that an email has been sent.
    - **Pass/Fail**: Pass.

![Screenshot of filled contact form](assets/readme-images/filled-contact-form.jpg)

- Screenshot of email account inbox where the email has been received.

![Screenshot of email inbox](assets/readme-images/email-inbox.jpg)


## Search: user story 11 is concerned with being able to search the site.

11. I am a site user and would like to be able to search the site, so that I can quickly and easily locate recipes.

- Navigate to the home page, by clicking the link on the navbar or the footer, or by clicking the site logo.

- **Test Case 20:** 
    - Ensure that when a search item is entered into the search box and submitted, the resuts are displayed on 'search results.html'. 
    If no results are found, then the user is informed by text saying
    - **Expected Result:** when a search item is entered into the search box and submitted, the resuts are displayed on 'search results.html'. 
    If no result is found, the user is informed that that is the case.
    - **Actual Result:** when a search item is entered into the search box and submitted, the resuts are displayed on 'search results.html'. 
    If no result is found, the user is informed that that is the case.
    - **Pass/Fail**: Pass.

![Screenshot of no recipes](assets/readme-images/no-recipes.jpg)