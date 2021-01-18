# spider

crawler for diverse data

## Dependencies
- pyenv
- python 3.7.6
- scrapy

## What's inside

- egloos blog crawler

## How to use

```shell
cd sample_spider
scrapy runspider quote.py -o quotes.jl

cd blog_spider
scrapy runspider egloos.py -o egloos.json
```