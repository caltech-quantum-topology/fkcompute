# Development Notes

## Install For Development

```bash
pip install -e .
pip install -e ".[full]"   # optional extras (sympy/rich/yaml/jupyter)
```

## Build The C++ Backend

The packaging build uses CMake (via scikit-build-core). For local work:

```bash
cmake -B build -S .
cmake --build build
```

This copies the built binary to `src/fkcompute/_bin/fk_main`.

For fast C++ iteration, you can also use:

```bash
make -C cpp fk_main
make -C cpp clean
```

## Tests

Run the focused public Python tests:

```bash
PYTHONPATH=src python -m pytest -q
```

The public suite covers the HiGHS-backed ILP feasibility checks, stable ILP
CSV output for small braids, inversion search ordering, and full
sign-assignment deduplication. Larger baseline datasets remain outside the
public snapshot.

For C++ build validation:

```bash
make -C cpp fk_main
make -C cpp clean
```

Python bytecode and C++ build outputs are ignored by `.gitignore`.

## Where To Make Changes

- CLI commands: `src/fkcompute/cli/commands.py`
- Public API: `src/fkcompute/api/compute.py`
- Config handling: `src/fkcompute/api/batch.py`, `src/fkcompute/infra/config.py`
- Inversion search: `src/fkcompute/inversion/*`
- Constraint system + reduction: `src/fkcompute/domain/*`
- ILP writer + HiGHS integration: `src/fkcompute/solver/ilp.py`
- Symbolic formatting: `src/fkcompute/output/symbolic.py`
- Mathematica bridge: `src/fkcompute/mathematica_bridge.py` and `mathematica/FkCompute/Kernel/FkCompute.wl`

## Versioning

The version is declared in:

- `pyproject.toml` (`[project].version`)
- `src/fkcompute/__init__.py` (`__version__`)

The man page header in `fk.1` also contains a version string.

## Design Boundary

The domain layer (`src/fkcompute/domain/`) is intended to be pure and testable:

- Avoid file I/O and subprocess calls there.
- Put system interactions in `src/fkcompute/infra/`.
