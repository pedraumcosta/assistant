# One image for the three kinds of container: the agent's tools, the
# verdict, and the ground-truth checks. Standard library plus pytest.
FROM python:3.12-slim
RUN pip install --no-cache-dir pytest==9.1.1
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /work
