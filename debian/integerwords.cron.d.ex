#
# Regular cron jobs for the integerwords package.
#
0 4	* * *	root	[ -x /usr/bin/integerwords_maintenance ] && /usr/bin/integerwords_maintenance
