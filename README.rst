`ffmpegio-plugin-plugin-static-ffmpeg`: A Python `ffmpegio` plugin to use FFmpeg binaries in `static-ffmpeg` package
====================================================================================================================

|pypi| |pypi-status| |pypi-pyvers| |github-license| |github-status|

.. |pypi| image:: https://img.shields.io/pypi/v/ffmpegio-plugin-static-ffmpeg
  :alt: PyPI
.. |pypi-status| image:: https://img.shields.io/pypi/status/ffmpegio-plugin-static-ffmpeg
  :alt: PyPI - Status
.. |pypi-pyvers| image:: https://img.shields.io/pypi/pyversions/ffmpegio-plugin-static-ffmpeg
  :alt: PyPI - Python Version
.. |github-license| image:: https://img.shields.io/github/license/python-ffmpegio/python-ffmpegio-plugin-static-ffmpeg
  :alt: GitHub License
.. |github-status| image:: https://img.shields.io/github/workflow/status/python-ffmpegio/python-ffmpegio-plugin-static-ffmpeg/Run%20Tests
  :alt: GitHub Workflow Status

Python `ffmpegio` package aims to bring the full capability of `FFmpeg <https://ffmpeg.org>`__
to read, write, and manipulate multimedia data to Python. FFmpeg is an open-source cross-platform 
multimedia framework, which can handle most of the multimedia formats available today.

`ffmpegio-plugin-static-ffmpeg` adds a capability to use the FFmpeg and FFprobe executable 
distributed in `static-ffmpeg` Python package.

To use the plugin, it just needs to be installed via `pip`, and `ffmpegio` will automatically detect 
the paths to FFmpeg and FFprobe when it is imported in a Python script.

.. code-block:: bash

  pip install ffmpegio-plugin-static-ffmpeg
