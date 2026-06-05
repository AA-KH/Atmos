#!/bin/sh

mkdir -p data/exports

python -m src.create_database

python main.py run-all

streamlit run app.py --server.address=0.0.0.0