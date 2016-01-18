from robber import expect
from log_analysis import log_format


ip = '24.234.66.218'
time = '1452725798.463'
req = 'GET /page.143678790852849234.html'
status = '200'
client = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)'
log = '%s\t%s\t%s\t%s\t%s\n' % (ip, time, req, status, client)


def test_get_ip():
    expect(log_format.get_ip(log)).to.eq(ip)


def test_get_time():
    expect(log_format.get_time(log)).to.eq(time)


def test_get_status():
    expect(log_format.get_status(log)).to.eq(status)


def test_ip_class_log():
    ip_class = 'A'
    expected = '%s\t%s' % ('A', log)

    result = log_format.ip_class_log(log, ip_class)

    expect(result).to.eq(expected)


def test_ip_info_log():
    pp_ses = 20
    pp_min = 1

    expected = '%s\t%i\t%.2f\n' % (ip, pp_ses, pp_min)
    result = log_format.ip_info_log(ip, pp_ses, pp_min)

    expect(result).to.eq(expected)
