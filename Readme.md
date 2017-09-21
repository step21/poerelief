# Readme.md

(Poetic Relief is published under AGPL v3, see LICENSE for details)

Required packages:

* Python 2 (not yet compatible with Python 3)

To Install/Run

* git clone or download the repository
* cd into cloned directory
* virtualenv poe (to create a new evironment)
* source poe/bin/activate to activate the new environment
* pip install -r requirements.txt to install the necessary python packages
* Download the databased (cleaned up) as used in production, and put it into the subdirectory poerelief
* The code is a bit unorganized, but running python run.py in the subdirectory poerelief should start the main app

* Poerelief 0.1.4
- cleaned up database https://mega.co.nz/#!ss1giCDI!obppI2RnUC36lEl2DOuqck8Oig3o6XUWsYyyurXjuMM (to remove square brackets and records that were missing crucial fields)
- better url replacement
- edition instead of recto/verso for better results

* Poerelief 0.1.3
- improved database dump
- basic ajax-y stuff working, esp. for name/date and pictures, text not so much

* Poerelief 0.1.2
- first databasedump
- improved parsing code
- better structure and basics for ajax-y access

* Poerelief 0.1.1
- reorganization  into proper package
- proper db access with sqlalchemy orm

* Poerelief 0.1
- initial version/commit
