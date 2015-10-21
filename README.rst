New Project: Arcfire
====================

Just getting started.

*Arcfire* is the working title for a new project of mine; a kind of world builder for creating nonlinear narrative, paired with a particular setting and cast of characters.

The setting will (probably) be in the Arctic, sometime around 50K years in the future, when the ice caps have melted and humanity has dwindled.  Kevin Costner will not be involved.

I look forward to hammering out further details.  Stay tuned!


About the title
---------------

*Arcfire* doesn't mean much, really; It's a mashup between the Arctic, the setting of this tale, and the presumed heat of a postapocalyptic climate.  I chose it quickly because I needed a working title, it's easy to type, and I didn't want to spend much time on it.  

So don't take the title too seriously.  A working title, a code name, which I plan to change sometime in the future.


Eventual deliverables
---------------------

* An API
* An HTML site
* A printed copy to take to the beach
* Lots of appendices, lateral narratives, maps, and other graphics.


Getting Started
===============

Technical stack
---------------

I'm planning to build the bulk of this with Python, Django, PostgreSQL, and HTML5.  Ultimately, when the API is settled, I may do something different on the front end: consume a Python-generated JSON API with a JS framework, for example.  I'd like to stay with Python for as long as possible, though, to benefit from its classical structure.


Database
--------

This software uses the open-source PostgreSQL database.  After installing Postgres, of course, you can start the database with this command:

* ``postgres -D /usr/local/var/postgres``


Building the project
--------------------

TODO. In addition to building the docs above, once some fixtures are in place and there's a regular need to rebuild the database, I will provide an Invoke script for this purpose.

At the moment, the only things (besides starting the database) that are necessary, is to provide a superuser...

``./manage.py createsuperuser --settings=core.settings.dev``

or to load the initial_data fixture:

``./manage.py loaddata arcfire/fixtures/initial_data.json --settings=core.settings.dev``


Starting the server (development)
---------------------------------

Should be as easy as:

* ``./manage.py runserver --settings=core.settings.dev``


Running the test suite (test)
--------------------------

TODO.  Note, a settings stub exists in the ``core/dev/settings.py`` file.  Alter or remove as necessary; not sure yet where this lives ala Postgres.


Starting the server (production)
--------------------

TODO.


Docs
----

I just created some Sphinx docs for the first time.  I will expand as I learn more about this project, and as I write code.

The tutorial to setup Sphinx is here:

* http://www.marinamele.com/2014/03/document-your-django-projects.html

To build the documentation:

* ``docs$ make html``