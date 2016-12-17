import os
import os.path


rootdir = '/the_path_to_your_src'

for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        peer_path = os.path.join(parent,filename)
        with open(peer_path, "r") as src:
        	data = src.read()
        with open("out.md", "a+") as out
            out.write("# " + peer_path)
            out.write("\n\n```\n")
            out.write(data)
            out.write("\n```\n")