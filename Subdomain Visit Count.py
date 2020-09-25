#Subdomain Visit Count

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        count = collections.Counter()
        for cpdomain in cpdomains:
            times, domain = cpdomain.split(" ")
            times = int(times)
            count[domain] += times
            for i, c in enumerate(domain):
                if c == '.':
                    count[domain[i + 1 : ]] += times
        return [str(times) + " " + domain for domain, times in count.items()]