#!/usr/bin/python
import web

def main(msg)
	print(msg)

main("Hello people")

urls = (
	'/', 'myClass'
	'/about', 'secondClass
	)
class myClass:
	def GET(self):
		return "<h1>Hello World</h1>"
		
class secondClass:
	def GET(self)
		return "<h1>This is a second route</h1>"

application = web.application(urls, globals()).wsgifunc()
