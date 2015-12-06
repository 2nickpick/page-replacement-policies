Nicholas Pickering
Operating Systems COP4610
Project 3 - Page Replacement Policies
Professor Littleton
Date Due: 12/13/2015
Date Submitted 12/13/2015

# Introduction
This program simulates two page replacement policies, and examines their performance:
- First In, First Out (FIFO),
- and Least Recently Used (LRU)

# Invoking the application
Invoke the application by calling:
    ./p3 num_pages max_integer page_frames

    where num_pages is the number of pages to use in the simulation,
    max_integer is the maximum possible value of a page,
    and page_frames is the value to be used by Round Robin as the Time Quantum

# Main, Library
The entry point to the application is main.py. This program references several helper classes in the lib directory.

# Output Files
This program produces output to the console.

An example result set for each test is saved to the output directory, with the same name as tests.
Tests are available in the data directory.

# Test Data
The project contains a directory named "data" which contains the provided test files.

# Issues / Difficulties
