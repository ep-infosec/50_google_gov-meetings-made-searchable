#!/usr/bin/env python

# This is not an officially supported Google product, though support
# will be provided on a best-effort basis.

# Copyright 2018 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License"); you
# may not use this file except in compliance with the License.

# You may obtain a copy of the License at:

#    https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import cgi
import utilities
import ujson as json


def meetingCount(orgIdentifier):
	sqlCmd = """select
		count(*) from meetingRegistry
		where orgIdentifier = %s
		and youtubeId is not NULL"""
	sqlData = (orgIdentifier)
	resultList = utilities.dbExecution(sqlCmd, sqlData)

	return resultList[2][0][0]


def main():
	passedArgs = cgi.FieldStorage()
	orgIdentifier = passedArgs["orgId"].value

	outputObj = {}
	outputObj["headerTxt"] = "__Jumbotron_Display_Name_for_Municipality__"
	outputObj["supportingTxt"] = "Public meetings and hearings"
	outputObj["headerImg"] = "img/sample-outline-map.jpg"
	outputObj["videoCnt"] = meetingCount(orgIdentifier)

	print "Content-Type: application/json\n"
	print json.dumps(outputObj)


if __name__ == "__main__":
	main()