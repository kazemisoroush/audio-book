#!/bin/bash
set -e

echo "Configuring Git..."
git config --global user.email 'kazemi.soroush@gmail.com'
git config --global user.name 'Soroush Kazemi'

echo "Installing Python dependencies..."
pip install -e ".[dev]"

echo "Running tests..."
python -m pytest tests/ -v

echo ""
echo "Post-create setup complete!"
echo ""
echo "To generate an audiobook:"
echo "  audiobook books/pg1342.txt --discover-characters"
echo "  audiobook books/pg1342.txt"
echo ""
echo "For more options:"
echo "  audiobook --help"
