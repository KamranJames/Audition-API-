

## Instructions.
1.  [Clone Repo](https://github.com/KamranJames/Audition-API-)

2.  Create a new venv. 
3.  Pip install requirements.txt
4.  Create database “audition_db”
5.  Create .env and add in this information: 

DATABASE_URL=postgresql+psycopg2://db_dev:passwordcoder@127.0.01:5432/audition_db<p>
JWT_SECRET_KEY=coderkey

6.  Flask db create, Flask db seed
7. If you would like to run queries as an admin in Postman login with these credentials: 

http://127.0.0.1:8080/auth/login

Method: Get 

{ "email":"johnwaters@gmail.com",

"name":"John Waters",

"password":"coder"}


## R1 , R2

  

*What Problem does this project solve? Why is it a _problem_ that needs solving? 

<p>As an actor for over 10 years, I found it incredibly hard to keep track of the thousands of auditions I had done throughout a single year. Sometimes you may book a job or get a callback two months down the line, you may not remember what you wore, any notes the casting director gave you or even what the project was.</p> <p>

  

My intent is to overcome these setbacks through the implementation of an Audition database.

  

The features of this database will allow a user to store information relating to a project. Through this project users will be able to attach roles of the project any actors or roles associated with that project, as well as casting directors connected to a project. This could be wildly beneficial to not only an actor but the majority of different positions on a film production, with the potential to scale up and serve as a major production database when constructing a feature film or television show, minimizing the overwhelming amount of moving parts, across multiple departments within the industry and ensuring less room for errors through one simple database. </p>

  


  
## R3
**Why have you chosen this database system. What are the drawbacks compared to others?**:

For my acting database I have opted to utilize Postgres SQL as the DBMS, this is due to its ability to support both Json and SQL querying, as well as its high level of stability, resilience and integrity. All features that are integral to the optimization of my database. My key focus is optimization and Postgres SQL is very well recognized for its excellence in this area. Our models will largely require Schemas for our structure, this makes the utilization of a NoSQL database not the optimal option.


One of the drawbacks to using PostgresSQL is its expandable documentation is only available in english, this creates a barrier to any user’s outside of the western market. An example could be a developer who isn’t a native English speaker trying to maintain and edit the acting database down the line. It is also not available on all hosts. Some of the other DBMS also have a higher reading speed, such as MySQL. But despite these setback’s PostgresSQL’s pro’s far out way its cons and will serve it’s purpose in my project.

## R4
**Identify and discuss the key functionalities and benefits of an ORM**:

In order to construct my database I will be utilizing the ORM, SQLAlchemy. ORM is an acronym for Object-Relational Mapping, it is a technique that allows one to interact and manipulate data in the database, through the use of queries. It is able to do this by accessing libraries in order to translate the object orientated code we are writing and then maps it onto the database. 

In the early days of programming, a coder would have to do manual tasks such as connecting to the database server, generating queries, sanitization of parameters if required and serialization of retrieved data. The ORM cuts down on these tasks by doing these for us through a function call, cutting down on a lot of time and mental strain throughout the process of development. It also cuts out the necessity to need to know SQL and protects queries against malicious intent such as SQL injection attacks. 

I have chosen SQLAlchemy as it is a great tool to produce queries from objects created utilizing the Python programming language, which is what my application will be written in. 


# R5
[End point documentation](https://www.dropbox.com/s/t3zmhrb8hcd6qzr/Audition%20API%20endpoint%20documentation.pdf?dl=0)

# R6
![ERD](./src/ERD.png)
## R7
**The third party services that are used in my application are**:

Bcrypt - This ensures that passwords are encrypted and salted

Jwt - This is the package that provides our authentication, providing JWT web tokens.

Flask - The web framework that the application will utilize.

marshmallow - Was used for serialization.

request - For http requests.

pip-review - To list available updates for our dependencies.

sqlalchemy - The toolkit for our API and also our ORM

psycopg2 - Allows the ability to perform SQL operations in the SQL alchemy database.

DateTime - Utilized to commit the date a new user was created or a new comment.

# R8
**Describe your projects _models_ in terms of the relationships they have with each other:**

At the base level of our API, the inner workings are all connected through the relationships they share with one another. I will use the project model as a first example as it forms the foundation of my database. As a parent of multiple child models within our function it contains nestled within it, various relationships that are backpopulated such as User, Castings, Actors, Comments and Roles, it also contains the FK user_id, this is demonstrating that every single model within our DB shares a relationship with projects in one way or another, these are also referenced with the fields class within the Project Schema.
In the example provided below you can see how all of these are connected to our project model.
![Example](src/1.png)
 
 If we move onto the child of the projects model the role model, it contains the project_id FK as a column within it's table, accompanied by the child of the Role model, the actor_id FK. Within the Role models schemas is contained the data for these two FK's, as they are referenced within the role cli_controller when inserting data, this way we can track what project and what actor are connected to the role we are querying. The actor model being a child of the role model calls the backpopulates command to establish that they share a relationship and also contains the project_id FK, which too is stored within the role schema, this way we can attach the project that the actor is connected to via its project_id when querying.

As mentioned previously the Casting model is a child of the parent Project model, it contains a project_id foreign key column within it tables, that way it can store the data of what project is associated with what casting. This information is able to be accessed and seeded into the db through Cli Commands, below is an example in which we are connecting this casting data to the first project contained within the db.


![Example2](src/2.png)
We also have a comment model which shares a relationship with both the project model and user model, containing both their FK ids within it's table and schemas, this way we can connect a users comment to a project. 
Tracing back to the User model which obviously shares a relationship with comments but too shares a relationship with the Project model directly as it contains both the projects and comments FK.



# R9
**Discuss the database relations to be implemented in your application**:

The models to be implemented throughout my MVC all share an important part in the overall functionality of my API . Cascading down from the Users model, which essentially functions as the jumping off point for administrators of my API, it shares a zero to many relationship with my comment model, such as a comment can have one user but a user can have zero to many comments, these comments are made to the project model which share's a many to zero relationship, a project can have zero to many comments yet a comment can only have one project. 

The project model is our main model and acts as the linchpin for our MVC and the main parent of the Casting model, Role model and Comments Model, two of the models contain it's FK as their data is reliant upon it. Project share's a one to many relationship with user and contains the user_id FK, as the user has the ability to input the project data or access/alter it. If the user is an admin they are also granted special privileges. The project contains tables within it that make up a substantial amount of the main data of the API such as name, director, year and status of the project.  The casting model is connected to the project model through a one to many relationship, as a project can have one casting  yet a casting can have many projects. The tables contained within the casting model contains the casting_associates information, in the acting industry this is the name of the casting director of the project, it is important to record that associates information in other columns within the table such as location and agency, these string values are essential and are required therefore are denoted by a NOT NULL value constraint, meaning we cannot leave this information out when adding a casting. 

Every project needs a role associated within it as how would it tell a story otherwise? This is demonstrated via a one to many relationship, a project needs to exist for a role to exist. There can be many roles on a project but a role is only connected to that one project, it also contains the FK of the project. The table contains columns of data such as name to denote the name of the project via a string, notes to add any specific information about that particular role. Interestingly this specific column notes, can be a NULL value, while it would be helpful to have notes always documented regarding a certain role, it is not a necessity.  In order for a role to be fulfilled on a certain project well it would require an actor, therefore a role is the parent of the actor model and they are connected through a one to many relationship. An actor can have many roles, but one role can only contain one actor, an actor FK also exists within the role model,

Just as an actor is important to a project so to is their relationship although they aren't directly linked, the actor references the project in the table through a FK to the project model. Within the models table contain the columns such as f_name the first name of an actor, l_name the last name of an actor and agency of the actor. This is all essential data and is denoted by the NOT NULL constraints. 


## R10
**Describe the way tasks are allocated and tracked in your project**:

[Trello Board Link](https://trello.com/invite/b/n7R4bIHN/ATTI22faf568fc5c7720d371620581a2529d777DD7BC/audition-api-trello)


Throughout the process I relied heavily on Trello, ensuring that I checked it everyday to gauge what was priority number one for that day. I utilized an in progress tab containing cards that would cascade down from most important to least pressing. 

If I faced any serious errors I would move that to the top of my in progress tab if I wasn't able to clear it before the EOD, that way I could come back the next day and understand where I was in the process. I also create a sprint tab and allotted myself Sprints, this gave me a good goal to aim for although sometimes this was hindered due to unexpected errors, the most important thing is I would circle back and try and ensure that Sprint was completed before progressing onto the next sprint. 

I create an Error Backlog, if I wasn't able to clear an error and required guidance from an educator a card would be put here and I would attempt to work around the error if possible whilst I awaited an answer, once this was cleared it would progress into the done tab. It was great to have a done tab in order to review what I had accomplished at the end of the day and feel hopeful that I was utilizing my time appropriately. This also served as a metric as to how I could alter my approach and what I could spend more time or less time on. For instance if I focused on one area and achieved very little at the end of the day. I might alter my approach to how I tackled that task.

I had a questions tab for any questions that did arise as well as an on hold tab for any features I wanted to add but wasn't the top of my priority. 

I found that Trello was an incredibly important tool in helping me understand where I was in the project and what I needed to work on. 

I also used github for my source control and attempted to commit meaningful messages, this way I would be able to get an idea of what I had cleared and worked through with each push. 
















