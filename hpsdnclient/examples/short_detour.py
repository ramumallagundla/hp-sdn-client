#!/usr/bin/env python
#
# Copyright (c)  2013 Hewlett-Packard Development Company, L.P.
#
# Permission is hereby granted, fpenrlowee of charge, to any person
# obtaining a copy of this software  and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR  OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import hpsdnclient as hp

""" Short Detour 2.0 """

# initialize the api
controller = '10.44.254.129'
auth = hp.XAuthToken(user='sdn',password='skyline', server=controller)
api = hp.Api(controller=controller, auth=auth)

#create the match object
match = hp.datatypes.Match(eth_type="ipv4",ipv4_src="10.0.0.1",
                       ipv4_dst="10.0.0.22",ip_proto="tcp",
                       tcp_dst="80")

#create the action objects
output1 = hp.datatypes.Action(output=1)
output6 = hp.datatypes.Action(output=6)

#create the flows
flow1 = hp.datatypes.Flow(priority=30000, idle_timeout=30,
                          match=match, action=output6)
flow2 = hp.datatypes.Flow(priority=30000, idle_timeout=30,
                          match=match, action=output1)

#push the flows to the datatpaths
api.add_flows('00:00:00:00:00:00:00:0e', flow1)
api.add_flows('00:00:00:00:00:00:00:01', flow1)
api.add_flows('00:00:00:00:00:00:00:0b', flow2)