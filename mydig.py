import dns
import dns.query
import time
import datetime
import dns.rdtypes.IN.A
import dns.rdtypes.ANY.CNAME
import dns.rdtypes.ANY.NS

root_servers = {
    "a": "198.41.0.4",
    "b": "199.9.14.201",
    "c": "192.33.4.12",
    "d": "199.7.91.13",
    "e": "192.203.230.10",
    "f": "192.5.5.241",
    "g": "192.112.36.4",
    "h": "198.97.190.53",
    "i": "192.36.148.17",
    "j": "192.58.128.30",
    "k": "193.0.14.129",
    "l": "199.7.83.42",
    "m": "202.12.27.33",
}

def main():
    domain = input("Enter domain: ")
    print()

    result = "QUESTION SECTION:" + "\n" + "{} {:<3}{:<5}".format(domain, "IN", "A") + "\n\n"

    resolved = False
    for i in root_servers:
        start = time.time()
        try:
            resolution = resolve(domain, root_servers[i], root_servers[i], set())

            if resolution != None:
                # add answer section text
                result += "ANSWER SECTION:" + "\n"
                result += resolution + "\n\n"

                # add query time text
                result += "QUERY TIME: "
                result += str((time.time()-start)*1000) + " ms" + "\n"

                result += "WHEN: " + str(datetime.datetime.now())

                # print the string result
                print(result)
                resolved = True
                break
        except Exception as e:
            print(e)
            print("Root server {} failed to resolve".format(i))
        break
    if not resolved:
        print("{} could not be resolved".format(domain))

def resolve(domain, server, original, visited):

    # if domain/server combination already visited, then return
    if (domain + " " + server) in visited:
        return None

    # add combination to the set
    visited.add(domain + " " + server)
    
    try:
        # create dns name object using domain url
        dns_name = dns.name.from_text(domain)
        
        # create query using dns name object
        query = dns.message.make_query(dns_name, dns.rdatatype.A)
        
        # send query via udp and get response
        response = dns.query.udp(query, server, .5)

        # if an error occured, raise an exception
        rcode = response.rcode()
        if rcode != dns.rcode.NOERROR:
            raise Exception("Error in DNS response while resolving {}".format(domain))

        # if there is an answer, return the path
        if response.answer != None and len(response.answer) > 0:
            for a in response.answer:

                # for every ip in the rrset object, check for A record and CNAME
                for i in a:

                    # if A record found, return
                    if type(i) == dns.rdtypes.IN.A.A:
                        return str(a)
                    
                    # if CNAME found, resolve the CNAME using the original server
                    elif type(i) == dns.rdtypes.ANY.CNAME.CNAME:
                        resolution = resolve(str(i), original, original, visited)
                        if resolution != None:
                            return resolution

        # iterate through additional servers and try to resolve recursively
        if response.additional != None and len(response.additional) > 0:
            for a in response.additional:

                # for every ip in the rrset object, check for A record and CNAME
                for i in a:

                    # if A record found, resolve the record
                    if type(i) == dns.rdtypes.IN.A.A:
                        resolution = resolve(domain, str(i), original, visited)
                        if resolution != None:
                            return resolution

                    # if CNAME found, resolve the CNAME using the original server
                    elif type(i) == dns.rdtypes.ANY.CNAME.CNAME:
                        resolution = resolve(str(i), original, original, visited)
                        if resolution != None:
                            return resolution

        # iterate through authority servers and try to resolve recursively
        if response.authority != None and len(response.authority) > 0:
            for a in response.authority:

                # for every ip in the rrset object, check for A record and CNAME
                for i in a:

                    # if A record found, resolve the record
                    if type(i) == dns.rdtypes.IN.A.A:
                        resolution = resolve(domain, str(i), original, visited)
                        if resolution != None:
                            return resolution

                    # if CNAME found, resolve the CNAME using the original server
                    elif type(i) == dns.rdtypes.ANY.CNAME.CNAME:
                        resolution = resolve(str(i), original, original, visited)
                        if resolution != None:
                            return resolution
                    
                    # if name server found, resolve it 
                    elif type(i) == dns.rdtypes.ANY.NS.NS:
                        resolution = resolve(str(i), original, original, visited)
                        if resolution != None:
                            return resolution
        return None

    except Exception as e:
        return None

if __name__ == "__main__":
    main()