# HireTrack

HireTrack is a full-stack Django web application designed to help users organise and track their job applications throughout the recruitment process.

Users can create an account, securely log in, add and manage job applications, update application statuses, and monitor their job search through a personalised dashboard.

---

## 🔗 Live Site  
https://hiretrackerheroku-98519fb8f772.herokuapp.com/

## 🔗 GitHub Repository  
https://github.com/queldx74/HireTrack

---

# Table of Contents
- [Project Overview](#project-overview)
- [Project Goals](#project-goals)
- [User Experience](#user-experience)
  - Target Audience  
  - User Goals  
  - User Stories  
- [Design](#design)
  - Wireframes  
  - Mockups  
  - Design Rationale  
  - Responsive Design  
  - Accessibility  
- [Agile Development](#agile-development)
- [Features](#features)
- [Data Model](#data-model)
- [CRUD Functionality](#crud-functionality)
- [Authentication and Authorization](#authentication-and-authorization)
- [Forms and Validation](#forms-and-validation)
- [User Feedback and Notifications](#user-feedback-and-notifications)
- [Business Logic](#business-logic)
- [Technologies Used](#technologies-used)
- [Testing Summary](#testing-summary)
- [Security](#security)
- [Deployment](#deployment)
- [AI Usage](#ai-usage)
- [Version Control](#version-control)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

---

# Project Overview

HireTrack provides job seekers with a simple and organised way to manage their job applications.  
Instead of relying on spreadsheets or notes, users can store applications in one location and track progress through different recruitment stages.

The application is built using Django and uses a persistent PostgreSQL database.

---

# Project Goals

HireTrack aims to:

- Allow users to securely register, log in, and log out  
- Allow users to create, read, update, and delete job applications  
- Ensure users can only access their own data  
- Track applications through recruitment stages  
- Provide a dashboard overview  
- Provide clear feedback after database changes  
- Deliver an accessible, responsive interface across all devices  

---

# User Experience

## Target Audience
Job seekers applying for multiple roles who need a central place to organise and monitor applications.

## User Goals
Users should be able to:

- Record new job applications quickly  
- View all applications  
- Track progress  
- Update application status  
- Delete applications  
- Access data securely  
- Understand job-search progress via dashboard  

## User Stories

### Authentication
- As a new user, I want to register for an account.  
- As a registered user, I want to log in securely.  
- As a logged-in user, I want to log out.

### Job Applications
- As a user, I want to create a job application.  
- As a user, I want to view my applications.  
- As a user, I want to view an individual application.  
- As a user, I want to edit an application.  
- As a user, I want to delete an application.  
- As a user, I want to update an application's status.

### Privacy
- As a user, I want my applications to remain private.

### Dashboard
- As a user, I want to see a summary of my applications.

### Filtering
- As a user, I want to filter applications by status.

---

# Design

## Wireframes  
[Balsamiq desktop wireframes](docs/wireframes/desktop-wireframe.png)
[Balsamiq tablet wireframes](docs/wireframes/tablet-wireframe.png)
[Balsamiq mobile wireframes](docs/wireframes/mobile-wireframe.png)

## Wireframes

The initial wireframes for HireTrack were created in Balsamiq during the
planning stage of the project. Their purpose was to establish the basic
structure, navigation and user journey before development began.

The final application differs from these original wireframes. During
development, the interface and functionality evolved as the project was
tested across different screen sizes and additional requirements were
implemented.

Some of the main changes from the original wireframes include:

- The original mobile-style bottom navigation was replaced with a responsive
  Bootstrap navigation bar that works across desktop, tablet and mobile
  devices.
- The original Dashboard and Applications concepts were developed into the
  final application dashboard, which provides application information,
  status summaries and filtering in one area.
- The original Profile concept evolved into Account Settings, focusing on
  account information, email and password management, and account deletion.
- The Add Application form was expanded as the data model developed to
  capture more useful information about each job application.
- Statistics functionality was introduced during development to give users
  an overview of their application progress.
- Role-based administration was added to support the HireTrack Admin
  functionality and was not part of the initial wireframes.

These differences demonstrate the development of the project from the
initial design concept to the final implementation. The wireframes were
used as a starting point rather than as a fixed specification.



## Mockups  
### Refined Design Mockups

Following the initial wireframing stage, more detailed mockups were created
in Figma to develop the visual direction of HireTrack.

The Figma designs introduced the colour scheme, typography, navigation,
cards, application tables and other interface elements that are much closer
to the final implementation, while retaining the core user
journey established during the initial planning stage.

#### Home Page Mockup

The refined home page mockup established the public-facing design, including
the HireTrack branding, feature overview, registration call-to-action and
step-by-step introduction to the application.
 Home page
![HireTrack home page mockup](docs/mockup/mockup-homepage.png)    

#### Dashboard Mockup

The refined dashboard mockup introduced the application summary cards,
status filtering, application table and primary application management
actions used in the final interface.

![HireTrack dashboard mockup](docs/mockup/mockup-dashboard.png)
- Dashboard mockup  

#### Design Changes During Development

The final dashboard remained close to the refined mockup, with some changes
made during implementation to improve the presentation of information.

One change was the removal of the **Rejected** summary card from the top
section of the dashboard. The final design keeps the three progress-focused
cards — **Applied, Interviews and Offers** — alongside the **Total
Applications** summary.

Rejected applications are still fully supported and can be viewed and
filtered within the application list. Removing the Rejected card from the
summary area allowed the top of the dashboard to focus on positive progress
through the job application process while keeping rejection information
available when required.

### Design Rationale

HireTrack was designed to provide a clear and straightforward way for users
to manage their job applications without overwhelming them with information.

A dark navy and green colour scheme was chosen to give the application a
professional appearance while providing clear contrast for navigation,
buttons and important actions. Bootstrap components and a consistent card
layout were used throughout the application to maintain a familiar and
cohesive interface.

The dashboard was designed as the main focus for authenticated users. It
provides an immediate overview of application progress before presenting
the individual applications below. Status filtering allows users to quickly
find applications at different stages of their job search.

The final dashboard was refined from the Figma mockup. The Rejected summary
card was removed so that the three cards beside Total Applications focus on
progress through the application process: Applied, Interviews and Offers.
Rejected applications remain available through the application list and
status filters.

Responsive design was also an important consideration. Layouts were adapted
for desktop, tablet and mobile devices so that application information and
actions remain accessible at different screen sizes.

The design developed from initial low-fidelity Balsamiq wireframes into
higher-fidelity Figma mockups and finally the implemented Django
application. Changes made during development were based on usability,
responsive behaviour and the functionality introduced as the project
developed.

### Typography
HireTrack uses **Inter** for readability and professional appearance.

### Colour Palette
- Navy `#1a3557` — navigation, headings, buttons  
- Dark navy `#15294a` — borders  
- Green `#2e9e62` — primary CTA  
- Background `#f5f7fa`  
- White `#ffffff`

### Status Colours
| Status     | Background | Text | Border |
|------------|------------|------|--------|
| Saved      | #f0f4ff    | #3b4fa8 | #c7d2fe |
| Applied    | #eff6ff    | #1d4ed8 | #bfdbfe |
| Interview  | #fffbeb    | #92400e | #fde68a |
| Offer      | #f0fdf4    | #166534 | #bbf7d0 |
| Rejected   | #fef2f2    | #991b1b | #fecaca |

### Spacing & Layout
Generous whitespace, consistent spacing, and card-based grouping improve readability.

### Navigation
Clear navigation with active page highlighting.

## Responsive Design
HireTrack adapts across desktop, tablet, and mobile using Flexbox, Grid, and media queries.

[desktop-hompepage](docs/screenshots-desktop/desktop-homepage.png)
[tablet-dashboard](docs/screenshots-tablet/ipadpro13-dashboard.png)
[mobile-applications](docs/screenshots-mobile/iphone-se-dashboard.png)


## Accessibility
HireTrack was developed with accessibility and WCAG best practices in mind.

- Semantic HTML  
- Logical heading hierarchy  
- Labelled forms  
- Colour contrast  
- Keyboard navigation  
- Visible focus states  
- Alt text  
- Status communicated via colour + text  

Accessibility testing is documented in TESTING.md.

---

# Agile Development

HireTrack was developed using Agile methodology, with GitHub Projects used
to organise and track the development of the application.

The project began with five core user stories covering registration, login,
authorisation, adding job applications and tracking job applications. As
development progressed, additional requirements and functionality were
identified and incorporated into the project.

## GitHub Project Board

The GitHub Project board was used to track user stories and development
tasks throughout the project.

![HireTrack GitHub Project Board](docs/images/project-board-screenshot.png)

[View the HireTrack GitHub Project Board](https://github.com/users/queldx74/projects/10)

## Workflow

Project items were tracked through the following stages:

- **To-do** - Work ready to be started.
- **In Progress** - Functionality currently being developed.
- **Done** - Completed functionality.
- **Backlog** - Requirements or ideas not currently being worked on.

## MoSCoW Prioritisation

MoSCoW prioritisation was used to classify requirements according to their
importance to the current release of HireTrack.

### Must Have

- User registration
- Login and logout
- User authorisation
- User-specific application data
- Create job applications
- View job applications
- Edit job applications
- Delete job applications
- Responsive interface

### Should Have

- Application status tracking
- Filtering applications by status
- Application statistics
- Account settings
- Password management

### Could Have

- HireTrack Admin Dashboard
- Admin user management
- Additional application analytics
- Application search

### Won't Have (This Release)

The following features were identified as possible future developments but
were outside the scope of the current release:

- Email reminders and notifications
- CV/document uploads
- Job board/API integration
- More advanced analytics

---

# Features

## User Registration
[Register](docs/feature-images/register.png)
User registration allows new users to create an account by providing a username, email address, and password. The registration form includes validation to ensure that all required fields are completed and that the email address is in a valid format. Upon successful registration, users are redirected to the login page to access their new account.


## Login and Logout
[Login](docs/feature-images/login.png)
[Logout](docs/feature-images/logout.png)
Login functionality allows registered users to securely access their accounts using their email and password. The login form includes validation to ensure that the provided credentials are correct. Upon successful login, users are redirected to their dashboard, where they can manage their job applications. Logout functionality is in the dropdown menu of the user profile, allowing users to securely end their session and return to the public-facing home page.

## Dashboard
[Dashboard](docs/feature-images/dashboard.png)
Dashboard functionality provides users with an overview of their job applications, including summary cards for total applications, applications in progress, interviews, and offers. The dashboard also includes a table listing all job applications, with options to view, edit, or delete each application. Users can filter applications by status to quickly find specific records.

## Create Application
[Create Application](docs/feature-images/create-application.png)
Creating a new job application allows users to input relevant details such as job title, company, location, date applied, status, job URL, salary, and notes. The form includes validation to ensure that all required fields are completed and that the data is in the correct format. Upon successful submission, the new application is added to the user's list of applications and a confirmation message is displayed.


## Applications Details
[View Applications](docs/feature-images/view-application.png)
All job applications are displayed in a table format, allowing users to quickly scan through their records. Each application entry includes key details such as job title, company, location, date applied, and status. Users can click on an individual application to view more detailed information.

## Edit Application
[Edit Application](docs/feature-images/edit-application.png)
Users can edit existing job applications by clicking the edit button next to each application in the table. The edit form allows users to update any of the application details, including job title, company, location, date applied, status, job URL, salary, and notes. The form includes validation to ensure that all required fields are completed and that the data is in the correct format. Upon successful submission, the updated application is saved and a confirmation message is displayed.


## Delete Application
[Delete Application](docs/feature-images/delete-application.png)
Users can delete existing job applications by clicking the delete button next to each application in the table. A confirmation dialog will appear to ensure that the user wants to proceed with the deletion. Upon successful deletion, the application is removed from the user's list of applications and a confirmation message is displayed.

## Status Filtering
[Status Filtering](docs/feature-images/status-filtering.png)
Users can filter their job applications by status using a dropdown menu on the dashboard. This allows users to quickly view applications that are in progress, have been interviewed, received offers, or have been rejected. The filtered results are displayed in the application table, making it easy for users to manage their job search effectively.


## Account Settings
[Account Settings](docs/feature-images/account-settings.png)
Account settings allow users to manage their account information, including updating their email address and password. Users can also delete their account if they wish to do so. The account settings page includes validation to ensure that all required fields are completed and that the data is in the correct format. Upon successful submission, the updated account information is saved and a confirmation message is displayed.

## HireTrack Admin Dashboard
[Admin Dashboard](docs/feature-images/admin-dashboard.png)
The HireTrack Admin Dashboard provides administrative users with an overview of all registered users and their job applications. Admin users can view, edit, and delete user accounts and applications, as well as manage user permissions. The admin dashboard includes summary cards for total users, total applications, and other relevant statistics. Access to the admin dashboard is restricted to users with administrative privileges.


## User Feedback

Django messages provide users with confirmation and feedback following
important actions.

*(Insert screenshot if required)*

*(Insert screenshots for each feature)*

### User Registration  
### Login & Logout  
### Dashboard  
### Create Application  
### View Applications  
### Application Details  
### Edit Application  
### Delete Application  
### Status Filtering  
### User Feedback (messages)

---

# Data Model

## ERD Diagram  
*(Insert ERD image here)*

Based on your uploaded ERD:

### User Table
- id  
- username  
- email  
- password  
- is_superuser  

### JobApplication Table
- id  
- user_id (FK → user.id)  
- job_title  
- company  
- location  
- date_applied  
- status  
- job_url  
- salary  
- notes  

### Relationship
A **User** can have **many JobApplications**.  
Each JobApplication belongs to exactly one User.

---

# CRUD Functionality

| Operation | HireTrack Functionality |
|----------|--------------------------|
| Create   | Add new job application |
| Read     | View list + details |
| Update   | Edit application |
| Delete   | Delete with confirmation |

Access controls ensure users can only modify their own records.

---

# Authentication and Authorization

HireTrack uses Django authentication.

Documented features:

- Registration  
- Login  
- Logout  
- Login state reflection  
- Protected pages  
- User-specific data  
- Admin access via Django admin  
- Permission checks preventing cross-user access  

---

# Forms and Validation

### Registration Form  
### Job Application Form  
### Edit Application Form  

Validation includes:

- Required fields  
- Date validation  
- Status validation  
- Error messages displayed clearly  

*(Insert screenshots of validation errors)*

---

# User Feedback and Notifications

HireTrack uses Django’s messages framework.

Examples:

- Application created  
- Application updated  
- Application deleted  
- Invalid form submission  
- Unauthorised access  

*(Insert screenshots of messages)*

---

# Business Logic

Custom Python logic includes:

- Filtering applications by logged-in user  
- Filtering by status  
- Dashboard statistics  
- Permission checks  
- Conditional rendering  
- Query optimisation  

---

# Technologies Used

### Languages
- Python  
- HTML5  
- CSS3  
- JavaScript (minimal)

### Frameworks
- Django  
- Bootstrap  

### Database
- PostgreSQL (production)  
- SQLite (development)

### Design Tools
- Balsamiq  
- Figma  

### Development Tools
- VS Code  
- Git  
- GitHub  

### Deployment
- Heroku  

---

# Testing Summary

Full testing documentation is in **TESTING.md**.

Summary:

- Manual functional testing  
- Authentication testing  
- CRUD testing  
- Permission testing  
- Form validation testing  
- User story testing  
- Automated Django tests  
- Responsive testing  
- Browser testing  
- Accessibility testing  
- HTML validation  
- CSS validation  
- Python validation  
- Bug documentation  

---

# Security

HireTrack implements:

- Environment variables for sensitive settings  
- SECRET_KEY not committed  
- `.gitignore` for local files  
- DEBUG=False in production  
- Allowed hosts configured  
- CSRF protection  
- User-specific access controls  
- Django password hashing  

---

# Deployment

## Local Development

Clone repository:
```bash
git clone https://github.com/queldx74/HireTrack
