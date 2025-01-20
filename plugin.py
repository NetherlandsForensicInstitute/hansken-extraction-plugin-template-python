from datetime import datetime
from typing import Sequence, Mapping

from hansken.util import Vector
from hansken_extraction_plugin.api.extraction_plugin import ExtractionPlugin
from hansken_extraction_plugin.api.plugin_info import Author, MaturityLevel, PluginId, PluginInfo, PluginResources
from hansken_extraction_plugin.decorators.transformer import transformer

from hansken_extraction_plugin.runtime.extraction_plugin_runner import run_with_hanskenpy
from logbook import Logger

log = Logger(__name__)


class Plugin(ExtractionPlugin):

    def plugin_info(self):
        plugin_info = PluginInfo(
            id=PluginId('nfi.nl', 'simple-plugin'),
            version='0.0.1',
            description='simple plugin with transformer',
            author=Author('Kean-Yew Lee', 'k.lee@nfi.nl', 'NFI'),
            maturity=MaturityLevel.PROOF_OF_CONCEPT,
            webpage_url='https://openai.com/blog/clip/',
            license='MIT',
            matcher=r'type:picture AND $data.mimeType:image\/*',
            resources=PluginResources(maximum_cpu=1, maximum_memory=12288),
        )
        return plugin_info

    def process(self, trace, data_context):
        log.info(f"processing trace {trace.get('name')}")
        # Add your plugin implementation here


if __name__ == '__main__':
    # optional main method to run your plugin with Hansken.py
    # see detail at:
    #  https://netherlandsforensicinstitute.github.io/hansken-extraction-plugin-sdk-documentation/latest/dev/python/hanskenpy.html
    run_with_hanskenpy(Plugin)

    @transformer
    def text_to_features(self, text: str) -> str:
        string = [str, ":)"]

        return ''.join(string)

    @transformer
    def picture_to_features(self, data: bytes) -> Vector:
        return


    @transformer
    def increment_by_one(self, number: int) -> int:
        return number + 1


    @transformer
    def reverse_boolean(self, boolean: bool) -> bool:
        return not boolean


    @transformer
    def increment_by_one_and_a_half(self, number: float) -> float:
        return number + 1.5


    @transformer
    def date_test(self, date: datetime) -> datetime:
        return date


    @transformer
    def vector_test(self, vect: Vector) -> Vector:
        return vect


    @transformer
    def get_last_from_sequense(self, seq: Sequence) -> str:
        return seq[-1]


    @transformer
    def check_map_contain_hansken(self, map: Mapping) -> bool:
        return map.__contains__("hansken")

