#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import pywr
import xmlutils

def test_simple1():
	'''Test parsing a simple XML document'''
	# parse the XML into a model
	data = file('simple1.xml', 'r').read()
	model = xmlutils.parse_xml(data)

	# metadata
	assert(model.metadata['title'] == 'Simple 1')
	assert(model.metadata['description'] == 'A very simple example.')

	# node names
	nodes = model.nodes()
	assert(len(nodes) == 3)
	name_to_node = {}
	for node in nodes:
		name_to_node[node.name] = node
	supply1 = name_to_node['supply1']
	link1 = name_to_node['link1']
	demand1 = name_to_node['demand1']

	# node types
	assert(type(supply1) is pywr.Supply)
	assert(type(link1) is pywr.Link)
	assert(type(demand1) is pywr.Demand)

	# node positions
	assert(supply1.position == (1,1))
	assert(link1.position == (2,1))
	assert(demand1.position == (3,1))

	model.check()
