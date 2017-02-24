
import logging
LOG = logging.getLogger(__name__)

import os, re, sys
import sass                 # pip install libsass
from bl.dict import Dict    # ordered dict with string keys
from bl.string import String
from .css import CSS

class SCSS(CSS):

    def render_css(self, fn=None, text=None, margin='', indent='\t'):
        """output css using the Sass processor"""
        from .css import CSS
        fn = fn or os.path.splitext(self.fn)[0]+'.css'
        if not os.path.exists(os.path.dirname(fn)):
            os.makedirs(os.path.dirname(fn))
        os.chdir(os.path.dirname(fn))               # needed in order for scss to relative @import
        LOG.debug(self.render_styles())
        return CSS(fn=fn, 
            text=sass.compile(string=text or self.render_styles()))
    
