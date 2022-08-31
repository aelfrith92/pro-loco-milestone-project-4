# Pro-Loco Supersano

Pro-Loco Supersano is an NGO based in Supersano - Italy, that gathers resourceful members always striving to organize events for the local community. This web-based app lets them have a general overview on events organized so far. Users visiting the website can interact with the content, depending on their admin rights. 

![Mock Up](docs/readme_images/multi-dev-mockup.png)

## Table of Contents
* [User Experience Design (UX)](#User-Experience-Design)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [Agile Planning](#Agile-Planning)
          * [User Stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plan)
    * [The Structure Plane](#The-Structure-Plan)
      * [Features](#Features)
      * [Future Features](#Features-Left-to-Implement)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframes)
        * [Database Design](#Database-Design)
        * [Security](#Security)
    * [The Surface Plane](#The-Surface-Plane)
        * [Design](#Design)
            * [Colour Scheme](#Colour-Scheme)
            * [Typography](#Typography)
            * [Imagery](#Imagery)
* [Technologies](#Technologies)
* [Testing](#Testing)
* [Deployment](#Deployment)
    * [Version Control](#Version-Control)
    * [Heroku Deployment](#Heroku-Deployment)
    * [Run Locally](#Run-Locally)
    * [Fork Project](#Fork-Project)
* [Credits](#Credits)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)

# User-Experience-Design

## The-Strategy-Plane

### Site-Goals

The site is aimed to give the NGO an online area where to show, organize, cancel local events, that are accessible to people that - otherwise - would not be able to view their events on other platforms. Moreover, as part of their policy, Pro-Loco Supersano also fosters active participation within the local community, turning into a chance to come up with one's suggestions via a dedicated form.

Eventually, users with admin rights (the staff) can approve both messages left on event pages and proposed events.

### Agile Planning

This project was developed using agile methodologies, by delivering small features (issues). Tasks have been prioritized differently - based on their importance.

All issues were assigned to a project, prioritized under the labels, Must have, Should have, Could have, good first issue. They were handled according to complexity. "Must have" stories were completed first, "should haves", "could haves", and "good first issue" seen as features that visiting users would have seen first on the home page - a blend of higher priority and user-oriented experience. It was done this way to ensure that all core requirements were completed first, while additional features enriching the user experience would have been added gradually.

The Kanban board was created using github projects and can be located [here](https://github.com/users/aelfrith92/projects/2/views/1?layout=board). It can be viewed to see more information on the project cards. Some stories have a set of acceptance criteria in order to define the functionality that marks that story as complete. Some other stories do not have acceptance criteria, as they were considered self-explanatory.

![Board](docs/readme_images/UserStories.png)

#### User Stories

The following user stories were completed over time. Basic setup stories - such as development-related ones - have been omitted, to prioritize those strictly pertaining the end-user experience. The categories of users described below are "Site User" - meant as a non-authenticated user OR an authenticated user without staff/admin rghts, "admin or privileged user" - meant as an authenticated user, that can be part of the staff. If someone is an admin, but not part of the staff, they may not have access to certain features and might need to access the Django admin overview.

**Customer's statement**

As the president of the association Pro-Loco Supersano, I would like a home page, where members and non-members can find information about our activities and initiatives

**Authentication**

As a Site User I can register an account, so that I can leave comments and my intention to join events

**Pagination and first impression**

As a Site User I can view a list of events with a short preview, so that I can select one to read about

As a Site User I can view a paginated list of events, so that I can easily select an event to view

**Interactions**

As a Site User I can click on an event in the home page, so that I can read about details: whereabouts, whenabouts, etc.

As a Site user I can leave comments on single event pages, so that I can interact with other site users

As a Site user I can join / remove participation to single events, so that I can let other users know that I am going to join an event

As a site user I can receive a notification banner at the top when an action was performed/processed successfully, so that I can have certainty of submitted data

As a Site user I can suggest an event, so that I can feel involved in the local community

As a site authenticated user I can suggest events and get warnings when I am trying to submit an overlapping event, so that I get more chances to see my suggestion approved

**Admin/staff actions**

As a site admin or privileged user (part of the staff) I can edit events, so that I can organize them better.

As a site admin or privileged user (part of the staff) I can delete events, so that get rid of unwanted records in the database.

As a Site Admin I can create, read, update posts, so that I can manage my blog content.

**Documentation**

Tasks:

* Complete readme documentation
* Complete testing documentation write up

## The-Scope-Plan

* Responsive Design - Site should be fully functional on all devices from 320px up
* Hamburger menu for mobile devices
* Ability to perform CRUD functionality on events - admins; Create/Suggest + Read for standard authenticated users
* Restricted role based features
* Home page with list of events

## The-Structure-Plan

### Features

``CUSTOMER'S STATEMENT - As the president (owner) of the association Pro-Loco Supersano, I would like a home page, where members and non-members can find information about our activities and initiatives``

Within the statement, there are a series of taken-for-granted features that should cover essential home page components, such as the navigation menu at the top.

Implementation:

**Navigation Menu**

 The Navigation contains links for Home, allauth options, suggestions (event creation for all authenticated users).

The following navigation items are available on all pages:
  * Home -> index.html - Visible to all
  * Login -> login.html - Visible to logged out users
  * Register -> signup.html - Visible to logged out users
  * Logout -> logout.html - Visible to logged in users
  * Suggest an event -> suggestion.html - Visible to logged in users

The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices. 

![Navbar](docs/readme_images/navbar.png)

There is a Welcome message on the right side of the navigation bar, which is moved to the bottom on mobile devices burger views:

![Burger_Menu](docs/readme_images/burger_nav.png)

``USER STORY - As a Site User I can view a list of events with a short preview, so that I can select one to read about``

``USER STORY - As a Site User I can view a paginated list of events, so that I can easily select an event to view``

Implementation:

**Home Page**

The home page contains a hero carousel, depicting members of the staff, a local farmer with the picturesque hill behind the dust, and some characters of the movie "La grande guerra del Salento", shot in Supersano. These will give the user an idea about the cultural content available on the website. Each image contains a different message that adds up to the user's initial assumption about the website content and objective.

![Hero Image](docs/readme_images/hero-img.png)

Under the carousel, users can see the list of events that are actually confirmed and scheduled. Pagination options limit them to 6 per page. Example without authentication below:

![List_of_Events](docs/readme_images/list_public.png)

This is the version of the same list when users are authenticated and marked as part of the staff:

![List_of_Events_Staff](docs/readme_images/list_auth.png)

Buttons "Update" and "Delete" can be viewed attached to each event by staff users only.

**Footer**

A footer has been added to the bottom of the site, this contains Youtube, Instagram, and Facebook links so that users can follow the restaurant on social media if they want to keep up to date with updates. These icons have aria-labels added to ensure users with assistive screen reading technology know what the purpose of the links are for. They also open in new tabs as they lead users away from the site.

At the bottom, presence on social networks can be found:

![Footer](docs/readme_images/social_footer.png)

``USER STORY - As a Site User I can register an account, so that I can leave comments and my intention to join events``

**Registration**

If visiting users wish to add their participation to events, comment, or suggest new ideas for future events, it can be done by registering first. Once the link "Register" on the nav menu is clicked, the public user is redirected to the registration form:

![Registration](docs/readme_images/reg_page.png)

The user will need to enter a unique username to sign up successfully, as well as an acceptable password with minimum security requirements - i.e. it cannot be set to "temporary".

``USER STORY - As a Site User I can click on an event in the home page, so that I can read about details: whereabouts, whenabouts, etc.``

**View Event Details**

Public users can click on events and view their dedicated page: The small poster picture employed in the home page is here extended to a larger image combined with the event details:

![Event_details](docs/readme_images/Event_details_overview.png)

Event information will include date, time, short description (text preview/summary), description, picture.

``USER STORY - As a Site user I can join / remove participation to single events, so that I can let other users know that I am going to join an event``

**Join/Unjoin Event Button**

Authenticated users can let the staff know that they are going to join the event, by clicking/tapping on the related icon wit the "+" (plus) sign:

![Join_Event_Button](docs/readme_images/join_event_button.png)

As soon as the button is clicked, it changes its form to the same icon, but with the sign "✓" (check) and a message confirming participation just beneath:

![Unjoin_Event_Button](docs/readme_images/unjoinevent.png)

To unjoin the event, the user will just need to re-click or re-tap.

``USER STORY - As a Site user I can leave comments on single event pages, so that I can interact with other site users``

**Leaving Comments**

Authenticated users can leave comments: Staff users get their comments approved as soon as they submit them, standard users need to wait for approvals instead:

![Approval](docs/readme_images/approval_banner.png)

While comments are styled as follows when these have been approved:

![Approved_Comments](docs/readme_images/Comment_area.png)

A badge confirms the username of the person who is leaving a comment, while the icon about comments indicate the quantity of those approved and listed beneath it.

``USER STORY - As a site user I can receive a notification banner at the top when an action was performed/processed successfully, so that I can have certainty of submitted data``

**Notifications and Banners**

Users will get notifications based on their actions on the website. Integrated features - for the time being - include authentication and event-creation-editing validation. Examples as follows:

![Authentication](docs/readme_images/Auth_logout.png)

![Event submission](docs/readme_images/Event_submission.png)

``USER STORY - As a Site user I can suggest an event, so that I can feel involved in the local community``

**Event creation and validation**

All authenticated users can suggest events and submit them for review to the staff. There are a few requirements to submit a request successfully:

* The chosen date should not overlap with other events 
* The chosen date should allow 14 days to the staff from the time of submission, to let them assess feasibility and organize everything on time

Once the authenticated user clicks/taps on the navigation menu item "Suggest an event", they are redirected to a new page, where to submit the suggestion:

![Navbar](docs/readme_images/navbar.png)

![Suggest form](docs/readme_images/suggest_event.png)


``USER STORY - As a site authenticated user I can suggest events and get warnings when I am trying to submit an overlapping event, so that I get more chances to see my suggestion approved``

Once the form is ready with all data (compulsory fields are marked with an asterisk), the user can click on the button "Submit" and wait for the outcome of their suggestion. The latter will be notified by the banners pasted above, however, users will also come across warnings instructing on minimum requirements to successfully submit an event. Trying to suggest an event the same day of one of those listed in the home page will return a warning banner.

``USER STORY - As a site admin or privileged user (part of the staff) I can edit events, so that I can organize them better.``

``USER STORY - As a site admin or privileged user (part of the staff) I can delete events, so that get rid of unwanted records in the database.``

**Event manipulation**

Staff users can edit or delete events:

* Buttons "Edit" and "Delete" show up next to each event within the home page, if the user is authenticated and is part of the staff.
* Editing the date of the event will require to allow at least 5 days to the staff, to let them assess the feasibility and further arrangements.
* Deletion request will be successful only upon confirmation.

![Edit and Delete](docs/readme_images/Edit_Delete.png)

``USER STORY - As a Site Admin I can create, read, update posts, so that I can manage my blog content.``

**Admin CRUD functionality**

Currently, the CRUD functionality is granted to the admin/staff user via separate areas on the website:

* "Suggest an Event" lets all authenticated users create events
* The home page lets all users see the list of scheduled events
* Edit buttons let the staff edit details of the events
* Delete buttons let the staff delete events from the database, upon confirmation

### Features Left To Implement

In the future, some obvious adjustments both in technical and UX terms will be applied. For example:
* Admins/Staff will have a dedicated dashboard where to perform all CRUD actions, without the need of moving from page to page;
* Thinking about deleting data from the database, events can be cancelled, rather than deleted, hence, the feature will be added and prioritized, to also let users know which events have been cancelled;
* Timestamps and time submission will be optimized to improve the UX and readibility. The current project focused on understanding and implementing essential CRUD notions, rather than researching Jinja adaptations of specific features;
* The general appearance will be better developed;
* Notification banners will disappear automatically after 6 seconds, as originally set, however, the function was removed when - after several attempts of refactoring - the .close()-related error message persisted within the browser console. In this sense, troubleshooting of this console error is postponed.
* Users will have the chance to review their submissions, even though limited permissions will be granted, to ease the administration effort in case of short notices;
* Information about location won't be added to the current Event model, even though initially taken into consideration: The NGO is based in Supersano, it arranges events located always in a limited area, points of interest are widely known among local people, hence, defining the location within the description will suffice.

``USER STORY - As an admin user I can leave internal notes about events, so that I can come up with suggestions about future events``

This user story is not currently implemented, as it was marked as "Could have". It would be nice having a sort of internal interactions within single event overviews, to let the staff discuss about to-dos etc. This will not affect the current models/tables of the database, that were designed with this feature in mind. The field "audience" will distinguish the target of the comments between "admin" and "everyone" (default).

## The-Skeleton-Plane

### Wireframes

The website was designed with responsiveness in mind, however, wireframing was meant to get a general idea of the first impression, hence, mobile wireframing is not available. There are tiny errors within the menu items depicted, as authenticated sessions change the content of the navbar.

* Home Page

![Home Page](docs/readme_images/Wireframing/Home_page.png)

* Event Overview

![Event Overview](docs/readme_images/Wireframing/Event_Overview.png)

* Event Update

![Event Update](docs/readme_images/Wireframing/Event_Update.png)

* Event Deletion

![Event Deletion](docs/readme_images/Wireframing/Event_deletion.png)

* Event Suggestion

![Event Suggestion](docs/readme_images/Wireframing/Event_suggestion.png)

* Account Registration

![Account Registration](docs/readme_images/Wireframing/Account_Registration.png)

* Account Logout

![Account Logout](docs/readme_images/Wireframing/Account_Logout.png)

There are obvious tiny changes in the final product. Errors 403, 404, 500 pages were designed following the same layout of the Event Deletion wireframe.

### Database-Design

The database was designed to allow CRUD functionality to be available to registered users, when signed in. The user model plays a crucial role in handling authentication, provided by Django. Enhanced user permissions were designed based on the user.is_staff boolean field, as it is intended to distinguish the admin role as user.is_superuser from staff members as user.is_staff. This way, future changes may for example grant special permissions to admins that intend to delete records from the database (superuser), instead of just cancelling an event (staff). Further information about this model can be found on [Django](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/).

The Event model includes information about the User who created/suggested the event, linked via a one-to-many relationship to the User model - as a foreign key then - mentioned above, under the field "author". Moreover, if one author is being deleted from the database, events created by that author will be deleted as well. 

The "joins" field returns information about the users that clicked/tapped on the join button, to confirm they will join a given events. In this sense, "join" is a many-to-many field, because an event can have multiple "joins" left by multiple users.

The Comment model presents a foreign key like the one above, in relation to the event it has been attached to. If an event is being deleted from the database, the attached comments will be deleted too. Finally, the field "audience" will determine the audience that the comment is meant for, however, as specified above, this feature will be implemented in the future.

Entity relationship diagram was created using [LucidChart](https://lucid.app/) and shows the schemas for each of the models and how they are related.

![Models](docs/readme_images/Models.png)