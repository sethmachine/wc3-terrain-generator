"""Transforms Warcraft III terrain data (.w3e) to and from numpy data structures.

"""


import hivewe.archive
import hivewe.terrain
import hivewe.terrain_manipulator
import hivewe.terrain_tiles
import hivewe.wc3_runner
import numpy

import utils

WC3_ROC_MAPS = 'data/maps'
WC3_TFT_MAPS = 'data/maps/FrozenThrone'


def get_wc3_map_files(indir):
    files = utils.absolute_filepaths(indir, 0, r'.+?\.w3[xm]')
    return files

def get_tft_map_files(indir=WC3_TFT_MAPS):
    return get_wc3_map_files(indir)

def get_roc_map_files(indir=WC3_ROC_MAPS):
    return get_wc3_map_files(indir)

def get_all_map_files():
    f1 = [x for x in get_roc_map_files()]
    f2 = [x for x in get_tft_map_files()]
    return f1 + f2


if __name__ == '__main__':
    l = get_all_map_files()
    tm = hivewe.terrain_manipulator.Terrain_Manipulator(l[5], 'foobar', 'foobar')
    tm.extract_assets()
    tm.read_terrain()
    t = tm.tiles
    y = hivewe.terrain.iter_tiles(tm.tiles)
    z = [x for x in y]
    lh = [x.layer_height for x in z]
    print(set(lh))
    wh = [x.water_height for x in z]
    print(set(wh))
    def foo(tiles):
        for tile in hivewe.terrain.iter_tiles(tiles):
            pass
            # if tile.layer_height == 1:
            #     tile.layer_height = 10
            # tile.ground_height = 8192
            # tile.water_height = 8192
            # tile.cliff_variation = 0
            # tile.cliff_texture = 0
    tm.mod_terrain(callback=foo)
    tm.write_new_terrain()
    w = hivewe.wc3_runner.Wc3_Runner()
    w.run_map(tm.outmap, 'foofbar')