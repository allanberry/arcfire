# New Project: Arcfire

Just getting started.

*Arcfire* is the working title for a new project of mine; a kind of world builder for creating nonlinear narrative, paired with a particular setting and cast of characters.  In the beginning, I intend to use it to describe existing stories; in the near future, I would like it to produce new ones.

My working scenario, in order to test the software, is the Arctic ocean, sometime around 5K years in the future, when the ice caps have melted and humanity has dwindled.  Kevin Costner will not be involved.

I look forward to hammering out further details.  Stay tuned!


### About the title


*Arcfire* doesn't mean much, really; It's a mashup between the Arctic, the setting of the potential tale, and the presumed heat of a postapocalyptic climate.  I chose it quickly because I needed a working title, it's easy to type, and I didn't want to spend much time on it.  

So don't take the title too seriously.  I plan to change it sometime in the future when I get a better idea.


### Eventual deliverables

* A comprehensive API.
* An HTML site with many entry points.
* The ability to print copies to take to the beach.
* Lots of appendices, lateral narratives, maps, and other graphics.  Info-vis, man!


### Technical stack


I'm planning to build the bulk of this with Python, Django, PostgreSQL, and HTML5.  Ultimately, when the API is settled, I may do something different on the front end: consume a Python-generated JSON API with a JS framework, for example.  I'd like to stay with Python for as long as possible, though, to benefit from its classical structure.


### Versions

(Canonical source is in requirements.txt)

* Host: webfaction
* Python 3.5.
* Django 1.9.
* Dev: is Mac OSX 10.11.
* Production: CentOS 6.7.


### Hosting Setup

TODO.  Explain/depict:

* The WebFaction directory structure
* How Git is used to transfer files, and the various steps required to move files around
* Setting up Python and Pip, with requirements files
* Other WebFaction tips, methods, and gotchas.


### Database

This software uses the open-source PostgreSQL database.  Make sure you install the [PostGIS](http://postgis.net/install/) extension (available as a checkbox add-on with Webfaction).

After installing Postgres, of course, you can start the database with this command:

* ``postgres -D /usr/local/var/postgres``


### Building the project

In addition to building the docs above, once some fixtures are in place and there's a regular need to rebuild the database, I will provide an Invoke script for this purpose.

The launch script I included with the project is for WebFaction only.

The following examples are for the production environment, but should work in development also, with the appropriate settings flag.

You need to provide a superuser...

* ``./manage.py createsuperuser --settings=core.settings.production``

...or to load the initial_data fixture:

* ``./manage.py loaddata arcfire/fixtures/initial_data.json --settings=core.settings.production``

Collect the static files:

* ``./manage.py collectstatic --settings=core.settings.production``

Finally, apply the existing migrations to the database, and you should be ready to rock and roll.

* ``./manage.py migrate --settings=core.settings.production``


### Starting the server

#### In development

* ``./manage.py runserver --settings=core.settings.dev``

In order to do frontend work, you will need to install and start Compass (to convert SCSS into CSS on the fly).  [Installation instructions for Compass](http://compass-style.org/install/).  Running the Compass monitor will require its own terminal window:

* ``compass watch arcfire/static/arcfire``

#### In production (only on WebFaction)

* ``../arcfire_admin.sh start``

(or ``../arcfire_admin.sh restart``/``../arcfire_admin.sh stop``, depending.)

The ``arcfire_admin.sh`` script gets Gunicorn running, and connects the software to the WebFaction port.  Other hosts will require a different solution.


### Running the test suite

This should work (only on development; I don't know how to run tests in production/staging):

* ``./manage.py test arcfire.tests --settings=core.settings.test``

TODO: adapt for Coverage.


### Docs

I just created some Sphinx docs for the first time.  I will expand as I learn more about this project, and as I write code.

The tutorial to setup Sphinx is here:

* http://www.marinamele.com/2014/03/document-your-django-projects.html

To build the documentation:

* ``docs$ make html``
