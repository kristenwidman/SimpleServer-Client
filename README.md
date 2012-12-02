#Very simple python server and client using sockets#

##To Use:##
1. Launch the simpleserver.py in a terminal window.
2. Launch the simpleclient.py in a separate terminal window.
3. See what happens.

##Learning:##
I played around with this to learn more about how sockets work. Of particular
interest to me was learning about how to indicate to sockets when to stop
listening for data. Two separate techniques are in this code (one commented
out) - shutting down the writing side of the client socket after writing, and
using a delimiter in the message sent. Sockets used here are blocking.
