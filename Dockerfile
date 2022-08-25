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

FROM python:3.10 AS builder
ARG PIP_INDEX_URL=https://pypi.org/simple/
# build wheels for all dependencies in /app/dist (compiling binary distributions for sdists containing non-python code)
RUN mkdir --parents /app/dist
COPY requirements.txt /app/requirements.txt
RUN pip wheel --requirement /app/requirements.txt --wheel-dir /app/dist


###############################################################################
# Stage 2: create the distributable plugin image
# use a 'slim' image for running the actual plugin

FROM python:3.10-slim
# copy and install the dependencies in wheel form from the builder
RUN mkdir --parents /app/dist
COPY --from=builder /app/dist/*.whl /app/dist/
RUN pip install --no-index /app/dist/*.whl

# copy the actual plugin file, run that on port 8999
COPY plugin.py /app
EXPOSE 8999
ENTRYPOINT ["/usr/local/bin/serve_plugin", "-v"]
CMD ["/app/plugin.py", "8999"]
