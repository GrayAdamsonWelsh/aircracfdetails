# Overview

This website is a simple site which hol;ds data about aircraft. It is designed to hold basic data about aircraft but it is designed to incorporate many more tables and fields in future.
This phase is just to see if it can be done and is just involved with just background details and the ability to show groups of aircraft based on their role.

## UX Design

### Initial entry into the home page

!(https://share.balsamiq.com/c/ae4Ci7eUY1ifvsJJ8DSej2.png)

This shows a list of all aircraft in the database and some limited information. It allows the user to do a number of operation.

These operations include 
- register
- login
- access all information about the aircraft to view but not to add new aircraft or amend existing aircraft.

The data shown will be manufacturer, name, type and the date the aircraft was added to the database.

The name wil be shown within an anchor and when it is clicked it will open the edit form  for this aircraft but it will only be for reading.

The login and register anchor tags opens the apporiate Django form to login or register a user.

___

###  Home page After sign in

!(https://share.balsamiq.com/c/7cAv48YL3BkHAForcajQJZ.png)

This again shows all the aircraft in the database and has add functionality.
 
Firstly there are added items in the navigation bar.

The first is Add Aircraft anchor tag, this opens the Add Aircraft page.
The second is Type anchor tag, this opens the Type page.
The third is Logout this allows the user to Logout of the system and returns to the page to it initial state.
The final item is the name of the user and this is just text.

The data shown for each aircraft is the same as in the initial status but with two buttons. The first is edit which is an anchor tag which opens up the edit page for the selected page. The second allows the user to delete the aircraft from the database.
___

###  Add Aircraft

!(https://share.balsamiq.com/c/kMDtbpbZ1ub6qSNaBS8FA8.png)

This allows the user to create a new record for an aircraft.

It shows all the fields used to describe the aircraft.

These are
-  Manufacturer
- Name
- Type
- First Flight
- Date Introduced
- Status
- Number Built
- History
- Author

The add button is an anchor tag.
___

### Edit Aircraft 

!(https://share.balsamiq.com/c/oheu8PaWFWQkGJBHkTk8Q3.png)

This allows the user to alter a record of an aircraft.

The fields are the same as for Add Aircraft page.

The Edit button is an anchor tag. 

___

### Type

!(https://share.balsamiq.com/c/stkPgqUb55hxYufXLWNF8B.png)

This allows the user to add a new types that gives a brief idea of the role the aircraft was designed for.

I has an input field called Type and holds the type of aircraft.

It has an anchor tags which is used as a button and adds the type to the type table.


## Technology


The technologies used were HTML/CSS/JavaScript, Python and Django.

## The webpages

The site has at present
	### A home page
    ![alt text](p1hqtgqsn2153nddt187nd3h12k04-0.jpg)
	### An add page for aircraft
    ![alt text](p1hqtgqsn2153nddt187nd3h12k04-1.jpg)
	### An edit page for aircraft
    ![alt text](p1hqtgqsn2153nddt187nd3h12k04-2.jpg)
	### A delete aircraft page
	### A type page which displays aircraft of a certain role
	### A login page
	### A register page


## Database Diagram

![alt text](<Blank diagram (3).jpeg>)

## User stories
1.	The customer requires the website to hold data about aircraft.
2.	The customer needs to have the ability for users to register to be allowed to create or edit details.
3.	 The customer has requested that there is a need to have all the information to be categorised based on their type (role).
4.	The customer requires that the main details are to be ordered by creation date
5.	The customer wants the data to be attractively displayed
6.	The customer wants information about variants, specifications and other data to be displayed.
7. 	The customer wants the history to be edited to display data in a format which can hold rich text.
8.	The customer needs to display photographs and images.

## Testing

| Number | Description | Date Tested | Result |
|     |     |    |     |
| 1   | Entry into the Home page (no user logged in). Check if the navbar is correct. Showing the title, register and login. That there are no edit or delete buttons visible |19/06/2024     | Passed     |
| --- | --- | --- | --- |
| 2   | Home page no user logged in, click on the name anchor tag and it will allow the user to go to the Edit page but the edit page doesn't allow the user to edit it. |  19/06/2024   |  Passed     |
| --- | --- | --- | --- |
| 3   | Home page no user logged in, press the nav bar Register. This should open registration form (Django registration form) |  19/06/2024   | Passed    |
| --- | --- | --- | --- |
| 4   | Home page no user logged in press the navbar item Login. This should open the login form (Django login form) |  19/06/2024   |  Passed   |
| --- | --- | --- | --- |
| 5   | Entry into the home page with a registered user. Check if the navbar is correct and that is is displaying Add Aircraft, Type and Logout anchor tags, as well as the user name. \For each aircraft there should be an Edit and Delete button should be visible. |  19/06/2024   |  Passed    |
| --- | --- | --- | --- |
| 6   | Home page with a user logged in user. \Click the Add Aircraft anchor tag, it should open the add page and the user should be allowed to create a new aircraft |  06/19/2024   |  Passed   |
| --- | --- | --- | --- |
| 7   | Home page with a logged in user. \Click on the Type anchor tag, it should open the Type page and the user should be allowed to create a new type |  19/06/2024   |  Passed   |
| --- | --- | --- | --- |
| 8   | Home page with a logged in user, click the Logout anchor tag, it should log the user out and then return the home page with the nav bar altered and the removal of edit and delete buttons | 16/06/2024    |  Passed    |
| --- | --- | --- | --- |
| 9   | Home page with a logged in user, click the name anchor tag for an aircraft and it should open the Edit page for the selected aircraft ready for the aircraft data to be changed |  19/06/2024   |  Passed    |
| --- | --- | --- | --- |
| 10  | Home page with a logged in user, click an Edit button for an aircraft, it will open the aircraft edit form with the correct data for the selected aircraft |   19/06/2024  |  Passed   |
| --- | --- | --- | --- |
| 11  | Home page with a logged in user. Click a Delete button for an aircraft will delete the aircraft from the database |  19/06/2024   |  Passed   |
| --- | --- | --- | --- |
| 12  | In edit page page change the status field then check to see if this has been altered | 19/o6/2024     |   Passed  |
| --- | --- | --- | --- |
| 13 | Create a new aircraft record | 19/o6/2024     |   Passed  |
| --- | --- | --- | --- |

#### Test images

For test 1

!(https://share.balsamiq.com/c/5RLqqpyYAUcuSiivDTkP4m.png)
 

For test 2

!(https://share.balsamiq.com/c/vrV7EZK4PQnrHvWj2rHJx9.png)


For test 3

!(https://share.balsamiq.com/c/sZnznNhGt45wPV4RCoEN81.png)

For test 4

!(https://share.balsamiq.com/c/cLqxtHjgjvPTM7FcEUiuwT.png)

For test 5

Start

!(https://share.balsamiq.com/c/cLqxtHjgjvPTM7FcEUiuwT.png)


Ready to sign in

!(https://share.balsamiq.com/c/9iXwepVE7bj6WAPahTcY1V.png)

After

!(https://share.balsamiq.com/c/449ce2LLxpownBTNvpkA9R.png)


For test 6

!(https://share.balsamiq.com/c/3uEhLDNjAKcgx2vg4LFmvn.png)

For test 7

!(https://share.balsamiq.com/c/1KtzUEkgGaGP1swjtaWFKw.png)



For test 8 

Before

!(https://share.balsamiq.com/c/axtnoBsvAADNRaunBHXvP1.png)

After

!(https://share.balsamiq.com/c/hU4rf8xHLd8Kjemkq2AtpK.png)

For test 9

!(https://share.balsamiq.com/c/eybQLsyAsk7mFm11myWgyq.png)

For test 10

Before
!(https://share.balsamiq.com/c/goZm23zpvMdoP8msvQo31F.png)

After
!(https://share.balsamiq.com/c/pte3d84YxAYMHxRAKBsjSM.png)

For test 11

Home page before delete
!(https://share.balsamiq.com/c/fYnynxkgaUyvHF7oQVHh2s.png)

Delete page shown
!(https://share.balsamiq.com/c/uhGJkSVjcKgK8eUX6YXiVc.png)

Main screen after delete
!(https://share.balsamiq.com/c/csXpUv16y6J27raoocb9YY.png)

For test 12

Home page before

!(https://share.balsamiq.com/c/qPry8bJyNNVUynr7v8Hbxp.png)

Edit page before

!(https://share.balsamiq.com/c/tcw3QQMGsdSkwTGurvH75p.png)

View of altered aircraft record

!(https://share.balsamiq.com/c/webZhzHjKRCYiMLmKFyqow.png)

Test 13

Before 

!(https://share.balsamiq.com/c/2NKoLDFSL1iG4AatKhgKrS.png)

After

!(https://share.balsamiq.com/c/4HQNyBgDVEWizxGtAmeV2q.png)

## What needs to be done next

	1.Improve the attractiveness of the website by CSS.
	2 Add the ability to show picture
	3.Ensure its responsive
	4 Add specifications table and if needed create more pages.
	5 Add variants table if needed to create more pages.

## Acknowledgment
	I used guide "Create A Simple Blog With Python and Django" from Codemy on Youtube