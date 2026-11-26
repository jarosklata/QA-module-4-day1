# Web site for the QA module 4 labs (the web/ folder), for deployment with Coolify.
# The build context is the repository root, because the site imports code from
# the lab, optional task and workshop folders.
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HOST=0.0.0.0 \
    PORT=8000

WORKDIR /app

# Only the folders the site reads. Keep these paths in step with web/server.py.
COPY web ./web
COPY DAY1-Labs ./DAY1-Labs
COPY Optional/Optional-Task-2/weather.py ./Optional/Optional-Task-2/weather.py
COPY Optional/Optional-Task-3/postcode_lookup.py ./Optional/Optional-Task-3/postcode_lookup.py
COPY Optional/Optional-Task-3/data ./Optional/Optional-Task-3/data
COPY DAY4-Workshop/football-monitor/part8-documentation/football_monitor.py ./DAY4-Workshop/football-monitor/part8-documentation/football_monitor.py

RUN useradd --system --no-create-home app
USER app

EXPOSE 8000

# Loading the postcode data takes a few seconds, so allow time before checking.
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
    CMD python -c "import os, urllib.request; urllib.request.urlopen('http://127.0.0.1:' + os.environ['PORT'] + '/api/modules', timeout=4)"

CMD ["python", "web/server.py"]
