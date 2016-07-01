import os

def read(filename, mode="rt"):
    # rt = "read text"
    with open(filename, mode) as fin:
        return fin.read()

def write(filename, contents, mode="wt"):
    # wt = "write text"
    with open(filename, mode) as fout:
        fout.write(contents)


def main():
	content = read("vocab.txt").splitlines()
	for index in xrange(len(content)):
		meaning = raw_input(content[index]+"\n")
		content[index] = "%s@%s@0"%(content[index], meaning)
		print content[index]
	content = "\n".join(content)
	write("vocab_with_def.txt", content)
	raw_input("Press enter to quit.")
	return

main()
