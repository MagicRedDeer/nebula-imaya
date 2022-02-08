# -*- coding: utf-8 -*-

from __future__ import print_function

import pymel.core as pc

try:
    import xgenm.xmaya.xgmExternalAPI as xgmapi
except ImportError:
    pc.loadPlugin('xgenToolkit.mll')
    import xgenm.xmaya.xgmExternalAPI as xgmapi


def load_xgen():
    loaded = pc.pluginInfo('xgenToolkit', loaded=True, q=True)
    if not loaded:
        pc.loadPlugin('xgenToolkit.mll')


def patch_guides(patch, description):
    return [guide for guide in xgmapi.descriptionGuides(description)
            if xgmapi.guidePatch(guide) == patch]


def print_xgentree():
    for palette in xgmapi.palettes():
        print('{} : paletter')
        for description in xgmapi.descriptions(palette):
            print('\t{} : Description'.format(description))
            for patch in xgmapi.descriptionPatches(description):
                print('\t\t{} : Patch'.format(patch))
                for guide in patch_guides(patch, description):
                    print('\t\t\t{} : Guide'.format(guide))


if __name__ == '__main__':

    def example_file():
        pc.openFile(
            'd:/talha.ahmed/Documents/maya/projects/default/scenes'
            '/abdul_kareem_hair.ma',
            force=True)

    #  example_file()
    load_xgen()
    print_xgentree()
