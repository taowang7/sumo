#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, match = netedit.setupAndStart(neteditTestRoot)

# recompute
netedit.rebuildNetwork()

# go to select mode
netedit.selectMode()

# select first edge
netedit.leftClick(match, 250, 180)

# select second edge
netedit.leftClick(match, 250, 100)

# go to inspect mode
netedit.inspectMode()

# inspect selected edges
netedit.leftClick(match, 250, 180)

# Change parameter 11 with a non valid value
netedit.modifyAttribute(11, "%%%$$$$$%")

# Change parameter 11 with a valid value
netedit.modifyAttribute(11, "my own name")

# recompute
netedit.rebuildNetwork()

# Check undos
netedit.undo(match, 1)

# recompute
netedit.rebuildNetwork()

# check redos
netedit.redo(match, 1)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)