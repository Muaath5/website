---
title: "Free Serverless websites"
description: "writing about tools that will help you create amazing website without server pain"
tags: ["webdev"]
lang: en
usemathjax: false
---

## Github pages
This gives you unlimited static websites.

### Github Actions
you can use this also to prebuild pages for your website which makes it fast and easy to maintain.

## Cloudflare D1 & Workers
Using this, you can configure a website to view any type of database, for example you have a webapp that is for students certificates export, you can do it as following:

**Cloudflare worker:**
- `/api/auth`: Checks the login secret if it was correct or not
- `/api/perform`: Performs an SQL query and returns the result, requires login secret for every operation

**Static website:**
- At first, you must login by the URL for the worker and the login secret
- Fetches the tables of students, and certificates
- You can add student/certificate, or even print a certificate all using Javascript and the API

## Firebase
I need to check the available options, probably same as Cloudflare workers.
