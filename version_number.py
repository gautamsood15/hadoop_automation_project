def version_change():
	ver=open("/root/project/namenode/VERSION","r")
	re=ver.read()
	posn=re.find("storageType=")
	posn+=12
	ver.close()
	ver=open("/root/project/namenode/VERSION","r+")
	ver.read(posn)
	ver.write("DATA_NODE\nlayoutVersion=-41")
	ver.close()

version_change()
