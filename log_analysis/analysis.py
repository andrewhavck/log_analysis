import argparse
import charting
import ip_classifier
import log_format

from session_info import SessionInfo


def write_session_info(sessions):
    with open('session_info.tsv', 'w') as w:
        for ip in sessions.ips:
            session_info = sessions.get_ip_info(ip)
            w.write(log_format.ip_info_log(ip,
                                           session_info.avg_pp_session(),
                                           session_info.avg_pp_min()))


def get_args():
    argp = argparse.ArgumentParser()
    argp.add_argument('-s', '--source', required=True, help="input file")
    return vars(argp.parse_args())


def analyze_log(source):
    sessions = SessionInfo()

    with open(source, 'r') as r:
        with open('log_class.tsv', 'w') as w:
            for line in r:
                ip = log_format.get_ip(line)
                sessions.add_request(ip, float(log_format.get_time(line)))
                w.write(log_format.ip_class_log(line, ip_classifier.get_class(ip)))

    write_session_info(sessions)
    charting.create_status_chart(source)


def main():
    args = get_args()
    analyze_log(args['source'])

if __name__ == '__main__':
    main()
