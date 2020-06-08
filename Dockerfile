FROM python:3-alpine
WORKDIR /app
COPY . .
EXPOSE 5000
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install -e .
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=js_example
CMD flask run —host=0.0.0.0
