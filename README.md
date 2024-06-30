# Quiz Application

This project is a web-based quiz application built with Flask and TailwindCSS. It allows users to log in as either an admin or a user. Admins can create quiz questions, while users can take quizzes and view their results.

## Features

- **User Authentication**: Separate login forms for users and admins.
- **Quiz Management**: Admins can add quiz questions.
- **Dynamic Quiz Taking**: Users can take quizzes and get immediate feedback.

## Project Structure

- `appy.py`: Flask application files.
- `env/`: Virtual environment directory.
- `static/`: Contains static files like CSS.
  - `src/input.css`: TailwindCSS entry point.
- `templates/`: HTML templates for the application.
  - `admin.html`: Admin interface for managing quizzes.
  - `index.html`: Landing page with login forms.
  - `quiz.html`: Quiz taking interface for users.
  - `result.html`: Displays quiz results to users.
- `tailwind.config.js`: TailwindCSS configuration.
- `connect.py`: Credentials to establish connection with Database.
- `package.json`: Node.js project file with dependencies.
- `requirements.txt`: Python dependencies.
- `interview_questions_mcq.xlsx`: Excel file containing quiz questions.

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/monishbl/DBMS_Projects/tree/4dc9463d3db3e910b08af322dd3d67444b36f588/Question_repo
```

2. **Install dependencies**

Ensure you have Node.js installed, then run:

```bash
npm install
```

3. **Generate TailwindCSS**

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
```

4. **Activate the virtual environment**

```bash
python -m venv env  # Create a virtual environment
```

```bash
source env/Scripts/activate  # On Windows
source env/bin/activate  # On Unix or MacOS
```

5. **Install Python dependencies**

```bash
pip install -r requirements.txt
```

6. **Change the Database Credentials**
```py
host="localhost"
user="<Your_Username>" # root is default user
password="<Your_Password>"
database="<Your_Database_Name>"
```

7. **Run the Flask application**

```bash
python appy.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
