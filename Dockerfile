# Multi-stage Dockerfile, to build and package an extraction plugin
#  Recommended way to build the plugin is by calling tox:
#    tox -e package
#  if you need to pass a proxy:
#    tox -e package -- --build-arg https_proxy=https://your-proxy
#  if you want to pass a private Python package index:
#     tox -e package -- --build-arg PIP_INDEX_URL=https://your-pypi-mirror

###############################################################################
# Stage 1: build the plugin
# use a 'fat' image to setup the dependencies we'll need

FROM python:3.13 AS builder
ARG PIP_INDEX_URL= https://nexus.dev.holmes.nl/repository/pypi-all/simple
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt /requirements.txt
RUN pip install -Ur /requirements.txt

LABEL maintainer="k.lee@nfi.nl"
LABEL hansken.extraction.plugin.name="simple-plugin"

###############################################################################
# Stage 2: create the distributable plugin image
# use a 'slim' image for running the actual plugin

FROM python:3.13-slim
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

COPY plugin.py /app/
EXPOSE 8999
ENTRYPOINT ["serve_plugin", "-v"]
CMD ["/app/plugin.py", "8999"]
