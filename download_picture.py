import requests
import os

def download_picture(url, save_path):
	try:
	    if not os.path.exists(save_path)
	    	os.mkdir(svae_path)
	    if not os.path.exists(save_path)
	    	r = requests.get(url)
	    	with open(save_path, 'wb') as f:
	    		f.write(r.content)
	    		f.close()
	    		print("download_picture success!\n")
	    else:
	    	print("Picture has existed!\n")
	except:
		print ("download error!\n")


def main():
