# Identification of the problem you are trying to solve by building this particular app.

In this day in age, there are that many streaming platforms that I couldn't name them all on two hands, and what comes with that is the seperation of hundreds if not thousands of movies and television shows that only supply certain streaming platforms. This problem has become incredibly annoying and for a lot of people, very expensive! 
<br>
But what If you could figure out a smart plan of attack on what streaming platform you should subscibe to for each month of the year, think of the amount of money saved and the time saved on only watching the movies/tv shows you like! Well thats where StreamPlanner comes into help. I'm building this application to help with this problem, and hopefully save the users money in the longrun. The application will take in input of that genres of movies and tv shows you like, figure out which streaming platform has the most hits with the genres, and tell you which streaming platform is the one for you. It will also give you movies soon to be added to the platform aswell incase of wanting to stay with them for another month. 

# Why is it a problem that needs solving?

Most households would have more than 1 streaming platform, just because one has different films/shows that others don't, or some movies are only on for a certain time, and having more than 1 platform generally means more spending! So Id like to save the users money, where somebody can save money and think smarter on which platforms should be bought per month.

# Why have you chosen this database system. What are the drawbacks compared to others?

I've chosen to use PSQL(PostgreSQL) because its a free and open sourced relational database management system. Has very simple and accessible technical standards that are built on the SQL language. Once you get your eyes around the simplistics of psql, all the queries just start working, and I found that really enjoyable. Because of me only having used POSTgreSQL, I've researched what the drawbacks are compared to others, and because my database is so small at the moment, I cannot tell the if the database is slow or not, but apparently its a huge problem with bigger databases.

# Identify and discuss the key functionalities and benefits of an ORM

First of all, the benefits of using an ORM were unreal straight from the start, just because of the struggle of learning how to write certain queries, I almost found it easier to pickup the ORM language of searching through the database into columns into other columns using simple ORM code. So some of the benefits I can think of would be;
- First of all connecting into the database
- Connecting into a column via query.
- Having the ability to filter the query to whatever paramater needed.
- Controlling the outcome of the query.

# Document all endpoints for your API

# User Endpoints
<details>
<summary>/user/register POST</summary>

Starts off with loading the user schema, which has the information required to create a user. From there we create the user with a query, this query also has an if statement which will only go off if the username is already in use. The same route is done witht he email.

If the user puts in all a new username and email, following with passsword,dob,country, the user will be created.

Once created a token is created for the user with the time of the code given: 1 day.
</details>
<details>
<summary>/user/login POST</summary>

Loads the user schema just like the route above. IF statement is prompted for username and password. The user needs to be in the database to pass this process. If you type in the wrong username or password, you will get an error telling you have the wrong details. If you type in a username and password thats on the database you will be given a token to proceed.
</details>
<details>
<summary>/user/login/admin POST</summary>

Different from the above routes, this one is for admin users. No register available for this action, only hardcoded logins available. 

Starts of getting the information from the admin schema. Same run through as a user, but now its with the Admin tag. If not correct details gives errors. Once logged in you will recieve a token which has the ability to add/delete/update certain controllers.
</details>
<details>
<summary>/user/preferences GET</summary>

JWT token needed, whatever token is linked with the user will have access to the preferences settings.
This route will query all the preferences attatched to the users token, and return it in jsonify.
</details>
<details>
<summary>/user/preferences/int:id GET</summary>

Because I don't want users being able to add to the database, I call for JWT, for all of my instances with authentication I use "@jwt_required()" which makes sure the only user who is allowed to add to this is the ones with "Admin" token. If you do not have the admin token, you will be given an permission error.

Works the same as above, but only queries the ID attatched to the route.
</details>
<details>
<summary>/user/preferences/add POST </summary>

Starts off the route with JWT authentication, in this case its only asking for a user token. If you don't have a user token you will get an error. 

Opening up the preference schema with the load functions (request.json) then into the model "Preference" where all of the fields "Action, adventure, comedy, fantasy, horror, mystery, drama, science_fiction" can be added. Then the database adds the post, commits it then dumps it with jsonify.
</details>
<details>
<summary>/user/preferences/update/int:id PUT</summary>
 TO BE ADDED
</details>
<details>
<summary>/user/services GET</summary>

Querys all of the data in services, then dumps it with jsonify.
</details>
<details>
<summary>/user/services/add POST</summary>

Because I don't want users being able to add to the database, I call for JWT, for all of my instances with authentication I use "@jwt_required()" which makes sure the only user who is allowed to add to this is the ones with "Admin" token. If you do not have the admin token, you will be given an permission error.

Next up is loading the services schema to get the information. Once thats done, the route opens up the Services model, and the needed information about the model to post. the name, price and description. Once this information is loaded up, its added and committed, then dumped using jsonify.
</details>
<details>
<summary>/user/services/delete/int:id DELETE</summary>

