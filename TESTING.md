# HireTrack Testing

This document contains the testing procedures and results for **HireTrack**.

Testing was carried out throughout development to evaluate:

* Functionality
* CRUD operations
* Authentication
* Authorization
* Database behaviour
* Form validation
* Responsiveness
* Accessibility
* Usability
* Code quality

---

## Table of Contents

* [Testing Strategy](#testing-strategy)
* [Manual Functional Testing](#manual-functional-testing)
* [Authentication Testing](#authentication-testing)
* [CRUD Testing](#crud-testing)
* [Permission and Security Testing](#permission-and-security-testing)
* [Form Validation Testing](#form-validation-testing)
* [User Story Testing](#user-story-testing)
* [Automated Testing](#automated-testing)
* [Responsive Testing](#responsive-testing)
* [Browser Testing](#browser-testing)
* [Accessibility Testing](#accessibility-testing)
* [HTML Validation](#html-validation)
* [CSS Validation](#css-validation)
* [Python Validation](#python-validation)
* [JavaScript Testing](#javascript-testing)
* [Bugs](#bugs)
* [Final Testing Summary](#final-testing-summary)

---

# Testing Strategy

HireTrack was tested using a combination of manual and automated testing.

Testing focused particularly on:

* Ensuring users can securely register and log in.
* Ensuring authenticated users can manage job applications.
* Confirming CRUD operations modify database records correctly.
* Confirming users cannot access another user's records.
* Verifying form validation.
* Ensuring appropriate feedback is displayed.
* Testing responsive behaviour.
* Checking accessibility.
* Validating HTML, CSS, and Python code.

---

# Manual Functional Testing

## Navigation

| Test                  | Expected Result          | Actual Result | Pass/Fail |
| --------------------- | ------------------------ | ------------- | --------- |
| Open homepage         | Homepage loads correctly |               |           |
| Click Dashboard       | Dashboard loads          |               |           |
| Click Applications    | Application list loads   |               |           |
| Click Add Application | Form loads               |               |           |
| Click Logout          | User is logged out       |               |           |

---

# Authentication Testing

## Registration

| Test                                 | Expected Result            | Actual Result | Pass/Fail |
| ------------------------------------ | -------------------------- | ------------- | --------- |
| Register with valid information      | Account is created         |               |           |
| Register with missing required field | Validation error displayed |               |           |
| Register with duplicate username     | Validation error displayed |               |           |
| Enter mismatched passwords           | Validation error displayed |               |           |

## Login

| Test                           | Expected Result   | Actual Result | Pass/Fail |
| ------------------------------ | ----------------- | ------------- | --------- |
| Login with correct credentials | User is logged in |               |           |
| Login with incorrect password  | Error displayed   |               |           |
| Login with invalid username    | Error displayed   |               |           |
| Required username left blank   | Error displayed   |               |           |

## Logout

| Test                              | Expected Result          | Actual Result | Pass/Fail |
| --------------------------------- | ------------------------ | ------------- | --------- |
| Logged-in user selects Logout     | Session ends             |               |           |
| Visit protected page after logout | User redirected to login |               |           |

---

# CRUD Testing

## Create

| Test                                  | Expected Result            | Actual Result | Pass/Fail |
| ------------------------------------- | -------------------------- | ------------- | --------- |
| Submit valid application              | Application created        |               |           |
| Application belongs to logged-in user | Correct user stored        |               |           |
| Required field missing                | Validation error displayed |               |           |
| Successful creation                   | Success message displayed  |               |           |

## Read

| Test                      | Expected Result               | Actual Result | Pass/Fail |
| ------------------------- | ----------------------------- | ------------- | --------- |
| Open application list     | User's applications displayed |               |           |
| Open application detail   | Correct application displayed |               |           |
| User with no applications | Empty state displayed         |               |           |

## Update

| Test                      | Expected Result            | Actual Result | Pass/Fail |
| ------------------------- | -------------------------- | ------------- | --------- |
| Edit application          | Existing data displayed    |               |           |
| Save valid changes        | Database record updated    |               |           |
| Change application status | New status displayed       |               |           |
| Submit invalid data       | Validation error displayed |               |           |
| Successful update         | Success message displayed  |               |           |

## Delete

| Test                | Expected Result           | Actual Result | Pass/Fail |
| ------------------- | ------------------------- | ------------- | --------- |
| Select Delete       | Confirmation displayed    |               |           |
| Cancel deletion     | Application remains       |               |           |
| Confirm deletion    | Record removed            |               |           |
| Successful deletion | Success message displayed |               |           |

---

# Permission and Security Testing

One of HireTrack's key requirements is ensuring users can only access their own records.

Create at least two test accounts when manually testing this section.

| Test                                             | Expected Result       | Actual Result | Pass/Fail |
| ------------------------------------------------ | --------------------- | ------------- | --------- |
| User A views own application                     | Application displayed |               |           |
| User A attempts to view User B's application URL | Access denied / 404   |               |           |
| User A attempts to edit User B's application     | Access denied         |               |           |
| User A attempts to delete User B's application   | Access denied         |               |           |
| Logged-out user accesses dashboard               | Redirected to login   |               |           |
| Logged-out user accesses create page             | Redirected to login   |               |           |

---

# Form Validation Testing

## Job Application Form

| Field/Test              | Expected Result  | Actual Result | Pass/Fail |
| ----------------------- | ---------------- | ------------- | --------- |
| Job title missing       | Validation error |               |           |
| Company missing         | Validation error |               |           |
| Valid date              | Accepted         |               |           |
| Invalid date            | Validation error |               |           |
| Valid status            | Accepted         |               |           |
| Invalid/modified status | Rejected         |               |           |
| Optional notes empty    | Form accepted    |               |           |

Add tests for every custom validation rule implemented.

---

# User Story Testing

Use this section to demonstrate that completed functionality satisfies your planned user stories.

| ID   | User Story          | Expected Behaviour                    | Result | Pass/Fail |
| ---- | ------------------- | ------------------------------------- | ------ | --------- |
| US01 | Register account    | User can successfully register        |        |           |
| US02 | Login               | Registered user can log in            |        |           |
| US03 | Logout              | User can securely log out             |        |           |
| US04 | Create application  | Application can be created            |        |           |
| US05 | View applications   | User can see own applications         |        |           |
| US06 | View details        | Individual record can be viewed       |        |           |
| US07 | Edit application    | Record can be updated                 |        |           |
| US08 | Delete application  | Record can be deleted                 |        |           |
| US09 | Update status       | Status can be changed                 |        |           |
| US10 | Privacy             | Other users' records are inaccessible |        |           |
| US11 | Dashboard           | Summary data is displayed correctly   |        |           |
| US12 | Filter applications | Applications filter correctly         |        |           |

---

# Automated Testing

Django automated tests were used to test key application functionality.

Tests should cover areas such as:

* Models
* Forms
* Views
* Authentication
* Permissions
* CRUD functionality
* Status filtering

## Running Tests

```bash
python manage.py test
```

### Test Results

```text
Paste final test output here.
```

### Model Tests

Describe model tests implemented.

### Form Tests

Describe form validation tests.

### View Tests

Describe tests for pages and status codes.

### Authentication Tests

Describe login/authentication tests.

### Permission Tests

Describe tests that ensure users cannot access records belonging to another user.

### CRUD Tests

Describe create/read/update/delete automated tests.

### GitHub Copilot

Document how GitHub Copilot assisted with creating unit tests.

Explain:

* What tests Copilot suggested.
* What you changed.
* Why changes were necessary.
* What each final test verifies.

---

# Responsive Testing

HireTrack was designed and tested across desktop, tablet, and mobile layouts.

| Device / Width | Pages Tested | Result | Pass/Fail |
| -------------- | ------------ | ------ | --------- |
| Desktop        |              |        |           |
| Tablet         |              |        |           |
| Mobile         |              |        |           |

Test:

* Navigation
* Dashboard cards
* Application table/cards
* Forms
* Buttons
* Status badges
* Footer
* Text wrapping
* Horizontal overflow

---

# Browser Testing

| Browser | Device                     | Result | Pass/Fail |
| ------- | -------------------------- | ------ | --------- |
| Chrome  | Desktop                    |        |           |
| Firefox | Desktop                    |        |           |
| Edge    | Desktop                    |        |           |
| Safari  | Mobile/tablet if available |        |           |

Only list browsers you genuinely tested.

---

# Accessibility Testing

Document the accessibility tools and methods used.

Possible checks include:

* Colour contrast
* Heading hierarchy
* Form labels
* Keyboard navigation
* Focus visibility
* Link/button descriptions
* Image alternative text
* Status labels
* ARIA usage where necessary

## Accessibility Results

| Page               | Test/Tool | Result | Issues Fixed |
| ------------------ | --------- | ------ | ------------ |
| Homepage           |           |        |              |
| Dashboard          |           |        |              |
| Application Form   |           |        |              |
| Application Detail |           |        |              |

Add screenshots where useful.

---

# HTML Validation

HTML was tested using [insert validator/tool].

| Page                | Result | Errors | Resolution |
| ------------------- | ------ | ------ | ---------- |
| Homepage            |        |        |            |
| Dashboard           |        |        |            |
| Add Application     |        |        |            |
| Application Details |        |        |            |
| Edit Application    |        |        |            |

If an error was discovered, explain how it was corrected.

---

# CSS Validation

CSS was validated using [insert validator/tool].

| File      | Result | Errors | Resolution |
| --------- | ------ | ------ | ---------- |
| style.css |        |        |            |

---

# Python Validation

Python code was checked for PEP 8 compliance using [insert tool].

Example:

```bash
flake8
```

or another tool used during the project.

| File      | Result | Issues Corrected |
| --------- | ------ | ---------------- |
| models.py |        |                  |
| views.py  |        |                  |
| forms.py  |        |                  |
| urls.py   |        |                  |
| tests.py  |        |                  |

---

# JavaScript Testing

If HireTrack uses JavaScript, document testing here.

| Feature | Expected Result | Actual Result | Pass/Fail |
| ------- | --------------- | ------------- | --------- |
|         |                 |               |           |

If JavaScript is not used:

> JavaScript-specific testing was not applicable because no custom JavaScript was implemented.

---

# Bugs

## Fixed Bugs

Document meaningful bugs encountered during development.

| Bug | Cause | Fix | Status |
| --- | ----- | --- | ------ |
|     |       |     | Fixed  |

Example structure:

### Application permissions bug

**Problem:**
[Describe what happened.]

**Cause:**
[Explain the cause.]

**Solution:**
[Explain how it was fixed.]

---

## Known Bugs

Document any unresolved issues honestly.

If none remain:

> No known bugs remain at the time of final submission.

---

# Final Testing Summary

At the completion of development:

* Core user stories were manually tested.
* CRUD functionality was verified.
* Authentication and authorization were tested.
* User-specific data access was tested.
* Form validation was tested.
* Responsive behaviour was tested.
* Accessibility testing was completed.
* HTML and CSS were validated.
* Python code was checked for code quality.
* Automated Django tests were executed.

**Final automated test result:** [Add result]

**Known critical issues:** [None / describe]

For information about the application, design process, deployment, and development methodology, see the main [README.md](README.md).
