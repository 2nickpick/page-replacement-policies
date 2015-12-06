Nicholas Pickering

Operating Systems COP4610

Project 3 - Page Replacement Policies

Professor Littleton

Date Due: 12/11/2015

Date Submitted: 12/06/2015

# Introduction
This program simulates two page replacement policies, and examines their performance:
- First In, First Out (FIFO),
- and Least Recently Used (LRU)

# Invoking the application
Invoke the application by calling:
    ./p3 number_of_page_requests number_of_pages

where number_of_page_requests is the number of page requests to use in the simulation,
number_of_pages is the number of unique pages in the request sequence

# Main
The entry point to the application is main.py.

# Output Files
This program produces output to the console.

An example result set for my initial test is saved to the output directory.

# Report
The required report regarding performance analysis is at data/report.txt.

# Issues / Difficulties
Simulating the Page Replacement Policies was very straightforward. The biggest challenge was perhaps the priority queue
necessary to manage the LRU replacement policy. As new pages were requested, it was necessary to update a priority
queue to keep track of how recently used each page in the page frames are.