Same as above route, needing the admin token, so JWT is authenticating this route aswell. Once connected with an admin token, once adding the ID to the route e.g www.streamplanner.com/services/delete/5, it will delete the ID attatched to the service_id, this being service_id #5. Once the route has been successfully executed, its deleted the service_id from the database, committing and saving the server and prompting with a message of "Movie had been deleted..."
</details>
<details>
<summary>/user/services/update/int:id PUT</summary>

Admin token needed again, JWT authentication. Once connected, fields are loaded with the service schema, then the fields that need to be placed in the put request. "Name, price, description" onces submitted, the route is committed and published by jsonify.
</details>
<br>

# Movie Endpoints
<details>
<summary>/movies GET</summary>

Because this route doesnt need to be authenticated, I haven't put jwt_required. Anybody can view the database for movies. 

If a user wants to search via the movies route with custom parameters, I've added in query strings, eg. movies?genre=Comedy, If you type something out of the three parameters, it will come up with an error.

Apart from that, the movies list is queried by the model, and dumped via jsonify and movies_schema.
</details>
<details>
<summary>/movies/int:id GET </summary>

Same as above, but no query strings, and works only with IDs, for search purposes only. movies/3 would responed with the movie id relating to 3.
</details>
<details>
<summary>/movies/add POST </summary>

As talked about above, JWT is called upon for authentication, because I don't want everybody to have the ability to add to the database, only admin tokens have the privelege. If an admin token isn't provided here, you'll get a permission error.

Once an acceptable admin token is provided, the movie schema loads with a json request, once inside the schema, we have access to the Movie model, where the fields of the movie are asked for the post. Fields include "Title, genre, genre, and service_id". Admins have access to the services list, therefor can add the service_id to the movie.

Once thats completed, the movie is added to the database, committed, then returned with a jsonify of the movie_schema.
</details>
<details>
<summary>/movies/delete/int:id DELETE</summary>

Same as POST, authentication required by an admin, once accepted in, the movie is deleted via what movie_id is published in the route. If an ID is prompted in the route thats not in the database, an error "movie not found" will prompt. Once an acceptable ID is provided, the movie is deleted with the session delete into session committing to the database, with a prompt of "Movie has been deleted.."
</details>
<details>
<summary>/movies/update/int:id PUT</summary>

Admin token needed again, JWT authentication. Once connected, fields are loaded with the service schema, then the fields that need to be placed in the put request. "title, genre, date_added, and service id" onces submitted, the route is committed and published by jsonify.
</details>
<br>

# Tv_show Endpoints
<details>
<summary>/tv_shows GET</summary>

Because this route doesnt need to be authenticated, I haven't put jwt_required. Anybody can view the database for movies. 

If a user wants to search via the movies route with custom parameters, I've added in query strings, eg. movies?genre=Comedy, If you type something out of the three parameters, it will come up with an error.

Apart from that, the tv_show list is queried by the model, and dumped via jsonify and tv_shows_schema.
</details>
<details>
<summary>tv_shows/int:id GET </summary>

Same as above, but no query strings, and works only with IDs, for search purposes only. tv_show/3 would responed with the tv_show id relating to 3.
</details>
<details>
<summary>/tv_shows/add POST </summary>

As talked about above, JWT is called upon for authentication, because I don't want everybody to have the ability to add to the database, only admin tokens have the privelege. If an admin token isn't provided here, you'll get a permission error.

Once an acceptable admin token is provided, the tv_show schema loads with a json request, once inside the schema, we have access to the TV Show model, where the fields of the movie are asked for the post. Fields include "Title, genre, genre, and service_id". Admins have access to the services list, therefor can add the service_id to the tv_show.

Once thats completed, the tv_show is added to the database, committed, then returned with a jsonify of the tv_show_schema.
</details>
<details>
<summary>/tv_shows/delete/int:id DELETE</summary>

Same as POST, authentication required by an admin, once accepted in, the tv_show is deleted via what tv_show_id is published in the route. If an ID is prompted in the route thats not in the database, an error "tv_show not found" will prompt. Once an acceptable ID is provided, the tv_show is deleted with the session delete into session committing to the database, with a prompt of "TV show has been deleted.."
</details>
<details>
<summary>/tv_shows/update/int:id PUT</summary>
<br>
Admin token needed again, JWT authentication. Once connected, fields are loaded with the service schema, then the fields that need to be placed in the put request. "title, genre, date_added, and service id" onces submitted, the route is committed and published by jsonify.
</details>

----------------------------------------------------------------

INSERT ERD HERE

----------------------------------------------------------------

# Detail any third party services that your app will use

