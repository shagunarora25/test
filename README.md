# Axiom SL CI/CD Release Automation Dashboard

A modern Streamlit-based control center for enterprise CI/CD release operations at Axiom SL. The MVP provides a unified interface for pipeline execution, monitoring, logs, artifacts, approvals, and deployments using mock data and service placeholders for future API integration.

## Features

- Executive release dashboard with summary metrics and charts
- Pipeline monitoring and actions with mock responses
- Pipeline log exploration with status coloring
- Nexus artifact tracking and promotion placeholders
- Approval workflow for release candidates
- Environment deployment monitoring and timeline view

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Project structure

- app.py - Main application entry point
- pages/ - Dashboard views for each operational area
- services/ - Placeholder service modules for future API integration
- components/ - Reusable UI building blocks
- mock_data/ - Static JSON datasets used for the MVP
