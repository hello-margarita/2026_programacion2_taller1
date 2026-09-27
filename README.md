## 2026_programacion2_taller1
Console-based clinic appointment management system built with Python (arrays and lists, OOP, and error handling) for a Programming II course.

## Overview
The program collects client data through the console, validates every input, calculates the cost of each appointment based on the client and treatment type, and stores all records in a list. 
Once all clients have been registered, it displays summary statistics, an ordered list of clients by total value, and allows searching for a specific client by ID number.

## Features

- Register multiple clients in a single session (the user decides when to stop).
- Input validation for every field: ID number, name, phone number, client type, treatment type, quantity, priority, and appointment date.
- Automatic cost calculation based on client type (Particular, EPS, Prepagada) and treatment type (Limpieza, Calzas, Extracción, Diagnóstico).
- Summary report: total number of clients, total revenue, and number of clients scheduled for a tooth extraction.
- Client list sorted from highest to lowest total value.
- Linear search by ID number, showing the number of comparisons performed and the client's full information.

## How to run

Make sure Python 3 is installed. Then, from the project folder, run: python consultorio_odontologico.py

The program will prompt you for each client's information in the console.

## Notes

- Built using only basic Python structures (`if`, `for`, `while`, functions, and classes), consistent with the level covered in the course at the time this assignment was developed.
- The program does not prevent the same ID number from being registered more than once, since a client may have multiple scheduled appointments. As a result, a search by ID returns the first matching record found in the list.
- Date validation accepts today's date or any future date, with no upper limit, as adding one was considered outside the scope of this assignment.

## Author

Margarita María Arango Vélez
Programming II — Universidad de Manizales
2026
