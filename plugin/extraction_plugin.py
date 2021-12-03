from hansken_extraction_plugin.api.extraction_plugin import ExtractionPlugin
from hansken_extraction_plugin.api.plugin_info import Author, MaturityLevel, PluginId, PluginInfo
from logbook import Logger

log = Logger(__name__)


class Plugin(ExtractionPlugin):

    def plugin_info(self):
        plugin_info = PluginInfo(
            self,
            version='0.0.0',
            description='description of your plugin',
            author=Author('Your name', 'your@email.address', 'your organisation'),
            maturity=MaturityLevel.PROOF_OF_CONCEPT,
            webpage_url='',  # e.g. url to the code repository of your plugin
            matcher='$data.type=raw',
            id=PluginId('domain', 'category', 'your_plugin_name'),
            license='Apache License 2.0'
        )
        return plugin_info

    def process(self, trace, data_context):
        log.info(f"processing trace {trace.get('name')}")
        # Add your plugin implementation here
