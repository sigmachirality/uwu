# Penn Labs: Backend Technical Challenge S19

## How to run

1. Clone this project.
2. Install Python3 and run '.pip install django', if necessary.
3. Run './manage.py makemigrations' and './manage.py migrate', if necessary.
4. Run './manage.py runserver'.

## Notes

I edited the provided template Django server instead of opting to write a server in either Flask or Node.js. I've left the db file created during my testing in the repo for your convenience. This means that clubs and members tables should already include several entries, so GET and POST requests should return meaningful data on all required routes.

I reckon that mystery_function returns the average quality rating across all Clubs in the db. I'm a bit unsure how the __getattr__ function operates though - I assume that it gets the attribute, but my research indicates that it's usually only called if the attribute of the object doesn't exist?

Member and comment functionality is theoretically supported by how the models are currently setup, but no routes have been made implementing such functionality.

## API Docs

### Models
- Club
    - name - 'Text'
    - description - 'Text'
    - quality - 'Decimal'
    - time_commitment - 'Decimal'
    - fun - 'Decimal'

- Member
    - name - 'Text'
    - clubs - 'ManyToMany \w Club'

- Comment
    - content - 'Text'
    - commenter - 'FK - Member'
    - clubs - 'FK - Club'

### Endpoints
All POST routes return a JSON indicating whether the operation was successful, alongside an applicable HTML response code.

- 'GET /api/clubs/' - returns a list of clubs in JSON format, with name, id, description, quality, time_commitment, fun, members, and comments fields.

- 'POST /api/clubs/' - creates a new club using information from parameters. Gracefully handles missing parameters and conflicts with existing clubs.

- 'POST /api/rankings/' - accepts three ratings and the club id and updates the club with said ratings. Gracefully handles the case where a club with the given club id does not exist and the case where there are missing parameters.

- 'POST /api/members/' - accepts a name parameter and adds a new member with said name. Gracefully handles the case where a member with the given name already exists and the case where there are missing parameters.

- 'POST /api/mystery/' - returns the average quality across all Clubs. 