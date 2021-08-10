# file used by distutils to create a distributable package and generate requirements.txt
from setuptools import setup


package_name = "extraction_plugin_skeleton"
version_string = "0.0.0"

dependencies = [
    "hansken-extraction-plugin==0.3.0",  # the plugin SDK
]

setup(
    name=package_name,
    version=version_string,
    author='YOUR NAME HERE',
    author_email='YOUR EMAIL HERE',
    description='PLUGIN DESCRIPTION HERE',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=['plugin'],
    include_package_data=True,
    install_requires=dependencies,
)
