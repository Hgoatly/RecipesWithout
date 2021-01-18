# Recipes Without

## A customisable online resource for recipes without gluten, dairy or eggs

## Site Owner Goals:

Recipes Without is a recipe site that is designed to be a customisable online resource for those looking to 
prepare meals free from gluten, dairy or eggs. It is primarily intened for those suffering from allergies or intolerances. 
However the recipies can be enjoyed by anyone. 

It has two main objectives: 

1. To allow site users to find recipies without allergens.
2. To allow site users to store and manage their favourite recipies in an easily accessable format.

## Business Owner Goals:

- The site has one main goal, which is to collect recipies in order to publish them in a physical book at a later date.

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

## Wireframes:

Original wireframes from the 17/01/2021 can be found here:
- <a href="assets/wireframes/sitemap-wireframes-recipes-without.pdf" target="_blank">Sitemap</a>
- <a href="assets/wireframes/desktop-wireframes-recipes-without.pdf" target="_blank">For Desktop</a>
- <a href="assets/wireframes/tablet-wireframes-recipes-without.pdf" target="_blank">For Tablet</a>
- <a href="assets/wireframes/smartphone-wireframes-recipes-without.pdf" target="_blank">For Smartphone</a>


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







