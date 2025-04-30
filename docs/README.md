DL-7450 SDK Documentation
=========================

Building the documentation locally
----------------------------------

If you are making changes to the documentation, you may want to build the
documentation locally so that you can preview your changes.

Install Sphinx, and optionally (for the RTD-styling), sphinx_rtd_theme.
This is preferably done in a virtualenv, which must exist outside of this
`docs` folder. You can automatically install all requirments
with:

     pip install -r requirements.txt

In `docs`, build the docs:

    make html

You'll find the index page at `docs/build/html/index.html`.

