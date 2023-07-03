TODOs
Finalize SQL table and make sure its changed throughout




# CS50 Final Project: LXG Fantasy Football Website

### Video Demo (VIDEO URL TODO)

For my final project in CS50 I created a functional website for my main fantasy football league. League mates and myself will be able to initially register on the site and then be able to log in at any time. Once logged in, they will be able to view a wide variety of pages such as member bios, league history and our Leagues Constitution. Users will be able to submit Keepers (franchise player), submit amendments and vote on said amendments. The website will serve a great and functional purpose as we have only done these items via text serve in the past.

## Programs utilized in design
- Python
- Flask
- Jinja
- HTML
- CSS
- SQL
- Bootstrap
- Canva
- Google Docs (Iframes)

## Breakdown of project files
app.py:
    Main file containing python code for all 22 routes on the website
helpers.py:
    Supplemental file containing 3 helper functions
images folder:
    Member pictures, graphics, league logo, and icons all in PNG format
styles.css:
    Linked CSS file containing styling properties for the website
html templates:
    - layout.html
        - Main layout file containing all links, html for NavBar and body by utilizing Jinja
    - 22 html templates for each route of website
        - Utilizes a wide variety of html tags used in conjunction with the linked style sheet to display forms, images, tables, and links throughout
SQL FILE(TODO):

## Breakdown of pages/routes
#### Register
This is where leauge members will register for the site. They will input their name and fantasy team name, choose a username and password and be prompted to confirm password. Once all information is inputted and submitted without error it will be stored in SQL database(TODO) in the 'managers' table. The table will assign them a 'user_id' number which is a unique identifier to be used throughout the rest of their time on the website as well as 'hash' their password for security purposes. The site will return an apology message/page if any input fields are missing or if passwords do not match.

#### Log In
Once managers are registered they will be able to login to the site. This page will simply allow them to enter username and password to log in. Site will return apology message/page for any missing input fields.

#### Homepage
NavBar:
The sites Navbar was implemented using some Bootstrap framework. Consists of our league name which is a link to the homepage and a simple drop down menu for (most of) the different routes. A cool feature I intergrated into the Navbar was having the 'Logout' link be able to display the name of the current user. Ie: 'Logout as Noah Dickson'
Body:
The homepage route and subsequent html file might have the most.
#### Members
#### History
#### Constitution
#### Amendments
#### Voting
#### Keepers/Change Keeper
#### Vote Log

## Documentation
## How to Access