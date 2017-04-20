import sublime
import sublime_plugin
import re

class SingleLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
		    if not region.empty():
		        s = self.view.substr(region)

		        pattern = re.compile(r'^(.*)(\{[\S\s]*\}\s*\;?\s*)$')

		        match = pattern.match(s)

		        if match:
		        	dec = match.group(1)
		        	obj = match.group(2)

		        obj = re.sub('\s', '', obj)

		        obj = re.sub('{', '{ ', obj)
		        obj = re.sub(':', ': ', obj)
		        obj = re.sub(',', ', ', obj)
		        obj = re.sub('}', ' }', obj)

		        self.view.replace(edit, region, dec + obj)
