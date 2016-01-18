
def __parse_line(line):
    return line.split('\t')


def get_ip(line):
    return __parse_line(line)[0]


def get_time(line):
    return __parse_line(line)[1]


def get_status(line):
    return __parse_line(line)[3]


def ip_class_log(line, ip_class):
    return '%s\t%s' % (ip_class, line)


def ip_info_log(ip, avg_pp_ses, avg_pp_min):
    return '%s\t%i\t%.2f\n' % (ip, avg_pp_ses, avg_pp_min)
