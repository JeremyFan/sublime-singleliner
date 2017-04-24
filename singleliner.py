import sublime
import sublime_plugin
import re

class SingleLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
		    if not region.empty():
		        s = self.view.substr(region)
		        result=[]

		        pattern = re.compile(r'^(.*\{)([\S\s]*)(\}[\S\s]*)$')

		        arr=s.split('=')

		        for i,a in enumerate(arr):
		        	match = pattern.match(a)

		        	if match:
		        		prefix = match.group(1)
		        		obj = match.group(2)
		        		postfix = match.group(3)

		        		obj = re.sub('\s', '', obj)

		        		prefix = re.sub('{', '{ ', prefix)
		        		obj = re.sub(':', ': ', obj)
		        		obj = re.sub(',', ', ', obj)
		        		postfix = re.sub('}', ' }', postfix)

		        		result.append(''.join([prefix, obj, postfix]))

		        	else:
		        		result.append(a)

		        self.view.replace(edit, region, '='.join(result))