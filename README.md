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

# Auth Endpoints

### **/user/register** POST

Starts off with loading the user schema, which has the information required to create a user. From there we create the user with a query, this query also has an if statement which will only go off if the username is already in use. The same route is done witht he email.

If the user puts in all a new username and email, following with passsword,dob,country, the user will be created.

Once created a token is created for the user with the time of the code given: 1 day.


### **/user/login** POST

Loads the user schema just like the route above. IF statement is prompted for username and password. The user needs to be in the database to pass this process. If you type in the wrong username or password, you will get an error telling you have the wrong details. If you type in a username and password thats on the database you will be given a token to proceed.


### **/user/login/admin** POST

Different from the above routes, this one is for admin users. No register available for this action, only hardcoded logins available. 

Starts of getting the information from the admin schema. Same run through as a user, but now its with the Admin tag. If not correct details gives errors. Once logged in you will recieve a token which has the ability to add/delete/update certain controllers.

### **/user/preferences** GET

JWT token needed, whatever token is linked with the user will have access to the preferences settings.
This route will query all the preferences attatched to the users token, and return it in jsonify.

### **/user/preferences/<int:id>** GET

Because I don't want users being able to add to the database, I call for JWT, for all of my instances with authentication I use "@jwt_required()" which makes sure the only user who is allowed to add to this is the ones with "Admin" token. If you do not have the admin token, you will be given an permission error.

Works the same as above, but only queries the ID attatched to the route.

### **/user/preferences/add** POST

Starts off the route with JWT authentication, in this case its only asking for a user token. If you don't have a user token you will get an error. 

Opening up the preference schema with the load functions (request.json) then into the model "Preference" where all of the fields "Action, adventure, comedy, fantasy, horror, mystery, drama, science_fiction" can be added. Then the database adds the post, commits it then dumps it with jsonify.

### **/preferences/update/<int:id>** PUT
 TO BE ADDED

### **/user/services** GET

Querys all of the data in services, then dumps it with jsonify.

### **/user/services/add** POST

Because I don't want users being able to add to the database, I call for JWT, for all of my instances with authentication I use "@jwt_required()" which makes sure the only user who is allowed to add to this is the ones with "Admin" token. If you do not have the admin token, you will be given an permission error.

Next up is loading the services schema to get the information. Once thats done, the route opens up the Services model, and the needed information about the model to post. the name, price and description. Once this information is loaded up, its added and committed, then dumped using jsonify.

### **/user/services/delete/<int:id>** DELETE

Same as above route, needing the admin token, so JWT is authenticating this route aswell. Once connected with an admin token, once adding the ID to the route e.g www.streamplanner.com/services/delete/5, it will delete the ID attatched to the service_id, this being service_id #5. Once the route has been successfully executed, its deleted the service_id from the database, committing and saving the server and prompting with a message of "Movie had been deleted..."

### **/user/services/update/<int:id>** PUT

Admin token needed again, JWT authentication. Once connected, fields are loaded with the service schema, then the fields that need to be placed in the put request. "Name, price, description" onces submitted, the route is committed and published by jsonify.

### **/movies** GET

Because this route doesnt need to be authentication, I haven't put jwt_required. Anybody can view the database for movies. 

If a user wants to search via the movies route with custom parameters, I've added in query strings, eg. movies?genre=Comedy, If you type something out of the three parameters, it will come up with an error.

Apart from that, the movies list is queried by the model, and dumped via jsonify and movies_schema.

### **/movies/<int:id>** GET

Same as above, but no query strings, and works only with IDs, for search purposes only. movies/3 would responed with the movie id relating to 3.

### **/movies/add** POST

As talked about above, JWT is called upon for authentication, because I don't want everybody to have the ability to add to the database, only admin tokens have the privelege. If an admin token isn't provided here, you'll get a permission error.

Once an acceptable admin token is provided, the movie schema loads with a json request, once inside the schema, we have access to the Movie model, where the fields of the movie are asked for the post. Fields include "Title, genre, genre, and service_id". Admins have access to the services list, therefor can add the service_id to the movie.

Once thats completed, the movie is added to the database, committed, then returned with a jsonify of the movie_schema.








