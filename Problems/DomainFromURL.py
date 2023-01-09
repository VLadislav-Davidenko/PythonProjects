def domain_name(url):
    if "http://www." in url:
        url = url.replace("http://www.", "")
    elif "https://www." in url:
        url = url.replace("https://www.", "")
    elif "https://" in url:
        url = url.replace("https://", "")
    elif "www." in url:
        url = url.replace("www.", "")
    else:
        url = url.replace("http://", "")
    x = url.find(".")
    return(url[:x])
    #return url.split("//")[-1].split("www.")[-1].split(".")[0]

print(domain_name("http://google.com"))
print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))