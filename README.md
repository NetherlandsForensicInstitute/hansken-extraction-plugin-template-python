# Hansken Extraction Plugin template for Python based on version 0.9.5

This repository contains a template for a Hansken extraction plugin written in Python.
This template is a minimal but complete example of a plugin implementation, including all required build steps.
You can simply clone this template plugin and start your implementation from here.

The [Hansken Extraction Plugins for plugin developers documentation](https://netherlandsforensicinstitute.github.io/hansken-extraction-plugin-sdk-documentation/latest/)
 contains further information on how to [get started](https://netherlandsforensicinstitute.github.io/hansken-extraction-plugin-sdk-documentation/latest/dev/python/getting_started.html).


To transform this skeleton in your plugin your may want to:

* Update the plugin info in [`plugin.py`](plugin.py)
* Create test input data in the folder [`testdata/input`](testdata/input)
  (refer to the [SDK manual for more details on how to define test data](https://netherlandsforensicinstitute.github.io/hansken-extraction-plugin-sdk-documentation/latest/dev/concepts/test_framework.html))
* Implement your plugin `process()` logic in [`plugin.py`](plugin.py)
* (Optional) Implement your own transformers(https://netherlandsforensicinstitute.github.io/hansken-extraction-plugin-sdk-documentation/latest/dev/python/transformers.html) in the example_transformer() [`plugin.py`](plugin.py),
  or remove the transformer method from the plugin.
* Add your dependencies by using `uv add <dependency>`. Once all dependencies are added, run `poe upgrade` to update the `uv.lock` file.
* Add any system dependencies to the [`Dockerfile`](Dockerfile)
* (Re)generate your expected test result data with `poe regenerate`
* Verify your expected test result data in [`testdata/result`](testdata/result)
* Update this `README.md`
* Publish your plugin to the Hansken community!

Tox commands that may be useful:
* `poe tests`: runs your tests
* `poe integration-test`: runs your tests against the packaged version of your plugin (requires Docker)
* `poe regenerate`: regenerates the expected test results (use after you update your plugin)
* `poe package`: creates a extraction plugin OCI/Docker image that can be published to Hansken (requires Docker)
* `poe upgrade`: regenerates the [uv.lock](uv.lock) file

Note: see the readme text in the [`Dockerfile`](Dockerfile) if you need to set proxies or private Python package registries for building a plugin.

> [TIP] If you want to pass in additional arguments to the  poe tasks separate poe args with `--`. FOr example:
> `poe package -- -t docker_image_tag`


> [!TIP]
> If you want to update your plugin to a newer Hansken Plugin SDK version, run `uv add hansken-extraction-plugin==<new_version>`.

> [!IMPORTANT]  
> Plugins based on this template require Hansken version `47.22.0` or higher.
> If your Hansken version is lower, please update the Hansken Plugin SDK version to `0.7.4`.
