import os

root = "../features/"
features = os.listdir(root)

for feature in features:
    if feature == "steps":
        continue

    #print "   code/" + os.path.splitext(feature)[0] + "_feature.rst"
    
    fin = open(root + feature, 'r')
    fout = open("source/code/" + os.path.splitext(feature)[0] +
                "_feature.rst", 'w')

    for line in fin:
        line = line.strip()
        
        if line[0:8] == "Feature:":
            fout.write(line + "\n")
            fout.write("=" * len(line))
            fout.write("\n")

        elif line[0:9] == "Scenario:":
            fout.write("\n" + line + "\n")
            fout.write("^" * len(line))
            fout.write("\n")

        elif line[0:5] == "Given":
            fout.write("\n| **Given**" + line[5:])
            fout.write("\n")

        elif line[0:4] == "When":
            fout.write("| **When**" + line[4:])
            fout.write("\n")

        elif line[0:4] == "Then":
            fout.write("| **Then**" + line[4:])
            fout.write("\n")

        else:
            fout.write(line)

    fin.close()
    fout.close()
