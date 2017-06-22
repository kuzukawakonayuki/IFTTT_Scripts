import requests
target_url = 'https://maker.ifttt.com/trigger/{XXXXXXX}/with/key/esNZA0_q9698h1gw9QaAY6VUj9n-6cqD10O_zRgZbmk'
r = requests.get(target_url)
print(r)
