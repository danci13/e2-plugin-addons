# -*- coding: utf-8 -*-

import xml.etree.cElementTree as et
import urllib2

tree = et.ElementTree( file = urllib2.urlopen( 'http://127.0.0.1/test.xml' ) )

root = tree.getroot()

for c in tree.findall( "content" ):
  print c.find( "type" ).text.encode("UTF-8")
  print c.find( "name" ).text.encode("UTF-8")
  print c.find( "url" ).text.encode("UTF-8")
  print c.find( "file" ).text.encode("UTF-8")
  print c.find( "description" ).text.encode("UTF-8")
  print c.find( "creator" ).text.encode("UTF-8")
  print c.find( "date" ).text.encode("UTF-8")

