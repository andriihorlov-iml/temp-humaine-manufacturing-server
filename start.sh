#!/bin/bash
# Render передає порт в $PORT
uvicorn server:app --host 0.0.0.0 --port ${PORT:-8081}