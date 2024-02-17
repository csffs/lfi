# Description:

The lfi parser contains a python script lfi_parce.py and a dictionary lfi.txt, 

## Files:

lfi.txt - this dictionary contains a list of important directories by 

 lfi_parce.py - this file adds paths from the lfi.txt file to the specified link.  

For example :

if:
       
       python lfi_parce.py -u 'http://test/../../..'

then the addition will look like this:
       http://test/../../../link_lfi (for example /etc/passwd)

## Usage :

lfi_parce.py contains the -h and -u options 

The options mean:
  -h, --help show arguments
  -u URL, --url URL lfi link, example https://test.com?url=file://

## Output:

the results are output to the console, as well as to the file lfi_res.txt in the same directory where the script is run.




