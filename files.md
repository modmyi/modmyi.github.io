Click [here](https://raw.githubusercontent.com/modmyi/modmyi.github.io/main/css_files/list_of_debs.txt) to view the list of debs on this repository.

Click [here](https://raw.githubusercontent.com/modmyi/modmyi.github.io/main/css_files/debs_i_dont_have.txt) to view the list of files (from ModMyi's wayback archive) that I do not have. 

Click [here](https://raw.githubusercontent.com/modmyi/modmyi.github.io/main/script.py) to download the script I used to sort the files into the Packages file.
<details>
  <summary><i>(quick rundown of how the script works, if anyone needs it)</i></summary>
  Sorry if this explanation is a bit hard to understand...  

  Here is how the script works:
  First, 90% of the package names from the archive are formatted like this:
```
  |       tweak ID       |     |architecture|
  |                      |     |           /
  com.jamied360.ncsettings_1.0_iphoneos-arm.deb
      |author | |       |  | |
                | name  |  | |
                           | |
                         version
```
  So it can automatically grab the tweak ID, author, name, version, and architecture just from the filename.

  <b>0.5. Grabs tweak ID, author, name, version, and architecture from filename.</b> It pulls up a cydiacrawler page `https://www.cydiacrawler.com/index.php?cat=package&id=[[PACKAGE-ID]]` and requests the content from it.  

  
  <b>1. Grabs package info from cydiacrawler.com using HTML scraping (e.g. grabs text from the website).</b>  
  It comes out looking somewhat like this:  
  `Name: NCSettingsDescription: Toggles in your notification center!Depencencies: (...)`  
  The reason for that is because cydiacrawler has no API that I can request package info from (AFAIK). So I have to grab the text from the HTML code of the webpage.
  
  <b>2. Seperates text into new lines to later grab info from it.</b>  
  ```
Name: NCSettings
Description: Toggles in your notification center!
Depencencies: (...)"
```
  <b>3. Gets info from seperated new lines.</b>
  ```
name = 'NCSettings'
desc = 'Toggles in your notification center!'
depencencies = '(...)'
```
  <b>4. Gets size and md5sum (not from cydiacrawler) and puts it in a template.</b>
  ```
Package: com.jamied360.ncsettings
Version: 1.0
Section: Addons
Maintainer: ModMyi
Architecture: iphoneos-arm
Size: 42
MD5sum: qwertyuiop12345
Description: Toggles in your notification center!
Name: NCSettings
Author: jamied360
Dependence: [left blank if there are none]
Filename: debs/com.jamied360.ncsettings_1.0_iphoneos-arm.deb
Conflict: [left blank if there are none]
```
  <b>5. Shoves it into the packages file and continues to the next. Pretty simple.</b>
</details>
  If there are any issues downloading files (the script isn't perfect, as sometimes it can't format text right...) please message [/u/East-Box-8015](https://www.reddit.com/u/East-Box-8015).
