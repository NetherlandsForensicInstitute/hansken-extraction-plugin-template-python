# Hansken Extraction Plugin skeleton for Python based on version 0.6.1

This repository contains a template for a Hansken extraction plugin written in Python.
This template is a minimal but complete example of a plugin implementation, including all required build steps.
You can simply clone this template plugin and start your implementation from here.

The [Hansken Extraction Plugins for plugin developers documentation](https://netherlandsforensicinstitute.github.io/hansken-extraction-plugin-sdk-documentation/latest/)
 contains further information on how to [get started](https://netherlandsforensicinstitute.github.io/hansken-extraction-plugin-sdk-documentation/latest/dev/python/getting_started.html).


To transform this skeleton in your plugin your may want to:

* Update the plugin info in [`plugin.py`](plugin.py)
* Create test input data in the folder [`testdata/input`](testdata/input)
  (refer to the SDK manual for more details on how to define test data)
* Implement your plugin `process()` logic in [`plugin.py`](plugin.py)
* Add your plugin dependencies to [`requirements.in`](requirements.in)
  and regenerate `requirements.txt` by calling `tox -e upgrade`
* Add any system dependencies to the [`Dockerfile`](Dockerfile)
* (Re)generate your expected test result data with `tox -e regenerate`
* Verify your expected test result data in [`testdata/result`](testdata/result)
* Update this `README.md`
* Publish your plugin to the Hansken community!

Tox commands that may be useful:
* `tox`: runs your tests
* `tox -e integration-test`: runs your tests against the packaged version of your plugin (requires Docker)
* `tox -e regenerate`: regenerates the expected test results (use after you update your plugin)
* `tox -e upgrade`: regenerates `requirements.txt` from [`requirements.in`](requirements.in)
* `tox -e package`: creates a extraction plugin OCI/Docker image that can be published to Hansken (requires Docker)

Note: see the readme text in the [`Dockerfile`](Dockerfile) if you need to set proxies or private Python package registries for building a plugin.
