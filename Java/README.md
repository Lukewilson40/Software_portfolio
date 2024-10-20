# Overview

This project demonstrates a simple **Journal Application** built in Java, designed to handle basic file input and output, serialization, and object management. The application allows users to create journal entries, view all entries, search for a specific entry by title, and save these entries persistently to a file. The main objective was to improve my understanding of Java's core features, particularly in terms of file handling and object-oriented design, while also implementing practical use cases that resemble tasks in real-world software engineering.

The purpose of writing this software was to deepen my knowledge of Java’s syntax and libraries, focusing on serialization for saving objects, managing user input through a command-line interface, and effectively handling error conditions. Through this project, I learned how to efficiently manage program state and provide a functional, user-friendly interface that persists data between sessions.

[Software Demo Video](https://youtu.be/yk5Lb0jtY30)

# Development Environment

The development environment for this project consisted of:

-   **IDE**: IntelliJ IDEA was used for writing and debugging the Java code.
-   **Java Version**: The code was written and tested using Java SE 17.
-   **File I/O**: Java’s `FileOutputStream` and `ObjectOutputStream` were used for writing the journal entries to a file, while `FileInputStream` and `ObjectInputStream` were used for loading them back.

The entire application was built using Java’s standard libraries without relying on any third-party libraries or frameworks.

# Useful Websites

-   [Oracle Java Documentation](https://docs.oracle.com/javase/8/docs/api/) – For understanding Java’s core classes, including file I/O and serialization.
-   [GeeksforGeeks](https://www.geeksforgeeks.org/) – Helpful in understanding serialization and file handling concepts.
-   [Stack Overflow](https://stackoverflow.com/) – Used for troubleshooting specific issues during development.

# Future Work

-   Implement a feature to edit existing journal entries.
-   Add functionality to delete journal entries.
-   Improve the file storage format by using JSON or plain text instead of Java serialization to make entries more human-readable.