## Services
<details>
<summary>Flask: Blueprint, Jsonify, Request</summary>

Blueprint
 - has been used in all of my controllers, without Blueprint, my routes would struggle to find the right way to be published. After registering each controller with a seperate url, I'm then given access to the ability of decorating my route.

Jsonify
- has been used in all of my controllers. Jsonify is used to serialize my data into "Javascript Object Notation" then wraps it in a response object. To simplify this, it turns my data into a more readable data.

Request
- Has been used in all of my controllers, have used it in all my of query strings, request is the function that sending all the data to the server, so without this function, I'm in a world of pain. Request was also used in all of the load functions 'request.json' same again this is doing the same function, but turning it into json.

</details>
<details>
<summary>Flask:JWT Extended</summary>

Create Access Token
- Creating an access token is the way of authenticating what kind of user you are, and who you are, Create access token is used when creating a user, this users id gets attatched to a token for a maximum of 1day at a time. Same thing works for the admin, generating a token will give a access token just for admins. 

JWT manager
- Is a key part to my database, all of the controllers are authenticated via a token. JWT manager makes storing and retrieving these said tokens easier. 

JWT required
- Is the other side of the access token, authenticating with JWT required is making sure all of the desired routes that I think need authentication have it. So calling for JWT required gives me the ability to add that step forward on only allowing certain users in. I've used this in all of my POST and PUT methods, some others, but mainly them. Mainly for authentication for the admin token.

Get JWT Identity
- Another side of the authentication proccess, this is the method of how you authenticate if the admin token is correct or not, (Well thats how I've been using it). Authenticates the token to make sure only "Admin" tokens are allowed into the route.

</details>
<details>
<summary>Marshmallow</summary>

- I've used Marshmallow system in Flask to create all of my Schemas. Marshmallow validates my data and helps my data with organization.

</details>
<details>
<summary>Bcrypt</summary>

- Bcrypt is used for encypting the users passwords, it encryps with a hashing proccess called upon with "generate_password_hash", this stores the password in the database with a hashed password, so just incase a data leak or potential hacking in the system, the users passwords are safe and encrypted.

</details>
<details>
<summary>SQLAlchemy</summary>

- this library is the absolute backbone of this API, its the joining product of my database and my code. Its the main ORM of my product and it cannot run without it. 
</details>

# Describe your projects models in terms of the relationships they have with each other

<details>
<summary>Admin Model</summary>

This model is very simple, is linked with nothing else in the database.

Admin_ID = a Integer which is the primary key, this id has access to all of the adding/deleting/updating features on streamplanner.

Username = only one admin, so the username will always be admin.
 
password = is hidden with the bcrypt library.
</details>
<details>
<summary> User Model </summary>

This model steps it up a little bit, most of the data saved in the database will link up in someway down the path.

User_id = the primary key, this ID is the way you will be starting the linking proccess to Streamplanner.
I decided not to add first and last name to this model as it's not needed, no point asking for something thats not needed.

Username is a unique string that links the username to the users account.

Email adress is also a unique string that is a pivital part of the sign up, an email address is a good way of authenticating who the user is incase of loss of password, or loss of username. Its also a great way of notifiying a user on up coming movies/tv shows.

password = is hidden with the bcrypt library.

dob is a way of authenticating age, incase for later on down the path If movies that have an age description on them, we can filter out the movies/tv shows. e.g If a Movie Is MA15+, and the user is only 14 years of age, it wont show these types of movies.

Country is also another way of authenticating, but for this case where you are in the world, at the moment all the streaming services are the ones only located in Australia, or the ones available for Australians. But potentially one day I can filter the ones not available in your area.
 
</details>

<details>
<summary>Preferences Model</summary>

Preference_id  is the primary key this key will be used to link the preferences with the user, then onto the final product.

The next 8 parts of the model are all types of genres [Action, Adventure, Comedy, Fantasy, Horror, Mystery, Drama, Science Fiction] which are all true/false factors (boolean) this is to show what genres you like and dont like, this data is what helps produce the final product on what streaming platforms you should go with.

The User_id is the ForeignKey of the preferences model, this is the way of linking the user to the preferences.
</details>
<details>
<summary>Services Model</summary>

Because of the way the API is structured, the streaming services have an ID and are only accessible via the admin, so all of the services are attatched to a "Service_id", This ID is the primary key for the services model, and a pivital part of my API.

The name of the service is a mandatory part of the service model, you can't pick which service you want without knowing the name.

The price column was added incase the user had a price range they wanted to work with.

Description column was added for a short little bio, or later on down the track added for what parts of the world its available in.
</details>
<details>
<summary>Movie Model</summary>

Movie_ID is the primary key for the movie model, this ID is the linking factor for the movie titles generically.



