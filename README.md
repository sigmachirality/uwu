# Server Challenge: Spring '19

Welcome to the Penn Labs backend challenge!

## About The Challenge

We want you to create a project named Penn Club Review, a site where students can share information clubs and rank them. Treat this assignment as if there were other developers who work on the same codebase, and that the code will potentially be in production for a long period of time.

Your task is to create various GET/POST endpoints that return responses in JSON format. If you have additional time, there are bonus challenges that you can complete.

## What We're Looking For

This mini project will help us get a better understanding of your technical abilities and your abilities in writing maintainable code. We provide you with initial code in order to test your abilities to read code and understand functionality while fixing bugs and implementing new features.

We highly recommend completing the challenge in Django, since many of our server backends are written using this framework. If you are not comfortable using Django, Flask or a Node.js server also suffice, but these will not have existing code for you to work off of. This challenge will primarily be graded by overall correctness and project design. *It is okay if not all of your features work.*

[Getting started with Django | Django](https://www.djangoproject.com/start/)

[Quickstart - Flask 1.0.2 documentation](http://flask.pocoo.org/docs/1.0/quickstart/)

[Getting Started Guide | Node.js](https://nodejs.org/en/docs/guides/getting-started-guide/)

# The Challenge

Penn Labs is building PennClubReview - a platform to view all the extracurricular activities available at the school. This is a project developed and maintained by at least three other developers at Penn Labs.

[ezwang/wow](https://github.com/ezwang/wow)

1. **Create additional database models and fields** in order to store all of the information that you will need to display to the user.
    1. You will need to store club objects, with each club having a name, description, and three rating factors: quality, time commitment, and fun. The factors should be *decimal numbers* (ex: 3.5 is a valid rating). The person who initially wrote the code assumed that we would be using integers, but we're sure that you should be able to fix this.
    2. Clubs can have comments and members. Members consist of a name and a rank (both text fields). Comments consist of a text field and are linked to an individual member. In our implementation, club members submit comments about clubs that they are in.
2. **Create a route at** `GET /api/clubs` that returns a list of clubs in JSON format, with the name, rating, and description.
    1. Bonus: Also return a list of comments and members in the JSON response.
3. **Create a route at** `POST /api/clubs` that creates a new club, with its club information as parameters in the request body. New clubs should be returned in subsequent call of `GET /api/clubs`.
4. **Create a route at** `POST /api/rankings` that accepts three ratings and a club id and updates the club to have the given ratings.
5. **Fix the route** `POST /api/members` to gracefully handle the condition when an existing member with the specified name already exists. 
6. **Decipher** the `mystery_function`  in `views.py` and rewrite the code to be more efficient and clear.

## Bonus Challenges

1. Write a frontend with React.js that can use this API to list and create clubs. Place the files associated with the frontend in a `frontend` folder.

[Tutorial: Intro to React - React](https://reactjs.org/tutorial/tutorial.html)

[AJAX and APIs - React](https://reactjs.org/docs/faq-ajax.html)