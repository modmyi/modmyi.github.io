"""
Package: []
Version: []
Section: [tw = tweaks, th= theme]
Maintainer: ModMyi
Architecture: iphoneos-arm
Filename: [auto]
Size: [auto]
MD5sum: [auto]
Description: [pull up cydiacrawler page], typing [NONE] placeholder ,,no info can be found excersice caution"
Name: []
Author: []
Depiction: file:///C:/Users/calvi/Desktop/DEBFILES/depictions/cn.tinyapps.wechatone_1.5_iphoneos-arm.deb.html
"""

"https://web.archive.org/web/20240413231302/https://modmyi.github.io/depictions/unknown.html"


import tkinter as tk
from tkinter import filedialog
import os
import re

mode = input("2: single file // 1: whole folder\n")

root = tk.Tk()
root.withdraw()
#file_path = filedialog.askopenfilename() #FULL PATH
    #filename = os.path.basename(file_path) #FILENAME

if '1' in mode:

    # Get the folder path
    folder_path = filedialog.askdirectory()

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Initialize the file index
    file_index = 0
else:
    file_path = filedialog.askopenfilename() #FULL PATH
    filename = os.path.basename(file_path) #FILENAME

while True:
    
    if '1' in mode:
        # Select the first file
        selected_file_full_path = os.path.join(folder_path, files[file_index])
        selected_file = os.path.basename(selected_file_full_path)

        # Increment the file index for the next iteration
        #file_index += 1

        # If the file index exceeds the number of files, reset it to 0
        if file_index >= len(files):
            break

        # Use selected_file and selected_file_full_path in your code
        #print("Selected File ", selected_file)
        #print("Selected File Full Path:", selected_file_full_path)
        print(f"File {file_index}")

        file_path = selected_file_full_path
        filename = selected_file

    #folder_path = filedialog.askdirectory()


    #print("\n" + filename)


    #md5
    """
    f = open("Packages", "a")
    f.write("\n")
    f.write("\n")
    f.write(finaltoadd)
    f.close()"""

    import hashlib
    f = open(file_path, "rb")
    filecontent = f.read()
    md5 = hashlib.md5(filecontent).hexdigest() ####
    f.close()

    #byte
    file_name = file_path
    file_stats = os.stat(file_name)
    SIZE = file_stats.st_size ####


    def extract_info_from_filename(filename2):
        """
        Extracts package ID, version, and author from the filename
        """
        # Define a regex pattern to match the filename pattern
        pattern = r'^([^_]+)\.([^_]+)\.([^_]+)_([^_]+)_([^_]+)\.deb$'
        match = re.match(pattern, filename)
        if match:
            package_id = f"{match.group(1)}.{match.group(2)}.{match.group(3)}"
            author = match.group(2)
            name = match.group(3)
            version = match.group(4)
            architecture = match.group(5)
            return package_id, author, name, version, architecture
        else:
            print("ERROR! FILE DOES NOT MATCH TEMPLATE...")
                #inputsd
            l1 = input("Package(us.calvin.ncsettings): ")
            import webbrowser
            webbrowser.open(f'https://www.cydiacrawler.com/index.php?cat=package&id={l1}', new=2)
            l2 = input("Version(1.0): ")
            l3 = input("Section(tw=tweak,th=theme,ut=utilities): ")
            l14 = input("Depends (com.calvin.ncsettings): ")
            l4 = 'ModMyi'
            l5 = 'iphoneos-arm'
            l6 = filename
            l7 = SIZE
            l8 = md5
            l9 = input("Description: ")
            l10 = input("Name of tweak(ncsettings): ")
            l11 = input("Author of tweak(calvin): ")
            l13 = input ("Minimum iOS version - Max iOS version (1.0-16.0 or 4.1+): ")
            
            l12 = f"Package: {l1}"
            l22 = f"Version: {l2}"
            if 'tw' in l3:
                l32 = 'Section: Tweaks'
            else:
                l32 = 'Section: Themes'
            l122 = f'Depends: {l14}'
            l42 = 'Maintainer: ModMyi'
            l52 = 'Architecture: iphoneos-arm'
            l62 = f'Filename: ./debs/{filename}'
            l72 = f'Size: {SIZE}'
            l82 = f'MD5sum: {md5}'
            l92 = f'Description: {l9} (Compatible with iOS {l13}.)'
            l102 = f'Name: {l10}'
            l112 = f'Author: {l11}'

            print(f"""
        {l12}
        {l22}
        {l32}
        {l122}
        {l42}
        {l52}
        {l62}
        {l72}
        {l82}
        {l92}
        {l102}
        {l112}
        """)
            return "NON", None, None, None, None

    # Example filename
    filename2 = filename

    # Extract information from the filename
    package_id, author, name, version, architecture = extract_info_from_filename(filename)
    #import webbrowser
    #webbrowser.open(f'https://www.cydiacrawler.com/index.php?cat=package&id={package_id}', new=2)
    

    if "NON" in package_id:
        pass #put in code to extract l__ vars
        print(f"SKIPPED {filename}. COME BACK LATER!")
    else:
        #print("extracted from template.")
        pass

