from helpers import Flattener, MRFOpen

def flatten_json(loc, out_dir, code_set = None, npi_set = None):
    """
    Pattern for flattening JSON and filtering with a code_set/npi_set.
    Functions like a finite state machine.
    """

    with MRFOpen(loc) as f:

        flattener = Flattener(code_set, npi_set)
        flattener.init_parser(f)

        # Build (but don't write) the root data
        flattener.build_root()

        # Jump (fast-forward) to provider references
        # Build (but don't write) the provider references
        flattener.ffwd(('', 'map_key', 'provider_references'))
        flattener.build_provider_references()
        flattener.build_remote_provider_references()
        flattener.make_provider_ref_map()

        """
        Sometimes it happens that the MRF is out of order: 
        the provider references are at the bottom. Fast-forwarding
        to the in-network items will result in a StopIteration.

        In this case, re-open the file (start a new parser in a
        new context) and then FFWD to the in-network items,
        while holding onto the previously computed provider references
        and root data.
        """

        try:
            flattener.ffwd(('in_network', 'start_array', None))
            while flattener.current_row != ('in_network', 'end_array', None):
                # Build and write the in-network items and 
                # all related data
                flattener.build_next_in_network_item()
                flattener.write_in_network_item(out_dir)
            return
        except StopIteration:
            pass

    with MRFOpen(loc) as f:
        flattener.init_parser(f)

        flattener.ffwd(('in_network', 'start_array', None))
        while flattener.current_row != ('in_network', 'end_array', None):
            flattener.build_next_in_network_item()
            flattener.write_in_network_item(out_dir)
        return