# Multi-stage Dockerfile, to build and package an extraction plugin
#  Recommended way to build the plugin is by calling poe:
#    poe package
#  if you need to pass a proxy:
#    poe package -- --build-arg https_proxy=https://your-proxy
#  if you want to pass a private Python package index:
#     poe package -- --build-arg PIP_INDEX_URL=https://your-pypi-mirror

###############################################################################
# Stage 1: build the plugin
# use a 'fat' image to setup the dependencies we'll need

FROM python:3.14 AS builder
ARG PIP_INDEX_URL=https://pypi.org/simple/
ENV UV_INDEX_URL=${PIP_INDEX_URL}
RUN python -m venv /venv
ENV VIRTUAL_ENV="/venv"
ENV UV_PROJECT_ENVIRONMENT="/venv"
ENV PATH="/venv/bin:$PATH"
RUN pip install uv
WORKDIR /app

# Change package name to match your plugin.
COPY dist/hansken_extraction_plugin_template_python-*-py3-none-any.whl /app/
RUN uv pip install /app/hansken_extraction_plugin_template_python-*.whl

###############################################################################
# Stage 2: create the distributable plugin image
# use a 'slim' image for running the actual plugin

FROM python:3.14-slim
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

EXPOSE 8999
ENTRYPOINT ["serve_plugin", "-v"]
CMD ["hansken_extraction_plugin_template_python.plugin", "8999"]
