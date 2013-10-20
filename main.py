#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2013 Krishna Ram <geekytux@fox>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import requests
from BeautifulSoup import BeautifulSoup

def startGrabbing(target):
	doc=fetchDoc(target)
	pDoc=BeautifulSoup(doc)
	dirList=[]
	fileList=[]
	for link in pDoc.html.body.table.findAll("a"):
		if isValidUrl(link.get('href'))==False:
			continue;
		compUrl=target+link.get('href')
		if compUrl[-1:]=='/': #Checking if it is directory
			dirList.append(compUrl)
		else:
			fileList.append(compUrl)
	print fileList
	print dirList

def fetchDoc(url):
	r=requests.get(url);
	if r.status_code != 200:
		print "Cannot fetch Document!"
		exit;
	return r.text

def isValidUrl(url):
	if url[:1]=='?' or url=='/':
		return False
	else:
		return True;

def main():
	target="http://localhost/projects/"
	startGrabbing(target)
	
	
if __name__ == '__main__':
	main()
	
