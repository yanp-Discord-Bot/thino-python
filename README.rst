thino-python
-------------
A simple async API wrapper for thino.pics API


This library was made for use with libraries such as discord.py, though let alone, this libary will work perfectly normally as long as there is an asyncio enviroment.

**Python 3.8 or higher**

To install the library, run the following command

.. code:: sh

  #Linux/macOS
  python3 -m pip install -U git+https://github.com/yanp-Discord-Bot/thino-python
  
  #Windows
  py -m pip install -U git+https://github.com/yanp-Discord-Bot/thino-python
  
Quick Example
-------------
  
.. code:: py
  
  import thino
  import asyncio
  
  async def main():
    return await thino.img("tomboy")

  tomboy_result = asyncio.run(main())
  print(tomboy_result)
