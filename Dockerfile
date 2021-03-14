FROM nexus.dev.holmes.nl:5000/hansken/python:3.8-slim AS base

FROM base AS builder
ARG PIP_INDEX_URL="https://nexus.dev.holmes.nl/repository/pypi-all/simple"
RUN mkdir -p /install
COPY dist distribution
RUN pip install --prefix='/install' --no-warn-script-location --index-url=${PIP_INDEX_URL} distribution/*.whl

FROM base
LABEL hansken.extraction.plugin true
COPY --from=builder /install /usr/local
COPY /plugin /
EXPOSE 8999
ENTRYPOINT ["/usr/local/bin/serve_plugin"]
CMD ["extraction_plugin.py", "8999"]
