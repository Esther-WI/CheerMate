# Project Title
CheerMate: Mood Tracking and Activity Suggestion CLI

## Description
CheerMate is a command-line interface (CLI) application designed to help users track their moods and get personalized activity suggestions to improve their well-being. The app stores data persistently using SQLAlchemy ORM with a SQLite database.

### Features
User management (create, view, delete users)

Mood logging with timestamps

Activity suggestions based on mood triggers

Data stored and managed in a relational database with 3 related tables: Users, Moods, Activities

Simple interactive CLI for seamless user experience

#### Technologies Used
Python 3.x

SQLAlchemy ORM for database interaction

SQLite as the database backend

Pipenv for virtual environment and dependency management

##### Installation and Setup
Clone the repo

Run pipenv install to install dependencies

Run pipenv shell to activate virtual environment

Launch the CLI: python lib/cli.py

###### Usage
Follow on-screen prompts to create users, log moods, view activities, and get suggestions.

Exit anytime by choosing the exit option.

###### Code Overview
cli.py handles the user interface and input/output loops.

helpers.py contains functions supporting CLI operations, such as validations and prompts.

models/ contain the ORM models (User, Mood, Activity) with relationships and validation logic.

Database sessions are managed through SQLAlchemy for persistent storage.

###### Challenges Faced
Handling ORM relationships and cascading deletes

Input validation for user data (e.g., email format)

Structuring CLI flow to be intuitive and modular

Managing module imports correctly for a clean project structure

###### Future Improvements
Add user authentication

Implement more sophisticated activity suggestions

Enhance CLI with search and filtering options

Build a web front-end for richer UX

