# -*- coding: utf-8 -*-
import json

with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

print("Current keys in data_sekolah.json:", list(db.keys()))
