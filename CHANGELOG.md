# Release 0.8.8 - Wednesday 17 May  10:23:51 AEST 2017

- Added Dynamic Search Ad type to text queryset

# Release 0.8.7 - Friday 21 April  14:47:38 AEST 2017

- Removed another deprecated field from report definitions

# Release 0.8.6 - Friday 21 April  14:37:25 AEST 2017

- Added to Chris' nasty hack with the integer field and with Google now returning doubles

# Release 0.8.5 - Friday 21 April  14:27:36 AEST 2017

- Removed another deprecated report definition field

# Release 0.8.4 - Friday 21 April  14:11:59 AEST 2017

- Removed ClickConversionRate from report definitions as it has been removed as of version V201702

# Release 0.8.3 - Thursday 6 April  10:24:39 AEST 2017

- Update to Adwords API v201702

# Release 0.8.2 - Thursday 10 November  12:57:31 AEDT 2016

- Added missing ad types and added expanded text ad to text qs.

# Release 0.8.1 - Tue Jun 21 15:05:12 AEST 2016

- Upgrade googleads to `~4.1.0`.

  (0.8.0 was a broken change…)

# Release 0.8.0 - Mon Jun 20 14:27:14 AEST 2016

Breaking change.

- Remove `Adwords*` compatibility aliases introduced in 0.7.7.

- Upgrade Google API to v201605.

  Note that in v201603 empty values become '--' (in my experience, maybe
  '-- '?) rather than an empty string. This may affect user code.

- Replace report definition key `includeZeroImpressions` with a keyword
  argument `include_zero_impressions` on `ReportFile.objects.request()`.

- Remove the `TargetCpa` (`max_cpa_converted_clicks`) ad group metrics field

# Release 0.7.7 - Mon Jun  6 08:43:24 AEST 2016

- Correct Adwords to AdWords everywhere.

  For members of the public API the old names have been left around as
  aliases, so there should not be any compatibility problems. Unless you
  were doing things like hardcoding the name of an exception as a string.
  Which is, I suppose, quite feasible. Still, I’m not going to consider it
  a breaking change.

- Support calculating spend with missing data.

  Insufficient data is not always a problem. If your access has been
  revoked, you may just wish to ignore the fact.

# Release 0.7.6 - Wed May 25 15:07:43 AEST 2016

- Fix `paged_request` if it yields no results

# Release 0.7.5 - Mon May  2 23:05:00 AEST 2016

- Kinda hackily fix 0.7.4 data import, with some wonky field types.

This is getting awfully tedious. We're seriously doing things the wrong way.

# Release 0.7.4 - Mon May  2 12:02:45 AEST 2016

- Fix 0.7.3.
- `est_*` and `*_est_*` fields removed from metrics.
- Other requirements updates/fixes

# Release 0.7.3 - Thu Apr 14 11:03:55 AEST 2016

This release is broken. Code changes *were* actually required.

- Update Google AdWords API from v201506 to v201509

# Release 0.7.2 - Mon Jul 27 08:24:50 AEST 2015

- Fixed incorrect googleads version in requirements to 3.5.0.

# Release 0.7.1 - Wed Jul  1 13:41:20 AEST 2015

- Updated django-cereal to 0.1.2

# Release 0.7.0 - Tue Jun 30 14:33:02 AEST 2015

- Support for v201506.
- Fixed references to bitbucket in README

# Release 0.6.4 - Mon Jun 29 13:25:11 AEST 2015

- Fixes #2: auto_now, auto_now_add, and default are mutually exclusive.

# Release 0.6.3 - Thu Jun 25 15:42:56 AEST 2015

- Now using django-appconf==1.0.1

# Release 0.6.2 - Thu Jun 25 14:48:36 AEST 2015

- Fixed issue with the finish_*_sync celery tasks not chaining as expected.

# Release 0.6.1 - Thu Jun 25 13:49:10 AEST 2015

- Updated README
- Fixed links to django-nose issues.

# Release 0.6.0 - Thu Jun 25 12:05:09 AEST 2015

- Added tox support with tests for Python 2.7, 3.3, 3.4 and PyPy.
- Updated README.md to README.rst in preparation for pypi support.
- Added runtests.py script to run tests inside app.
- Moved repository from bitbucket to github.
- Removed random printing.
- PEP8 support (mostly...).
- Fixed issue that could occur with locking on memcache.
- Now using django-cereal for more efficient communication over the wire in Celery.
- Changed setting `GOOGLEADWORDS_START_FINISH_CELERY_QUEUE` to `GOOGLEADWORDS_HOUSEKEEPING_CELERY_QUEUE`.
- Removed `Alert.sync_alerts()`, `Alert.get_selector()` and task `sync_alerts` as the services that these functions call have been discontinued in the Google API. The :code:`Alert` model remains in place so that existing alerts can be accessed if required.

# Release 0.5.0 - Thu May 21 12:27:05 AEST 2015

- Modified cache based locking mechanisms to improve speed.

# Release 0.4.2 - Thu Mar 19 15:41:22 AEDT 2015

- Ensured Account.QuerySet methods return data ordered by day.
- Added helper methods on Account for ad_groups and ads and Campaign for ads.

# Release 0.4.1 - Mon Mar  2 08:42:34 AEDT 2015

- Changed to use latest version of api

# Release 0.4.0 - Wed Jan 28 15:25:00 AEDT 2015

- Django 1.7 support
- Now using django-money instead of python-money (which looks to be no longer supported and doesn't work in Django 1.7 - thanks t3kn0s).
- Exception AdwordsDataInconsistency is now AdwordsDataInconsistencyError
- Currency is no longer a default on each model Money field, it's now derived from the returned data
- New settings GOOGLEADWORDS_CELERY_TIMELIMIT and GOOGLEADWORDS_CELERY_SOFTTIMELIMIT
- Updated README with requirements and installation instructions
- PEP8
- Replaced the use of the 'money' module with 'djmoney' since the python-money module hasn't been updated for >3 years. Replaced the hard-coded currency with a variable

# Release 0.3.4 - Mon Aug 18 11:06:19 EST 2014

- Added some querysets

# Release 0.3.3 - Wed Aug 13 08:45:18 EST 2014

- Added Ad approval status field to model

# Release 0.3.2 - Thu Aug  7 11:34:15 EST 2014

- Changed some field names, changed tests to use gz files

# Release 0.3.1 - Fri Aug  1 13:55:09 EST 2014

- Changed top ads adgroup by conversion
- Added custom sync tasks

# Release 0.3.0 - Thu Jul 31 15:21:22 EST 2014

- Bug fix
- Added more queryset filters
- Changed report downloaded to use csv.gz
- Added queryset helpers to AdGroup
- Changed sync celery queue.
- 'account_metrics' getter now 'metrics' to follow convention.
- Added 'with_period' queryset
- Removed get_ from queryset filters
- Refs #1769: Added get data queryset methods
- Updated to use googleads 2.0.0
- Made some changes, error handling, model changes
- Refactored a bit of stuff and added more last synced dates for different aspects

# Release 0.2.0 - Mon Jul 28 14:23:35 EST 2014

- Support for Google Adwords v201402

# Release 0.1.0 - Mon Jul 21 10:55:51 EST 2014

- Initial release

