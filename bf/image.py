
import logging
log = logging.getLogger(__name__)

import math, os, shutil, sys, subprocess
from bl.file import File

class Image(File):

    def gm(self, cmd, **params):
        args = ['gm', cmd]
        for key in params.keys():
            args += ['-'+key]
            if str(params[key]) != "":
                args += [str(params[key])]
        args += [self.fn]
        log.debug("%r" % args)
        o = subprocess.check_output(args).decode('utf8')
        return o.strip()

    def mogrify(self, **params):
        return self.gm('mogrify', **params)

    def identify(self, **params):
        return self.gm('identify', **params)

    def convert(self, outfn=None, **params):
        args = ['gm', 'convert', self.fn]
        if outfn is None: 
            outfn = self.fn
        for key in params.keys():
            args += ['-'+key, str(params[key])]
        args += [outfn]
        log.debug("%r" % args)
        if not os.path.exists(os.path.dirname(outfn)):
            os.makedirs(os.path.dirname(outfn))
        o = subprocess.check_output(args).decode('utf8')
        return o.strip()
