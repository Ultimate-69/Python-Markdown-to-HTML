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
    return line

if __name__ == "__main__":
    main()