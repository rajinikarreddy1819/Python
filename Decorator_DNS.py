class DNS:
    def dns_resolver(func):
        dns_chache = {"WWW.GOOGLE.COM": "199.0.0.1"}
        def wrapper(self, website):
            if website in dns_chache:
                 return dns_chache[website]
            website_ip = func(self,website)
            dns_chache[website] = website_ip
            return website_ip
        return wrapper
    @dns_resolver
    def fetch_ip(self,website):
        dns_server= {
           "WWW.Amazon.com": "54.239.28.85",
            "WWW.Facebook.com": "157.240.22.35",
            "WWW.OpenAI.com": "104.18.33.45"
        }
        return dns_server.get(website, "IP Not Found")
q1 = DNS()
print(q1.fetch_ip("WWW.GOOGLE.COM")  )  
print(q1.fetch_ip("WWW.Amazon.com"))

