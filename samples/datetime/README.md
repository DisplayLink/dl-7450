# datetime

The DL-7450 comes with a simplified implementation of the datetime module.

A [sample app](dst_timezone.py) has been provided that demonstrates
converting between UTC and the timezone used in the UK. The app will cycle
through a predetermined set of datetimes, converting each one and
displaying both original and converted times on the splash screen.

It is worth changing the default list of datetimes to display other time
conversions, perhaps from different years, and comparing those results to
the actual conversions.

A base class for defining custom Daylight Savings timezones is provided,
which allows for the definition of new timezones that take advantage of
Daylight Savings. It is encouraged to try using this base class to
implement a similar time zone, such as Central European (Summer) Time.
