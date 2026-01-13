## Superheroes API
-This is a Flask-based RESTful API designed to track heroes and their unique superpowers. The application manages a many-to-many relationship where heroes can have multiple powers, and each power can be assigned to multiple heroes through a join table that tracks the strength of that specific connection.

## Project Features
-Hero Management: Retrieve a list of all heroes or view specific hero details along with their associated powers.

-Power Management: View existing powers or update their descriptions with built-in validation.

-HeroPower Linking: Assign powers to heroes with a specific strength level ('Strong', 'Weak', 'Average').

-Data Integrity: Strict validations ensure descriptions meet length requirements and strength levels remain         consistent.

-Email Support: Integrated Flask-Mail capabilities for system notifications.

## Setup & Installation
-Clone the repository
-Setup the virtual environment
-Install sependancies
-Initialize the database
-Run the application

## API Endpoints
Method,Endpoint,Description
GET,/heroes,Returns a list of all heroes
GET,/heroes/:id,Returns a hero's details and their powers
GET,/powers,Returns a list of all powers
GET,/powers/:id,Returns details of a specific power
PATCH,/powers/:id,Updates a power's description
POST,/hero_powers,Creates a new link between a hero and a power
 
## Validations
Power: The description must be at least 20 characters long.
HeroPower: The strength must be one of the following: 'Strong', 'Weak', or 'Average'. 

## Author
Brandon Dikirr

## License
This Project is Licensed 