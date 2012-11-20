Lumos: a pure Python E1.31 library
==================================

Lumos is a Python library for working with DMX512_ lighting control signals sent
over ethernet. This is done using multicast UDP as a sub-protocol of ACN_
referred to as E1.31 or streaming ACN.

.. _DMX512: http://en.wikipedia.org/wiki/DMX512
.. _ACN: http://en.wikipedia.org/wiki/Architecture_for_Control_Networks

This is currently only an implementation of basic transmit functionality.

Usage
-----

The entirety of the current functionality is exposed through a single class::

    from lumos import DMXSource

    source = DMXSource(universe=1)

    # data is an iterable of DMX512 bytes
    data = [255] * 50

    source.send_data(data)
