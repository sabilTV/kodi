# -*- coding: utf-8 -*-
# Module: default
# Author: Fakhrul Adabi Nawi
# Created on: 1 Muharam 1437
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","root","1","sabiltv")


def get_menus(pgno):
    cursor = db.cursor()
    cursor.execute("SELECT label, thumb, fanart FROM menus WHERE active=%s LIMIT 50", (1))
    # Fetch a single row using fetchone() method.
    items = []
    data = cursor.fetchall()
    # print the rows
    for row in data :
        item_dict = {'label': row[0], 'thumb': row[1], 'fanart': row[2]}
        #yourlist.append(yourdict.copy())
        items.append(item_dict.copy())
        #items.append(row[0])

    # disconnect from server
    db.close()

    return items

def get_muallims(pgno):
    cursor = db.cursor()
    cursor.execute("SELECT nama_penuh, thumb, fanart, kod_nama, id FROM muallims WHERE active=%s LIMIT 50", (1))
    # Fetch a single row using fetchone() method.
    items = []
    data = cursor.fetchall()
    # print the rows
    for row in data :
        item_dict = {'label': row[0], 'thumb': row[1], 'fanart': row[2], 'kod_nama': row[3], 'muallim_id': row[4]}
        #yourlist.append(yourdict.copy())
        items.append(item_dict.copy())
        #items.append(row[0])

    # disconnect from server
    db.close()

    return items

def get_videos(pgno,category,muallim_id):
    cursor = db.cursor()

    cursor.execute("SELECT title, thumb, fanart, item_id FROM ilmus WHERE active=%s AND muallim_id = %s LIMIT 50", (1,muallim_id))
    # Fetch a single row using fetchone() method.
    items = []
    data = cursor.fetchall()

    print(data)

    # print the rows
    for row in data :
        item_dict = {'label': row[0], 'thumb': row[1], 'fanart': row[2], 'video_id': row[3]}
        #yourlist.append(yourdict.copy())
        items.append(item_dict.copy())
        #items.append(row[0])

    # disconnect from server
    db.close()

    return items
