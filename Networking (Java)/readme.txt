This directory includes the project built over the course of a semester. The completed project are simple server and client programs written in java.

The purpose of the project was to teach students how to implement threading in java and demonstrate the advantages of a concurrent server.

Specifications for the project can be found below:

Network Management Application using the Sockets API
Project #1
This client-server programming project is an iterative TCP based network
administration tool. The server provides current system status as requested
from the client. The client can request from the server such information as
the system time, the uptime, the memory use, netstat, current users, and the
running processes. The client program displays a text menu for the user. The
user makes requests by selecting a menu option.
The user will enter the server hostname as a command line argument when
the client program is invoked. If there is no command line argument then the
program will print an error message and exit. The client program then enters
a loop until told to quit where it will:
• Display a menu
• Prompt the user for a command
• Test user input for command validity. If user command is invalid,
inform the user and redisplay the menu.
• Send that command request to the server on the host
• Get response back from server
• Display response for user
The menu will provide the following choices to the user:
1. Host current Date and Time
2. Host uptime
3. Host memory use
4. Host Netstat
5. Host current users
6. Host running processes
7. Quit
Have your server print out diagnostic messages about what it is doing (e.g.,
“accepting a new connection”, etc.)
You may use the popen() library function to get the output of a command
into your program.

Project #2
Make your server concurrent by having it spawn a thread/process to handle
each client request.
Plot two graphs of the latency (mean server response time) versus number of
clients for the netstat and current date and time commands. Increase the
number of clients as follows: 1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100.
