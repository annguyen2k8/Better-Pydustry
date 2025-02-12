Better Pydustry
=================
# A module check info server mindustry.
It's insprited by https://github.com/RCR-OOP/pydustry.py but I made it better.

How to install it?
------------------
.. code:: sh
   pip install pydustry

Or...

.. code:: sh
   pip install git+https://github.com/annguyen2k8/Better-Pydustry

Example
^^^^^^^

.. code:: python

   from pydustry import Network

   server = Network.getServer("103.20.96.24")
   print(server) 
   # Host(ping=7, name='[#0073E]V[#00BFF]N[#00FFF]M \ue807', address='103.20.96.24', port=6567, mapName='[#0073E]V[#00BFF]N[#00FFF]M [#FF149]HUB [#FFFF]\ue807', wave=1, players=0, version=146, versionType='official', mode='survive', playerLimit=30, description='MindustryTool server hub', modeName='HUB')