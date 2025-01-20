from hansken_extraction_plugin.api.extraction_plugin import ExtractionPlugin
from hansken_extraction_plugin.api.plugin_info import Author, MaturityLevel, PluginId, PluginInfo, PluginResources
from hansken_extraction_plugin.decorators.transformer import transformer
from hansken_extraction_plugin.runtime.extraction_plugin_runner import run_with_hanskenpy
from logbook import Logger

log = Logger(__name__)


class Plugin(ExtractionPlugin):

    def plugin_info(self):
        plugin_info = PluginInfo(
            id=PluginId(domain='domain', category='category', name='your_plugin_name'),
            version='0.0.0',
            description='description of your plugin',
            author=Author('Your name', 'your@email.address', 'your organisation'),
            maturity=MaturityLevel.PROOF_OF_CONCEPT,
            webpage_url='',  # e.g. url to the code repository of your plugin
            matcher='$data.type=raw',  # add the query for the types of traces your plugin should match
            license='Apache License 2.0',
            resources=PluginResources(maximum_cpu=2, maximum_memory=512, maximum_workers=6),
        )
        return plugin_info

    def process(self, trace, data_context):
        log.info(f"processing trace {trace.get('name')}")
        # Add your plugin implementation here

    # @Transformer enables the HANSKEN to execute code in the plugin
    # The transformer can be found in when you expand the plugin in the extraction tools
    # the transformers can be accessed with the /tools/transformers URL in HANSKEN
    @transformer
    def example_transformer(self, number: int) -> int:
        return number + 1

if __name__ == '__main__':
    # optional main method to run your plugin with Hansken.py
    # see detail at:
    #  https://netherlandsforensicinstitute.github.io/hansken-extraction-plugin-sdk-documentation/latest/dev/python/hanskenpy.html
    run_with_hanskenpy(Plugin)

