"""Demo module: deliberately insecure, used to exercise the PR review webhook."""

import os
import subprocess

DB_PASSWORD = "hunter2-prod-2024"          # hard-coded secret


def lookup(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + name + "'")   # SQL concatenation
    return cur.fetchall()


def render(template):
    return eval(template)                   # code injection


def backup(path):
    return subprocess.check_output("tar czf - " + path, shell=True)   # shell=True


def parse(value):
    try:
        return int(value)
    except:                                 # bare except
        pass


print("debug", DB_PASSWORD)                 # debug print
