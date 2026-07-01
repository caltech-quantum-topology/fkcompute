Installation
============

This page covers all steps required to build and install **fkcompute**,
including the compiled C++ backend and its system-level dependencies.

.. tip::

   It is strongly recommended to install **fkcompute** inside a dedicated
   Python environment rather than into your system Python.  This avoids
   dependency conflicts with other packages and makes it easy to remove or
   upgrade the installation later.

   .. tab-set::

      .. tab-item:: venv (standard library)

         .. code-block:: bash

            python -m venv fkenv
            source fkenv/bin/activate      # macOS / Linux
            # fkenv\Scripts\activate       # Windows

      .. tab-item:: conda / mamba

         .. code-block:: bash

            conda create -n fkenv python=3.11
            conda activate fkenv

   All subsequent ``pip install`` commands should be run with the environment
   active.

System Dependencies (C++ Backend)
----------------------------------

The C++ backend requires three libraries to be installed at the system level
before you run ``pip install``.  The build system (CMake) will detect them
automatically.

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Library
     - Purpose
     - Minimum version
   * - **FLINT** (+ GMP)
     - Arbitrary-precision polynomial arithmetic
     - 2.8
   * - **OpenMP**
     - Parallel loop execution in the backend
     - runtime ≥ 4.5
   * - **BLAS** (OpenBLAS recommended)
     - Dense linear algebra
     - any

You also need a C++ compiler and CMake.

.. tab-set::

   .. tab-item:: macOS (Homebrew)

      .. code-block:: bash

         brew install flint libomp openblas

         # Optional: make sure CMake >= 3.20 is available
         brew install cmake

   .. tab-item:: Ubuntu / Debian

      .. code-block:: bash

         sudo apt-get update
         sudo apt-get install \
             libflint-dev \
             libgomp1 \
             libopenblas-dev \
             cmake \
             g++

   .. tab-item:: RHEL / Fedora / CentOS

      .. code-block:: bash

         sudo yum install \
             flint-devel \
             gcc-openmp \
             openblas-devel \
             cmake \
             gcc-c++


Installing the Python Package
------------------------------

Once system dependencies are present, install the package from the repository
root with ``pip``:

.. code-block:: bash

   pip install .

The build system (**scikit-build-core** + CMake) will automatically compile
``fk_main`` and bundle it inside the wheel at ``fkcompute/_bin/fk_main``.

Optional Extras
~~~~~~~~~~~~~~~

Several features are gated behind optional Python dependencies that you can
install alongside the package:

.. code-block:: bash

   # Symbolic polynomial output (pretty / LaTeX / Mathematica)
   pip install ".[symbolic]"

   # Rich-based interactive terminal wizard
   pip install ".[interactive]"

   # YAML configuration file support
   pip install ".[yaml]"

   # Jupyter / IPython visualization utilities
   pip install ".[viz]"

   # Everything at once
   pip install ".[full]"

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Extra
     - Python packages installed
     - Unlocks
   * - ``symbolic``
     - ``sympy >= 1.10``
     - ``--symbolic``, ``--format latex``, ``matrix_to_polynomial()``
   * - ``interactive``
     - ``rich >= 13``
     - ``fk`` interactive wizard, progress bars
   * - ``yaml``
     - ``PyYAML >= 6``
     - YAML config files (``.yaml`` / ``.yml``)
   * - ``viz``
     - ``ipython >= 8``, ``jupyter``
     - Jupyter notebook integration
   * - ``full``
     - all of the above
     - Everything


HiGHS Solver
------------

**fkcompute** uses the open-source `HiGHS <https://highs.dev/>`_ solver through
the ``highspy`` Python package to check integer-program feasibility and
boundedness. ``highspy`` is installed automatically by ``pip install .`` and
does not require a separate solver installation or licence.

To verify the solver installation:

.. code-block:: python

   import highspy

   print("HiGHS OK, version:", highspy.Highs().version())


Development Install
--------------------

To install in editable mode (so that changes to Python source files are
immediately reflected without reinstalling):

.. code-block:: bash

   # Install Python layer in editable mode
   pip install -e .

   # Build C++ backend separately
   cmake -B build -S .
   cmake --build build

   # Run the test suite
   pytest

.. note::

   After any change to C++ source files you must re-run ``cmake --build build``
   and copy the resulting ``fk_main`` binary to ``src/fkcompute/_bin/``.

Verifying the Installation
---------------------------

.. code-block:: bash

   # Check that the CLI is on your PATH
   fk --help

   # Run a quick computation
   fk simple "[1,1,1]" 2

You should see a JSON result dictionary printed to the terminal.

.. code-block:: python

   # Or from Python
   from fkcompute import fk
   result = fk([1, 1, 1], 2)
   print(result["metadata"]["components"])  # 1
