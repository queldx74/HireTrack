TESTING.md
HireTrack Testing Documentation
This document contains the full testing procedures and results for HireTrack, including manual testing, automated testing, validation, accessibility checks, and bug documentation.

HireTrack was tested throughout development to ensure correct functionality, secure data handling, responsiveness, accessibility, and code quality.

Table of Contents
Testing Strategy

Manual Functional Testing

Authentication Testing

CRUD Testing

Permission and Security Testing

Form Validation Testing

User Story Testing

Automated Testing

Responsive Testing

Browser Testing

Accessibility Testing

HTML Validation

CSS Validation

Python Validation

JavaScript Testing

Bugs

Final Testing Summary

Testing Strategy
HireTrack was tested using a combination of:

Manual functional testing

Automated Django unit tests

Validation tools (HTML, CSS, Python)

Accessibility tools

Browser/device testing

Testing focused on:

Authentication

CRUD operations

Permissions

Form validation

Dashboard logic

Responsive behaviour

Accessibility

Code quality

Manual Functional Testing
Navigation
Test	Expected Result	Actual Result	Pass/Fail
Open homepage	Homepage loads correctly		
Click Dashboard	Dashboard loads		
Click Applications	Application list loads		
Click Add Application	Form loads		
Click Logout	User is logged out		


Authentication Testing
Registration
Test	Expected Result	Actual Result	Pass/Fail
Register with valid information	Account is created		
Missing required field	Validation error displayed		
Duplicate username	Validation error displayed		
Mismatched passwords	Validation error displayed		


Login
Test	Expected Result	Actual Result	Pass/Fail
Correct credentials	User is logged in		
Incorrect password	Error displayed		
Invalid username	Error displayed		
Blank username	Error displayed		


Logout
Test	Expected Result	Actual Result	Pass/Fail
Logged-in user selects Logout	Session ends		
Visit protected page after logout	Redirect to login		


CRUD Testing
Create
Test	Expected Result	Actual Result	Pass/Fail
Submit valid application	Application created		
Application belongs to logged-in user	Correct user stored		
Missing required field	Validation error displayed		
Successful creation	Success message displayed		


Read
Test	Expected Result	Actual Result	Pass/Fail
Open application list	User's applications displayed		
Open application detail	Correct application displayed		
User with no applications	Empty state displayed		


Update
Test	Expected Result	Actual Result	Pass/Fail
Edit application	Existing data displayed		
Save valid changes	Database updated		
Change status	New status displayed		
Submit invalid data	Validation error displayed		
Successful update	Success message displayed		


Delete
Test	Expected Result	Actual Result	Pass/Fail
Select Delete	Confirmation displayed		
Cancel deletion	Application remains		
Confirm deletion	Record removed		
Successful deletion	Success message displayed		


Permission and Security Testing
Create at least two test accounts.

Test	Expected Result	Actual Result	Pass/Fail
User A views own application	Application displayed		
User A attempts to view User B's application	Access denied / 404		
User A attempts to edit User B's application	Access denied		
User A attempts to delete User B's application	Access denied		
Logged-out user accesses dashboard	Redirect to login		
Logged-out user accesses create page	Redirect to login		


Form Validation Testing
Job Application Form
Field/Test	Expected Result	Actual Result	Pass/Fail
Job title missing	Validation error		
Company missing	Validation error		
Valid date	Accepted		
Invalid date	Validation error		
Valid status	Accepted		
Invalid status	Rejected		
Notes empty	Accepted		


User Story Testing
ID	User Story	Expected Behaviour	Result	Pass/Fail
US01	Register account	User can register		
US02	Login	User can log in		
US03	Logout	User can log out		
US04	Create application	Application created		
US05	View applications	User sees own applications		
US06	View details	Individual record visible		
US07	Edit application	Record updated		
US08	Delete application	Record deleted		
US09	Update status	Status updated		
US10	Privacy	Other users' records inaccessible		
US11	Dashboard	Summary displayed correctly		
US12	Filter applications	Filtering works		


Automated Testing
Django automated tests were used to test:

Models

Forms

Views

Authentication

Permissions

CRUD functionality

Status filtering

Running Tests
bash
python manage.py test
Test Results
(Paste final test output here)

Model Tests
Describe model tests implemented.

Form Tests
Describe form validation tests.

View Tests
Describe tests for pages and status codes.

Authentication Tests
Describe login/authentication tests.

Permission Tests
Describe tests ensuring users cannot access other users' records.

CRUD Tests
Describe automated CRUD tests.

GitHub Copilot Usage
Explain:

What tests Copilot suggested

What you changed

Why changes were necessary

What each final test verifies

Responsive Testing
Device / Width	Pages Tested	Result	Pass/Fail
Desktop	All pages		
Tablet	All pages		
Mobile	All pages		


Tested:

Navigation

Dashboard cards

Application table/cards

Forms

Buttons

Status badges

Footer

Text wrapping

Horizontal overflow

Browser Testing
Browser	Device	Result	Pass/Fail
Chrome	Desktop		
Firefox	Desktop		
Edge	Desktop		
Safari	Mobile/tablet		


Accessibility Testing
Tools used:

WAVE

Lighthouse

Axe DevTools

Manual keyboard navigation

Checks:

Colour contrast

Heading hierarchy

Form labels

Keyboard navigation

Focus visibility

Link/button descriptions

Alt text

ARIA usage

Page	Test/Tool	Result	Issues Fixed
Homepage	WAVE		
Dashboard	Lighthouse		
Application Form	Axe		
Application Detail	Manual		


HTML Validation
HTML validated using W3C Validator.

Page	Result	Errors	Resolution
Homepage			
Dashboard			
Add Application			
Application Details			
Edit Application			


CSS Validation
CSS validated using W3C CSS Validator.

File	Result	Errors	Resolution
style.css			


Python Validation
Python code checked for PEP 8 compliance using flake8.

File	Result	Issues Corrected
models.py		
views.py		
forms.py		
urls.py		
tests.py		


JavaScript Testing
If JavaScript is used:

Feature	Expected Result	Actual Result	Pass/Fail


If not used:

JavaScript-specific testing was not applicable because no custom JavaScript was implemented.

Bugs
Fixed Bugs
Bug	Cause	Fix	Status
Example: Permission bug	Incorrect queryset	Filter by request.user	Fixed


(Add more as needed)

Known Bugs
If none remain:

No known bugs remain at the time of final submission.

Final Testing Summary
At the completion of development:

Core user stories were manually tested

CRUD functionality was verified

Authentication and authorization were tested

User-specific data access was tested

Form validation was tested

Responsive behaviour was tested

Accessibility testing was completed

HTML and CSS were validated

Python code was checked for code quality

Automated Django tests were executed

Final automated test result: (Add result)  
Known critical issues: (None / describe)

For information about the application, design process, deployment, and development methodology, see the main README.md.