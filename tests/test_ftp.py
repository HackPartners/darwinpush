import os
import sys
sys.path.append(os.getcwd())

import datetime

import pytest
import darwinpush.ftp as ftp


class FakeFtp():
    def __init__(self, files):
        self.files = files

    def nlst(self):
        """ Fake listing all the files """
        return self.files


def test_log_filenames():
    fakeftp = FakeFtp([
        "20150926020724_ref_v3.xml.gz",
        "20150926020724_v8.xml.gz",
        "pPortData.log.2015-09-26-09-44",
        "pPortData.log.2015-09-26-09-49",
        "pPortData.log.2015-09-26-09-54",
        "pPortData.log.2015-09-26-09-59", # all files including this one
        "pPortData.log.2015-09-26-10-04",
        "pPortData.log.2015-09-26-10-09",
        "pPortData.log.2015-09-26-10-14",
        "pPortData.log.2015-09-26-10-19",
        "some weird stuff",
        "pPortData.log.2015-09-26-10-24",
        "pPortData.log.2015-09-26-10-29",
        "pPortData.log.2015-09-26-10-34",
        "pPortData.log",
    ])

    min_date = datetime.datetime(
        year=2015,
        month=9,
        day=26,
        hour=10,
        minute=2
    )

    # manually filter the names
    index = fakeftp.files.index("pPortData.log.2015-09-26-09-59")
    expected = [i for i in filter(
        lambda x: x!="some weird stuff",
        fakeftp.files[index:len(fakeftp.files)-1]
    )]

    result = [i for i in ftp.log_filenames(fakeftp, min_date)]
    assert(result == expected)

def test_snapshot_filename():
    fakeftp = FakeFtp([
        "20150926020724_ref_v3.xml.gz",
        "pPortData.log.2015-09-26-09-44",
        "pPortData.log.2015-09-26-09-49",
        "20150926020724_v8.xml.gz",
        "pPortData.log.2015-09-26-09-54",
        "pPortData.log.2015-09-26-09-59",
        "pPortData.log.2015-09-26-10-04",
        "pPortData.log.2015-09-26-10-09",
        "pPortData.log.2015-09-26-10-14",
        "pPortData.log.2015-09-26-10-19",
        "some weird stuff",
        "pPortData.log.2015-09-26-10-24",
        "pPortData.log.2015-09-26-10-29",
        "pPortData.log.2015-09-26-10-34",
        "pPortData.log",
    ])

    result = ftp.snapshot_filename(fakeftp)
    assert(result == "20150926020724_v8.xml.gz")

def test_snapshot_filename_none():
    fakeftp = FakeFtp([
        "pPortData.log.2015-09-26-09-44",
        "pPortData.log.2015-09-26-09-49",
        "pPortData.log.2015-09-26-09-54",
        "pPortData.log.2015-09-26-09-59",
        "pPortData.log.2015-09-26-10-04",
    ])

    result = ftp.snapshot_filename(fakeftp)
    assert(result == None)

def test_snapshot_filename_more():
    fakeftp = FakeFtp([
        "20150925020724_v8.xml.gz",
        "haha",
        "20150926020724_v8.xml.gz", # this is the maximum
        "some weird stuff",
        "pPortData.log.2015-09-26-10-24",
        "20150826020724_v8.xml.gz",
        "pPortData.log.2015-09-26-10-29",
        "pPortData.log.2015-09-26-10-34",
    ])

    result = ftp.snapshot_filename(fakeftp)
    assert(result == "20150926020724_v8.xml.gz")
