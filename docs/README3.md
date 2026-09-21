HireTrack
HireTrack is a full-stack Django web application designed to help users organise and track their job applications throughout the recruitment process.

Users can create an account, securely log in, add and manage job applications, update application statuses, and monitor their job search through a personalised dashboard.

Live Site: https://hiretrackerheroku-98519fb8f772.herokuapp.com/  
GitHub Repository: https://github.com/queldx74/HireTrack

Table of Contents
Project Overview

Project Goals

User Experience

Target Audience

User Goals

User Stories

Design

Wireframes

Mockups

Design Rationale

Responsive Design

Accessibility

Agile Development

Features

Data Model

CRUD Functionality

Authentication and Authorization

Forms and Validation

User Feedback and Notifications

Business Logic

Technologies Used

Testing Summary

Security

Deployment

AI Usage

Version Control

Credits

Acknowledgements

Project Overview
HireTrack was created to provide job seekers with a simple and organised way to manage their job applications.

Instead of relying on spreadsheets, notes, or several different websites, users can store their applications in one location and monitor the progress of each application through different recruitment stages.

The application is built using Django and uses a persistent database to store user and job application information.

Project Goals
The main goals of HireTrack are to:

Allow users to securely register, log in, and log out.

Allow users to create, read, update, and delete job applications.

Ensure users can only access and manage their own application data.

Allow users to track applications through different recruitment stages.

Provide a dashboard showing an overview of the user's job search.

Provide clear feedback after database changes.

Provide an accessible and responsive interface across desktop, tablet, and mobile devices.

User Experience
Target Audience
HireTrack is primarily designed for job seekers who are applying for several positions and want a central location to organise and monitor their job applications.

User Goals
Users should be able to:

Record a new job application quickly.

View all current applications.

See which applications have reached interview or offer stage.

Update an application when its status changes.

Remove applications they no longer require.

Access their application information securely.

Understand the current state of their job search from the dashboard.

User Stories
Authentication
As a new user, I want to register for an account so that I can use HireTrack.

As a registered user, I want to log in so that I can securely access my applications.

As a logged-in user, I want to log out so that my account remains secure.

Job Applications
As a user, I want to create a job application so that I can record jobs I have applied for.

As a user, I want to view my applications so that I can monitor my job search.

As a user, I want to view an individual application so that I can see its full information.

As a user, I want to edit an application so that I can keep its information up to date.

As a user, I want to delete an application so that I can remove records I no longer need.

As a user, I want to update an application's status so that I can track its progress.

Privacy
As a user, I want my applications to remain private so that other users cannot access or modify my job-search information.

Dashboard
As a user, I want to see a summary of my applications so that I can quickly understand my job-search progress.

Filtering
As a user, I want to filter applications by status so that I can quickly locate applications at a particular stage.

Design
The design process began with low-fidelity wireframes created in Balsamiq before progressing to a higher-fidelity Figma mockup.

This process helped establish the application's structure, navigation, content hierarchy, visual appearance, and responsive behaviour before development.

Wireframes
Wireframes were created using Balsamiq.

They were used to plan:

Page structure

Navigation

Forms

Dashboard layout

CRUD interactions

Content hierarchy

Responsive behaviour

Desktop
[Looks like the result wasn't safe to show. Let's switch things up and try something else!]

Tablet
[Looks like the result wasn't safe to show. Let's switch things up and try something else!]

Mobile
[Looks like the result wasn't safe to show. Let's switch things up and try something else!]

Mockups
A higher-fidelity mockup was created in Figma to establish the final visual direction of HireTrack.

Dashboard Mockup
(Insert dashboard mockup image here)

Design Rationale
Typography
Inter is used throughout HireTrack.

Weights:

400 — Regular

500 — Medium

600 — Semibold

700 — Bold

Colour Palette
Primary navy: #1a3557

Dark navy: #15294a

Accent green: #2e9e62

Background: #f5f7fa

White: #ffffff

Status Colours
Status	Background	Text	Border
Saved	#f0f4ff	#3b4fa8	#c7d2fe
Applied	#eff6ff	#1d4ed8	#bfdbfe
Interview	#fffbeb	#92400e	#fde68a
Offer	#f0fdf4	#166534	#bbf7d0
Rejected	#fef2f2	#991b1b	#fecaca


Status information is communicated using both colour and written labels.

Spacing and Layout
Generous whitespace and consistent spacing are used to prevent visual clutter. Related information is grouped into cards and sections.

Navigation
Navigation provides direct access to:

Dashboard

Applications

Add Application

User account

Logout

The currently active page is visually highlighted.

Responsive Design
HireTrack is designed for desktop, tablet, and mobile devices.

On larger screens, dashboard statistics are displayed horizontally and applications are presented in a table.

On smaller screens, components wrap or stack where necessary, and application information may switch from a table layout to cards.

Accessibility
Accessibility considerations include:

Semantic HTML

Logical heading hierarchy

Clearly labelled forms

Good colour contrast

Keyboard-accessible controls

Visible focus states

Descriptive links and buttons

Status communicated through both colour and text

Appropriate alternative text

Full accessibility testing is documented in TESTING.md.

Agile Development
HireTrack was developed using Agile methodology.

GitHub Projects was used to manage:

User stories

Acceptance criteria

Implementation tasks

Development progress

Project Board: (Add GitHub Project link)

Typical workflow:

To Do

In Progress

Testing

Done

MoSCoW Prioritisation
Must Have
Registration

Login/logout

Create application

Read applications

Edit application

Delete application

User-specific data

Persistent database

