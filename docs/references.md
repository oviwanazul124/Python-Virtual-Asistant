# References

References to multiples functions used around the Virtual Assistant

## readJSON()

### Returns

  - `dict["str1", "str2"]`: A mapping of translations key to translated string

### Notes

  - Only the language from the `config.ini` will be used
  - Will raise the following exceptions:
      - `FileNotFoundError`: The language set in the `config.ini` is not found in the `.\languages` folder.
      -  `json.JSONDecodeError`: The JSON that is trying to load have an error will return the error.
      -  `KeyError`: The key reference you are trying to access dosen't exists.

### Import

``` python3
from utils.jsonImporting.jsonimport import readJSON
```

### Example

An example from this function can be used:

``` python3

from utils.jsonImporting.jsonimport import readJSON

translations = readJSON()
print(translations["hello"])
# -> "Hello, my name is artemis"

```

## wikipediaSearch()

### Requirements

The requirements that will need this function are:

  - [configGet]()
  - [readJSON](https://github.com/oviwanazul124/Python-Virtual-Asistant/edit/main/docs/references.md#readjson)
  - [loggingF](https://github.com/oviwanazul124/Python-Virtual-Asistant/edit/main/docs/references.md#loggingf)

### Values

  - `wilkipediaSearch(data)`:
      - `data`: It is a `string` that came from the speech recognition from the user.

### Return

  - `result`: Will return a `string` summary from the `data` value of `4` sentences

### Notes

  - Will return it in the language configuration set up in `config.ini` on the `wikipedia` section
  - Will raise the following exceptions:
      - `wikipedia.exceptions.PageError`: Will return the translation `["command"]["wikipedia"]["pageError"]`
      - `wikipedia.exceptions.HTTPTimeoutError`: Will return the translation `["command"]["wikipedia"]["HTTPTimeoutError"]`
      - `wikipedia.exceptions.DisambiguationError`: Will return the translation `["command"]["wikipedia"]["disambiguationError"]`

### Import

``` python3
from utils.commands.wikipediaSearch.wikipediaSearch import wikipediaSearch
```

### Example

An example from this function can be used:

``` python3
from utils.commands.wikipediaSearch.wikipediaSearch import wikipediaSearch

data = "Minecraft"
value = wikipediaSearch(data)
print(value)
# -> "Minecraft is a sandbox game developed and published by Mojang Studios. Formally released on 18 November 2011 for personal computers following its initial public alpha release on 17 May 2009, it has been ported to numerous platforms, including mobile devices and various video game consoles.\nIn Minecraft, players explore a procedurally generated, three-dimensional world with virtually infinite terrain made up of voxels (cubes). Players can discover and extract raw materials, craft tools and items, and build structures, earthworks, and machines."
```
## cShutdown()

### Requirements

  - [platform](https://docs.python.org/3/library/platform.html)
  - [subprocess](https://docs.python.org/3/library/subprocess.html)
  - [readJSON](https://github.com/oviwanazul124/Python-Virtual-Asistant/edit/main/docs/references.md#readjson)
  - [loggingF](https://github.com/oviwanazul124/Python-Virtual-Asistant/edit/main/docs/references.md#loggingF)

### Notes

  - Will store the platform of execution in `rOS` variable.

### Import

``` python3
from utils.commands.shutdown.cShutdown import cShutdown
```

### Example

An example from this function can be used:

``` python3
from utils.commands.shutdown.cShutdown import cShutdown

cShutdown()
# -> The device will shutdown
```
## loggingF()

### Values

  - `loggingF(type, string)`
      - `type`: It is an int betweent 1-4 meaning the type of logging you want to sent to the `.log`
          - `1`: Debug Logging
          - `2`: Info Logging
          - `3`: Warning Logging
          - `4`: Error Logging

### Notes

  - Upon execution of `main.py` will create a .log with the following format `Y%-%m-%d_%H-%M-%S.log`
  - Will raise the following exceptions:
      - If the `type` value is not inside 1-4, will print `Logger is not working` to the `.log`

### Import

``` python3
from utils.logger.logger import loggingF
```

### Example

An example from this function can be used:

``` python3
from utils.logger.logger import loggingF

loggingF(1, "This a logging with debug")
# .\Y%-%m-%d_%H-%M-%S.log -> XXXX-XX-XX XX:XX:XX,XXX - DEBUG - This a logging with debug
loggingF(2, "This a logging with info")
# .\Y%-%m-%d_%H-%M-%S.log -> XXXX-XX-XX XX:XX:XX,XXX - INFO - This a logging with info
loggingF(3, "This a logging with warning")
# .\Y%-%m-%d_%H-%M-%S.log -> XXXX-XX-XX XX:XX:XX,XXX - WARNING - This a logging with warning
loggingF(4, "This a logging with error")
# .\Y%-%m-%d_%H-%M-%S.log -> XXXX-XX-XX XX:XX:XX,XXX - DANGER - This a logging with error

```
## openWeb()

### Requirements

The requirements that will need this function are:

  - [webbrowser](https://docs.python.org/3/library/webbrowser.html)
  - [readJSON](https://github.com/oviwanazul124/Python-Virtual-Asistant/edit/main/docs/references.md#readjson)
  - [loggingF](https://github.com/oviwanazul124/Python-Virtual-Asistant/edit/main/docs/references.md#loggingf)


### Values

  - `cOpenWeb(data)`
      - `data`: It is a `string` that came from the speech recognition from the user.

### Notes

  - Will raise the following exceptions:
      - webbrowser.Error: returning the translations `["command"]["open"]["web"]["error"]`

### Import

``` python3
from utils.commands.openWeb.cOpenWeb import cOpenWeb
```

### Example

An example from this function can be used:

``` python3
from utils.commands.openWeb.cOpenWeb import cOpenWeb

cOpenWeb("google.com")
# -> Will open the default browser and the URL `https://www.google.com`
```
