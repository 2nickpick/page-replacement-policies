#
#
#   Main
#   This module acts as the starting point for the simulation
#
#   The goal of this project is to simulate and analyze two page replacement policies.
#
#   The algorithms are simulated in the following order:
#   - First In, First Out (FIFO)
#   - Least Recently Used (LRU)
#
#

import sys
from lib import util
from random import randint

__author__ = 'Nicholas Pickering'


number_of_page_requests = 0
number_of_pages = 0
number_of_experiments = 100

#   Start Main Program
print("Page Replacement Policy Simulation")
print("Written by Nicholas Pickering")

#   Read in file for processing...
if len(sys.argv) == 3:
    number_of_page_requests = int(sys.argv[1])
    number_of_pages = int(sys.argv[2])
else:
    util.error("Incorrect number of arguments... Exiting...", True)

#
#   Process Input
#

print("Number of Page Requests: ", number_of_page_requests)
print("Number of Pages: ", number_of_pages)

page_requests = []


for x in range(0, number_of_page_requests):
    page_requests.append(randint(0, number_of_pages))

for page_frame_count in range(2, number_of_pages+1):

    # test out algorithms with number of page frames leading up to max page frames
    print("Starting Tests for Page Frame Count: ", page_frame_count)

    page_faults_fifo_total = 0
    page_faults_lru_total = 0

    for counter in range(0, number_of_experiments):

        page_frames_fifo = []
        page_faults_fifo = 0

        page_frames_lru = []
        page_faults_lru = 0

        page_frames_priority_lru = []

        # Execute the FIFO algorithm

        for page_request in page_requests:

            if page_request not in page_frames_fifo:
                page_faults_fifo += 1
                page_faults_fifo_total += 1
                if len(page_frames_fifo) < page_frame_count:
                    page_frames_fifo.append(page_request)
                else:
                    # add page to page frames according to FIFO
                    page_frames_fifo.pop(0)
                    page_frames_fifo.append(page_request)

        # Execute the LRU algorithm

        for page_request in page_requests:

            if page_request not in page_frames_lru:
                page_faults_lru += 1
                page_faults_lru_total += 1

                if len(page_frames_lru) < page_frame_count:
                    page_frames_lru.append(page_request)

                else:
                    page_frame_to_remove = page_frames_priority_lru.pop(0)
                    page_frame_index = page_frames_lru.index(page_frame_to_remove)
                    page_frames_lru.remove(page_frame_to_remove)
                    page_frames_lru.insert(page_frame_index, page_request)

            # manage priority queue
            if page_request in page_frames_priority_lru:
                page_frames_priority_lru.remove(page_request)
            page_frames_priority_lru.append(page_request)

    total_page_requests = len(page_requests) * number_of_experiments

    print("FIFO\tPage Faults: {}\tPage Requests: {}\tSuccess Rate: {}\tFailure Rate: {}"
          .format(page_faults_fifo_total, total_page_requests, 1.0 - (page_faults_fifo_total / total_page_requests), page_faults_fifo_total / total_page_requests))

    print("LRU \tPage Faults: {}\tPage Requests: {}\tSuccess Rate: {} \tFailure Rate: {}"
          .format(page_faults_lru_total , total_page_requests, 1.0 - (page_faults_lru_total / total_page_requests), page_faults_lru_total / total_page_requests))

    print("---------------------------------------\n")

print("End Simulation")


