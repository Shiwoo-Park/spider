blog_id=$1
paging=$2

if [ -z $blog_id ]; then
  echo "Usage: script.sh <BLOG_ID> <PAGING_YN>"
  exit 1
fi

if [ -z $paging ]; then
  echo "Usage: script.sh <BLOG_ID> <PAGING_YN>"
  exit 1
fi

cd /Users/silva.park/git-my/spider

rm -f resources/*
scrapy runspider blog_spider/egloos.py -a user_id=$blog_id -a paging=$paging -o resources/egloos_$blog_id.json
python utils/json_to_mdfile.py > output.log