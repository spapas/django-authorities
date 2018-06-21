==================
django-authorities
==================

An application for managing your organization's authorities (departments, directorates etc)

Installation
============

Install it with ``pip install django-authorities``, or if you want to use the latest version on github, try ``pip install git+https://github.com/spapas/django-authorities``.

After it is installed, put ``authorities`` in your ``INSTALLED_APPS`` setting.  

Simple usage
============

This is a very simple app with two models and a couple of views for editing these.

After you've installed it, you can visit the django admin to edit ``authorities.Authority``s and
``authorities.AuthorityKind``s. ``AuthorityKind`` only has a name (so it can be directorate, department
team etc) while ``Authority`` has ``kind`` (``AuthorityKind``), ``is_active`` (boolean), ``parent`` 
(an optional FK to another ``Authority`` to create hierarchies) and ``users`` (an M2M relation with 
``settings.AUTH_USER_MODEL``; each user can belong to multiple authorities and each authority will
have more than one user).

Also I've included a couple of non-admin views which you can use
as they are or modify. Either inherit from them, put them in your own urls.py or ``include`` the
whole ``authorities.urls``. The templates of these views inherit from a ``base.html`` which needs 
to provide a ``content`` block.


v.0.1.2
-------

- Add template tags to get current user authorities
- Improve README

v.0.1.0
-------

- Initial version
