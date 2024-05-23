def comparestring(filep):
    examplestring = ["<html>", "</html>", "<img>", "<script>", "<button>",
                       ".msi", ".exe", ".pdf", ".pptx", ".xsl", ".bat", "</https:>",
                       "http", "drive"]
    with open(filep, 'r') as file:
      with open(outfilep, 'w') as outfile:
        for line_number, line in enumerate(file, start=1):
            for examplestring in examplestring:
                if examplestring in line:
                    outfile.write(f"Line {line_number}: {line.strip()}\n")
                    break
   
filep = "~/bobprojectpython/emailcrawlraw/emailraw.txt"
outfilep = "~/bobprojectpython/result/result.txt"
examplestring(filep)


