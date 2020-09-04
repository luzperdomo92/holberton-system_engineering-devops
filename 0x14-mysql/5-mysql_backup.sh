#!/usr/bin/env bash
# generates a MySQL dump, creates a compressed archive out of it.

mysqldump -u root -p"$1" --all-databases > backup.sql
tar -czf $(date +%d-%m-%Y).tar.gz backup.sql
