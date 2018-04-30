#!/use/bin/python
import argparse
from contextlib import closing
import csv
from dateutil import rrule
from datetime import date, datetime, timezone
import requests
import sys
import time


SAMDI_URL = "http://www.marinedebris.engr.uga.edu/mdtapp/getLoggedData.php"
SAMDI_LIST = 22


def make_requests(ini_date, end_date, file_name):
    dates = list(rrule.rrule(rrule.MONTHLY, dtstart=ini_date, until=end_date))
    dates.append(end_date)
    # see form details at http://www.marinedebris.engr.uga.edu/newmap/
    form_data = {
        'lists[]': SAMDI_LIST,
        'from': None,
        'to': None,
        # unused fields
        'username': None,
        'password': None,
        'keywords': None,
    }
    keys = {
        "altitude",
        "description",
        "id",
        "item_id",
        "iteminstance_description",
        "itemlist_id",
        "itemname",
        "latitude",
        "longitude",
        "listname",
        "location",
        "material_id",
        "quantity",
        "radius",
        "timestamp",
        "date"
    }

    with open(file_name, 'w', newline='', encoding="utf-8") as dest_file:
        writer = csv.DictWriter(dest_file, keys, delimiter=';', quotechar='"', restval='')
        writer.writeheader()
        for start, end in zip(dates, dates[1:]):
            form_data['from'] = int(start.timestamp()*1000)
            form_data['to'] = int(end.timestamp()*1000)

            with closing(requests.post(SAMDI_URL, data=form_data, stream=True)) as r:
                if r.status_code != 200:
                    raise Exception("Problems requesting the data.")
                data_dict = r.json()['data']
                for d in data_dict:
                    if d['timestamp'] is not None:
                        d['date'] = d['timestamp'][:4] + '-' + d['timestamp'][4:6] + '-' + d['timestamp'][6:8] + ' ' + d['timestamp'][8:10] + ':' + d['timestamp'][10:12] + ':' + d['timestamp'][12:14]
                    else:
                        d['date'] = ''
                writer.writerows(data_dict)
            time.sleep(3)
            print("Request finished from %s to %s" % (form_data['from'], form_data['to']))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ini_date', type=lambda s: datetime.strptime(s, '%m-%d-%Y'))
    parser.add_argument('end_date', type=lambda s: datetime.strptime(s, '%m-%d-%Y'))
    parser.add_argument("file_name", type=str)
    args = parser.parse_args()
    args.ini_date = args.ini_date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=timezone.utc)
    args.end_date = args.end_date.replace(hour=23, minute=59, second=59, microsecond=999999, tzinfo=timezone.utc)
    print("Pulling records from %s to %s.." % (args.ini_date, args.end_date))
    make_requests(args.ini_date, args.end_date, args.file_name)


if __name__ == "__main__":
    main()
