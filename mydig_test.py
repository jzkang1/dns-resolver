import dns
import dns.query
import dns.resolver
import time
import matplotlib

root_servers = [
    "198.41.0.4",
    "199.9.14.201",
    "192.33.4.12",
    "199.7.91.13",
    "192.203.230.10",
    "192.5.5.241",
    "192.112.36.4",
    "198.97.190.53",
    "192.36.148.17",
    "192.58.128.30",
    "193.0.14.129",
    "199.7.83.42",
    "202.12.27.33"
]

sites = [
    "Google.com",
    "Youtube.com",
    "Facebook.com",
    "Qq.com",
    "Taobao.com",
    "Yahoo.com",
    "Zhihu.com",
    "Wikipedia.org",
    "Instagram.com",
    "Netflix.com",
]

print(repr(dns.resolver.get_default_resolver().domain))

def resolver_name(n):
    if n == 0:
        return "own"
    elif n == 1:
        return "local"
    elif n == 2:
        return "google"
    else:
        return ""

def main():
    if len(sites) != 10:
        return

    for domain in sites:
        for resolver in range(2,3):
            server_list = []
            # if resolver == 0:
            #     server_list = root_servers
            # if resolver == 1:
            #     server_list = ["130.245.255.4"]
            if resolver == 2:
                server_list = ["8.8.8.8"]
            else:
                break

            # count number of resolutions in case one fails
            num_resolved = 0
            times = []
            for i in range(10):
                for server in server_list:
                    start = time.time()
                    # print("resolving {} using root server {}".format(domain, server))
                    resolution = resolve(domain, server, "")
                    if resolution != None:
                        # add resolution time (ms)
                        times.append((time.time()-start)*1000)
                        num_resolved += 1
                        break
                    
            print("Sample for {} was {} resolutions using resolver: {}. Data: {}".format(domain, num_resolved, resolver_name(resolver), times))

def resolve(domain, server, path):
    try:
        dns_name = dns.name.from_text(domain)
        
        query = dns.message.make_query(dns_name, dns.rdatatype.A)
        response = dns.query.udp(query, server, .5)
        rcode = response.rcode()

        if rcode != dns.rcode.NOERROR:
            raise Exception("Error in DNS response")

        # if there is an answer, return the path
        if response.answer != None and len(response.answer) > 0:
            for i in response.answer:
                i = i.to_text()
                next_path = path+i+"\n"
                if "IN A" in i:
                    return next_path
                elif "CNAME" in i:
                    a = i.split(" ")
                    resolution = resolve(domain, a[len(a)-1], next_path)
                    if resolution != None:
                        return resolution

        # iterate through additional servers and try to resolve recursively
        if response.additional != None and len(response.additional) > 0:
            for i in response.additional:
                i = i.to_text()
                next_path = path+i+"\n"
                a = i.split(" ")
                resolution = resolve(domain, a[len(a)-1], path + i + "\n")
                if resolution != None:
                    return resolution

        # iterate through authority servers and try to resolve recursively
        if response.authority != None and len(response.authority) > 0:
            for i in response.authority:
                i = i.to_text()
                next_path = path+i+"\n"
                a = i.split(" ")
                resolution = resolve(domain, a[len(a)-1], path + i + "\n")
                if resolution != None:
                    return resolution
                    
    except Exception as e:
        return None


if __name__ == "__main__":
    main()