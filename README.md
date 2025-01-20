# Hansken Extraction Plugin template for Python based on version 0.9.1

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
* implement your own @transformers in the example_transformer() [`plugin.py`](plugin.py)
  transformers are an optional feature
  To implement a transformer add a tag @transformer above the desired function you want as transformer
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
* `tox -e package`: creates a extraction plugin OCI/Docker image that can be published to Hansken (requires Docker)
* `tox -e upgrade`: regenerates `requirements.txt` from [`requirements.in`](requirements.in)

Note: see the readme text in the [`Dockerfile`](Dockerfile) if you need to set proxies or private Python package registries for building a plugin.


> [!IMPORTANT]  
> Plugins based on this template require Hansken version `47.22.0` or higher.
> If your Hansken version is lower, please use the template tagged with `version/0.7.1`, or downgrade the used SDK in the following way:
>  * set the `hansken-extraction-plugin` version to `0.7.4` in [requirements.in](requirements.in)
>  * and then run:
>    ```shell
>    tox -e upgrade
>    ```
