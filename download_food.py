from pathlib import Path
from urllib.request import Request,urlopen
base=Path('/Users/dikapranandaputra/dokumen/jejak-deli-serdang/assets')
items={
'roti-jala.jpg':'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e2/Roti_jala_Indonesia.JPG/960px-Roti_jala_Indonesia.JPG',
'bubur-pedas.jpg':'https://thumb.wikimedia.org/wikipedia/commons/thumb/8/89/Bubur_pedas_melayu.jpg/960px-Bubur_pedas_melayu.jpg',
'sate-kerang.jpg':'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/1a/Sate_Kerang.jpg/960px-Sate_Kerang.jpg',
'gulai-ikan.jpg':'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/ae/Gulai_Ikan_101659.jpg/960px-Gulai_Ikan_101659.jpg',
}
for n,u in items.items():
 d=urlopen(Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read();(base/n).write_bytes(d);print(n,len(d))
