#!/usr/bin/env python3

from xml.etree import ElementTree as et
import sys, re, os

BASE = 'base'
LWT = 'lwt'
TRAINING = 'training'
TMVA = 'TMVA'
CONVERTER = 'converter'
THEANO = 'theano'


def run():
    args = {'xml': sys.argv[1], 'outdir': 'figures'}
    print_with([BASE], BASE, **args)
    print_with([BASE, TRAINING], TRAINING, **args)
    print_with([BASE, TRAINING, TMVA], 'tmva', **args)
    print_with([BASE, TRAINING, THEANO], THEANO, **args)
    print_with([BASE, TRAINING, THEANO, LWT], LWT, **args)
    print_with([BASE, TRAINING, THEANO, LWT, CONVERTER], CONVERTER, **args)

def _use_element(element, layers):
    lab_re = re.compile('.*label.*')
    for attr, val in element.attrib.items():
        if lab_re.search(attr):
            if val in layers:
                return True
            else:
                return False
    return False

def print_with(layers, name, xml, outdir):
    ns = {'svg':'http://www.w3.org/2000/svg',
          'inkscape': "http://www.inkscape.org/namespaces/inkscape"}
    tree = et.parse(xml)
    svg = tree.getroot()
    for element in svg.findall("svg:g", namespaces=ns):
        if not _use_element(element, layers):
            svg.remove(element)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    tree.write('{}/{}.svg'.format(outdir, name))

if __name__ == "__main__":
    run()
