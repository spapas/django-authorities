==================
django-authorities
==================

An application for managing your organization's authorities (departments, directorates etc). This is an app built to mainly cover the needs of the organization I work for (a public sector organization in Greece); however feel free to use it if you like it.

Rationale
=========

This more or less is a *better* ``auth.Group`` to help you building the hierarchy of an organization. Why not just use ``auth.Group``? Well, unfortunately, ``auth.Group`` is missing various needed things like:

* ``category``: You may have departments, teams, directoratates
* ``active``: Some authorities are de-activated; they should not be deleted though
* ``parent``: You'll need to have a proper authority hierarchy

Also, for me the django ``auth.Group`` entity feels more like an application/system-related concept (vs the HR Authority provided in this add-on). I.e you can have a django auth group of "Administrators" or "Advanced users" or "Moderators" etc; these people may belong to various directorates; not all people in the "IT department" need to be Administrators of the application.

Now, there are *more* things that may be useful for an authority/HR system, like

* ``manager``: Who manages the authority
* ``user-job``: The users of an authority may have different jobs like manager (this is complementary to the first one), teller, client development etc

I haven't added these fields yet because I don't need them for my projects. If the need arises I'll add them.

Installation
============

Install it with ``pip install django-authorities``, or if you want to use the latest version on github, try ``pip install git+https://github.com/spapas/django-authorities``.

After it is installed, put ``authorities`` in your ``INSTALLED_APPS`` setting.  

Simple usage
============

This is a very simple app with two models and a couple of views for editing these.

After you've installed it, you can visit the django admin to edit ``authorities.Authority`` and
``authorities.AuthorityKind``. ``AuthorityKind`` only has a name (so it can be directorate, department
team etc) while ``Authority`` has ``kind`` (``AuthorityKind``), ``is_active`` (boolean), ``parent`` 
(an optional FK to another ``Authority`` to create hierarchies) and ``users`` (an M2M relation with 
``settings.AUTH_USER_MODEL``; each user can belong to multiple authorities and each authority will
have more than one user).

Also I've included a couple of non-admin views which you can use
as they are or modify them to fit your needs. Either inherit from or and them in your own urls.py as they are or ``include`` the
whole ``authorities.urls``. The templates of these views inherit from a ``base.html`` which needs 
to provide a ``content`` and a ``{% page_title %}`` block. Thus your ``base.html`` template could be like this:


.. code::

    <html>
        <body>
            <h1>{% block page_title %}{% endblock %}</h1>
            {% block content %}{% endblock %}
        </body>
    </html>


These views are:

- authorities.views.AuthorityListView
- authorities.views.AuthorityCreateView
- authorities.views.AuthorityUpdateView
- authorities.views.AuthorityDetailView
- authorities.views.AuthorityEditUsersView


The names are self-explanatory; notice that the Create and Update views do not allow you to edit the users of that authority; you must use the ``AuthorityEditUsersView`` for that.

You can either use these views in your urls.py or just add something like ``path("authorities/", include("authorities.urls")),`` in your urls.py.

To improve security a bit I'm checking that a user has the proper permission for authority in the app's urls.py before allowing access to these views, i.e ``authorities.view_authority``
for list and view, ``authorities.add_authority`` for add and ``authorities.change_authority`` for edit and edit users.


To use the provided template tag, you need to ``{% load authorities_tags %}`` and then you can do something
like this in your template:

.. code::

    {% if user.is_authenticated %}
        {% user_authorities as my_authorities %}
        {% if my_authorities %}
            My authorities are: 
            <ul>
            {% for a in my_authorities  %}
                <li>{{ a.name }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endif %}
	
v.0.2.3
-------

- Improve permissions

v.0.2.2
-------

- Fix MANIFEST.in to include locale files


v.0.2.1
-------

- Add a missing migration

v.0.2.0
-------

- Add greek translations
- Improve standard views a bit
- Add some security to the builtin views


v.0.1.2
-------

- Add template tags to get current user authorities
- Improve README

v.0.1.0
-------

- Initial version