###########################################################################################################################AUTO-GRAB STUFF
    import requests
    from bs4 import BeautifulSoup

    url_input = f'https://www.cydiacrawler.com/index.php?cat=package&id={package_id}'

    # Function to extract information from HTML content
    def extract_info(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        extracted_info = {}

        # Find div with 7px padding
        div_with_padding = soup.find('div', style=lambda style: style and 'padding: 7px' in style)
        if div_with_padding:
            # Extract text from the div
            div_text = div_with_padding.get_text()

            # Split the text into lines
            lines = div_text.split('\n')

            # Iterate over lines and extract label-value pairs
            labels = ["Name:", "Version:", "Updated:", "Price:", "Description:", "Dependence:"]
            for line in lines:
                for label in labels:
                    if label in line:
                        value = line.replace(label, '').strip()
                        extracted_info[label.strip(':')] = value
                        break

        return extracted_info

    # Function to fetch HTML content from a URL
    def fetch_html_content(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching URL: {e}")
            return None

    # URL of the website to scrape
    url = url_input

    # Fetch HTML content from the URL
    html_content = fetch_html_content(url)

    if html_content:
        # Extract information from the HTML content
        info = extract_info(html_content)

        # Print the extracted information neatly
        for key, value in info.items():
            #print(f"{key}: {value}")
            pass
    else:
        print("No HTML content fetched.")

    extracted_info_str = ""
    for key, value in info.items():
        extracted_info_str += f"{key}: {value}"
    extracted_info_str = extracted_info_str.rstrip()

    def split_lines(jumbled_text):
        keywords = ["Name:", "Section:", "Description:", "Dependence:", "Size:", "Conflicts:"]
        lines = []

        # Split the text at each keyword occurrence
        for keyword in keywords:
            index = jumbled_text.find(keyword)
            if index != -1:
                # Special handling for removing text between "Version:" and "Description:"
                if keyword == "Description:":
                    version_index = jumbled_text.find("Version:")
                    if version_index != -1:
                        lines.append(jumbled_text[:version_index].strip())
                else:
                    lines.append(jumbled_text[:index].strip())
                # Stop splitting if "Size:" or "Conflicts:" is found
                if keyword in ["Size:", "Conflicts:"]:
                    break
                jumbled_text = jumbled_text[index:]

        return lines

    # Function to extract fields from lines
    def extract_fields(lines):
        extracted_info = {}
        for line in lines:
            if line.startswith("Name:"):
                extracted_info["Name"] = line.replace("Name:", "").strip()
            elif line.startswith("Section:"):
                extracted_info["Section"] = line.replace("Section:", "").strip()
            elif line.startswith("Description:"):
                extracted_info["Description"] = line.replace("Description:", "").strip()
            elif line.startswith("Dependence:"):
                extracted_info["Dependence"] = line.replace("Dependence:", "").strip()
            elif line.startswith("Conflicts:"):
                extracted_info["Conflicts"] = line.replace("Conflicts:", "").strip()
        return extracted_info


    # Sample jumbled text
    jumbled_text = extracted_info_str

    # Split the jumbled text into separate lines
    lines = split_lines(jumbled_text)

    # Extract fields from lines
    info = extract_fields(lines)

    # Print the extracted information neatly
    for key, value in info.items():
        #print(f"{key}: {value}")
        pass

    my_string = '\n'.join([f"{key}: {value}" for key, value in info.items()])

    def extract_info(text):
        # Initialize variables to store extracted fields
        name = ''
        section = ''
        description = ''
        dependence = ''

        # Split the text into lines
        lines = text.split('\n')

        # Iterate over lines to find and extract the fields
        for line in lines:
            line = line.strip()
            if line.startswith("Name:"):
                name = line.replace("Name:", "").strip()
            elif line.startswith("Section:"):
                section = line.replace("Section:", "").strip()
            elif line.startswith("Description:"):
                description = line.replace("Description:", "").strip()
            elif line.startswith("Dependence:"):
                dependence = line.replace("Dependence:", "").strip()

        return name, section, description, dependence

    # Sample text
    text = my_string

    # Extract information from the text
    name, section, description, dependence = extract_info(text)

    def extract_conflicts(text):
        # Find the index of "Conflicts: " in the text
        index = text.find("Conflicts: ")
        
        # If "Conflicts: " is found, extract the text after it
        if index != -1:
            conflicts = text[index + len("Conflicts: "):]
            return conflicts.strip()  # Remove leading/trailing whitespace
        else:
            return ''

    conflicts = extract_conflicts(description)
    #print(conflicts)

    def remove_words_after_conflicts(text):
        # Find the index of "Conflicts" in the text
        index = text.find("Conflicts")

        # If "Conflicts" is found, remove it along with all words after it
        if index != -1:
            # Find the index of the next newline character after "Conflicts"
            next_newline_index = text.find("\n", index)

            # If a newline character is found after "Conflicts", remove the substring from "Conflicts" to the newline
            if next_newline_index != -1:
                return text[:index] + text[next_newline_index:]
            else:
                # If no newline character is found after "Conflicts", remove "Conflicts" and everything after it
                return text[:index]
        else:
            # If "Conflicts" is not found, return the original text
            return text


    sample_text = description

    # Remove words after conflicts from the sample text
    text_without_words_after_conflicts = remove_words_after_conflicts(sample_text)


    # Print the extracted information
    #print(f"Name: {name}")
    if 'Addons' in section:
        section='Addons'
    elif 'App Add' in section or 'Applica' in section:
        section ='Application'
    elif 'Carrier' in section:
        section='Carrier Bundles'
    elif 'Cydgets (Lock' in section:
        section ='Cydgets (Lock)'
    elif 'Cydia Cate' in section:
        section='Cydia Category'
    elif 'Development' in section:
        section = 'Development'
    elif 'Education' in section:
        section = 'Education'
    elif 'Entertainment' in section:
        section = 'Entertainment'
    elif 'Fonts' in section:
        section = 'Fonts'
    elif 'Games' in section:
        section = 'Games'
    elif 'Keyboards' in section:
        section = 'Keyboards'
    elif 'Localization' in section:
        section = 'Localization'
    elif 'Messaging' in section:
        section = 'Messaging'
    elif 'Multimedia' in section:
        section = 'Multimedia'
    elif 'Navigation' in section:
        section = 'Navigation'
    elif 'Networking' in section:
        section = 'Networking'
    elif 'Productivity' in section:
        section = 'Productivity'
    elif 'Ringtones' in section:
        section = 'Ringtones'
    elif 'Security' in section:
        section = 'Security'
    elif 'Site-Specific' in section:
        section = 'Site-Specific'
    elif 'Social' in section:
        section = 'Social'
    elif 'Soundboards' in section:
        section = 'Soundboards'
    elif 'System' in section:
        section = 'System'
    elif 'Terminal Support' in section:
        section = 'Terminal Support'
    elif 'Theme' in section:
        section = 'Themes'
    elif 'Toys' in section:
        section = 'Toys'
    elif 'Tweak' in section:
        section = 'Tweaks'
    elif 'Utilit' in section:
        section = 'Utilites'
    elif 'Wallpaper' in section:
        section = 'Wallpaper'
    elif 'Widget' in section:
        section = 'Widgets'
    #print(f"Section: {section}")
    #print(f"Description: {text_without_words_after_conflicts}")
    #print(f"Dependence: {dependence}")
    #print(f"Conflicts: {conflicts}")
##########################################################################################################################################

    # SEPERATE DEPENDENCE AND CONFLITCS
    input_string = dependence
    output_string = ""

    i = 0
    while i < len(input_string):
        # If the character is not a space, add it to the output string
        if input_string[i] != " ":
            output_string += input_string[i]
            i += 1
        else:
            # If the next character is a letter or an opening parenthesis, and the previous character is not a comma, add a comma
            if i + 1 < len(input_string) and (input_string[i + 1].isalpha() or input_string[i + 1] == "(") and (i == 0 or input_string[i - 1] != ","):
                output_string += ","
            i += 1


    input_string = output_string
    output_string = re.sub(r',(?=\([^)]+\))', '', input_string)

    output_string = dependence
    
    input_string = conflicts
    output_string = ""

    i = 0
    while i < len(input_string):
        # If the character is not a space, add it to the output string
        if input_string[i] != " ":
            output_string += input_string[i]
            i += 1
        else:
            # If the next character is a letter or an opening parenthesis, and the previous character is not a comma, add a comma
            if i + 1 < len(input_string) and (input_string[i + 1].isalpha() or input_string[i + 1] == "(") and (i == 0 or input_string[i - 1] != ","):
                output_string += ","
            i += 1


    input_string = output_string
    output_string = re.sub(r',(?=\([^)]+\))', '', input_string)

    output_string = conflicts


    finaltoadd= f"""
Package: {package_id}
Version: {version}
Section: {section}
Maintainer: ModMyi
Architecture: iphoneos-arm
Size: {SIZE}
MD5sum: {md5}
Description: {text_without_words_after_conflicts}
Name: {name}
Author: {author}
Dependence: {dependence}
Filename: debs/{filename}
Conflict: {conflicts}
"""
    
    print(finaltoadd)
    
    f = open("Packages.txt", "a", encoding="utf-8")
    f.write("\n")
    f.write(finaltoadd)
    f.close()
    print("Appended to Packages. remember to later convert to BZ2 for changes to take effect.")
    if '1' in mode:
        file_index += 1
    else:
        break

print("DONE!")
from time import sleep
sleep(9999)
