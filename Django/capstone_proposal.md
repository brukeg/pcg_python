# Capstone Proposal

  Use Python, HTML, CSS, JavaScript (+React), and Django to build a web application that touches on every major technology we've covered. Below are the criteria for your proposal: 
- Proposal must set specific and attainable goals
- Proposal must cover all major topics we've covered
- Proposal must include the sections below


## Name
### [Silamoney.com](https://www.silamoney.com)


## Project Overview
Rebuild my company website, [Silamoney.com](https://www.silamoney.com), in Django and React and include a demo of our API using our Python [SDK](https://github.com/Sila-Money/Sila-Python).


## Features
Pages:
1. Home (index): will include a rundown of what are product is, technical use cases, how it works, who is involved in the company, and how to contact us (w/included chat widget). The following links will also be included:
  * home: a link back to `silamoney.com/#`.
  * contact sales: mailto:contact@silamoney.com.
  * careers: an external link to our company Indeed profile.
  * blog: an external link to our company blog hosted by Medium.
  * news: a page containing recent press write-ups.
  * about: a page containing bio information about our team.
2. Docs: an external link to our API documentation hosted by slate. This will be in both the header, footer, and possibly in the body.
3. Demo: my primary milestone will be a demonstration of our API, so a customer can input dummy user data to see how our API links bank accounts, identifies users, and sends money. This will be a page on the website, like, silamoney.com/demo
4. Login: this will be a page where existing users can login to their accounts and access their developer console.
5. Sandbox/register: before logging in you first have to register for access, this will be that page.
6. Console: the console is where our developer customers can see their apps and data regarding their apps.


### User stories
1. Demo: as a prospective customer I want to see how Sila's API could be implemented. I want to input dummy user data and see how account linking, ID verification, and money transfers work before I commit.
**backlog:**
   - [ ] Use Python [SDK](https://github.com/Sila-Money/Sila-Python) to build demo application.
   - [ ] backlog 
   - [ ] backlog

2. Sandbox: as a customer of Sila I want to start building my application in an evironment that's safe and easy to use before I request production access to Sila.
**backlog:**
   - [ ] Require all prospective customers to register as a developer.
   - [ ] backlog
   - [ ] backlog

3. Console: as a customer of Sila I need to see all the apps I have in sandbox and production in one place. I should also be able to see associated data like user count or transaction count by day, week, and month. In addition I need to be able to update my billing information.
**backlog:**
   - [ ] Make all users login before accessing silamoney.com/console
   - [ ] Re-write current console in Django/React.
   - [ ] Allow users to update billing information.


#### Questions to ask yourself about functionalities

- What will the user see on each page? 
- What can they input and click and see? 
- How will their actions correspond to events on the back-end?

## Data Model
- handle (developer_org.silamoney.eth)
- address
- DOB
- first name
- last name
- SSN
- company name
- passphrase
- ethereum address
- private key


## Schedule
1. Milestone 1: Demo, 1-2 weeks, easily the hardest and most involved because I'll building it from scratch excepting the SDK. I'll use Django and React to implement our API to show off what an application could look like. Sprint one, is to get a Django app running which displays all the forms. Sprint two will be to wire up the forms so they function and make calls to our API. Demo takes the data model above.
  * Essential features:
  * Really-great-to-haves:
  * Nice-to-haves:


2. Milestone 2: Register, 1 week, I'll be re-writing an existing codebase in Django/React. Sprint one, will be to wire up the forms so they function and make calls to our API. Register takes the data model above.
  * Essential features:
  * Really-great-to-haves:
  * Nice-to-haves:


3. Milestone 3: Home, 1 week, I'll be re-writing an existing codebase in Django/React. Sprint one, is to get a Django app running which displays all the current company information outlined in Features above.
  * Essential features:
  * Really-great-to-haves:
  * Nice-to-haves:


4. Milestone 4: Login, 1 week, I'll be re-writing an existing codebase in Django/React. **This will commence after class.** Sprint one, will be to wire up the forms so they function and make calls to our API. Login takes handle and passphrase only.
  * Essential features:
  * Really-great-to-haves:
  * Nice-to-haves:


5. Milestone 5: Console, 1-2 weeks, I'll be re-writing an existing codebase in Django/React. **This will commence after class.** First sprint, is to get a Django app running which displays all the apps and users information. Sprint to will be focused on displaying application data.
  * Essential features:
  * Really-great-to-haves:
  * Nice-to-haves:



### Agiles/Scrum Methodology and Workflow
We're going to be following a modified [Agile/Scrum](https://linchpinseo.com/the-agile-method/) workflow. Most software development teams follow Agile/Scrum methodology, so we're going to as well. The difference is that rather than working on a team, you'll be working as a team of one with me as your *Scrum Master*. 

#### Iterative Development
Agile development is **iterative development**. The goal is to set short sprints (1-4 week intervals), where at the end of each sprint you have a **minimal viable product**, or **MVP**. This means you have a functioning, *end-to-end* application at the end of each iteration.

So, rather than spend a huge amount of time building up the infrastructure for your application (i.e. setting up the wheels and frame for a car) and not have a complete, shippable product until the very end of the process, you build MVPs each sprint (i.e. start off with a scooter, then bike, then motorcycle, until eventually you have a car). 

![MVP diagram](./Making-sense-of-MVP-.jpg)

This way, you can fall back to a shippable, completed product at any phase. Also, if your requirements change (as they often do) midway through development, your product can much more easily adapt to changing needs since you haven't locked yourself in with an extensive infrastructure.

#### Setting up MVP
You want each of your milestones to result in a minimal viable product. For each milestone, take a few features off of your **product backlog** (the set of user stories you have defined). 

Generally, you want to rank your product backlog in terms of:

- Essential features:
- Really-great-to-haves:
- Nice-to-haves:

Structure your milestones first to cover essential features. Then, think about adding the great-to-haves and nice-to-haves in terms of how much they'd improve your application and how difficult it would be to implement them.

Each MVP must be a completed *end-to-end product*. What this means is you need a functioning back-end connected to a functioning front-end. Get all your models, views/templates, and controller/views connected.

These MVPs are what you should strive to work on. Build up your application, feature by feature, until you're at a working state. Then commit and push your working MVP before you start on the next version. Rinse and repeat until you're ready to ship!