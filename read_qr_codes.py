import os
import qrtools

def read_qr_codes(directory, search_term, verbose=True):
	# initalize a list for holding our hits
	matches = []

	# for each qr image in the directory ....
	for f in os.listdir(directory):
		img_path = os.path.join(directory, f)
		code = qrtools.QR(filename=img_path)
		# check if we can decode the image
		if code.decode():
			# convert the code to a string
			code_value = code.data_to_string()
			# if verbose is toggled, output the qr code values
			if verbose: print img_path + ", " + code_value

			#if we find the search term add it to the matches list
			if search_term in code_value:
				matches.append({img_path: str(code_value)})
		else:
			print "Could not decode:", img_path

	#print all the matches
	print len(matches), "match(es) were found:"
	for finding in matches:
		for key in finding:
			print key + ', ' + finding[key]

read_qr_codes('/root/Desktop/day9/output','ADCTF_', False)