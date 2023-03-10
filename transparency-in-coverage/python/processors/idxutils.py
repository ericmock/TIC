import ijson
import logging
from mrfutils import MRFOpen

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

def gen_in_network_links(index_loc,):
    """
    Gets in-network files from index.json files
    :param index.json URL:
    """
    with MRFOpen(index_loc) as f:
        count = 0
        parser = ijson.parse(f, use_float=True)
        for prefix, event, value in parser:
            if (
                prefix.endswith('location')
                and event == 'string'
                and 'in-network' in value
            ):
                log.debug(value)
                yield value
                count += 1

    log.debug(f'Found: {count} in-network files.')