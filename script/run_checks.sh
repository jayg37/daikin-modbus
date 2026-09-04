#!/usr/bin/env bash
set -euo pipefail
uv sync --extra dev
uv run ruff check .
uv run ruff format --check .
uv run pytest
