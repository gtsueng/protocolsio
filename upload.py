import biothings.hub.dataload.uploader
import os

import requests
import biothings
import config
biothings.config_for_app(config)

MAP_URL = "https://raw.githubusercontent.com/SuLab/outbreak.info-resources/master/outbreak_resources_es_mapping.json"
MAP_VARS = ["@type", "abstract", "author", "citedBy", "curatedBy", "dateModified", "datePublished", "doi", "funding", "identifier", "isBasedOn", "issueNumber", "journalName", "journalNameAbbrev", "keywords", "license", "name", "pmid", "publicationType", "relatedTo", "url", "volumeNumber"]

# when code is exported, import becomes relative
try:
    from protocolsio.parser import load_annotations as parser_func
except ImportError:
    from .parser import load_annotations as parser_func


class ProtocolsUploader(biothings.hub.dataload.uploader.BaseSourceUploader):

    main_source="protocolsio"
    name = "protocolsio"
    __metadata__ = {
        "src_meta": {
            "author":{
                "name": "Marco Cano",
                "url": "https://github.com/marcodarko"
            },
            "code":{
                "branch": "master",
                "repo": "https://github.com/marcodarko/biorxiv.git"
            }
        }
    }
    idconverter = None
    storage_class = biothings.hub.dataload.storage.BasicStorage

    def load_data(self, data_folder):
        self.logger.info("No data to load from file for protocolsio")
        return parser_func()

    @classmethod
    def get_mapping(klass):
        r = requests.get(MAP_URL)
        if(r.status_code == 200):
            mapping = r.json()
            mapping_dict = { key: mapping[key] for key in MAP_VARS }
            return mapping_dict