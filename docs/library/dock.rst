.. currentmodule:: dock

:mod:`dock` --- Dock Management Services
========================================

.. module:: dock
   :synopsis: Dock Management Services

This module contains classes and functions for managing the DL-7450. Using the
functionality in the :py:mod:`dock <dock>` module allows applications to
retrieve and set information to enable local or remote dock management
decision making. The information can be:

   - immutable information such as the dock unique identifier.
   - ephemeral information such as connected devices, the dock's IP address and
     the dock's timezone.
   - live information such as the current network bandwidth.


Classes
-------

.. toctree::
    :maxdepth: 1

    dock.DockInfo.rst
    dock.DockControl.rst

