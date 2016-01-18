import re


valid_ip = re.compile('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
                      '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
                      '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
                      '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
class_a = re.compile('[0-9][0-9]?$|1[0-1][0-9]|12[0-7]')
class_b = re.compile('12[8-9]|1[3-8][0-9]|19[0-1]')
class_c = re.compile('19[2-9]|2[0-1][0-9]|22[0-3]')
class_d = re.compile('22[4-9]|23[0-9]')
class_e = re.compile('24[0-9]|25[0-5]')


def get_class(ip):

    match = re.match(valid_ip, ip)
    if match:
        start_octet = match.group(1)
        if(re.match(class_a, start_octet)):
            return 'A'
        elif(re.match(class_b, start_octet)):
            return 'B'
        elif(re.match(class_c, start_octet)):
            return 'C'
        elif(re.match(class_d, start_octet)):
            return 'D'
        return 'E'

    return None
