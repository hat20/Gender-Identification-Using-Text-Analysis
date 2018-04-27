import os
from os import listdir
import re
import sys

saveToFile = "/home/ht2s/Desktop/Gender-Identification-Using-Text-Analysis/extracted_input_blogFile"

# XML file parser
def parseXMLFile(fileName):
	
	print "Parsing file : ", fileName
	fr = open(fileName)
	xmlData = fr.read()
	fw = open(saveToFile, 'a+')
	xmlData = xmlData.replace('<Blog>', '').replace('</Blog>', '').replace('\n', '').replace('\r', '').replace('urlLink','')
	post_list = xmlData.split('<date>')
	blog_list = []
	for post in post_list:
		try:
			# We don't need date
			date = post.split('</date>')[0]
			# Get the blogpost
			post = post.split('<post>')[1].split('</post>')[0].strip()
			# Write to the file
			fw.write(post + '\n')		
		except:
			pass

	# Close all file handles
	fr.close()
	fw.close()



'''print "1 : Provide File input in XML format"
print "2 : Provide File input in plaintext format"
print "3 : Provide console input"'''

'''syntax python inputDataExtractor.py <FileName> <inputOption>'''


files = []
files = os.listdir("./")

[str(i) for i in files]

for fileName in files:
	if not fileName.endswith('.xml'): 
		continue
	fileName.replace('\'','')
	parseXMLFile(fileName)
	


'''
if str(inputOption) == "1":
	#print "File Name : ",
	#fileName = str(raw_input())
	parseXMLFile(fileName)
elif str(inputOption) == "3":
	print "Enter the text, when done write \"ctrl + D\" in the new line!"
	outputFileHandle = open(saveToFile, "w")
	for line in sys.stdin:
		outputFileHandle.write(line)
	outputFileHandle.close()'''
