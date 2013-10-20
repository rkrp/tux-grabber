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
	#Checking if it is a directory listing
	try:
		if pDoc.head.title.text[:8] != ("Index of"):
			return 
	except:
		return
	dirList=[]
	fileList=[]
	
	try:
		for link in pDoc.html.body.findAll("a"):
			#Checking whether URL is valid
			if isValidUrl(link.get('href'))==False:
				continue;
			
			urlHref=link.get('href')
			
			if urlHref[-1:]=='/': #Checking if it is directory
				dirList.append(target+urlHref)
			else:
				fileList.append(target+urlHref)
	except:
		return
	#output
	printList(target,dirList,fileList)
	
	#Grabbing the subdirs		
	for subDir in dirList:
		startGrabbing(subDir)
		#~ print target+subDir

def fetchDoc(url):
	print "getting from "+url
	r=requests.get(url);
	if r.status_code != 200:
		print "Cannot fetch Document!"
		exit;
	return r.text

def isValidUrl(url):
	if url[:1]=='?' or url[:1]=='/':
		return False
	else:
		return True;
		
def printList(target,dirList,fileList):
	if len(fileList)!=0:
		#~ print target+" - Files:"
		for filename in fileList:
			print filename
	
	if len(dirList)!=0:
		#~ print target+" - Folders:"
		for dirName in dirList:
			print dirName

def main():
	target="http://kernel.org/pub/"
	startGrabbing(target)
	
	
if __name__ == '__main__':
	main()
	
