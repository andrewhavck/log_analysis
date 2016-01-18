from __future__ import division


class IpInfo:
    def __init__(self, ip, time, inactive_window):
        self.ip = ip
        self.total_pages = 1
        self.total_sessions = 1
        self.inactive_window = inactive_window
        self.total_time = inactive_window
        self.last_request = time

    def __is_new_session(self, time):
        return self.last_request < (time - self.inactive_window)

    def __calc_time_delta(self, time):
        return time - self.last_request

    def avg_pp_session(self):
        return self.total_pages / self.total_sessions

    def avg_pp_min(self):
        return self.total_pages / (self.total_time / 60)

    def add_request(self, time):
        self.total_pages += 1

        if self.__is_new_session(time):
            self.total_sessions += 1
            self.total_time += self.inactive_window
        else:
            self.total_time += self.__calc_time_delta(time)

        self.last_request = time


class SessionInfo:
    twenty_minutes_in_seconds = 1200

    def __init__(self):
        self.ips = {}

    def add_request(self, ip, time):
        entry = self.ips.get(ip, None)
        if entry:
            self.ips[ip].add_request(time)
        else:
            self.ips[ip] = IpInfo(ip, time, self.twenty_minutes_in_seconds)

    def get_ip_info(self, ip):
        return self.ips[ip]
