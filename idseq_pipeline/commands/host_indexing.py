"""The host-indexing command."""
from .base import Base


class Host_indexing(Base):
    """Perform indexing"""

    def run(self):
        from .host_indexing_functions import *

        set_up_stdout()
        make_indexes(self.version)
