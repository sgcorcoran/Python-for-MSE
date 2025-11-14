# Python-for-MSE

## Cursor issue

Workaround: Kernel selection not working in Cursor + Jupyter

I was hitting the same issue where kernel selection in Cursor didn’t work. What fixed it for me was starting the Jupyter server manually and then attaching Cursor to that running server instead of letting Cursor start it.

Steps:

Start Jupyter yourself (from a terminal):

jupyter lab
# or
jupyter notebook

When it starts, copy the full URL from the terminal output, e.g. something like:

http://localhost:8888/?token=XXXXXXXXXXXXXXXXXXXXXXXX

Go back to Cursor.
When it asks you to select a kernel / Jupyter server, choose the option to connect to an existing server (or wherever it lets you paste a URL).

Paste the Jupyter URL you copied and confirm.

After doing this, kernel selection works correctly and I can run cells from Cursor without issues.

## Notes

* Need to add lesson on week 6 of 03 lesson. No current lesson on building a dashboard only the guided activity.

## ChangeLog

* [2025-09-05] Lesson 02 prompt engineering and case study finished
* [2025-06-08] First drafts of 02.5 "bridge lesson" and 03 modern data tools introduction

## Fall 2025: Complete rework of course now with AI focus

- Post `01_getting_started.pdf` to canvas so students can get started installing software. Until they do this, they can't read .ipynb files.
- `01_part1_ai_tools_setup_and_basic_analysis.ipynb` notebook of the above pdf file.
- `01_part2_ai_tools_setup_and_basic_analysis.ipynb` for second week with assignment.
- normally there would be one file for each 2 weeks; a lesson week and a homework week.

## Before Spring 2025

A live version of this textbook can be found at [https://sgcorcoran.github.io/Python-for-MSE/intro.html](https://sgcorcoran.github.io/Python-for-MSE/intro.html)
This is a work in progress for MSE 2114 & MSE 3114 a 2 credit series of courses introducing students at Virginia Tech
programming in python with applications in Materials Science and Engineering.
