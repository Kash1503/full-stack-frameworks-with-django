# UnicornAttractor - Full Stack Development with Django

This is a website designed to allow fans of the UnicornAttractor web app to log any technical issues they are having or request that the developers of the app create a new feature. Users can track the status of any issues or features, and even see how the development team are progressing through use of the analytics section, providing transparency between the dev team and the user. 


## UX

This project is aimed at users of the UnicornAttractor app. This covers a wide demographic, meaning that the site needs to be simple enough for the less computer literate users to navigate, yet complex enough to meet the demands and expectations of the more computer savvy users. 

### User Stories

- As a user, I want to view existing bugs with the UnicornAttractor App (epic)
  - As a user, I want to see information about each ticket
  - As a user, I want to see how many upvotes the ticket has had
  - As a user, I want to be able to upvote any existing bugs that I am also experiencing
  - As a user, I want to be able to comment on a ticket for further information

- As a user, I want to create a profile in order to create and edit tickets, as well as pay for features and leave comments (epic)
  - As a user, I want to be able to create a profile with a unique username
  - As a user, I want to be able to be able to secure my profile with a password
  - As a user, I want to be be able to recover my password in the event I lose/forget it
  - As a user, I want to leave comments on tickets to engage in the community
  - As a user, I want to contribute to the creation of new features by up-voting the relevant ticket

- As a user, I want to be able to create tickets for bugs I am experiencing (epic)
  - As a user, I want to be able to input information about the bug I am experiencing

- As a user, I want to be able to create tickets for new feature ideas (epic)
  - As a user, I want to add to the pool of feature ideas
  - As a user, I want to leave information about the desired feature

- As a user, I want to be able to edit tickets I have created (epic)
  - As a user, I want to be able to update the status of a ticket
  - As a user, I want to be able to update the description of the ticket

- As a user, I want to see high level statistics about the tickets stored on the website (epic)
  - As a user, I want to see the top 5 features as per the upvotes
  - As a user, I want to see the top 5 bugs as per the upvotes
  - As a user, I want to see how many bugs and features have been resolved over time

- As a user, I want to be able to securely pay for upvotes on features (epic)
  - As a user, I want to use a trusted payment service 
  - As a user, I want the payment process to be easy and efficient
  - As a user, I want to be able to pay for multiple upvotes in one transaction
  - As a user, I want to be able to choose how much I pay for an upvote 

### Planning 

Wireframes and other documentation is stored in the [Planning Folder](planning)


## Features

### Existing features

- User registration: Allows users to create their own account with a unique username and email address. This allows the user to view existing tickets, create new ones, upvote tickets or pledge money to a feature they want to see created.
- Passoword recovery/reset: This will allow the user to reset their password if they feel it is no longer secure, or receive an email with details as to how to change their password in the event that it has been forgotten.
- User profile: This allows users to see the information we hold on them, including a list of all their tickets, open or closed. 
- Issue tracker: This will allow users to view the list of currently open tickets with high level information such as the title, ticket type(feature or bug), amount pledged to a feature currently, upvotes on bugs and also how many views the ticket has had. This can be filtered using the filter options to best suit the users search.
- Ticket details: This will provide more detailed information that the issue tracker, including a description of the ticket, the option to upvote or pledge, or leave comments to engage with the community.
- Create/edit ticket: This page allows users to create or edit a ticket, providing a title and description. This will then be added to the database and become viewable by all users, including the development team.
- Pledge/checkout service: This feature allows users to pledge funds to any given feature ticket, with a view that the top paid for features will be developed by the dev team. It will allow users to add multiple feature tickets to their shopping cart if they wish, enabling them to make a single payment for multiple tickets. The checkout page then creates an order for development team to see, and allows the user to make their payment.
- Analytics: This is a high level data dashboard showing the top 5 bugs and features currently open. It also shows a graph of all tickets closed over time, showing users the efficiency at which the dev team are working.
- Home page: This is a simple page showing some information about the app and the issue tracker site. It also describes to the user the mission of the development team, in that 50% of time spent developing will be used to develop the top paid for feature request.

### Features ideas yet to be added

- User should only be able to like a ticket once.
- More detailed information to be displayed on the analytics page.
- Search bar to use a keyword search for tickets. This was planned, however cut due to time constraints
- 'Previous' and 'Next' buttons used for pagination on tracker page
- Tags or categories for the tickets, enabling a more detailed filter option for the user 
- Clickable links for each ticket displayed on the top 5 lists
- Profile image to be uploaded by users to personalise their account


## Technologies Used