Responsive interface

Should Have
Application statuses

Filtering

Dashboard statistics

Could Have
Search

Additional statistics

Additional application fields

Won't Have This Release
Social networking

Chat

AI recommendations

Push notifications

Job-board integrations

Features
User Registration
[Describe completed feature and add screenshot.]

Login and Logout
[Describe completed feature.]

Dashboard
[Describe statistics and application overview.]

Create Job Application
[Describe functionality.]

View Applications
[Describe application list.]

Application Details
[Describe detail page.]

Edit Application
[Describe update functionality.]

Delete Application
[Describe confirmation and deletion.]

Status Filtering
[Describe filtering functionality.]

User Feedback
[Describe success/error messages.]

Future Features
Possible future improvements include:

Application search

Interview dates

Reminders

Application history

Additional dashboard analytics

Improved reporting

Data Model
Database Design
HireTrack uses a relational database to store application and user information.

[Looks like the result wasn't safe to show. Let's switch things up and try something else!]

The ERD shows:

A User table with fields: id, username, email, password, is_superuser.

A JobApplication table with fields: id, user_id, job_title, company, location, date_applied, status, job_url, salary, notes.

A one-to-many relationship: one user can have many job applications.

JobApplication Model
Field	Purpose
User	Links the application to its owner
Job Title	Position being applied for
Company	Employer
Location	Job location
Date Applied	Application date
Status	Current recruitment stage
Job URL	Original vacancy link
Salary	Salary information where available
Notes	Additional information


Model Relationships
A user can own multiple job applications, while each job application belongs to one user.

CRUD Functionality
Operation	HireTrack Functionality
Create	Create a job application
Read	View applications and application details
Update	Edit application information or status
Delete	Delete an application after confirmation


Access controls ensure users can only modify records they are authorised to manage.

Authentication and Authorization
HireTrack uses Django authentication.

Documented:

Registration

Login

Logout

Login state reflection

Protected pages

Unauthenticated redirects

User-specific data protection

Admin permissions

HireTrack prevents one user from accessing another user's application records by filtering queries by the logged-in user and enforcing permission checks in views.

Forms and Validation
Registration Form
[Describe fields and validation.]

Job Application Form
[Describe fields and validation.]

Edit Application Form
[Describe editing behaviour.]

Validation Feedback
Validation errors are displayed near the relevant fields with clear messages.

User Feedback and Notifications
HireTrack provides clear feedback when data changes.

Examples:

Application successfully created.

Application successfully updated.

Application successfully deleted.

Invalid form submission.

Unauthorised access attempt.

Django’s messages framework is used to display these notifications.

Business Logic
Custom Python logic includes:

Filtering applications by logged-in user

Filtering by status

Calculating dashboard statistics

Permission checks

Conditional logic

Database queries

Technologies Used
Languages
Python

HTML5

CSS3

JavaScript

Frameworks and Libraries
Django

Bootstrap

Database
PostgreSQL

SQLite

Design
Balsamiq

Figma

Development
VS Code

Git

GitHub

Deployment
Heroku

Testing Summary
HireTrack was tested throughout development for functionality, data management, responsiveness, accessibility, authentication, permissions, and usability.

Detailed test procedures, results, validation evidence, and bug documentation are contained in TESTING.md.

Summary:

Manual functional testing

Automated Django testing

User story testing

Authentication and permission testing

CRUD testing

Responsive testing

Accessibility testing

HTML validation

CSS validation

Python/PEP 8 validation

JavaScript testing (if applicable)

Bug documentation

Security
Security measures include:

Environment variables for sensitive settings

No secret keys committed to GitHub

.gitignore used for sensitive/local files

DEBUG=False in production

Authentication required for protected functionality

User-specific access controls

Django password handling

CSRF protection

Server-side validation

Deployment
Local Development
Clone Repository
bash
git clone https://github.com/queldx74/HireTrack
Create Virtual Environment
bash
python -m venv .venv
Activate Virtual Environment
(Add Windows/macOS/Linux commands as appropriate.)

Install Dependencies
bash
pip install -r requirements.txt
Apply Migrations
bash
python manage.py migrate
Run Development Server
bash
python manage.py runserver
Environment Variables
Variable	Purpose
SECRET_KEY	Django secret key
DATABASE_URL	Production database connection


Heroku Deployment
Steps:

Create the Heroku application.

Configure the PostgreSQL database.

Configure environment variables.

Configure Django production settings.

Deploy the application.

Run migrations.

Verify application functionality.

Confirm DEBUG=False.

AI Usage
Code Creation
Describe where AI supported code creation and how generated code was reviewed or modified.

Debugging
Describe examples where AI helped identify and resolve bugs.

Performance and UX
Describe where AI contributed to UX, accessibility, or performance improvements.

Automated Tests
Document how GitHub Copilot was used to assist with Django unit tests and what changes were made.

Reflection
Reflect briefly on:

Where AI saved time

Where AI output needed modification

How generated code was verified

What was learned

How AI affected the development workflow

Version Control
Git and GitHub were used throughout development.

Commits were made regularly to document incremental development.

Examples:

Add responsive HireTrack wireframes

Add HireTrack dashboard mockup

Create JobApplication model

Add registration functionality

Add application CRUD functionality

Add dashboard statistics

Add responsive styling

Add permission checks

Add Django tests

Configure production deployment

Update project documentation

Credits
Code
[List external tutorials, documentation, snippets, etc.]

Media
[List icons/images requiring attribution.]

Font
HireTrack uses Inter from Google Fonts.

Acknowledgemen