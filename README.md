# [CNC Bosch Rexroth MTX](https://github.com/deathaxe/sublime-mtx)

This package provides syntax highlighting support for the
Bosch Rexroth MTX Numerical Control to the SublimeText 3 Editor.

### Features:

* NC cycles
  * syntax highlighting
    * ISO G-Code
    * CPL highlevel commands
    * known NC functions and commands
  * indention rules

* Sercos Settings Files (*.scs)
  * syntax highlighting

### Installing

**With the Package Control plugin:** The easiest way to install SublimeCodeIntel is through Package Control, which can be found at this site: http://wbond.net/sublime_packages/package_control

Once you install Package Control, restart Sublime Text and bring up the Command Palette (``Command+Shift+P`` on OS X, ``Control+Shift+P`` on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select ``CNC BoschRexroth MTX`` when the list appears. The advantage of using this method is that Package Control will automatically keep ``CNC BoschRexroth MTX`` up to date with the latest version.

**Without Git:** Download the latest source from `GitHub <https://github.com/deathaxe/sublime-mtx>` and copy the whole directory into the Packages directory.

**With Git:** Clone the repository in your Sublime Text Packages directory, located somewhere in user's "Home" directory::

    git clone git://github.com/deathaxe/sublime-mtx.git "CNC BoschRexroth MTX"


The "Packages" packages directory is located differently in different platforms. To access the directory use:

* OS X::

    Sublime Text -> Preferences -> Browse Packages...

* Linux::

    Preferences -> Browse Packages...

* Windows::

    Preferences -> Browse Packages...

### Setup

The package contains a **mtx_npg.sublime-settings** file, which is recommended
to be copied to the Data/User folder to enable the follwing language specific
settings.

- "ensure_newline_at_eof_on_save": true
- "translate_tabs_to_spaces": true
- "use_tab_stops": false

They are all required to ensure NC will read the resulting file correctly.
