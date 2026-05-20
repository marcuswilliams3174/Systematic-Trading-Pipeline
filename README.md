# Systematic Trading Research Platform

End-to-end quantitative trading framework that transforms raw market signals into a fully risk-adjusted portfolio simulation.

## Pipeline

Signal → Position → PnL → Risk Normalization → Returns → Equity Curve

## Core Modules

- Signal generation (alpha logic)
- Position sizing (bounded exposure)
- Backtesting engine (vectorized)
- Risk normalization (vol scaling)
- Performance analytics
- Streamlit dashboard interface

## Key Features

- Robust return normalization pipeline
- Stable equity curve construction
- Drawdown analysis
- Modular architecture (production-style separation)
- Interactive dashboard (Streamlit)

## Tech Stack

Python, Pandas, NumPy, Matplotlib, Streamlit

## Outputs

- Equity curve
- Drawdown series
- Return distribution
- Signal diagnostics
- Saved dashboard plots

## How to Run

```bash
streamlit run streamlit_app.py
