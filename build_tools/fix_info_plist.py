#!/usr/bin/env python
# -*- coding: utf-8 -*-#
###############################################################################
#
# fix_info_plist.py: Support script for coffeegrindsize Mac executable build
#
###############################################################################
#
# This file contains a Python script to assist in the process of
# building a Mac executable for the coffeegrindsize application.
#
# Its input is the default Info.plist file that pyinstaller generates.
# It modifies that file as follows:
#
#   - Changes the value of CFBundleShortVersionString to the version
#     number in the version.txt file
#   - Adds NSHumanReadableCopyright with the copyright string
#   - Adds NSHighResolutionCapable, set to True
#   - Adds NSRequiresAquaSystemAppearance, set to True (NO Dark Mode)
#
#  usage: fix_info_plist.py [-h] info_plist_file
#
#  positional arguments:
#    info_plist_file  (full or relative path)
#
#  optional arguments:
#    -h, --help       show this help message and exit
#
from __future__ import print_function
from __future__ import unicode_literals
import argparse
import plistlib
import os


def get_version():
    try:
        version_file = os.path.join(os.environ['GITHUB'],
                                    "coffeegrindsize",
                                    "build_tools",
                                    "version.txt")
    except KeyError:
        print("**************************************************************")
        print("* ERROR: you must have the environment variable $GITHUB set  *")
        print("*  e.g.:   export GITHUB=\"$HOME/GitHub\"                      *")
        print("**************************************************************")
        raise
    try:
        with open(version_file, "r") as f:
            lines = f.read().splitlines()
            if len(lines) != 1:
                print("ERROR: {} has {} lines".format(version_file,
                                                      len(lines)))
                return "vFIXME"
            version = lines[0]
            if len(version) == 0 or version[0] != 'v':
                print("ERROR: {} has invalid version: {}"
                      .format(version_file, version))
                return "vFIXME"
            print("Application version: {}".format(version))
            return version
    except IOError:
        print("ERROR: {} doesn't exist".format(version_file))
        return "vFIXME"


# Parse command line args
parser = argparse.ArgumentParser()
parser.add_argument("info_plist", metavar='info_plist_file',
                    type=str, nargs=1,
                    help=("(full or relative path)"))
args = parser.parse_args()

# Get the version number
app_path = os.path.join(".", "dist", "coffeegrindsize")
version_from_file = get_version()           # vX.X.X
version = version_from_file[1:]             # X.X.X

# Read Info.plist into a plist object
try:
    # Python 3
    with open(args.info_plist[0], 'rb') as fp:
        plist = plistlib.load(fp)
except AttributeError:
    # Python 2
    plist = plistlib.readPlist(args.info_plist[0])

# Change version number
plist['CFBundleShortVersionString'] = version

# Add copyright string
plist['NSHumanReadableCopyright'] = u"Copyright © 2021  Jonathan Gagne"

# Enable retina display resolution
plist['NSHighResolutionCapable'] = True

# Write the modified plist back to the Info.plist file
if hasattr(plistlib, 'dump'):
    # Python 3
    plist['NSRequiresAquaSystemAppearance'] = True  # DISABLE dark mode
    with open(args.info_plist[0], 'wb') as fp:
        plistlib.dump(plist, fp)
else:
    # Python 2
    plistlib.writePlist(plist, args.info_plist[0])
