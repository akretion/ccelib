# -*- coding: utf-8 -*-

import os
import sys
from os import path
from xmldiff import main
sys.path.append(path.join(path.dirname(__file__), '..', 'ccelib'))
from ccelib.v1_00 import leiauteCCe as cce


def test_in_out_leiauteCCe():
    path = 'tests/cce/v1_00/leiauteCCe'
    for filename in os.listdir(path):
        inputfile = '%s/%s' % (path, filename,)
        obj = cce.parse(inputfile)

        outputfile = 'tests/output.xml'
        with open(outputfile, 'w') as f:
            obj.export(f, level=0, name_='evento',
                namespacedef_='xmlns="http://www.portalfiscal.inf.br/nfe"')

        diff = main.diff_files(inputfile, outputfile)
        print(diff)
        assert len(diff) == 0

def test_init_all():
    for mod in [cce]:
        for class_name in mod.__all__:
            cls = getattr(mod, class_name)
            if issubclass(cls, mod.GeneratedsSuper):
                cls()
