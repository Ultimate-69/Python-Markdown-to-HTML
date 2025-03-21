import os

def main():
    path_to_file = str(input("Enter the path to your md file: "))
    if (os.path.isfile(path_to_file)):
        if os.path.splitext(path_to_file)[1] != ".md":
            print("Not a markdown file.")
            return

        print("reading file...")
        md_file = open(path_to_file, "r")
        html = ""

        for line in md_file:
            html += convert_to_html(line)

        md_file.close()
        html_file = open(os.path.splitext(md_file.name)[0] + ".html", "w")
        html_file.write(html)
        html_file.close()
    else:
        print("invalid path to file.")
        return



def convert_to_html(line):
    if line[0] == "#":
        hashtag_count = 0
        for i in line:
            if i == "#":
                if hashtag_count <= 5:
                    hashtag_count += 1
                else:
                    hashtag_count = 6
        line = line[hashtag_count:]
        line = f"<h{hashtag_count}>" + line.strip() + f"</h{hashtag_count}>\n"
    elif line[0] == ">":
        line = line[1:]
        line = "<blockquote>" + line.strip() + "</blockquote>\n"
    elif line.strip() == "---" or line.strip() == "***":
        line = "<hr>\n"
    else:
        if line.strip() != "":
            line = "<p>" + line.strip() + "</p>\n"

    for char in line:
        print(char)pass
    return line

if __name__ == "__main__":
    main()