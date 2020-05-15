import os
import sys
import re
import subprocess
try:
	from PIL import Image
except ImportError:
	print("WARNING: Install Pillow if you want to use to_png extraction!")

def countPages(filename):
	''' Counts number of pages in PDF '''

	# NOTE: Currently does not work 100% of the time
	rxcountpages = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE|re.DOTALL)
	data = open(filename,"r", encoding = "ISO-8859-1").read()
	return len(rxcountpages.findall(data))

def to_png(file_loc, pages_to_extract=()):
	''' Converts PDF to PNG image

	Args
	- - - - - - -
		file_loc: path to pdf document, string
		pages_to_extract: list of pages to extract, if empty all pages will be extracted

	Returns
	- - - - - - -
		pngs: list of PIL.PngImageFile
	'''
	pages=pages_to_extract
	try:
		if os.path.isabs(file_loc):
			full_file_loc = file_loc
		else:
			cd = os.getcwd()
			full_file_loc = os.path.join(cd, file_loc)
		pngs = []
		actual_count = 0
		num = countPages(full_file_loc)
		# Accounts for errors occuring in countPages function
		if num == 0:
			num = 100
		for i in range(num):
			actual = i + 1
			if (not pages) or (pages and any(actual is element for element in pages)):
				subprocess.call(['pdftopng', '-f', str(actual),'-l', str(actual), full_file_loc, full_file_loc.replace('.pdf','')])
				# Opens file saved to disk
				num_string = '-' + str(actual).zfill(6) + '.png'
				saved_file = full_file_loc.replace('.pdf',num_string)
				if os.path.exists(saved_file)_
					image = Image.open(saved_file)
					pngs.append(image)
					os.remove(saved_file)
			actual_count += 1
		return pngs
	except NameError:
		raise ImportError("Pillow library is not installed!")

def to_text(file_loc, page_nums = True):
	''' Converts PDF to text

	Args
	- - - - - - -
		file_loc: path to pdf document, string
		page_nums: whether to insert page numbers into document, boolean

	Returns
	- - - - - - -
		text: extracted text from pdf document, string
		actual_count: estimated number of pages for pdf document, integer

	'''

	# Determines location of file
	if os.path.isabs(file_loc):
		full_file_loc = file_loc
	else:
		cd = os.getcwd()
		full_file_loc = os.path.join(cd, file_loc)

	text = ''
	actual_count = 0

	# If page numbers are to be inserted
	if page_nums:
		# Count number of pages
		num = countPages(full_file_loc)
		# Accounts for errors occuring in countPages function
		if num == 0:
			num = 100
		for i in range(num):
			actual = i + 1
			# Calls xpdf
			subprocess.call(['pdftotext', '-f', str(actual),'-l', str(actual), full_file_loc])
			# Opens file saved to disk
			saved_file = full_file_loc.replace('.pdf','.txt')
			file = open(saved_file,'r', encoding = "ISO-8859-1")
			t = file.read()
			# If the page is blank, it is not a real page
			if t == '':
				continue
			else:
				actual_count += 1
			# Add text and page count to existing string
			text += '***Page {}*** {}'.format(actual, t)
			file.close()
	else:
		# TO BE IMPLEMENTED
		pass

	# Remove file saved to disk
	os.remove(saved_file)

	return text, actual_count

def extract_images(file_loc):
	''' Extracts images from PDF document

	Args
	- - - - - - -
		file_loc: path to pdf document, string

	Returns
	- - - - - - -
		image_locs: location of saved images files, list

	'''
	# Determines location of file
	if os.path.isabs(file_loc):
		full_file_loc = file_loc
	else:
		cd = os.getcwd()
		full_file_loc = os.path.join(cd, file_loc)

	subprocess.call(['pdfimages'])