- [jQuery](http://jquery.com/)
  - jQuery has been used to assist in the styling and creating the charts
- [D3.js](https://d3js.org/)
- [DC.js](https://dc-js.github.io/dc.js/)
- [Crossfilter](https://square.github.io/crossfilter/)
  - D3.js, DC.js and Crossfilter have been used to create the graphs for the Analytics page
- [Bootstrap v3.3.7](https://getbootstrap.com/docs/3.3/)
  - Bootstrap used for styling of the site
- [Django v2.2](https://www.djangoproject.com/)
  - Django used to build the front and backend of the site
- [Stripe API](https://stripe.com/gb)
  - Stripe has been used to implement the checkout and payment system
- [Coverage](https://coverage.readthedocs.io/en/v4.5.x/)
  - Coverage has been used to ensure there is test coverage accross all possible code
- [SQLite](https://www.sqlite.org/index.html)
  - SQLite has been used as the test database for production version of the site
- [PostgreSQL](https://www.postgresql.org/)
  - PostgreSQL has been used for the deployed version of the site


## Testing

All testing completed on Safari and Google Chrome at both mobile and desktop size on macbook pro and iphone XR. Unable to see difference between browsers tested on.

*Manual Testing*

1. Login Page:
 - Go to the 'Login' page
 - Attempted to submit an empty form
 - Attempted to input invalid username
 - Attempted to input valid username

2. Register Page:
 - Go to the 'Register' page
 - Attempted to submit empty form
 - Attempted to submit partially complete form
 - Attempted to register with username which is already in use
 - Attempted to register a new user with a new username
 - Tested all buttons visible on the page
 - Attempted to use a different password for confirmation
 - Attempted to use an email address which is already in use

3. Home Page:
 - Go to the 'User/Home' page
 - Ensure styling and responsiveness was effective on all tested devices

4. Tracker Page:
 - Go to the Tracker page
 - Check that if not logged in, this redirects to the login page
 - Ensure filter options work correctly
 - Ensure that the 'Request Feature' and 'Log Bug' buttons take you to the respective page
 - Ensure that the amount of pages shown for pagination is calculated correctly
 - Test all buttons work as intended

5. Ticket Details Page:
 - Go to the 'Recipe Details' Page
 - Ensured that the information visible was displaying correctly and was accurate
 - Test the 'I'm having this issue too' and 'I want this too!' Buttons
   - Ensured that these Button was only clickable for recipes I had not created
 - Tested the 'Like' button for individual comments
 - Tested the comment feature to add a comment to a ticket

6. Create/Edit ticker Pages:
 - Go to the Create/Edit ticket page
 - Attmped to submit an empty form
 - Attempted to submit a partially complete form
 - Attempted to submit a complete form
 - Ensured that the ticket was added to the database once submitted
 - Tested all buttons visible on page

7. Analytics Page:
 - Go to the 'Analytics' page
 - Ensured that all data was accurate according to the data held in the database
 - Ensure that the Closed ticket chart displayed correctly accross all screen sizes

 8. Password reset:
  - Follow the 'Forgot password' link on the login page
  - Entered email address of the desired account
  - Followed link sent via email
  - Checked that email rendered correctly and contained the right information
  - Entered new password into form
  - Attempted to enter different confirmation password


*Automatic Testing*

To run the automatic tests, please use the command 'python3 manage.py test' in the console. All tests should pass.

You can also use the command 'coverage run manage.py test' to use Coverage to run the tests, and then the command 'coverage report -m' to see the coverage of tests accross the code.


*Bugs*

Encountered various bugs while testing:

- Bug found where the original implementation of pagination on the tracker and profile pages did not work with the tracker page filter options. This required a re-write of the pagination logic on the back end
- Encountered bugs where the 'Closed Tickets' chart did not render properly at mobile screen size. Implemented a new chart designed for mobile to fix
- Bug when implementing the search bar on the nav bar. Due to time constraints, unable to fix. This would be planned for a future update


## Deployment

In order to deploy this project, regular commits were made to the Github repository and then using Heroku I was able to deploy the website. No apparent difference between development and deployed builds.

To deploy to Heroku I have created a requirements.txt file to hold informtion on the different technologies required by Python to run the app. This can be used for others to download and install the required files. A Procfile was also required by Heroku to run the app.

The environment variables needed to be applied to the Heroku app so these were set on the Heroku dashboard. I was also required to add the new web address to the 'Allowed Hosts' in the settings.py file.

Finally, a Posgres database has been used for production, so this was also implemented on the Heroku dashboard, and in the settings.py file, set to use the Postgres database for deployment, but to use the SQLite database for development. This also required that 'Debug' mode was turned off in deployment and turned on in development so as to prevent users seeing debug code when using the app.

I have only used multiple git branches for development. One to implement the dashboard, one for the unit tests and the master branch. Initially began working soley from the master branch however, after speaking with my course mentor, used the other branches.

[Click here to go to the website](https://data-centric-design.herokuapp.com/)

### Content

Only one image was used for this project, the user avatar image on the home page and comments section.

- [User avatar image](https://upload.wikimedia.org/wikipedia/commons/1/1e/Default-avatar.jpg)

### Acknowledgments

Inspiration was taken from the following: 

- [Github Issues](https://github.com/issues)
- [Stack Overflow](https://stackoverflow.com/)