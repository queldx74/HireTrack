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
*(Insert images here)*  
- Desktop wireframes  
- Tablet wireframes  
- Mobile wireframes  

## Mockups  
*(Insert Figma mockups here)*  
- Dashboard mockup  
- Application list mockup  
- Forms mockup  

## Design Rationale

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

*(Insert responsive screenshots here)*

## Accessibility
HireTrack follows WCAG guidelines:

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

HireTrack was developed using Agile methodology with GitHub Projects.

### GitHub Project Board  
*(Insert screenshot here)*  
Link: https://github.com/queldx74/HireTrack/projects

### Workflow
- To Do  
- In Progress  
- Testing  
- Done  

### MoSCoW Prioritisation
**Must Have:**  
Registration, Login, CRUD, User-specific data, Responsive design  

**Should Have:**  
Statuses, Filtering, Dashboard statistics  

**Could Have:**  
Search, Additional analytics  

**Won’t Have:**  
Social features, Chat, Push notifications  

---

# Features

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
