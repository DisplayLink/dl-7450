.. currentmodule:: network
.. _network.LAN:

class LAN -- control an Ethernet interface
==========================================

This class allows you to control the Ethernet interface.

Constructors
------------

.. class:: LAN()

   Create a LAN driver object.

.. method:: LAN.ifconfig()

   Get the IP address, subnet mask, gateway and DNS for the interface. This
   method returns a 4-tuple with the above information. For example::

      ip, subnet, gw, dns = nic.ifconfig()


.. method:: LAN.mac()

   Get the MAC address of the network interface. For example::
   
      mac_address = nic.mac()

