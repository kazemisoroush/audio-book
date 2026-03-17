#!/bin/bash
set -e

echo "Configuring Git..."
git config --global user.email 'kazemi.soroush@gmail.com'
git config --global user.name 'Soroush Kazemi'

# Dependencies are pre-installed in the Docker image (see Dockerfile).
# This re-registers the package in editable mode against the mounted source.
# It is fast — pip skips deps that are already satisfied.
echo "Registering package in editable mode..."
pip install --quiet --no-deps -e ".[dev]"

echo ""
echo "Post-create setup complete. Dependencies are ready."
echo ""
echo "Common commands:"
echo "  audiobook --help"
echo "  pytest -v"
echo "  ruff check src/ tests/"
echo "  mypy src/"
