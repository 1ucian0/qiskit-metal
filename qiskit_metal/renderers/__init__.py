# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
=================================================
Renderers (:mod:`qiskit_metal.renderers`)
=================================================

.. currentmodule:: qiskit_metal.renderers

Created on Tue May 14 17:13:40 2019

@author: Zlatko

UNDER CONSTRUCTION

Renderer Base
---------------

.. autosummary::
    :toctree: ../stubs/

    QRenderer
    QRendererGui


MPL Renderer
---------------

.. autosummary::
    :toctree: ../stubs/

    PlotCanvas-TBD
    MplInteraction-TBD
    ZoomOnWheel-TBD
    PanAndZoom-TBD
    QMplRenderer-TBD


MPL Submodules
---------------

.. autosummary::
    :toctree: ../stubs/

    mpl_interaction-TBD
    mpl_toolbox-TBD


Ansys Submodules
----------------

.. autosummary::
    :toctree: ../stubs/

    config-TBD
    parse-TBD


"""

from .setup_default import setup_renderers

from .. import config
if config.is_building_docs():
    from .renderer_base.renderer_base import QRenderer
    from .renderer_base.renderer_gui_base import QRendererGui
