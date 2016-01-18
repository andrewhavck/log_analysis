from robber import expect
from log_analysis.session_info import IpInfo
from log_analysis.session_info import SessionInfo


inactive_window = 1200  # twenty minutes in seconds


def test_ip_info_init():
    ip = '127.0.0.1'
    time = 1452978797
    ip_info = IpInfo(ip, time, inactive_window)

    expect(ip_info.ip).to.eq(ip)
    expect(ip_info.total_pages).to.eq(1)
    expect(ip_info.total_sessions).to.eq(1)
    expect(ip_info.total_time).to.eq(1200)
    expect(ip_info.avg_pp_session()).to.eq(1)
    expect(ip_info.avg_pp_min()).to.eq(0.05)


def test_ip_info_add_request_same_session():
    ip = '10.7.39.1'
    time = 1452978000
    ip_info = IpInfo(ip, time, inactive_window)

    ip_info.add_request(time + 1198)
    ip_info.add_request(time + 1199)
    expect(ip_info.total_pages).to.eq(3)
    expect(ip_info.total_sessions).to.eq(1)
    expect(ip_info.total_time).to.eq(2399)
    expect(ip_info.avg_pp_session()).to.eq(3.0)
    expect(ip_info.avg_pp_min()).to.be.within(0.075, 0.0751)


def test_ip_info_add_request_new_session():
    ip = '230.90.10.71'
    time = 1452978709
    ip_info = IpInfo(ip, time, inactive_window)

    ip_info.add_request(time + 1201)
    expect(ip_info.total_pages).to.eq(2)
    expect(ip_info.total_sessions).to.eq(2)
    expect(ip_info.total_time).to.eq(2400)
    expect(ip_info.avg_pp_session()).to.eq(1.0)
    expect(ip_info.avg_pp_min()).to.eq(0.05)


def test_session_info_add_request():
    session_info = SessionInfo()
    time = 1452978797
    ip1 = '127.0.0.1'
    ip2 = '56.3.8.1'

    session_info.add_request(ip1, time)
    session_info.add_request(ip2, time)

    expect(session_info.get_ip_info(ip1).ip).to.eq(ip1)
    expect(session_info.get_ip_info(ip2).ip).to.eq(ip2)
