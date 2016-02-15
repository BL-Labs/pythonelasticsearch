#!/bin/bash

if [ -f venv/bin/activate ]; then
  echo "Sandbox environment is already set up"
else
  pyvenv-3.4 venv
  source venv/bin/activate
  pip install elasticsearch elasticsearch_dsl
  echo "Python environment is now setup."
fi
echo "Run the following to enter the python environment:"
echo "  source venv/bin/activate"
