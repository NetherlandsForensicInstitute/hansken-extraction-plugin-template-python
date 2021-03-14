# Hansken extraction skeleton plugin for Python

This repository contains a skeleton for a Hansken extraction plugin written in Python.
This skeleton plugin is a minimal but complete example of a plugin implementation,
including all required build steps.
You can simply clone this skeleton plugin and start your implementation from here.

To transform this skeleton in your plugin your may want to:

* Update the plugin info in `plugin/extraction_plugin.py`
* Update the plugin info in `setup.py`
* Create test input data in the folder `testdata/input`
  (refer to the SDK manual for more details on how to define testdata)
* Implement your plugin `process()` logic in `plugin/extraction_plugin.py`
* (Re)generate your expected test result data with `tox -e regenerate`
* Verify your expected test result data in `testdata/result`
* Update this `README.md`
* Publish your plugin to the Hansken community!

The Hansken extraction plugin developer guide contains further information on how to get started.


## Building this plugin

To build this plugin into a Docker image that can be used in future releases
of Hansken, you can run the following command:
  `tox && docker build -t your_plugin_name`

Verify that your plugin works as expected by running:
  `tox -e verify-plugin your_plugin_name`
