# Vacations Management System - Part I

This project is the first part of a three-part series focused on building a Vacations Management System. In this initial phase, the goal is to create the foundational backend using Flask and MySQL, establishing a basic server framework that connects to a database and demonstrates core functionalities. This is the base upon which subsequent projects will build, ultimately culminating in a complete full-stack application with React and Django.

## Project Overview

The Vacations Management System allows users to view vacations, like/unlike vacations, and provides administrative controls for managing the vacations. The system supports two types of roles:

1. **Admin**: Can view, add, update, and delete vacations.
2. **User**: Can view vacations and like or unlike them.

This initial part focuses on setting up the server-side architecture, data models, and business logic using Flask and MySQL.

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Virtual Environment**: Python virtual environment with `requirements.txt` for dependencies

## Project Structure

The project is organized into several key components:

- **Logic Layer (`src/logic/`)**: Implements the business logic required for managing users, vacations, roles, likes, and countries. This includes files like:
  - `countries_logic.py`
  - `likes_logic.py`
  - `roles_logic.py`
  - `users_logic.py`
  - `vacations_logic.py`

- **Models Layer (`src/models/`)**: Defines the data models representing the different entities in the system such as users, roles, countries, vacations, and likes. Each model file corresponds to a specific table in the database:
  - `countries_model.py`
  - `likes_model.py`
  - `roles_model.py`
  - `users_model.py`
  - `vacations_model.py`

- **Data Access Layer (`src/utils/dal.py`)**: Handles interactions with the MySQL database, including connecting/disconnecting and performing CRUD operations (Create, Read, Update, Delete).

- **Utilities (`src/utils/app_config.py`)**: Contains configuration settings for the application.

- **Testing (`src/tests/test.py`)**: A `Test` class that includes unit tests to validate the functionality of the different components in the system. Each function in the facade is tested with hardcoded values, ensuring that correct responses are returned, and exceptions are handled appropriately.

## Database Structure

The database consists of the following tables:

1. **Roles (`roles`)**:
   - `role_id` (Primary Key)
   - `role_name` (Admin, User)

2. **Users (`users`)**:
   - `user_id` (Primary Key)
   - `first_name`, `last_name`, `email`, `password`
   - `role_id` (Foreign Key)

3. **Countries (`countries`)**:
   - `country_id` (Primary Key)
   - `country_name`

4. **Vacations (`vacations`)**:
   - `vacation_id` (Primary Key)
   - `country_id` (Foreign Key)
   - `description`, `start_date`, `end_date`, `price`, `image_file`

5. **Likes (`likes`)**:
   - `user_id` (Foreign Key)
   - `vacation_id` (Foreign Key)

## Features Implemented

1. **Database Setup**:
   - Creation of tables and setting up relationships.
   - Initial data population (roles, users, countries, vacations).

2. **Data Access Layer (DAL)**:
   - Connect/disconnect from the MySQL database.
   - Perform CRUD operations on various tables.

3. **Business Logic**:
   - User Management: Register users, verify login credentials, validate unique emails.
   - Vacation Management: Add, update, delete vacations, retrieve vacations sorted by start date.
   - Like Management: Add/remove likes for specific vacations.

4. **Facade Layer**:
   - Handles registration, login, vacation retrieval, and CRUD operations for vacations and likes.

5. **Testing**:
   - `Test` class validates each facade function with hardcoded values and ensures expected behavior.

## Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/hagarhorvitz/freedom_project_part1.git
   cd src
   ```

2. Set up the virtual environment:
   ```bash
   python -m venv ve_freedom
   source ve_freedom/bin/activate  # On Windows: ve_freedom\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   - Import the provided SQL schema (`schema.sql`) and data into your MySQL server.

4. Run the Flask application:
   - Ensure `app.py` is in the correct location (`src/` directory or root as applicable).
   ```bash
   python app.py
   ```

## Notes

- This is the foundational part of an ongoing project that will be expanded in future phases to include a complete frontend using React and a backend with Django.
- The admin role and some initial data are hardcoded for this part of the project.
- Make sure the `app.py` file exists and is in the correct directory before running the application.

## Future Development

This project is the first of three phases:
1. **Part I**: Backend foundation with Flask and MySQL (current).
2. **Part II**: Full-stack development using Flask for both backend and frontend.
3. **Part III**: Advanced full-stack development with Django for the backend and React for the frontend.

## Author
This project is part of the Full Stack Web Development course.

## License
This project is for educational purposes only and follows the terms provided by the course.

