from robber import expect
from log_analysis import ip_classifier


def test_get_ip_class_empty_string():
    ip_class = ip_classifier.get_class('')
    expect(ip_class).to.eq(None)


def test_get_ip_class_invalid_ip():
    ip_class = ip_classifier.get_class('999.0.0.0')
    expect(ip_class).to.eq(None)


def test_get_ip_class_a_lower_bound():
    ip_class = ip_classifier.get_class('0.0.0.0')
    expect(ip_class).to.eq('A')


def test_get_ip_class_a_upper_bound():
    ip_class = ip_classifier.get_class('127.255.255.255')
    expect(ip_class).to.eq('A')


def test_get_ip_class_b_lower_bound():
    ip_class = ip_classifier.get_class('128.0.0.0')
    expect(ip_class).to.eq('B')


def test_get_ip_class_b_upper_bound():
    ip_class = ip_classifier.get_class('191.255.255.255')
    expect(ip_class).to.eq('B')


def test_get_ip_class_c_lower_bound():
    ip_class = ip_classifier.get_class('192.0.0.0')
    expect(ip_class).to.eq('C')


def test_get_ip_class_c_upper_bound():
    ip_class = ip_classifier.get_class('223.255.255.255')
    expect(ip_class).to.eq('C')


def test_get_ip_class_d_lower_bound():
    ip_class = ip_classifier.get_class('224.0.0.0')
    expect(ip_class).to.eq('D')


def test_get_ip_class_d_upper_bound():
    ip_class = ip_classifier.get_class('239.255.255.255')
    expect(ip_class).to.eq('D')


def test_get_ip_class_e_lower_bound():
    ip_class = ip_classifier.get_class('240.0.0.0')
    expect(ip_class).to.eq('E')


def test_get_ip_class_e_upper_bound():
    ip_class = ip_classifier.get_class('255.255.255.255')
    expect(ip_class).to.eq('E')
