# This code is part of the DisplayLink DL-7450 Software Development Kit
# Copyright (c) DisplayLink UK 2025

from datetime import datetime, timedelta, timezone, tzinfo
from splashscreen import Splashscreen
from wakeup import wakeup


class DaylightSavingsTimeZone(tzinfo):
    DST_OFFSET = timedelta(hours=1)

    @staticmethod
    def dst_start(dt) -> datetime:
        raise NotImplementedError

    @staticmethod
    def dst_end(dt) -> datetime:
        raise NotImplementedError

    @staticmethod
    def timezone_name(is_dst) -> str:
        raise NotImplementedError

    def _check_tzinfo(self, dt):
        if dt.tzinfo is not self:
            raise ValueError("dt.tzinfo is not self")

    def _dst_from_utc(self, dt):
        dt = dt.replace(tzinfo=None)  # Remove timezone info for calculation

        dst_start = self.dst_start(dt)
        dst_end = self.dst_end(dt)

        dst_fold_start = dst_end
        dst_fold_end = dst_fold_start + self.DST_OFFSET

        is_dst = dst_start <= dt < dst_end
        fold = dst_fold_start <= dt < dst_fold_end

        return is_dst, fold

    def _dst_from_current_tz(self, dt) -> bool:
        dt = dt.replace(tzinfo=None)  # Remove timezone info for calculation

        dst_start = self.dst_start(dt)
        dst_end = self.dst_end(dt) + self.DST_OFFSET
        is_dst = (dst_start <= dt < dst_end) and not dt.fold

        return is_dst

    def utcoffset(self, dt) -> timedelta:
        self._check_tzinfo(dt)
        is_dst = self._dst_from_current_tz(dt)
        return timedelta(hours=is_dst)

    def fromutc(self, dt):
        self._check_tzinfo(dt)
        isdst, fold = self._dst_from_utc(dt)
        dt += timedelta(hours=isdst)
        dt = dt.replace(fold=fold)
        return dt

    def dst(self, dt) -> timedelta:
        self._check_tzinfo(dt)
        is_dst = self._dst_from_current_tz(dt)
        return timedelta(hours=is_dst)

    def tzname(self, dt) -> str:
        is_dst = self._dst_from_current_tz(dt)
        return self.timezone_name(is_dst)


class BritishTimeZone(DaylightSavingsTimeZone):
    @staticmethod
    def dst_start(dt) -> datetime:
        march_end = dt.replace(month=3, day=31, fold=0)
        last_sunday_in_march = march_end - timedelta(days=march_end.isoweekday())
        dst_start = last_sunday_in_march.replace(hour=1, minute=0, second=0)
        return dst_start

    @staticmethod
    def dst_end(dt) -> datetime:
        october_end = dt.replace(month=10, day=31, fold=0)
        last_sunday_in_october = october_end - timedelta(days=october_end.isoweekday())
        dst_end = last_sunday_in_october.replace(hour=1, minute=0, second=0)
        return dst_end

    @staticmethod
    def timezone_name(is_dst) -> str:
        return "BST" if is_dst else "GMT"


splashscreen = Splashscreen()


class DateTimeCycler:
    def __init__(self, datetimes, timezones=[timezone.utc]):
        self.datetimes = datetimes
        self.timezones = timezones
        self.running = False
        self.current_index = 0
        self.timer = None

    def _display_next(self):
        dt = self.datetimes[self.current_index]
        converted_dts = (dt.astimezone(tz) for tz in self.timezones)
        text = [f"{converted_dt} {converted_dt.tzname()}" for converted_dt in converted_dts]
        splashscreen.add_text_box(text)
        self.current_index = (self.current_index + 1) % len(self.datetimes)

    def run(self):
        if self.running:
            raise Exception("Cycler already running")
        self.running = True
        self.timer = wakeup(self._display_next, 0, 3000)


datetimes = [
    datetime(2025,  3, 29, 23, 59, 59, tzinfo=timezone(timedelta(hours=-1))),
    datetime(2025,  3, 30, 3,  0,  0, tzinfo=timezone(timedelta(hours=2))),
    datetime(2025, 10, 26, 8, 59, 59, tzinfo=timezone(timedelta(hours=8))),
    datetime(2025, 10, 25, 13,  0,  0, tzinfo=timezone(timedelta(hours=-12))),
]
timezones = [
    timezone.utc,
    BritishTimeZone(),
    timezone(timedelta(hours=8)),
]
cycler = DateTimeCycler(datetimes, timezones=timezones)
cycler.run()
