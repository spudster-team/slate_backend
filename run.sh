#!/usr/bin/env bash
export DJANGO_SETTINGS_MODULE=slate.settings
uvicorn slate.wsgi:application --host 0.0.0.0 --port 8000
