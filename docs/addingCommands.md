# Adding Commands
## Where to add the new command

To add the new command you should create it inside the utils folder and commands folder.
[IMAGE]

## Developing our first command

First we need to know what would we want to add in our command, we are going to disect to basics commands, the Wikipedia search command and the Hello command

### Developing the hello command
The first thing we can see it is that we are importing to utilities the [readJSON]() function and the [loggingF]()

![Importing Utils](screenshots\importingUtilsDocsHello.png)

`` 

from utils.jsonImporting

``

After that we execute the [readJSON]() function, this function will read the config.ini, get the language selected by the user and get all the info from the json file. It returns as a dictionary and I tipically save it in a variable named 'translations'.

Now we define the main function of the command, in this case the first thing that will be executed is the [loggingF]() that sends to the log, what will write inside 

[IMAGE]
