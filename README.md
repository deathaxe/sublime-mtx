# [CNC BoschRexroth MTX language support](https://github.com/deathaxe/sublime-mtx)

This package provides syntax highlighting support for the
BoschRexroth MTX Computerized Numerical Control to the [SublimeText 3 Editor](http://www.sublimetext.com).

![screenshot](https://raw.github.com/deathaxe/sublime-mtx/master/screenshot.png)

### Features:

* NC cycles
  * syntax highlighting
    * ISO G-Code
    * CPL high level commands
    * known NC functions and commands
  * symbols for
    * LPS - local sub programs
    * LBL - labels (goto targets)
    * auto completion for the most common DIN/CPL functions

* Sercos Settings Files (*.scs)
  * syntax highlighting

### Installing
##### ... with Package Control
The easiest way to install _CNC BoschRexroth MTX_ is through _Package Control_ plugin, which can be found at <https://packagecontrol.io>

Once you installed _Package Control_, open the Command Palette (``Command+Shift+P`` on OS X, ``Control+Shift+P`` on Linux/Windows). Select "Package Control: Install Package", wait until the latest list of packages is fetched and search for _CNC BoschRexroth MTX_ when the list appears. Package Control will automatically keep all packages installed this way up to date.


##### ... with Git
Clone the repository in your Sublime Text Packages directory, located somewhere in user's "Home" directory:

    git clone git://github.com/deathaxe/sublime-mtx.git "CNC BoschRexroth MTX"


##### ... manually
Download the latest source from GitHub [https://github.com/deathaxe/sublime-mtx](https://github.com/deathaxe/sublime-mtx/archive/master.zip) and extract the whole content into the _"Packages/CNC BoschRexroth MTX"_ directory.


The "Packages" packages directory is located differently in different platforms. To access the directory use:

* OS X:

    Sublime Text -> Preferences -> Browse Packages...

* Linux:

    Preferences -> Browse Packages...

* Windows:

    Preferences -> Browse Packages...

### Setup

The package contains the syntax specific settings files ``mtx_npg.sublime-settings`` and ``mtx_scs.sublime-settings`` with the following required default settings:

- "ensure_newline_at_eof_on_save": true
- "translate_tabs_to_spaces": true
- "use_tab_stops": false

They are all required to ensure NC will read the resulting file correctly.
You can override these settings by creating your own syntax specific setting ``Preferences->Settings - Syntax Specific``

### License
[Copyright &copy; 2016 DeathAxe](https://github.com/deathaxe/sublime-mtx/blob/master/LICENSE)
