# TaskQuest – Python Authentication & Task Challenge Project

## Project Overview

TaskQuest is a **Python console-based project** where users must **sign up and log in** to access a dashboard containing different tasks.
The project uses **Python decorators** to protect dashboard functionality and ensure that only logged-in users can access tasks.

Users complete tasks such as **fetching jokes from an API** and **playing a random number game**.
After completing tasks, the user receives **scores**, which are stored and displayed on the home dashboard.

This project demonstrates several important Python concepts including:

* Functions
* Decorators
* File handling
* API fetching
* Random module
* Basic game logic
* Authentication system
* Score tracking

---

# Project Workflow

```
Start Program
     │
     ▼
Signup / Login
     │
     ▼
Login Validation
     │
     ▼
Dashboard Access (Protected by Decorator)
     │
     ▼
User Completes Tasks
     │
     ▼
Score Calculation
     │
     ▼
Score Display on Home Dashboard
```

---

# Project Features

### 1. User Authentication

The system allows users to create accounts and log in.

Features:

* Signup with username and password
* Login validation
* User data stored in a file

Data storage example:

```
users.txt

deepak:1234
rahul:abcd
```

---

# 2. Decorator-Based Login Protection

The project uses a **Python decorator** to restrict access to the dashboard.

Only logged-in users can access protected functions.

Example concept:

```
@require_login
def dashboard():
    show_tasks()
```

Decorator logic:

* Check if the user is logged in
* If true → execute function
* If false → ask user to login

---

# 3. Dashboard System

After login, the user is redirected to a dashboard.

Example dashboard:

```
-------- DASHBOARD --------

1. Fetch Joke Task
2. Play Random Game
3. Show Score
4. Logout
```

---

# 4. Task System

Users must complete tasks to earn points.

Tasks included:

### Task 1 – Joke API Fetch

The user must fetch a random joke from a public API.

Example API:

```
https://official-joke-api.appspot.com/random_joke
```

Example output:

```
Why did the chicken cross the road?
To get to the other side.
```

Concepts used:

* requests module
* API fetching
* JSON handling

Score:

```
+5 points
```

---

### Task 2 – Random Guessing Game

A simple number guessing game.

Game logic:

* Computer generates a random number (1–10)
* User tries to guess the number

Example:

```
Computer picked a number between 1 and 10
Enter your guess:
```

Result:

```
Correct Guess → +10 points
Wrong Guess → 0 points
```

Concepts used:

* random module
* loops
* conditions

---

# 5. Score System

Each completed task gives points.

Example scoring system:

```
Joke task → 5 points
Game win → 10 points
```

Scores are stored in a file.

Example:

```
scores.txt

deepak:15
rahul:10
```

---

# 6. Home Dashboard

After login, the user can see their score.

Example:

```
Welcome Deepak

Your Score: 15
```

---

# Project Structure

```
TaskQuest/

main.py
auth.py
decorators.py
dashboard.py
tasks.py
game.py
score.py

users.txt
scores.txt
README.md
```

---

# Concepts Used

* Python Functions
* Decorators
* File Handling
* API Integration
* Random Module
* Basic Game Logic
* Authentication System

---

# Learning Outcomes

By completing this project, you will learn:

* How authentication systems work
* How decorators protect routes/functions
* How to fetch data from APIs
* How to structure a Python project
* How to store and manage user data
* How to build small interactive programs

---

# Future Improvements

Possible upgrades:

* Convert the project into a **Flask web application**
* Add **multiple games**
* Add **leaderboard system**
* Use **database instead of text files**
* Add **password hashing**
* Create a **GUI version**

---

# Author

Deepak Pandey

Frontend Developer | Learning Backend Development | Python Enthusiast
