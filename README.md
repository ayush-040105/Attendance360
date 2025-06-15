# Attendance360
Attendance360 is a Python-based attendance management system tailored for educational institutions. It streamlines administrative tasks by centralizing student attendance, course information, and attendance logs into a secure, accessible database. With a focus on usability and efficiency, Attendance360 helps faculty save time and improve accuracy in tracking attendance.


**Table of Contents**
------
- [Features](#Features)
- [Technologies Used](#Technologies-Used)
- [Installation](#Installation)
- [Usage](#Usage)
- [Challenges Faced](#Challenges-Faced)
- [Future Scope](#Future-Scope)
- [Contributing](#Contributing)


**Features**
------

**Core Features**
- Student Attendance Management: Track and manage daily attendance logs for each course.
- Course Management: Add, update, and delete course details as per institutional requirements.
- Centralized Database: All attendance and course data is securely stored for quick access and backup.

**Additional Functionalities**
- User-Friendly Interface: Simple and intuitive UI for faculty and administrators.
- Data Consistency: Ensures integrity and avoids duplication or data loss.
- Reports Generation: Easily generate attendance summaries for individual students or entire courses.


**Technologies Used**
------
- Python
- Tkinter (for GUI)
- MySQL (for database)
- Object-Oriented Programming (OOP)


Installation
------

To install and run Attendance360 locally:

1. Clone the repository
```
git clone https://github.com/yourusername/attendance360.git
```

2. Navigate to the project folder
```
cd attendance360
```

3. Install required dependencies
```
pip install pandas mysql-connector-python PyPDF2 pdfplumber pyttsx3 SpeechRecognition pyaudio
```

4. Run the application

Usage
-------

1. Launch the application.
2. Add students and courses using the dashboard.
3. Mark daily attendance.
4. View or export attendance logs when needed.


Challenges Faced
-------

- Database Syncing: Maintaining data consistency between UI operations and database.
- Jarvis Training: Training Jarvis to work efficiently with the application and follow voice command.


Future Scope
-------

- Integrate biometric or QR-based attendance input.
- Enable web-based access with login authentication.
- Add lectures schedules.


Contributing
-------

Contributions are welcome! Here's how to get started:

1. Fork this repository.
2. Create a new branch (git checkout -b feature-name).
3. Commit your changes (git commit -m "Added new feature").
4. Push to the branch (git push origin feature-name).
5. Create a pull request.
