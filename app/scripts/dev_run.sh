#!/bin/bash
set -e
set -x

# run dev
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
