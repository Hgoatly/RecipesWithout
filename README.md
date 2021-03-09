# Recipes Without

## A customisable online resource for recipes without gluten, dairy or eggs

# **Table of Contents:**

- [Site Owner Goals](#site-owner-goals)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
    - [First Time Visitor Goals](#first-time-visitor-goals)
    - [Returning Visitor Goals](#returning-visitor-goals)
    - [Frequent Visitor Goals](#frequent-visitor-goals)
  - [Design](#Design)
    - [Colours Used](#colours-used)
    - [Typography](#typography) 
    - [Imagery](#imagery)
    - [Layout](#layout)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [Mobile Design Features](#mobile-design-features)
    - [Tablet Design Features](#tablet-design-features)
    - [Desktop Design Features](#desktop-design-features)
    - [How The Features Relate To The User Stories](#how-the-features-relate-to-the-user-stories)
    - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries and Other Sources Used](#frameworks,-libraries-and-other-sources-used)
  - [Application Programming Interfaces Used (APIs)](#application-programming-interfaces-used-(APIs))
- [Testing](#testing)
  - [Known Bugs and Fixes](#known-bugs-and-fixes)
- [Deployment](#deployment)
  - [Github Pages](#github-pages)
  - [Forking The Repository](#forking-the-repository)
  - [Making A Local Clone](#making-a-local-clone)
- [Credits](#credits)
- [Version Control](#version-control)


## Site Owner Goals:

Recipes Without is a recipe site that is designed to be a customisable online resource for those looking to 
prepare meals free from gluten, dairy or eggs. It is primarily intened for those suffering from allergies or intolerances. 
However the recipies can be enjoyed by anyone. 

The main objectives are as follows: 

1. To allow site users to find recipies without allergens.
2. To allow site users to view their own and other users recipes.
3. To allow site users to view recipes on allergen-specific pages.
4. To allow site users to add recipes to the site.
5. To allow site users to upvote/downvote their own, and other people's recipes.
6. To allow site users to update their own previously upladed recipes.
7. To allow site users to delete their previously uploaded recipes.
8. To allow site users to search the site for key words.
9. To allow the site owner (admin) to create, read, update and delete recipes added by any user - including themselves.
10. To allow the site owner (admin) to view and delete user recipes and user accounts.

The site uses CRUD (create, Read, Update, Delete) functionality in order to create an interactive user experience. 

The site is based around a multi-page layout, with access to different pages and features available according to whether or 
not you are a logged in registered user, or whether you are the site owner (admin).

The pages are detailed in the 'Design' section below: 

### First Time Visitor Goals:
- To easily find out the main purpose of the site. 
- To easily navigate around the site to find relevant content.
- To create an acount and begin to upload and manage recipes.

### Returning Visitor Goals:
- To find out if any new recipes have been added to the site, so that the user can use them for mealtime inspiration.
- To create an account if the user has not previously done so.
- To create, read, update or delete any recipes previously added by the user.

### Frequent Visitor Goals: 
- To find out if any new recipes have been added to the site, so that the user can use them for mealtime inspiration..
- To maintain an account with recipes that are reglarly created, read, edited and deleted.

## Business Owner Goals:

- The site has one main goal, which is to collect recipies in order to publish them in a physical book at a later date.
The site will be populated by recipes uploaded by users, using the CRUD functionality. 

- The secondary goal is for the site to be monetised through the advertising of appropriate allergen-free ingredients
by appropriate companies. This will be implemented at a later date. 

## UX:

### User Stories:

1. I have an allergy or intolerance to gluten, dairy or eggs and would like to find some appropriate recipes so that 
I can prepare myself a tasty meal that is also safe for me to eat.
2. I have a friend or relative who has an allergy or intolerance to gluten, dairy or eggs, and I would like to find some 
recipes so that I can safely cook them a tasty meal. 
3. I am a restaurant or cafe owner, and I would like to find inspiration for dishes that I can add to my menu that would
be suitable for diners with intolerances to gluten, dairy or eggs.
4. I am any of the above users, and I would like to be able to upload, edit and delete my own recipes, without other 
users being able to tamper with them.
5. I am a user who enjoys cooking, and I would like to have all of my favourite recipes easily accessible in a digital format, 
so that I can access them fromm anywhere.
6. I am the site owner, and I would like to be able to edit or delete other users recipes if I decide that they are inappropriate 
or offensive.
7. I am the site owner and I would like to collect recipes uploaded by users so that I can create a book to sell. 
8. I want to be able to get in touch with the site owner so that I can share any comments or criticisms about the site.
9. I have forgotten my password, and would like to be able to reset my password easily so that I can continue accessing my account.

### Design: 

** Home Page **
- The idea of the 'Recipes Without' homepage is to give the site visitor a preview of what they can find on the site. The hero image shows a tabletop
with food around the edges, and an empty space in the middle. Something is missing - which is a visual metaphor for 'Recipes Without', as all the 
recipes on the site have either no gluten, no dairy, or no eggs in them.
- Beneath the Hero image, there is a paragraph of text explaining the purpose and features of the site. This section is crucial, as without it the 
site visitor may not understand the purpose of the site, or may be unaware of its features.
- Below the paragraph, there is a search box, where the user can choose to perform a basic or advanced search of the site.
- Below the search box, there are 9 recipe cards - each of which display a randomly selected recipe from the database collection.
- At the bottom of the page is the footer Element. This contains links to Social Media sites, and a link back to the homepage. 

- ** Navbar: ** All pages except for the error pages have a fixed navbar at the top. This displays different nav elements according to whether the user is 
logged in or not, or whether the user is the site owner (admin). These are listed in the 'Site Owner Goals.

- ** Footer: ** All pages except for the error pages have a fixed footer at the bottom. From the footer, the user can navigate to the home, register, login and 
contact pages. There are also links to external social media sites.

- ### Accessible to all users via the navbar:
    - Home
    - Gluten Free: Images and titles of all gluten free recipes are displayed on cards, as well as the number of upvotes and downvotes they have. If the user is logged in, they are able to upvote/downvote the recipe. 
    - Dairy Free: Images and titles of all dairy free recipes are displayed on cards, as well as the number of upvotes and downvotes they have. If the user is logged in, they are able to upvote/downvote the recipe. 
    - Egg Free: Images and titles of all gluten free recipes are displayed on cards, as well as the number of upvotes and downvotes they have. If the user is logged in, they are able to upvote/downvote the recipe. 
    - Contact: A contact form with 'name', 'email address' and 'message' fields is displayed on a card. This is superimposed upon an image of a table of food.
    - Login:  A contact form with 'username', 'password' and 'confirm password' fields is displayed on a card. This is superimposed upon an image of a table of food.
    - register: A contact form with 'username', 'email address', 'memorable name', 'password' and 'confirm password' fields is displayed on a card. This is superimposed upon an image of a table of food.

- ### Accessible to all users via the search boxes:
    - Search Results

- ### Accessible to all users via the recipe cards:
    - Recipe: The entire recipe is displayed on a card, with an image of the recipe at the top of the card. The card is superimposed on a background image of fruit and vegetables on a table.

- ### Accessible to registered users via the navbar:
    - Add Recipes: A card entitled 'Add Your Recipe' with 'choose category', 'recipe name', 'equipment needed', 'number of portions', 'ingredients', 'method', 'add an image url' and 'describe your image' fields are superimposed
    on an image.  
    - My Recipes: Images of all of the recipes added by that user are displayed on individual cards, along with their titles, date they were added, buttons to view, edit or delete the recipe, buttons to upvote or downvote the recipe, 
    and the number of upvotes/downvotes that recipe has.  
    - Manage account: A card panel saying "(User)'s Recipes". Beneath, there is one button linking to the user recipes page, and another button that invites the user to delete their account. When clicked, a modal opens which asks: 
    "Are you sure you want to delete your account?" The user can then choose to click 'cancel', in order to close the modal, or "Yes I'm Sure" in order to delete their account.
    The panel is superimposed on an image of food items on a table.
    - Log out: This is not a separate page, but logs the user out of the site when it is clicked.

- ### Accessible to registered users via the My Recipes page:
    - Recipe (via the 'view recipe' 
    - Edit Recipe: A card entitled 'Edit Recipe' with 'choose category', 'Edit Recipe Name', 'Edit Equipment needed', 'Edit Number of Portions', 'Edit Ingredients', 'Edit Method', 'Edit image url' and 'Edit Image Description' fields are superimposed
    on an image or a chopping board with a knife and some herbs round the edges.  

- ### Accessible to registered users via the Manage Account page.
    - My Recipes: 

- ### Accessible only to the site owner (admin user):
    - Admin Section: A card panel with the title "Admin Section", which has a "Admin's Recipes" button that links to all of the recipes added by the site owner. Below, there are card panels that display a button, which when clicked, takes the user to 
    the "Users Recipes" page. Additionally there is a button that invites the user to delete that account. When clicked, a modal opens which asks: 
    "Are you sure you want to delete this account?" The user can then choose to click 'cancel', in order to close the modal, or "Yes I'm Sure" in order to delete their account.
    The panel is superimposed on an image of cakes on plates on a table.
    - User's Recipes:

- ### Error Pages:
    - 404 and 500 error pages are provided. They both show a background image of an empty plate on a table. The 404 page has the words "No Recipes Here" superimposed on the picture, and the 500 page says "Something's Wrong". On both pages, there is a button
     underneath which says: "Back To Recipes Without" on it, which when clicked take the user back to the home page. 

- ### Additional features available to logged in users:
    - On the My Recipes Page: Delete Recipe, Upvote, Downvote.
    - On the Recipe Category pages (Gluten Free, Dairy Free, Egg Free): Delete Recipe.
    - On the Manage Account Page: Delete Account.

- ### Additional features available to any user who is not logged in:
    - Reset Password form (accesssed via the login form).
    - Password Reset (accessed via an email link generated from submitting the Reset Password form).

## Colours Used: 
- ** Navbar and Footer: ** The Materialize colour "teal lighten-4" (#b2dfdb) was used as the background colour, 
because it is striking and fresh looking, and contrasts well with the images used throughout the site. The Materialize colour
"brown-text text-darken-3" (#4e342e) because it was a good contrast with the background colour, whilst matching the colours of the images. 

- ** Body: ** The colour chosen for the body was chosen as the Materialize colour "grey lighten-3" (#eee) as it was felt tht it would make 
a subtle but distinct contrast with the other content. 

- ** Buttons: ** The Materialize colour "teal lighten-3" (#80cbc4) was chosen in order to match the Navbar and Footer. Although it is not 
an exact match with the navbar and footer background colour, it as felt by the developer that "teal lighten-4" would be too light, and would not
meet accessibility guidelines. The text on the buttons is white, in order to make a contrast with the buttons themselves.

- ** Cards and Collapsibles: ** The Materialize colour "grey lighten-5" was used for all collapsible and card elements in order to contrast with the body.
It was decided by the developer that white (#fff) would be too bright. 

- ** Text: ** The Materialize colour "brown" (#795548) was chosen for the text throughout the page because it contrasts well with the background colours and images, and looks attractive.

## Wireframes:

Original wireframes from the 17/01/2021 can be found here:
- <a href="assets/wireframes/sitemap-wireframes-recipes-without.pdf" target="_blank">Sitemap</a>
- <a href="assets/wireframes/desktop-wireframes-recipes-without.pdf" target="_blank">For Desktop</a>
- <a href="assets/wireframes/tablet-wireframes-recipes-without.pdf" target="_blank">For Tablet</a>
- <a href="assets/wireframes/smartphone-wireframes-recipes-without.pdf" target="_blank">For Smartphone</a>

## Technologies Used:

### languages Used:
- HTML5
- CSS3
- Javascript
- Python


## Deployment: 

The project was written in Gitpod, pushed to a repository in Github for version control, and deployed to Heroku 
by following these steps:

1. Ensure that the requirements.txt, Procfile and gitignore files exist in your repository, and that they are up to date.

If not present, add them by typing the following commands into the CLI:

```
touch .gitignore
```

```
pip3 freeze --local > requirements.txt
```
for the requirements file.

```
echo web: python app.py > Procfile
```
for the Prcofile. Ensure that the Procfile has an upper-case P in the filename.

2. Inside the Procfile, make sure that it contains the following line:
```
web: python app.py
```
3. Delete any blank lines below the first line in the Procfile.

4. Inside the gitignore file, make sure that it contains the following lines of code so that the sensitive 
information contained within the env.py file and pycache directory will not be pushed to Github and made public:
```
env.py
__pycache__/
```

4. Login to Heroku, or sign up if you don't already have an account.
![heroku-login-page](assets/readme-images/heroku-login.jpg)

5. In the top right hand corner click on the 'new' button, and from the dropdown select 'create new app'.
![heroku-create-new-app-dropdown](assets/readme-images/heroku-new-dropdown.jpg)

6. On the next screen, choose a unique name for your app, and select your region, and click 'Create app'.
![heroku-create-new-app](assets/readme-images/heroku-create-new-app.jpg)

7. On the next page, click on 'connect to gitHub' next to the Github icon and search for your repository in the search box. 
![heroku-connect-github](assets/readme-images/heroku-connect-github.jpg)

8.  When your repository is listed, click on connect.
![heroku-connect-github-repository](assets/readme-images/heroku-connect-repository.jpg)

9. If successful, the text next to the Github icon will turn green, and say 'connected' 
![heroku-successfully-connected](assets/readme-images/heroku-github-connected.jpg)

10. Click on 'Settings' tab at the top of the page:
![heroku-settings-tab](assets/readme-images/heroku-settings-tab.jpg)

11. Scroll down the page and click on 'Reveal Config Vars'. Enter the following information as key/value pairs
into the empty input fields. They should match the content of your env.py file. Click 'add' after entering each key/value
pair in order to reveal new blank input fields.

```
IP = 0.0.0.0
PORT = 5000
SECRET_KEY = YOUR_SECRET_KEY
MONGO_URI = YOUR_MONGODB_URI
MONGO_DBNAME = DATABASE_NAME
```
The value for 'YOUR_SECRET_KEY' should match the one in your env.py file. 

12. Return to the deployment page, by clicking on the 'deploy' tab at the top of the page.
![heroku-deploy-tab](assets/readme-images/heroku-deploy-tab.jpg)

13. Click on 'Enable Automatic Deploys'. Select the branch you would like to deploy, in this case 'master',
and click 'Deploy Branch'.
![heroku-deploy-tab](assets/readme-images/heroku-automatic-deploys.jpg)

14. If successful, 'Your app was successfully deployed' should be displayed.
![heroku-deploy-tab](assets/readme-images/heroku-app-deployed.jpg)







