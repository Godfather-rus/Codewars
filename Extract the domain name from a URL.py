import re

def domain_name(url):
    #pattern = r"\bp[a-z]*"
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

def domain_name2(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

def domain_name3(url):
    return re.search("(//|www.)(\w+)[.]", url).group(2)

def domain_name4(url):
    headers = ["http://", "https://", "www.", "http://www", "https://www."]
    for header in headers:
        if header in url:
            url = url.replace(header, "")
    domain = url.split(".")[0]
    return domain

if __name__ == '__main__':
    print(domain_name("http://google.com"))